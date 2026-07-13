from __future__ import annotations

import argparse
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


LOCKED_SIZE = (1536, 2048)
TARGET_RATIO = LOCKED_SIZE[0] / LOCKED_SIZE[1]

PAGE_TEXT = {
    1: "泥土里，\n小种子睡着了。",
    2: "滴答，滴答。\n雨点来敲门。",
    3: "喝饱水，\n小种子裂开啦。",
    4: "小白根，\n先往下伸一伸。",
    5: "小嫩芽，\n再往上顶一顶。",
    6: "太阳照一照，\n两片小叶张开了。",
    7: "雨点来，太阳照。\n真叶一片片长。",
    8: "茎长高了，\n小花苞也来了。",
    9: "一片，两片……\n花开了！",
}

PAGE_SIDE = {1: "left", 2: "right", 3: "left", 4: "right", 5: "left", 6: "right", 7: "left", 8: "right", 9: "left"}
LIGHT_TEXT_PAGES = {3, 4}


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
) -> None:
    draw = ImageDraw.Draw(image)
    box = draw.multiline_textbbox((0, 0), text, font=font, spacing=18, stroke_width=3)
    width = box[2] - box[0]
    left = 120 if side == "left" else LOCKED_SIZE[0] - 120 - width
    draw.multiline_text(
        (left, top),
        text,
        font=font,
        fill=fill,
        spacing=18,
        stroke_width=3,
        stroke_fill=stroke_fill,
    )


def compose(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    output_dir = root / "artwork" / "composited"
    output_dir.mkdir(parents=True, exist_ok=True)
    expected = [clean_dir / "cover-clean.png", *[clean_dir / f"page-{page:02d}-clean.png" for page in range(1, 10)]]
    missing = [path.name for path in expected if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing clean artwork: {', '.join(missing)}")

    font_path = resolve_font_path()
    body_font = load_font(font_path, 72)
    title_font = load_font(font_path, 180)
    credit_font = load_font(font_path, 46)

    with Image.open(clean_dir / "cover-clean.png") as source:
        cover = source.convert("RGB")
    if cover.size != LOCKED_SIZE:
        raise ValueError(f"cover-clean.png must be {LOCKED_SIZE}, got {cover.size}")
    draw_multiline(cover, "花开了", title_font, "left", 130, (48, 61, 54), (244, 241, 228))
    ImageDraw.Draw(cover).text(
        (120, LOCKED_SIZE[1] - 150),
        "图/文：小葫芦",
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
            fill, stroke = (48, 61, 54), (246, 243, 232)
        draw_multiline(rendered, text, body_font, PAGE_SIDE[page], 145, fill, stroke)
        rendered.save(output_dir / f"page-{page:02d}-final.png", optimize=True)

    (root / "layout").mkdir(parents=True, exist_ok=True)
    (root / "layout" / "font-used.txt").write_text(str(font_path), encoding="utf-8")
    print(f"composited=10 font={font_path}")
    return 0


def contact_sheet(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    items = [("封面", clean_dir / "cover-clean.png")]
    items.extend((f"第 {page} 页", clean_dir / f"page-{page:02d}-clean.png") for page in range(1, 10))
    missing = [path.name for _, path in items if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing clean artwork: {', '.join(missing)}")

    sheet = Image.new("RGB", (1350, 760), "#eef1e9")
    draw = ImageDraw.Draw(sheet)
    label_font = load_font(resolve_font_path(), 30)
    for index, (label, path) in enumerate(items):
        row, column = divmod(index, 5)
        cell_left = 50 + column * 250
        cell_top = 30 + row * 350
        with Image.open(path) as source:
            thumb = ImageOps.fit(source.convert("RGB"), (230, 307), method=Image.Resampling.LANCZOS)
        sheet.paste(thumb, (cell_left + 10, cell_top + 38))
        label_box = draw.textbbox((0, 0), label, font=label_font)
        label_width = label_box[2] - label_box[0]
        draw.text(
            (cell_left + (250 - label_width) // 2, cell_top),
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


def verify(root: Path) -> int:
    clean_dir = root / "artwork" / "clean"
    composited_dir = root / "artwork" / "composited"
    stems = ["cover", *[f"page-{page:02d}" for page in range(1, 10)]]
    clean_files = [clean_dir / f"{stem}-clean.png" for stem in stems]
    composited_files = [composited_dir / f"{stem}-final.png" for stem in stems]
    expected = [*clean_files, *composited_files, root / "bible" / "storyboard-contact-sheet.png"]
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
    parser = argparse.ArgumentParser(description="Render the Hua Kai Le picturebook")
    parser.add_argument("command", choices=("normalize", "compose", "contact-sheet", "verify"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "normalize":
        return normalize(args.root.resolve())
    if args.command == "compose":
        return compose(args.root.resolve())
    if args.command == "contact-sheet":
        return contact_sheet(args.root.resolve())
    if args.command == "verify":
        return verify(args.root.resolve())
    raise AssertionError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
