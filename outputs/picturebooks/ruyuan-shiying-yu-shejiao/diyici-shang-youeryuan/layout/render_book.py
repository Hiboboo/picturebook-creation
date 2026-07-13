from __future__ import annotations

import argparse
import html
import os
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont, ImageOps
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


LOCKED_SIZE = (1536, 2048)
TARGET_RATIO = LOCKED_SIZE[0] / LOCKED_SIZE[1]
SLIDE_CX = 6_858_000
SLIDE_CY = 9_144_000

SERIES_SLUG = "ruyuan-shiying-yu-shejiao"
TITLE_SLUG = "diyici-shang-youeryuan"
BOOK_TITLE = "第一次\n上幼儿园"
CREDIT = "图/文：小葫芦"

PAGE_TEXT = {
    1: "轻轻背上\n可爱的小书包。",
    2: "好漂亮的\n幼儿园。",
    3: "妈妈\n蹲下来。",
    4: "老师说，\n进来看一看吧。",
    5: "小格子，\n等我哟。",
    6: "我坐边边\n看一看。",
    7: "圆圆球，\n咕噜咕噜跑过来。",
    8: "我也\n咕噜回去。",
    9: "妈妈\n来接我啦。",
    10: "明天，\n我还要来幼儿园。",
}

PAGE_LAYOUT = {
    1: ("left", 130),
    2: ("left", 135),
    3: ("left", 135),
    4: ("left", 135),
    5: ("right", 135),
    6: ("right", 135),
    7: ("left", 130),
    8: ("left", 130),
    9: ("left", 135),
    10: ("left", 135),
}

LIGHT_TEXT_PAGES: set[int] = set()


def center_crop_box(width: int, height: int) -> tuple[int, int, int, int]:
    current_ratio = width / height
    if current_ratio > TARGET_RATIO:
        crop_width = round(height * TARGET_RATIO)
        left = (width - crop_width) // 2
        return left, 0, left + crop_width, height
    crop_height = round(width / TARGET_RATIO)
    top = (height - crop_height) // 2
    return 0, top, width, top + crop_height


def normalize_image(path: Path) -> None:
    with Image.open(path) as source:
        image = source.convert("RGB")
        image = image.crop(center_crop_box(*image.size))
        image = image.resize(LOCKED_SIZE, Image.Resampling.LANCZOS)
        temporary = path.with_suffix(".normalized.png")
        image.save(temporary, format="PNG", optimize=True)
    temporary.replace(path)


def normalize(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    files = sorted(clean_dir.glob("*.png"))
    if not files:
        raise FileNotFoundError(f"No PNG files found in {clean_dir}")
    for path in files:
        normalize_image(path)
    print(f"normalized={len(files)} size={LOCKED_SIZE[0]}x{LOCKED_SIZE[1]}")
    return 0


def font_candidates() -> list[Path]:
    candidates: list[Path] = []
    if configured := os.environ.get("PICTUREBOOK_FONT"):
        candidates.append(Path(configured))
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        local_fonts = Path(local_app_data) / "Microsoft" / "Windows" / "Fonts"
        candidates.extend(
            [
                local_fonts / "SourceHanSansSC-Regular.otf",
                local_fonts / "NotoSansCJKsc-Regular.otf",
            ]
        )
    windows_fonts = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    candidates.extend(
        [
            windows_fonts / "SourceHanSansSC-Regular.otf",
            windows_fonts / "NotoSansCJKsc-Regular.otf",
            windows_fonts / "msyh.ttc",
            windows_fonts / "simhei.ttf",
        ]
    )
    return candidates


def resolve_font_path() -> Path:
    for candidate in font_candidates():
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("No Chinese-capable font found; set PICTUREBOOK_FONT")


def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def draw_multiline(
    image: Image.Image,
    text: str,
    font: ImageFont.FreeTypeFont,
    side: str,
    top: int,
    fill: tuple[int, int, int],
    stroke_fill: tuple[int, int, int],
    margin: int = 120,
    spacing: int = 18,
) -> None:
    draw = ImageDraw.Draw(image)
    box = draw.multiline_textbbox((0, 0), text, font=font, spacing=spacing, stroke_width=3)
    width = box[2] - box[0]
    left = margin if side == "left" else LOCKED_SIZE[0] - margin - width
    draw.multiline_text(
        (left, top),
        text,
        font=font,
        fill=fill,
        spacing=spacing,
        stroke_width=3,
        stroke_fill=stroke_fill,
    )


def wrap_cjk(text: str, max_chars: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        if char == "\n":
            if current:
                lines.append(current)
                current = ""
            continue
        current += char
        if len(current) >= max_chars:
            lines.append(current)
            current = ""
    if current:
        lines.append(current)
    return lines


def draw_parent_page(path: Path, font_path: Path) -> None:
    image = Image.new("RGB", LOCKED_SIZE, "#f6f5ee")
    draw = ImageDraw.Draw(image)
    title_font = load_font(font_path, 76)
    heading_font = load_font(font_path, 46)
    body_font = load_font(font_path, 36)
    small_font = load_font(font_path, 32)
    ink = (50, 64, 60)
    soft = (82, 101, 94)
    accent = (66, 126, 126)
    draw.text((120, 115), "给家长的话", font=title_font, fill=ink)

    sections = [
        (
            "这个故事想让孩子感受到什么",
            "第一次上幼儿园时，孩子可以停住、想牵手、先看一看。适应不是一下子完成的事，也可以从坐在边边观察、把球轻轻滚回去这样的小动作开始。",
        ),
        (
            "共读提醒",
            "请不要用故事要求孩子“明天不能哭”，也不要把进教室、交朋友、不想妈妈当作必须完成的目标。",
        ),
        (
            "亲子互动",
            "读到园门和教室门口时，可以问：“小柚想先看哪里？”读到圆圆球时，可以和孩子轻轻滚球，试一试来和回。",
        ),
        (
            "可使用的支持性语言",
            "你想先牵着我，还是先看一看？我听见你说想慢一点。今天做到这一小步，就可以了。",
        ),
        ("适合幼儿年龄", "主要适合 3-4 岁，3-5 岁可亲子共读。入园前、入园第一周或长假后返园都可使用。"),
    ]

    y = 260
    for heading, body in sections:
        draw.text((120, y), heading, font=heading_font, fill=accent)
        y += 66
        for line in wrap_cjk(body, 31):
            draw.text((120, y), line, font=body_font, fill=soft)
            y += 52
        y += 36

    draw.text((120, LOCKED_SIZE[1] - 130), CREDIT, font=small_font, fill=(79, 89, 84))
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, optimize=True)


def compose(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    output_dir = root / "artwork" / "composited"
    output_dir.mkdir(parents=True, exist_ok=True)
    expected = [clean_dir / "cover-clean.png", *[clean_dir / f"page-{page:02d}-clean.png" for page in range(1, 11)]]
    missing = [path.name for path in expected if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing clean artwork: {', '.join(missing)}")

    font_path = resolve_font_path()
    body_font = load_font(font_path, 72)
    title_font = load_font(font_path, 168)
    credit_font = load_font(font_path, 46)

    with Image.open(clean_dir / "cover-clean.png") as source:
        cover = source.convert("RGB")
    if cover.size != LOCKED_SIZE:
        raise ValueError(f"cover-clean.png must be {LOCKED_SIZE}, got {cover.size}")
    draw_multiline(cover, BOOK_TITLE, title_font, "left", 115, (44, 73, 72), (244, 246, 238), spacing=26)
    ImageDraw.Draw(cover).text(
        (120, LOCKED_SIZE[1] - 150),
        CREDIT,
        font=credit_font,
        fill=(54, 62, 58),
        stroke_width=2,
        stroke_fill=(245, 242, 231),
    )
    cover.save(output_dir / "cover-final.png", optimize=True)

    for page, text in PAGE_TEXT.items():
        source_path = clean_dir / f"page-{page:02d}-clean.png"
        with Image.open(source_path) as source:
            rendered = source.convert("RGB")
        if rendered.size != LOCKED_SIZE:
            raise ValueError(f"{source_path.name} must be {LOCKED_SIZE}, got {rendered.size}")
        if page in LIGHT_TEXT_PAGES:
            fill, stroke = (247, 242, 226), (79, 61, 45)
        else:
            fill, stroke = (44, 64, 61), (246, 244, 235)
        side, top = PAGE_LAYOUT[page]
        draw_multiline(rendered, text, body_font, side, top, fill, stroke)
        rendered.save(output_dir / f"page-{page:02d}-final.png", optimize=True)

    draw_parent_page(output_dir / "parent-guide-final.png", font_path)
    write_editable_layout(root, font_path)
    (root / "layout" / "font-used.txt").write_text(str(font_path), encoding="utf-8")
    print(f"composited=12 font={font_path}")
    return 0


def contact_sheet(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    items = [("封面", clean_dir / "cover-clean.png")]
    items.extend((f"第 {page} 页", clean_dir / f"page-{page:02d}-clean.png") for page in range(1, 11))
    missing = [path.name for _, path in items if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing clean artwork: {', '.join(missing)}")

    sheet = Image.new("RGB", (1500, 960), "#eef1e9")
    draw = ImageDraw.Draw(sheet)
    label_font = load_font(resolve_font_path(), 30)
    for index, (label, path) in enumerate(items):
        row, column = divmod(index, 6)
        cell_left = 35 + column * 240
        cell_top = 30 + row * 440
        with Image.open(path) as source:
            thumb = ImageOps.fit(source.convert("RGB"), (210, 280), method=Image.Resampling.LANCZOS)
        sheet.paste(thumb, (cell_left + 15, cell_top + 48))
        label_box = draw.textbbox((0, 0), label, font=label_font)
        label_width = label_box[2] - label_box[0]
        draw.text(
            (cell_left + (240 - label_width) // 2, cell_top),
            label,
            font=label_font,
            fill=(58, 70, 63),
        )

    bible_dir = root / "bible"
    bible_dir.mkdir(parents=True, exist_ok=True)
    output = bible_dir / "storyboard-contact-sheet.png"
    sheet.save(output, optimize=True)
    print(f"contact_sheet={output}")
    return 0


def final_image_paths(root: Path) -> list[Path]:
    composited_dir = root / "artwork" / "composited"
    return [
        composited_dir / "cover-final.png",
        *[composited_dir / f"page-{page:02d}-final.png" for page in range(1, 11)],
        composited_dir / "parent-guide-final.png",
    ]


def export_pdf(root: Path, images: list[Path]) -> Path:
    output_dir = root / "export"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = output_dir / f"{SERIES_SLUG}-{TITLE_SLUG}.pdf"
    page_width, page_height = LOCKED_SIZE
    doc = canvas.Canvas(str(pdf_path), pagesize=(page_width, page_height))
    for image_path in images:
        doc.drawImage(ImageReader(str(image_path)), 0, 0, width=page_width, height=page_height)
        doc.showPage()
    doc.save()
    return pdf_path


def xml_rels_root() -> str:
    return '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'


def write_pptx(root: Path, images: list[Path]) -> Path:
    output_dir = root / "export"
    output_dir.mkdir(parents=True, exist_ok=True)
    pptx_path = output_dir / f"{SERIES_SLUG}-{TITLE_SLUG}.pptx"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    with zipfile.ZipFile(pptx_path, "w", compression=zipfile.ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", content_types_xml(len(images)))
        package.writestr(
            "_rels/.rels",
            f'{xml_rels_root()}<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>',
        )
        package.writestr("docProps/core.xml", core_xml(now))
        package.writestr("docProps/app.xml", app_xml(len(images)))
        package.writestr("ppt/presentation.xml", presentation_xml(len(images)))
        package.writestr("ppt/_rels/presentation.xml.rels", presentation_rels_xml(len(images)))
        package.writestr("ppt/slideMasters/slideMaster1.xml", slide_master_xml())
        package.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", slide_master_rels_xml())
        package.writestr("ppt/slideLayouts/slideLayout1.xml", slide_layout_xml())
        package.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", slide_layout_rels_xml())
        package.writestr("ppt/theme/theme1.xml", theme_xml())
        package.writestr("ppt/presProps.xml", pres_props_xml())
        package.writestr("ppt/viewProps.xml", view_props_xml())
        package.writestr("ppt/tableStyles.xml", table_styles_xml())
        for index, image_path in enumerate(images, start=1):
            package.write(image_path, f"ppt/media/image{index}.png")
            package.writestr(f"ppt/slides/slide{index}.xml", slide_xml(index))
            package.writestr(f"ppt/slides/_rels/slide{index}.xml.rels", slide_rels_xml(index))
    return pptx_path


def content_types_xml(slide_count: int) -> str:
    slide_overrides = "".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, slide_count + 1)
    )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Default Extension="png" ContentType="image/png"/>
<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
<Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>
<Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>
<Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
{slide_overrides}
</Types>'''


def core_xml(now: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>{escape("第一次上幼儿园")}</dc:title><dc:creator>{escape(CREDIT)}</dc:creator>
<cp:lastModifiedBy>{escape(CREDIT)}</cp:lastModifiedBy>
<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>'''


def app_xml(slide_count: int) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>Codex</Application><PresentationFormat>3:4</PresentationFormat><Slides>{slide_count}</Slides>
</Properties>'''


def presentation_xml(slide_count: int) -> str:
    slide_ids = "".join(
        f'<p:sldId id="{255 + i}" r:id="rId{1 + i}"/>' for i in range(1, slide_count + 1)
    )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
<p:sldIdLst>{slide_ids}</p:sldIdLst>
<p:sldSz cx="{SLIDE_CX}" cy="{SLIDE_CY}" type="custom"/><p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>'''


def presentation_rels_xml(slide_count: int) -> str:
    rels = [f'{xml_rels_root()}<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
    for i in range(1, slide_count + 1):
        rels.append(
            f'<Relationship Id="rId{1 + i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
        )
    rels.extend(
        [
            f'<Relationship Id="rId{slide_count + 2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/presProps" Target="presProps.xml"/>',
            f'<Relationship Id="rId{slide_count + 3}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps" Target="viewProps.xml"/>',
            f'<Relationship Id="rId{slide_count + 4}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableStyles" Target="tableStyles.xml"/>',
        ]
    )
    rels.append("</Relationships>")
    return "".join(rels)


def slide_xml(index: int) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:cSld><p:spTree>
<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{SLIDE_CX}" cy="{SLIDE_CY}"/><a:chOff x="0" y="0"/><a:chExt cx="{SLIDE_CX}" cy="{SLIDE_CY}"/></a:xfrm></p:grpSpPr>
<p:pic><p:nvPicPr><p:cNvPr id="2" name="picture-{index}"/><p:cNvPicPr/><p:nvPr/></p:nvPicPr>
<p:blipFill><a:blip r:embed="rId1"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
<p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{SLIDE_CX}" cy="{SLIDE_CY}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>
</p:pic>
</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''


def slide_rels_xml(index: int) -> str:
    return f'{xml_rels_root()}<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/image{index}.png"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>'


def slide_master_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{SLIDE_CX}" cy="{SLIDE_CY}"/><a:chOff x="0" y="0"/><a:chExt cx="{SLIDE_CX}" cy="{SLIDE_CY}"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
<p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
<p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
<p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>'''


def slide_master_rels_xml() -> str:
    return f'{xml_rels_root()}<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/></Relationships>'


def slide_layout_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
<p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{SLIDE_CX}" cy="{SLIDE_CY}"/><a:chOff x="0" y="0"/><a:chExt cx="{SLIDE_CX}" cy="{SLIDE_CY}"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>'''


def slide_layout_rels_xml() -> str:
    return f'{xml_rels_root()}<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>'


def theme_xml() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Picturebook">
<a:themeElements><a:clrScheme name="Picturebook"><a:dk1><a:srgbClr val="2C403D"/></a:dk1><a:lt1><a:srgbClr val="F6F4EB"/></a:lt1><a:dk2><a:srgbClr val="36514F"/></a:dk2><a:lt2><a:srgbClr val="EEF1E9"/></a:lt2><a:accent1><a:srgbClr val="427E7E"/></a:accent1><a:accent2><a:srgbClr val="D88972"/></a:accent2><a:accent3><a:srgbClr val="78A66F"/></a:accent3><a:accent4><a:srgbClr val="6A8CA9"/></a:accent4><a:accent5><a:srgbClr val="B8C8D5"/></a:accent5><a:accent6><a:srgbClr val="F2D2C2"/></a:accent6><a:hlink><a:srgbClr val="427E7E"/></a:hlink><a:folHlink><a:srgbClr val="36514F"/></a:folHlink></a:clrScheme><a:fontScheme name="Picturebook"><a:majorFont><a:latin typeface="Arial"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Arial"/></a:majorFont><a:minorFont><a:latin typeface="Arial"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Arial"/></a:minorFont></a:fontScheme><a:fmtScheme name="Picturebook"><a:fillStyleLst/><a:lnStyleLst/><a:effectStyleLst/><a:bgFillStyleLst/></a:fmtScheme></a:themeElements>
</a:theme>'''


def pres_props_xml() -> str:
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentationPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>'


def view_props_xml() -> str:
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:viewPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:normalViewPr/></p:viewPr>'


def table_styles_xml() -> str:
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:tblStyleLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"/>'


def export_book(root: Path) -> int:
    images = final_image_paths(root)
    missing = [str(path.relative_to(root)) for path in images if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing composited artwork: {', '.join(missing)}")
    pdf_path = export_pdf(root, images)
    pptx_path = write_pptx(root, images)
    print(f"pdf={pdf_path}")
    print(f"pptx={pptx_path}")
    print(f"pages={len(images)} slides={len(images)}")
    return 0


def write_editable_layout(root: Path, font_path: Path) -> None:
    output = root / "layout" / "editable-layout.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    page_items = [("封面", "cover-final.png", BOOK_TITLE.replace("\n", ""))]
    page_items.extend((f"第 {page} 页", f"page-{page:02d}-final.png", PAGE_TEXT[page].replace("\n", "")) for page in range(1, 11))
    page_items.append(("家长页", "parent-guide-final.png", "给家长的话"))
    cards = "\n".join(
        f'<section class="page"><img src="../artwork/composited/{image}" alt="{html.escape(label)}"><p><strong>{html.escape(label)}</strong> {html.escape(text)}</p></section>'
        for label, image, text in page_items
    )
    output.write_text(
        f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>第一次上幼儿园 - editable layout</title>
<style>
body {{ margin: 0; font-family: "Microsoft YaHei", sans-serif; background: #eef1e9; color: #2c403d; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px; }}
.page {{ margin: 0 0 32px; padding: 0; }}
.page img {{ width: 360px; max-width: 100%; aspect-ratio: 3 / 4; object-fit: contain; display: block; box-shadow: 0 2px 10px rgba(0,0,0,.12); }}
.page p {{ font-size: 18px; line-height: 1.7; }}
.meta {{ font-size: 14px; color: #52655e; }}
</style>
</head>
<body><main>
<h1>第一次上幼儿园</h1>
<p class="meta">可编辑排版核对页。最终中文文字由本地脚本叠加，使用字体：{html.escape(str(font_path))}</p>
{cards}
</main></body></html>
''',
        encoding="utf-8",
    )


def verify(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    composited_dir = root / "artwork" / "composited"
    stems = ["cover", *[f"page-{page:02d}" for page in range(1, 11)]]
    clean_files = [clean_dir / f"{stem}-clean.png" for stem in stems]
    composited_files = [composited_dir / f"{stem}-final.png" for stem in stems]
    expected = [
        *clean_files,
        *composited_files,
        composited_dir / "parent-guide-final.png",
        root / "bible" / "storyboard-contact-sheet.png",
        root / "layout" / "editable-layout.html",
        root / "export" / f"{SERIES_SLUG}-{TITLE_SLUG}.pdf",
        root / "export" / f"{SERIES_SLUG}-{TITLE_SLUG}.pptx",
    ]
    missing = [str(path.relative_to(root)) for path in expected if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing assets: {', '.join(missing)}")

    for path in [*clean_files, *composited_files, composited_dir / "parent-guide-final.png"]:
        with Image.open(path) as image:
            if image.size != LOCKED_SIZE:
                raise ValueError(f"{path.name} has size {image.size}, expected {LOCKED_SIZE}")
            if image.mode not in {"RGB", "RGBA"}:
                raise ValueError(f"{path.name} has mode {image.mode}, expected RGB or RGBA")

    print(f"clean={len(clean_files)} composited={len(composited_files) + 1} size={LOCKED_SIZE[0]}x{LOCKED_SIZE[1]}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render and export the Diyici Shang Youeryuan picturebook")
    parser.add_argument("command", choices=("normalize", "compose", "contact-sheet", "export", "verify"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if args.command == "normalize":
        return normalize(root)
    if args.command == "compose":
        return compose(root)
    if args.command == "contact-sheet":
        return contact_sheet(root)
    if args.command == "export":
        return export_book(root)
    if args.command == "verify":
        return verify(root)
    raise AssertionError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
