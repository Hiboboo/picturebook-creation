from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


LOCKED_SIZE = (1536, 2048)
TARGET_RATIO = LOCKED_SIZE[0] / LOCKED_SIZE[1]


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
        image = source.convert("RGB").crop(center_crop_box(*source.size))
        image = image.resize(LOCKED_SIZE, Image.Resampling.LANCZOS)
        temporary = path.with_suffix(".normalized.png")
        image.save(temporary, format="PNG", optimize=True)
    temporary.replace(path)


def normalize(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    expected = [clean_dir / "cover-clean.png", *[clean_dir / f"page-{page:02d}-clean.png" for page in range(1, 11)]]
    missing = [path.name for path in expected if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing clean artwork: {', '.join(missing)}")
    for path in expected:
        normalize_image(path)
    print(f"normalized={len(expected)} size={LOCKED_SIZE[0]}x{LOCKED_SIZE[1]}")
    return 0


def font_candidates() -> list[Path]:
    candidates: list[Path] = []
    if configured := os.environ.get("PICTUREBOOK_FONT"):
        candidates.append(Path(configured))
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


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, width: int) -> str:
    lines: list[str] = []
    for source_line in text.split("\n"):
        current = ""
        for char in source_line:
            candidate = current + char
            if current and draw.textlength(candidate, font=font) > width:
                lines.append(current)
                current = char
            else:
                current = candidate
        if current:
            lines.append(current)
    return "\n".join(lines)


def draw_text_layer(image: Image.Image, text: str, box: dict[str, int | str], font_path: Path, fill: str, stroke: str) -> None:
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(str(font_path), int(box["fontSize"]))
    rendered = wrap_text(draw, text, font, int(box["width"]))
    spacing = int(box.get("lineSpacing", 12))
    x = int(box["x"])
    y = int(box["y"])
    align = str(box.get("align", "left"))
    draw.multiline_text(
        (x, y),
        rendered,
        font=font,
        fill=fill,
        spacing=spacing,
        align=align,
        stroke_width=2,
        stroke_fill=stroke,
    )


def load_layout(root: Path) -> dict:
    layout_path = root / "layout" / "text-layout.json"
    return json.loads(layout_path.read_text(encoding="utf-8"))


def compose(root: Path) -> int:
    layout = load_layout(root)
    clean_dir = root / "artwork" / "clean"
    output_dir = root / "artwork" / "composited"
    output_dir.mkdir(parents=True, exist_ok=True)
    font_path = resolve_font_path()

    cover_source = clean_dir / "cover-clean.png"
    with Image.open(cover_source) as source:
        cover = source.convert("RGB")
    if cover.size != LOCKED_SIZE:
        raise ValueError(f"{cover_source.name} must be {LOCKED_SIZE}, got {cover.size}")
    draw_text_layer(cover, layout["cover"]["title"], layout["cover"]["titleBox"], font_path, "#314A63", "#F1F0EA")
    draw_text_layer(cover, layout["cover"]["credit"], layout["cover"]["creditBox"], font_path, "#514542", "#F1F0EA")
    cover.save(output_dir / "cover-final.png", optimize=True)

    for item in layout["pages"]:
        page = str(item["page"])
        source_path = clean_dir / f"page-{page}-clean.png"
        with Image.open(source_path) as source:
            image = source.convert("RGB")
        if image.size != LOCKED_SIZE:
            raise ValueError(f"{source_path.name} must be {LOCKED_SIZE}, got {image.size}")
        if page == "10":
            fill, stroke = "#F4F3EE", "#314A63"
        else:
            fill, stroke = "#514542", "#F1F0EA"
        draw_text_layer(image, item["text"], item["box"], font_path, fill, stroke)
        image.save(output_dir / f"page-{page}-final.png", optimize=True)

    (root / "layout" / "font-used.txt").write_text(str(font_path), encoding="utf-8")
    print(f"composited=11 font={font_path}")
    return 0


def contact_sheet(root: Path, source: str) -> int:
    if source not in {"clean", "composited"}:
        raise ValueError("source must be clean or composited")
    source_dir = root / "artwork" / source
    suffix = "-clean.png" if source == "clean" else "-final.png"
    items = [("封面", source_dir / f"cover{suffix}")]
    items.extend((f"第 {page} 页", source_dir / f"page-{page:02d}{suffix}") for page in range(1, 11))
    missing = [path.name for _, path in items if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing {source} artwork: {', '.join(missing)}")

    columns, cell_w, cell_h = 4, 340, 490
    rows = (len(items) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_w + 80, rows * cell_h + 50), "#E7EAEC")
    draw = ImageDraw.Draw(sheet)
    label_font = ImageFont.truetype(str(resolve_font_path()), 30)
    for index, (label, path) in enumerate(items):
        row, column = divmod(index, columns)
        left = 40 + column * cell_w
        top = 25 + row * cell_h
        with Image.open(path) as source_image:
            thumb = ImageOps.fit(source_image.convert("RGB"), (290, 387), method=Image.Resampling.LANCZOS)
        sheet.paste(thumb, (left + 5, top + 48))
        label_width = draw.textbbox((0, 0), label, font=label_font)[2]
        draw.text((left + (300 - label_width) // 2, top + 4), label, font=label_font, fill="#314A63")
    output = root / "bible" / ("storyboard-contact-sheet.png" if source == "clean" else "storyboard-final-contact-sheet.png")
    sheet.save(output, optimize=True)
    print(f"contact_sheet={output}")
    return 0


def verify(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    composited_dir = root / "artwork" / "composited"
    stems = ["cover", *[f"page-{page:02d}" for page in range(1, 11)]]
    clean_files = [clean_dir / f"{stem}-clean.png" for stem in stems]
    composited_files = [composited_dir / f"{stem}-final.png" for stem in stems]
    expected = [*clean_files, *composited_files, root / "bible" / "storyboard-contact-sheet.png", root / "bible" / "storyboard-final-contact-sheet.png"]
    missing = [str(path.relative_to(root)) for path in expected if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing assets: {', '.join(missing)}")
    for path in [*clean_files, *composited_files]:
        with Image.open(path) as image:
            if image.size != LOCKED_SIZE:
                raise ValueError(f"{path.name} has size {image.size}, expected {LOCKED_SIZE}")
            if image.mode not in {"RGB", "RGBA"}:
                raise ValueError(f"{path.name} has mode {image.mode}, expected RGB or RGBA")
    print(f"clean={len(clean_files)} composited={len(composited_files)} size={LOCKED_SIZE[0]}x{LOCKED_SIZE[1]}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the Beiwo Li De Wananxin picturebook")
    parser.add_argument("command", choices=("normalize", "compose", "contact-sheet", "verify"))
    parser.add_argument("--source", choices=("clean", "composited"), default="clean")
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
        return contact_sheet(root, args.source)
    if args.command == "verify":
        return verify(root)
    raise AssertionError("Unsupported command")


if __name__ == "__main__":
    raise SystemExit(main())
