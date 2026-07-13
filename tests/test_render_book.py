from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / "outputs"
    / "picturebooks"
    / "dongwu-yu-ziran-kepu"
    / "zhiwu-shengzhang-hua-kai-le"
    / "layout"
    / "render_book.py"
)


def run_render_book(command: str, root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), command, "--root", str(root)],
        check=False,
        capture_output=True,
        text=True,
    )


def test_normalize_writes_locked_picturebook_dimensions(tmp_path: Path) -> None:
    clean = tmp_path / "artwork" / "clean"
    clean.mkdir(parents=True)
    source = clean / "cover-clean.png"
    Image.new("RGB", (100, 150), "#ddeeff").save(source)

    result = run_render_book("normalize", tmp_path)

    assert result.returncode == 0, result.stderr
    with Image.open(source) as image:
        assert image.size == (1536, 2048)
        assert image.mode == "RGB"


def test_compose_creates_ten_text_layer_previews(tmp_path: Path) -> None:
    clean = tmp_path / "artwork" / "clean"
    clean.mkdir(parents=True)
    filenames = ["cover-clean.png", *[f"page-{page:02d}-clean.png" for page in range(1, 10)]]
    for filename in filenames:
        Image.new("RGB", (1536, 2048), "#dceaf0").save(clean / filename)

    result = run_render_book("compose", tmp_path)

    assert result.returncode == 0, result.stderr
    composited = tmp_path / "artwork" / "composited"
    outputs = sorted(composited.glob("*.png"))
    assert len(outputs) == 10
    with Image.open(clean / "page-01-clean.png") as source, Image.open(
        composited / "page-01-final.png"
    ) as rendered:
        assert rendered.size == (1536, 2048)
        assert ImageChops.difference(source, rendered).getbbox() is not None


def test_contact_sheet_has_cover_and_nine_pages(tmp_path: Path) -> None:
    clean = tmp_path / "artwork" / "clean"
    clean.mkdir(parents=True)
    filenames = ["cover-clean.png", *[f"page-{page:02d}-clean.png" for page in range(1, 10)]]
    for index, filename in enumerate(filenames):
        Image.new("RGB", (1536, 2048), (180 + index, 210, 220)).save(clean / filename)

    result = run_render_book("contact-sheet", tmp_path)

    assert result.returncode == 0, result.stderr
    sheet = tmp_path / "bible" / "storyboard-contact-sheet.png"
    assert sheet.is_file()
    with Image.open(sheet) as image:
        assert image.size == (1350, 760)


def test_verify_accepts_complete_locked_asset_set(tmp_path: Path) -> None:
    clean = tmp_path / "artwork" / "clean"
    composited = tmp_path / "artwork" / "composited"
    bible = tmp_path / "bible"
    clean.mkdir(parents=True)
    composited.mkdir(parents=True)
    bible.mkdir(parents=True)
    Image.new("RGB", (1350, 760), "white").save(bible / "storyboard-contact-sheet.png")
    for stem in ["cover", *[f"page-{page:02d}" for page in range(1, 10)]]:
        Image.new("RGB", (1536, 2048), "#dceaf0").save(clean / f"{stem}-clean.png")
        Image.new("RGB", (1536, 2048), "#dceaf0").save(composited / f"{stem}-final.png")

    result = run_render_book("verify", tmp_path)

    assert result.returncode == 0, result.stderr
    assert "clean=10" in result.stdout
    assert "composited=10" in result.stdout
