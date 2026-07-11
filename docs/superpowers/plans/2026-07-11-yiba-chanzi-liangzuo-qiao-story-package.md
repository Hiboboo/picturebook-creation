# 《一把铲子，两座桥》完整故事包与插画实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 基于已批准规格，完成《一把铲子，两座桥》的故事文本、视觉圣经、角色与环境参考图、封面和 10 张无字内页、可编辑中文排版、逐页质检与本地草稿记录更新。

**架构：** 所有绘本成果集中在 `outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/`。先完成文本与四项锁定，再用内置 `imagegen` 逐资产生成角色、环境和关键样张；关键样张经用户确认后补齐全书。中文由本地排版工具叠加到无字插画，并同步生成 `editable-layout.pptx`；本计划不导出最终 PDF，也不把 SQLite 状态改成 `completed`。

**技术栈：** Markdown、内置 `imagegen`、`view_image`、Python 3.14、Pillow、python-pptx、PowerShell、项目内 SQLite 记录脚本、Git。

---

## 实施边界

- 只使用内置 `imagegen`，不使用 CLI fallback，不要求 `OPENAI_API_KEY`。
- 每个不同资产独立调用一次 `imagegen`；不把多个不同页面作为同一提示词的变体生成。
- 图像模型只生成无字插画；中文标题、署名和正文必须由后期可编辑文本层加入。
- 所有最终资产必须复制到项目输出目录，不得只留在 `$CODEX_HOME/generated_images/`。
- 当前工作区已有 `records/` 修改、`.superpowers/` 原型和 `outputs/picturebooks/anquan-jiaoyu/` 未提交内容。任何 `git add` 都必须列出本书的精确路径，禁止使用 `git add .`。
- `records/picturebook_records.sqlite` 与 `records/records.json` 含有本任务开始前的改动；允许按技能更新，但不得在无法隔离差异时提交这两个文件。
- 图片不满足 `1536x2048` 或 3:4 比例时优先重新生成；不得靠裁切掩盖构图、肢体或安全区问题。
- 关键样张用户确认是批量生成关卡。未确认时停止在任务 5，不进入任务 6。

## 文件结构

- 创建：`requirements-picturebook.txt`
  - 职责：声明本地排版与联系表生成所需的 Pillow、python-pptx。
- 创建：`scripts/__init__.py`
  - 职责：允许标准库 `unittest` 导入排版工具。
- 创建：`scripts/render_picturebook_layout.py`
  - 职责：校验画布和文字框、生成带字 PNG、创建可编辑 PPTX 与整本联系表。
- 创建：`scripts/assert_staged_paths.py`
  - 职责：在每次提交前断言暂存区只包含本任务明确列出的白名单路径。
- 创建：`tests/test_render_picturebook_layout.py`
  - 职责：验证错误画布被拒绝、11 张排版图/PPTX/联系表能生成。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/story-package.md`
  - 职责：按故事输出契约整合基本信息、安全策略、故事设定、逐页详情、状态与素材清单。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/page-script.md`
  - 职责：保存 10 页定稿文字、汉字数、导演式构图、文字区和逐页无字插画提示词。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/parent-guide.md`
  - 职责：给家长的共读提醒、互动动作、支持性语言与禁用表达。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/character-bible.md`
  - 职责：锁定 C01-小米、C02-乐乐和两名角色的不可变/可变特征。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/environment-map.md`
  - 职责：锁定沙池、围栏、树、长椅、两桥方向、行动轴与主光源。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/color-and-style-bible.md`
  - 职责：锁定透明水彩和彩铅、色彩弧线、自然不完美、版式和视觉禁区。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/continuity-matrix.md`
  - 职责：逐页列出角色、红铲子、蓝桶、两桥、空间、镜头和光线状态。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/c01-xiaomi-reference.png`
  - 职责：小米转面与表情参考。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/c02-lele-reference.png`
  - 职责：乐乐转面与表情参考。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/sandpit-style-reference.png`
  - 职责：沙池空间、媒介、光源与色板参考。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/storyboard-contact-sheet.png`
  - 职责：并排检查封面和 10 页的镜头、色彩和连续性。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/cover-clean.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-01-clean.png` 至 `page-10-clean.png`
  - 职责：无字、统一画布的最终插画。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/cover-final.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-01-final.png` 至 `page-10-final.png`
  - 职责：加入后期中文文字的阅读版图片。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/layout/text-layout.json`
  - 职责：保存所有可编辑文字、字体、框坐标和源/目标图片路径。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/layout/editable-layout.pptx`
  - 职责：提供可编辑的中文文本层和逐页背景图。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/story-and-text-qa.md`
  - 职责：记录字数、朗读、安全、单一主题与结尾审查。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md`
  - 职责：记录角色、道具、空间、镜头、色板和文字区审查。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md`
  - 职责：逐图记录 P0/P1/P2、手部、持握、乱码和 AI 同质化审查。
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/key-sample-review.md`
  - 职责：记录封面、第 3、7、10 页关键样张的用户确认与逐项审查。
- 修改：`records/picturebook_records.sqlite`
  - 职责：保持 `draft`，补充摘要、角色、风格和输出目录。
- 修改：`records/records.json`
  - 职责：从 SQLite 刷新可读导出。

## 全局插画提示词合同

以下文本是所有封面和内页提示词必须完整包含的基线。每页只追加本计划给出的页面覆盖段，不删除基线约束。

```text
Use case: illustration-story
Asset type: clean preschool picturebook artwork, exact 3:4 portrait canvas, 1536x2048
Input images: Image 1 is the locked C01 Xiaomi character reference; Image 2 is the locked C02 Lele character reference; Image 3 is the locked kindergarten sandpit environment and style reference.
Scene/backdrop: a real Chinese kindergarten sandpit at about 10 a.m.; pale blue rounded metal fence on the north side, muted green shrubs behind it, one tree on the west side, one low wooden bench on the east side, rounded rubber sandpit border on the south side.
Characters: preserve the exact faces, hair, proportions, outfits, shoes, height relationship, and identifying details from the character references. Xiaomi stays on the left side of the action axis; Lele stays on the right side.
Style/medium: transparent watercolor washes with light colored-pencil contours, subtle natural paper variation, moderate-to-simple detail, believable preschool body weight and hand contact, hand-drawn irregularity without visual noise.
Lighting/mood: clear natural morning light from upper right toward lower left, soft transparent shadows, safe and emotionally observant, no dramatic spotlight.
Color palette: clear pale blue, muted leaf green, natural sand beige, Xiaomi coral red and gray-blue, Lele blue-green and mustard khaki, coral-red shovel and sky-blue bucket as controlled accents.
Text: no text of any kind in the generated artwork.
Constraints: preserve the left-right action axis, fixed fence/tree/bench positions, realistic sand contact, natural clothing folds, lightly sandy knees and shoe edges, a natural low-detail text area in the specified position, at least 6 percent safe margin around faces, hands, feet, tool exchange, and bridge connection.
Avoid: mature or child-inappropriate content, violence, scary imagery, coercion, shaming, grabbing, throwing sand, dangerous behavior, extra fingers, missing fingers, fused hands, extra limbs, malformed anatomy, duplicated people, face drift, outfit changes, hairstyle changes, height drift, floating bodies, impossible grip, warped perspective, flipped environment, duplicated shovel or bucket, premature bridge connection, readable signs, letters, numbers, pseudo-Chinese, logos, watermark, plastic skin, identical smiles, yellow filter, orange skin, excessive glow, random stars, decorative clutter, template-like symmetry.
```

## 任务 1：建立可测试的排版工具

**文件：**
- 创建：`requirements-picturebook.txt`
- 创建：`scripts/__init__.py`
- 创建：`scripts/render_picturebook_layout.py`
- 创建：`scripts/assert_staged_paths.py`
- 创建：`tests/test_render_picturebook_layout.py`

- [ ] **步骤 1：检查既有暂存区**

运行：

```powershell
git diff --cached --name-only
```

预期：无输出。如果有任何输出，立即停止并请用户处理；不得自行取消、覆盖或提交用户原有 staged 文件。

- [ ] **步骤 2：确认依赖尚未安装并写入依赖文件**

使用 `apply_patch` 创建：

```text
Pillow
python-pptx
```

运行：

```powershell
python -c "import PIL, pptx"
```

当前环境预期：FAIL，提示缺少 `PIL` 或 `pptx`。这是依赖安装前的基线证据。

- [ ] **步骤 3：安装排版依赖**

运行：

```powershell
python -m pip install -r requirements-picturebook.txt
```

此步骤需要网络和包安装权限；执行代理必须使用沙箱升级请求。预期：命令退出码为 `0`。

再次运行：

```powershell
python -c "import PIL, pptx; print(PIL.__version__); print(pptx.__version__)"
```

预期：输出两个版本号，退出码为 `0`。

- [ ] **步骤 4：编写失败的排版工具测试**

使用 `apply_patch` 创建空的 `scripts/__init__.py`，并创建以下完整测试文件：

```python
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from scripts.render_picturebook_layout import render_all


FONT_PATH = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")


class PicturebookLayoutRendererTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "book"
        (self.root / "artwork" / "clean").mkdir(parents=True)
        (self.root / "artwork" / "composited").mkdir(parents=True)
        (self.root / "layout").mkdir(parents=True)
        (self.root / "bible").mkdir(parents=True)

        image = Image.new("RGB", (1536, 2048), "#E7EFEA")
        image.save(self.root / "artwork" / "clean" / "cover-clean.png")
        for page in range(1, 11):
            image.save(self.root / "artwork" / "clean" / f"page-{page:02d}-clean.png")

        box = {"x": 100, "y": 100, "width": 900, "height": 260, "align": "left"}
        config = {
            "title": "一把铲子，两座桥",
            "canvas": {"width": 1536, "height": 2048, "aspect_ratio": "3:4"},
            "font": {
                "family": "Noto Sans SC",
                "file": str(FONT_PATH),
                "body_size_px": 56,
                "cover_title_size_px": 132,
                "cover_credit_size_px": 42,
                "fill": "#24383A",
                "stroke": "#F8FBF6",
                "stroke_width": 2,
                "line_spacing_px": 16,
            },
            "cover": {
                "source": "artwork/clean/cover-clean.png",
                "output": "artwork/composited/cover-final.png",
                "title_text": "一把铲子，\n两座桥",
                "credit_text": "图/文：小葫芦",
                "title_box": box,
                "credit_box": {"x": 100, "y": 430, "width": 560, "height": 90, "align": "left"},
            },
            "pages": [
                {
                    "page": page,
                    "source": f"artwork/clean/page-{page:02d}-clean.png",
                    "output": f"artwork/composited/page-{page:02d}-final.png",
                    "text": f"第{page}页",
                    "box": box,
                }
                for page in range(1, 11)
            ],
        }
        (self.root / "layout" / "text-layout.json").write_text(
            json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_render_all_creates_images_pptx_and_contact_sheet(self) -> None:
        render_all(self.root)
        self.assertTrue((self.root / "artwork" / "composited" / "cover-final.png").exists())
        self.assertEqual(
            10,
            len(list((self.root / "artwork" / "composited").glob("page-*-final.png"))),
        )
        self.assertTrue((self.root / "layout" / "editable-layout.pptx").exists())
        contact_sheet = self.root / "bible" / "storyboard-contact-sheet.png"
        self.assertTrue(contact_sheet.exists())
        self.assertGreater(Image.open(contact_sheet).width, 900)

    def test_render_all_rejects_wrong_canvas(self) -> None:
        Image.new("RGB", (1024, 1536), "white").save(
            self.root / "artwork" / "clean" / "page-03-clean.png"
        )
        with self.assertRaisesRegex(ValueError, "1536x2048"):
            render_all(self.root)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **步骤 5：运行测试并确认失败**

运行：

```powershell
python -m unittest tests.test_render_picturebook_layout -v
```

预期：ERROR，提示 `No module named 'scripts.render_picturebook_layout'`。

- [ ] **步骤 6：实现最少可用排版工具与暂存白名单工具**

使用 `apply_patch` 创建以下完整实现：

```python
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


SLIDE_WIDTH_IN = 7.5
SLIDE_HEIGHT_IN = 10.0


def _load_config(root: Path) -> dict[str, Any]:
    path = root / "layout" / "text-layout.json"
    config = json.loads(path.read_text(encoding="utf-8"))
    pages = config.get("pages", [])
    if [page.get("page") for page in pages] != list(range(1, 11)):
        raise ValueError("layout pages must be exactly 1 through 10")
    font_path = Path(config["font"]["file"])
    if not font_path.exists():
        raise ValueError(f"font file does not exist: {font_path}")
    return config


def _rgb(hex_value: str) -> tuple[int, int, int]:
    value = hex_value.lstrip("#")
    if len(value) != 6:
        raise ValueError(f"invalid color: {hex_value}")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def _open_canvas(root: Path, relative_path: str, width: int, height: int) -> Image.Image:
    path = root / relative_path
    image = Image.open(path).convert("RGB")
    if image.size != (width, height):
        raise ValueError(
            f"{relative_path} must be {width}x{height}, got {image.width}x{image.height}"
        )
    return image


def _font(config: dict[str, Any], size_key: str) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(config["font"]["file"], config["font"][size_key])


def _draw_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: dict[str, Any],
    font: ImageFont.FreeTypeFont,
    config: dict[str, Any],
) -> None:
    align = box["align"]
    spacing = config["font"]["line_spacing_px"]
    stroke_width = config["font"]["stroke_width"]
    bbox = draw.multiline_textbbox(
        (0, 0), text, font=font, spacing=spacing, align=align, stroke_width=stroke_width
    )
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    if text_width > box["width"] or text_height > box["height"]:
        raise ValueError(
            f"text does not fit box: {text!r}, text={text_width}x{text_height}, "
            f"box={box['width']}x{box['height']}"
        )
    if align == "right":
        x = box["x"] + box["width"] - text_width - bbox[0]
    elif align == "center":
        x = box["x"] + (box["width"] - text_width) / 2 - bbox[0]
    else:
        x = box["x"] - bbox[0]
    y = box["y"] + (box["height"] - text_height) / 2 - bbox[1]
    draw.multiline_text(
        (x, y),
        text,
        font=font,
        fill=_rgb(config["font"]["fill"]),
        spacing=spacing,
        align=align,
        stroke_width=stroke_width,
        stroke_fill=_rgb(config["font"]["stroke"]),
    )


def _render_pngs(root: Path, config: dict[str, Any]) -> None:
    width = config["canvas"]["width"]
    height = config["canvas"]["height"]
    cover = config["cover"]
    cover_image = _open_canvas(root, cover["source"], width, height)
    cover_draw = ImageDraw.Draw(cover_image)
    _draw_block(cover_draw, cover["title_text"], cover["title_box"], _font(config, "cover_title_size_px"), config)
    _draw_block(cover_draw, cover["credit_text"], cover["credit_box"], _font(config, "cover_credit_size_px"), config)
    cover_output = root / cover["output"]
    cover_output.parent.mkdir(parents=True, exist_ok=True)
    cover_image.save(cover_output)

    body_font = _font(config, "body_size_px")
    for page in config["pages"]:
        image = _open_canvas(root, page["source"], width, height)
        _draw_block(ImageDraw.Draw(image), page["text"], page["box"], body_font, config)
        output = root / page["output"]
        output.parent.mkdir(parents=True, exist_ok=True)
        image.save(output)


def _ppt_alignment(value: str) -> PP_ALIGN:
    return {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}[value]


def _add_ppt_text(
    slide: Any,
    text: str,
    box: dict[str, Any],
    size_px: int,
    config: dict[str, Any],
) -> None:
    canvas = config["canvas"]
    shape = slide.shapes.add_textbox(
        Inches(box["x"] / canvas["width"] * SLIDE_WIDTH_IN),
        Inches(box["y"] / canvas["height"] * SLIDE_HEIGHT_IN),
        Inches(box["width"] / canvas["width"] * SLIDE_WIDTH_IN),
        Inches(box["height"] / canvas["height"] * SLIDE_HEIGHT_IN),
    )
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
    lines = text.split("\n")
    for index, line in enumerate(lines):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.alignment = _ppt_alignment(box["align"])
        paragraph.text = line
        for run in paragraph.runs:
            run.font.name = config["font"]["family"]
            run.font.size = Pt(size_px / canvas["width"] * SLIDE_WIDTH_IN * 72)
            run.font.color.rgb = RGBColor(*_rgb(config["font"]["fill"]))
    shape.fill.background()
    shape.line.fill.background()


def _build_pptx(root: Path, config: dict[str, Any]) -> None:
    presentation = Presentation()
    presentation.slide_width = Inches(SLIDE_WIDTH_IN)
    presentation.slide_height = Inches(SLIDE_HEIGHT_IN)
    blank = presentation.slide_layouts[6]
    entries = [config["cover"], *config["pages"]]
    for entry in entries:
        slide = presentation.slides.add_slide(blank)
        slide.shapes.add_picture(
            str(root / entry["source"]), 0, 0, presentation.slide_width, presentation.slide_height
        )
        if "title_text" in entry:
            _add_ppt_text(slide, entry["title_text"], entry["title_box"], config["font"]["cover_title_size_px"], config)
            _add_ppt_text(slide, entry["credit_text"], entry["credit_box"], config["font"]["cover_credit_size_px"], config)
        else:
            _add_ppt_text(slide, entry["text"], entry["box"], config["font"]["body_size_px"], config)
    output = root / "layout" / "editable-layout.pptx"
    output.parent.mkdir(parents=True, exist_ok=True)
    presentation.save(output)


def _build_contact_sheet(root: Path, config: dict[str, Any]) -> None:
    entries = [("封面", config["cover"]["source"])] + [
        (f"第 {page['page']} 页", page["source"]) for page in config["pages"]
    ]
    columns = 4
    thumb_width = 240
    thumb_height = 320
    label_height = 36
    gap = 20
    rows = math.ceil(len(entries) / columns)
    sheet = Image.new(
        "RGB",
        (columns * thumb_width + (columns + 1) * gap, rows * (thumb_height + label_height) + (rows + 1) * gap),
        "#EDF2EF",
    )
    draw = ImageDraw.Draw(sheet)
    label_font = ImageFont.truetype(config["font"]["file"], 22)
    for index, (label, relative_path) in enumerate(entries):
        row, column = divmod(index, columns)
        x = gap + column * (thumb_width + gap)
        y = gap + row * (thumb_height + label_height + gap)
        image = Image.open(root / relative_path).convert("RGB")
        image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
        sheet.paste(image, (x + (thumb_width - image.width) // 2, y))
        draw.text((x + thumb_width / 2, y + thumb_height + 4), label, font=label_font, fill="#33483E", anchor="ma")
    output = root / "bible" / "storyboard-contact-sheet.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def render_all(root: Path) -> None:
    config = _load_config(root)
    _render_pngs(root, config)
    _build_pptx(root, config)
    _build_contact_sheet(root, config)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    render_all(args.root.resolve())


if __name__ == "__main__":
    main()
```

同时使用 `apply_patch` 创建 `scripts/assert_staged_paths.py`：

```python
from __future__ import annotations

import subprocess
import sys


def main() -> None:
    expected = sorted(path.replace("\\", "/") for path in sys.argv[1:])
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        check=True,
        capture_output=True,
        text=True,
    )
    actual = sorted(line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip())
    if actual != expected:
        print("staged path whitelist mismatch", file=sys.stderr)
        print(f"expected: {expected}", file=sys.stderr)
        print(f"actual:   {actual}", file=sys.stderr)
        raise SystemExit(1)
    print(f"staged path whitelist OK: {len(actual)} files")


if __name__ == "__main__":
    main()
```

- [ ] **步骤 7：运行排版工具测试并确认通过**

运行：

```powershell
python -m unittest tests.test_render_picturebook_layout -v
```

预期：`Ran 2 tests` 与 `OK`。

- [ ] **步骤 8：提交排版工具**

运行：

```powershell
git add -- requirements-picturebook.txt scripts/__init__.py scripts/render_picturebook_layout.py scripts/assert_staged_paths.py tests/test_render_picturebook_layout.py
git diff --cached --check
python scripts\assert_staged_paths.py requirements-picturebook.txt scripts/__init__.py scripts/render_picturebook_layout.py scripts/assert_staged_paths.py tests/test_render_picturebook_layout.py
git commit -m "feat: add editable picturebook layout renderer"
```

预期：白名单输出 `5 files`，提交只包含上述 5 个文件。

## 任务 2：创建定稿故事文本

**文件：**
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/story-package.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/page-script.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/parent-guide.md`

- [ ] **步骤 1：用 `apply_patch` 创建故事包总文档**

以 `skills/picturebook-story-design/references/story-output-contract.md` 为字段清单，以已批准规格为唯一设计来源。故事包必须明确写入：

- 当前状态：`故事与视觉设定完成，实际图片未生成`
- 实际图片生成：`否`
- 系列、书名、主题、3-4 岁、10 页、`1536x2048`、6% 安全边距和固定输出目录
- 儿童主体性：小米可以说“我还在用”，乐乐可以失望，双方没有被成人催促
- 两座桥隐喻：S01 与 S02 各自保留，直到第 9 页填缺口、第 10 页稳定相连
- 角色、道具、空间、镜头、色彩、版式和 P0/P1/P2 规则
- 封面与每页图片路径均写成精确目标路径，状态写 `未生成`
- 所有中文由后期文本层加入，图像模型不得生成文字

- [ ] **步骤 2：写入 10 页定稿正文与汉字数**

`page-script.md` 与 `story-package.md` 必须使用下表中的相同文字，不得擅自增加品德总结：

| 页码 | 定稿正文 | 汉字数 |
|---|---|---:|
| 1 | 小米在沙池里，挖一座弯弯的小桥。 | 14 |
| 2 | 乐乐也想挖。他蹲下来看看。 | 11 |
| 3 | 小米把铲子收近一点：“我还在用。” | 13 |
| 4 | 乐乐有一点点失望。 | 8 |
| 5 | “你先帮我装沙，好吗？” | 8 |
| 6 | 一铲，一桶。第一座桥慢慢长高。 | 12 |
| 7 | 小米停了一小会儿：“挖好啦，轮到你。” | 14 |
| 8 | 哗啦！桥边滑下来一点。 | 9 |
| 9 | 还差一点点。我们一起来。 | 10 |
| 10 | 两座桥碰到一起，变成一条长长的路。 | 15 |

每页同时写入：中心意思、情绪变化、儿童主体性、文字与画面分工、翻页动力、景别、机位、演员、道具状态、空间锚点、光线、文字区、全局提示词合同和对应的页面覆盖段。

- [ ] **步骤 3：写入家长指南**

`parent-guide.md` 必须包含以下确定内容：

- 核心感受：`我的需要可以被尊重，你的愿望也值得被听见。`
- 共读提醒：不要用本书追问孩子“以后会不会马上分享”，也不要比较谁更大方。
- 互动一：用两块积木模拟“两座桥”，让孩子决定中间何时连接。
- 互动二：轮流说“我还在用”“我可以等一会儿”“我们能一起玩吗”。
- 互动三：观察第 3、4、7、8 页身体动作，说出“舍不得、失望、犹豫、挫败”。
- 支持性语言：`你还在用，可以告诉他。`、`他也很想玩，我们一起想个办法。`、`你们可以先停一下，再决定。`
- 不建议语言：`快给他玩。`、`不要小气。`、`好孩子就要分享。`

- [ ] **步骤 4：验证正文与安全边界**

运行：

```powershell
python -c "import re; from pathlib import Path; p=Path(r'outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/page-script.md').read_text(encoding='utf-8'); lines=['小米在沙池里，挖一座弯弯的小桥。','乐乐也想挖。他蹲下来看看。','小米把铲子收近一点：“我还在用。”','乐乐有一点点失望。','“你先帮我装沙，好吗？”','一铲，一桶。第一座桥慢慢长高。','小米停了一小会儿：“挖好啦，轮到你。”','哗啦！桥边滑下来一点。','还差一点点。我们一起来。','两座桥碰到一起，变成一条长长的路。']; assert all(x in p for x in lines); print([len(re.findall(r'[\u4e00-\u9fff]', x)) for x in lines])"
```

预期：输出 `[14, 11, 13, 8, 8, 12, 14, 9, 10, 15]`。

运行：

```powershell
rg -n "快给他玩|不要小气|好孩子就要分享|你看别人多大方" outputs\picturebooks\pinge-yangcheng\yiba-chanzi-liangzuo-qiao\story
```

预期：只在家长指南的“不建议语言”或故事包“禁用表达”章节命中，不出现在 10 页正文中。

- [ ] **步骤 5：提交故事文本**

运行：

```powershell
git add -- outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story
git diff --cached --check
python scripts\assert_staged_paths.py outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/story-package.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/page-script.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/parent-guide.md
git commit -m "docs: add sharing picturebook story text"
```

预期：提交只包含 `story/` 下 3 个 Markdown 文件。

## 任务 3：创建视觉圣经、连续性矩阵和 QA 基线

**文件：**
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/character-bible.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/environment-map.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/color-and-style-bible.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/continuity-matrix.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/story-and-text-qa.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md`
- 修改但不提交：`records/picturebook_records.sqlite`
- 修改但不提交：`records/records.json`

- [ ] **步骤 1：写入角色、道具和演员锁定**

`character-bible.md` 必须逐字段记录：

- `C01-小米`：3.5 头身、略矮、黑色齐耳短发、左侧黄色小发夹、珊瑚红短袖、灰蓝背带裤、米白短袜、藏蓝布鞋
- `C02-乐乐`：3.5 头身、略高约 3%、黑色微卷短发、右侧弯曲刘海、蓝绿色短袖、芥末卡其短裤、米白短袜、棕色布鞋
- 表情不得只有笑；小米包含专注/防守/犹豫/松动，乐乐包含期待/失望/挫败/放松
- 固定演员只有两人，不加入教师、第三名儿童或背景复制人物
- `D01-红铲子`：珊瑚红铲面、浅木色塑料柄；第 7 页交给乐乐；第 8-10 页放在右侧
- `D02-蓝桶`：天蓝色无标识；第 8 页由小米使用；第 8-10 页放在左侧
- `S01` 从左向中心，`S02` 从右向中心；第 8 页末留一掌宽缺口，第 9 页填合，第 10 页稳定连接

- [ ] **步骤 2：写入环境地图与色彩圣经**

`environment-map.md` 必须写明北侧浅蓝围栏、西侧树、东侧长椅、南侧圆角沙池边、主机位在南、人物左右轴线、上午右上到左下主光。

`color-and-style-bible.md` 必须写明透明水彩洗色、彩铅轮廓、轻微纸感、自然沙痕、无全局黄滤镜、无塑料皮肤、无随机星光；并列出第 1-2、3-4、5-6、7-8、9-10 页的五段色彩弧线。

- [ ] **步骤 3：写入逐页连续性矩阵**

`continuity-matrix.md` 使用以下状态，不得省略任何页：

| 页码 | 小米 | 乐乐 | 红铲子 | 蓝桶 | 沙桥状态 | 镜头锚点 |
|---|---|---|---|---|---|---|
| 1 | 左侧主导 | 不出场 | 小米持握 | 不出现 | S01 半成 | 围栏、树 |
| 2 | 左侧 | 右侧进入 | 小米持握 | 乐乐右后方 | S01 半成 | 围栏、长椅 |
| 3 | 左侧近景 | 仅边缘或不出画 | 小米收近 | 不突出 | S01 未变 | 树或围栏 |
| 4 | 不主导 | 右侧近景 | 画外、仍归小米 | 乐乐身侧 | S01 未变 | 长椅 |
| 5 | 左侧 | 右侧 | 小米持握 | 两人之间偏右 | S01 待完成 | 围栏、两人视线 |
| 6 | 左侧 | 右侧 | 小米铲沙 | 乐乐倒沙 | S01 完成且略不对称 | 围栏、桥 |
| 7 | 左侧 | 右侧 | 柄朝右交接 | 右侧地面 | S01 完成，S02 未开始 | 手、桥方向 |
| 8 | 左侧修沙 | 右侧修沙 | 放在乐乐右侧 | 放在小米左侧 | S02 塌一角后修稳，中心留一掌宽 | 长椅、两桥方向 |
| 9 | 左手入画 | 右手入画 | 远右 | 远左 | 两双手填中心缺口 | 俯视、两桥 |
| 10 | 左侧坐近 | 右侧坐近 | 右侧放下 | 左侧放下 | S01/S02 稳定连接 | 围栏、树、长椅 |

- [ ] **步骤 4：建立 QA 基线**

三个 QA 文件初始状态统一写 `实际图片未生成`。`story-and-text-qa.md` 记录 10 个汉字数和朗读结果；`visual-consistency-qa.md` 记录待核对的不可变项；`ai-artifact-audit.md` 创建封面与 10 页表格，状态均为 `未生成，未审计`，并列出 P0/P1/P2 定义。

- [ ] **步骤 5：补充 SQLite 草稿元数据并导出**

运行：

```powershell
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py add --series "品格养成系列" --theme "分享" --title "一把铲子，两座桥" --status "draft" --summary "小米在沙池里表达自己还在使用红铲子，乐乐先用蓝桶参与；两人轮流并共同连接两座桥，感受到彼此需要都值得被听见。" --characters "C01-小米; C02-乐乐" --style "透明水彩与彩铅轮廓，清爽上午沙池，真实儿童小情绪，3:4竖版，1536x2048，无字插画后期中文排版" --output-dir "outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao"
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py export
```

预期：记录 ID 仍为 `3d8e7e8b12b7102a`，状态仍为 `draft`，导出记录数至少为 `9`。不要暂存两个记录文件。

- [ ] **步骤 6：验证并提交视觉圣经与 QA 基线**

运行：

```powershell
Get-ChildItem outputs\picturebooks\pinge-yangcheng\yiba-chanzi-liangzuo-qiao\bible -File | Measure-Object
Get-ChildItem outputs\picturebooks\pinge-yangcheng\yiba-chanzi-liangzuo-qiao\qa -File | Measure-Object
```

预期：`bible` 文件数为 `4`，`qa` 文件数为 `3`。

运行：

```powershell
git add -- outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/character-bible.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/environment-map.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/color-and-style-bible.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/continuity-matrix.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/story-and-text-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git diff --cached --check
python scripts\assert_staged_paths.py outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/character-bible.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/environment-map.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/color-and-style-bible.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/continuity-matrix.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/story-and-text-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git commit -m "docs: add sharing picturebook visual bible"
```

预期：提交不包含 `records/`、`.superpowers/` 或其他绘本目录。

## 任务 4：生成角色与环境参考图

**文件：**
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/c01-xiaomi-reference.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/c02-lele-reference.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/sandpit-style-reference.png`
- 修改：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md`
- 修改：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md`

- [ ] **步骤 1：生成小米角色参考图**

调用内置 `imagegen`，不传参考图，使用以下完整提示词：

```text
Use case: illustration-story
Asset type: locked preschool picturebook character reference sheet, exact 3:4 portrait, 1536x2048
Primary request: Show the same Chinese preschool girl C01 Xiaomi repeatedly on one clean reference sheet: full-body front view, three-quarter view, side view, and back view, plus six head-and-shoulder expressions for focused, protective/hesitant, observing, uncertain, relaxing, and naturally happy. No labels and no text.
Subject: about three and a half years old, 3.5-head-tall preschool proportions, gentle round face, black ear-length bob, short bangs, one naturally loose strand, small yellow hair clip on her left side, coral-red short-sleeve shirt, gray-blue overalls, off-white ankle socks, navy canvas shoes. Natural medium-light Chinese skin tone. The same exact child in every pose.
Style/medium: transparent watercolor wash with light colored-pencil contours, subtle paper variation, moderate-to-simple detail, authentic child body weight and clothing folds.
Composition: organized visual reference sheet on a clean pale blue-gray low-detail background, generous separation between poses, every hand and shoe fully visible, no cropping.
Lighting/mood: neutral soft morning studio-like daylight consistent with the book, no dramatic shadows.
Constraints: preserve one identity, one outfit, one hairstyle, one hair-clip side, consistent proportions; natural expressions, not all smiling.
Avoid: text, labels, letters, numbers, logos, watermark, duplicated limbs, extra fingers, fused hands, missing hands, face drift, outfit drift, hairstyle drift, yellow filter, orange skin, plastic 3D look, anime eyes, glossy commercial cartoon finish, decorative clutter.
```

从工具结果读取实际生成文件路径，将选定图复制为 `c01-xiaomi-reference.png`。不得覆盖同名文件；若已存在，先比较并按 `-v2` 命名，确认后再更新引用。

- [ ] **步骤 2：生成乐乐角色参考图**

调用内置 `imagegen`，不传参考图，使用以下完整提示词：

```text
Use case: illustration-story
Asset type: locked preschool picturebook character reference sheet, exact 3:4 portrait, 1536x2048
Primary request: Show the same Chinese preschool boy C02 Lele repeatedly on one clean reference sheet: full-body front view, three-quarter view, side view, and back view, plus six head-and-shoulder expressions for curious, hopeful, disappointed, waiting, frustrated, and relaxed. No labels and no text.
Subject: about three and a half years old, 3.5-head-tall preschool proportions, about three percent taller than Xiaomi, round-square face, short slightly wavy black hair with one curved fringe on his right side, muted blue-green short-sleeve shirt, mustard-khaki shorts, off-white ankle socks, brown canvas shoes. Natural medium-light Chinese skin tone. The same exact child in every pose.
Style/medium: transparent watercolor wash with light colored-pencil contours, subtle paper variation, moderate-to-simple detail, authentic child body weight and clothing folds.
Composition: organized visual reference sheet on a clean pale blue-gray low-detail background, generous separation between poses, every hand and shoe fully visible, no cropping.
Lighting/mood: neutral soft morning studio-like daylight consistent with the book, no dramatic shadows.
Constraints: preserve one identity, one outfit, one hairstyle, one curved-fringe side, consistent proportions; natural expressions, not all smiling.
Avoid: text, labels, letters, numbers, logos, watermark, duplicated limbs, extra fingers, fused hands, missing hands, face drift, outfit drift, hairstyle drift, yellow filter, orange skin, plastic 3D look, anime eyes, glossy commercial cartoon finish, decorative clutter.
```

将选定图复制为 `c02-lele-reference.png`。

- [ ] **步骤 3：生成沙池环境与风格参考图**

调用内置 `imagegen`，不传参考图，使用以下完整提示词：

```text
Use case: illustration-story
Asset type: locked preschool picturebook environment and style reference, exact 3:4 portrait, 1536x2048
Primary request: A clear establishing view of an empty real Chinese kindergarten sandpit from the south side looking north, prepared as the environment and painting-style reference for a full picturebook. No children, no sand bridges, no text.
Scene/backdrop: rectangular sandpit; pale blue rounded metal fence across the north side; muted green shrubs beyond; one tree on the west/left side casting a small soft broken shadow; one low wooden bench on the east/right side; rounded rubber sandpit border along the south foreground. Leave clear working zones on left and right that can later hold two bridges growing toward the center.
Style/medium: transparent watercolor wash with light colored-pencil contours, subtle natural paper variation, moderate-to-simple detail, believable sand texture only near important areas, hand-drawn irregularity.
Composition/framing: child-eye-level establishing view, spatial anchors fully visible, natural low-detail sky and fence zones for later text, no excessive empty wall or decorative objects.
Lighting/mood: clear 10 a.m. natural light from upper right to lower left, soft transparent shadows, fresh pale-blue and muted-green air, natural sand beige.
Constraints: fixed left tree, right bench, north fence, south rubber border, physically coherent perspective and light.
Avoid: people, animals, text, signs, letters, logos, toys, random flowers, stars, glowing particles, yellow filter, over-warm cream cast, plastic surfaces, perfect showroom cleanliness, clutter, impossible fence or bench geometry.
```

将选定图复制为 `sandpit-style-reference.png`。

- [ ] **步骤 4：逐张检查参考图**

对 3 张图分别使用 `view_image`，逐项检查：

- 角色参考是否为同一个人、同一服装、正确发夹/刘海侧、手脚完整、无文字
- 小米与乐乐身高和体型是否接近，乐乐仅略高
- 环境参考是否保持左树、右长椅、北围栏、南边框和右上主光
- 是否存在统一笑脸、塑料皮肤、黄滤镜、伪中文或装饰堆叠

任何 P0 问题必须用一次针对性重生成修正，不得靠裁切遮盖。

- [ ] **步骤 5：验证尺寸并记录生成方式**

运行：

```powershell
python -c "from pathlib import Path; from PIL import Image; root=Path(r'outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference'); files=sorted(root.glob('*.png')); assert len(files)==3; sizes={p.name:Image.open(p).size for p in files}; print(sizes); assert all(v==(1536,2048) for v in sizes.values())"
```

预期：3 张图均为 `(1536, 2048)`。在 QA 中记录使用内置 `imagegen`、实际输出路径和审查结果。

- [ ] **步骤 6：提交参考图**

运行：

```powershell
git add -- outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git diff --cached --check
python scripts\assert_staged_paths.py outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/c01-xiaomi-reference.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/c02-lele-reference.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/reference/sandpit-style-reference.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git commit -m "art: add sharing picturebook references"
```

预期：提交只包含 3 张参考图和 2 个 QA 文档更新。

## 任务 5：生成并确认四张关键样张

**文件：**
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/cover-clean.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-03-clean.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-07-clean.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-10-clean.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/key-sample-review.md`
- 修改：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md`

每次调用都使用 `referenced_image_paths`，顺序固定为小米参考、乐乐参考、沙池参考，并在全局提示词合同后追加对应覆盖段。

- [ ] **步骤 1：生成无字封面**

追加：

```text
Page-specific direction: clean front cover artwork. Xiaomi is on the left beside S01, holding the coral-red shovel; Lele is on the right beside S02 with the sky-blue bucket. The two unfinished sand bridges angle toward a visible center gap but are not connected. Their eyes and body directions gently lead toward the gap. Xiaomi looks focused with a small softening, Lele looks hopeful and patient; neither has a broad standard smile. Keep the upper 22 percent as a natural pale-sky and low-detail fence title area and reserve a small lower-right credit area. Do not show the ending and do not generate any text.
```

保存为 `cover-clean.png`。

- [ ] **步骤 2：生成第 3 页**

追加：

```text
Page-specific direction: page 3 emotional close view. Xiaomi remains on the left, drawing the shovel handle slightly closer to her body; her navy shoe toe presses gently into the sand, mouth corners tighten a little, shoulders are not aggressive. Lele is only a soft partial presence at the far right edge or just outside frame. Keep the first unfinished bridge direction and one tree-or-fence anchor visible. Natural upper-left low-detail text area. The emotion is protective hesitation, not anger, greed, or villainy.
```

保存为 `page-03-clean.png`。

- [ ] **步骤 3：生成第 7 页**

追加：

```text
Page-specific direction: page 7 key handoff close view. Xiaomi on the left has paused for one small beat and turns the shovel handle toward Lele on the right. Lele reaches with one open hand; the handle, both hands, and both natural expressions are clearly visible, with correct fingers and believable distance. S01 is complete but rough, S02 has not started. The blue bucket rests on the right. Keep a natural upper-right low-detail text area. Show willingness after hesitation, not a ceremonial or overly perfect exchange.
```

保存为 `page-07-clean.png`。

- [ ] **步骤 4：生成第 10 页**

追加：

```text
Page-specific direction: page 10 satisfying wide ending. S01 from the left and S02 from the right are now stably connected into one long sandy route. Xiaomi sits on the left and Lele sits on the right, naturally a little closer than before, with sandy knees and shoe edges, relaxed small smiles rather than cheering. The red shovel lies on the far right near Lele; the blue bucket rests on the far left near Xiaomi. Show the fixed fence, west tree, east bench, and consistent morning light. Keep a natural upper-left text area. No moral slogan and no text.
```

保存为 `page-10-clean.png`。

- [ ] **步骤 5：逐张解剖、叙事和一致性检查**

分别使用 `view_image` 检查原始分辨率。`key-sample-review.md` 对每张写：角色识别、服装、手指、持握、脚与重心、桥状态、道具位置、空间锚点、光源、色彩、文字区、乱码、AI 同质化、P0/P1/P2 结论。

运行尺寸检查：

```powershell
python -c "from pathlib import Path; from PIL import Image; root=Path(r'outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean'); names=['cover-clean.png','page-03-clean.png','page-07-clean.png','page-10-clean.png']; sizes={n:Image.open(root/n).size for n in names}; print(sizes); assert all(v==(1536,2048) for v in sizes.values())"
```

预期：4 张图均为 `(1536, 2048)`。

- [ ] **步骤 6：用户关键样张确认关卡**

在对话中并排展示 4 张实际样张，明确请用户确认角色、媒介、真实小情绪、色板、空间和手部动作。没有明确确认时停止，不生成其余 7 页。

- [ ] **步骤 7：确认后提交关键样张**

运行：

```powershell
git add -- outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/cover-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-03-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-07-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-10-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/key-sample-review.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git diff --cached --check
python scripts\assert_staged_paths.py outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/cover-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-03-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-07-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-10-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/key-sample-review.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git commit -m "art: add approved sharing picturebook samples"
```

预期：只提交 4 张已确认样张和对应 QA。

## 任务 6：生成剩余七张无字内页

**文件：**
- 创建：`artwork/clean/page-01-clean.png`
- 创建：`artwork/clean/page-02-clean.png`
- 创建：`artwork/clean/page-04-clean.png`
- 创建：`artwork/clean/page-05-clean.png`
- 创建：`artwork/clean/page-06-clean.png`
- 创建：`artwork/clean/page-08-clean.png`
- 创建：`artwork/clean/page-09-clean.png`
- 修改：`qa/ai-artifact-audit.md`
- 修改：`qa/visual-consistency-qa.md`

以下相对路径均位于 `outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/`。每页单独调用 `imagegen`，使用相同 3 张参考图和全局提示词合同。

- [ ] **步骤 1：生成第 1 页**

追加：

```text
Page-specific direction: page 1 establishing medium-wide child-eye view. Xiaomi alone on the left is absorbed in digging S01 with the red shovel; S01 is only half formed and points toward the empty center. Lele and the blue bucket are absent. Show the fixed fence and west tree, with the east bench secondary. Natural upper-left text area. Her posture shows concentration and ownership without posing for the viewer.
```

- [ ] **步骤 2：生成第 2 页**

追加：

```text
Page-specific direction: page 2 relationship medium view from just behind Lele's right shoulder. Lele enters from the right and crouches to look before asking; his blue bucket sits just behind his right side. Xiaomi remains left with the red shovel and unfinished S01. Both bodies remain on their locked sides. Natural upper-right text area, fence and east bench visible.
```

- [ ] **步骤 3：生成第 4 页**

追加：

```text
Page-specific direction: page 4 quiet reaction close view. Lele is on the right with shoulders slightly lowered, using one finger to draw a short line in the sand; he looks mildly disappointed, not devastated and not instantly cheerful. The blue bucket remains beside him. Xiaomi and the shovel may stay outside frame. Preserve the east bench as a spatial anchor and leave a natural upper-right text area.
```

- [ ] **步骤 4：生成第 5 页**

追加：

```text
Page-specific direction: page 5 balanced two-child medium view. Xiaomi on the left still holds the shovel but looks toward the blue bucket and makes a small open invitation gesture. Lele on the right listens; the bucket sits between them but slightly right. S01 is still unfinished. Their expressions show cautious possibility, not instant harmony. Natural upper-left text area.
```

- [ ] **步骤 5：生成第 6 页**

追加：

```text
Page-specific direction: page 6 medium-close view with a slight overhead angle. In the foreground, Xiaomi's red shovel makes real contact with sand while Lele tips the blue bucket so sand actually lands on S01; both full torsos and the rough first bridge remain readable in one single composition. S01 becomes complete but naturally uneven. Keep upper-right text space and preserve the fixed fence.
```

- [ ] **步骤 6：生成第 8 页**

追加：

```text
Page-specific direction: page 8 side medium view after a small collapse. S02 on the right has slipped at one edge. Lele has placed the red shovel flat on his far right; Xiaomi has placed the blue bucket on her far left. Both children use their free hands to press the bridge edge back into a stable shape, first wearing small frustrated frowns. At the end of the scene S02 remains one preschool palm-width away from S01. Keep upper-left text space and the east bench anchor.
```

- [ ] **步骤 7：生成第 9 页**

追加：

```text
Page-specific direction: page 9 overhead action close view. S01 enters from the left and S02 from the right, with a visible small center gap. Xiaomi's two hands enter from the left and Lele's two hands enter from the right to fill the gap together; all fingers are clearly separated and naturally pressing sand. The red shovel is far right and the blue bucket far left, outside the central action. Keep a clean top-center text zone. No faces are required; hands and bridge connection are the sole focus.
```

- [ ] **步骤 8：保存、检查并在需要时单页重做**

每次生成后，把选定输出复制到对应两位页码文件名，随后立即使用 `view_image` 检查。任何 P0 立即重做该页；P1 只做一次针对性重生成并复检；P2 记录到审计文件。

- [ ] **步骤 9：验证全书无字图数量与尺寸**

运行：

```powershell
python -c "from pathlib import Path; from PIL import Image; root=Path(r'outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean'); files=[root/'cover-clean.png',*sorted(root.glob('page-*-clean.png'))]; assert len(files)==11, len(files); sizes={p.name:Image.open(p).size for p in files}; print(sizes); assert all(v==(1536,2048) for v in sizes.values())"
```

预期：共 `11` 张，全部 `(1536, 2048)`。

- [ ] **步骤 10：提交全书无字图**

运行：

```powershell
git add -- outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md
git diff --cached --check
python scripts\assert_staged_paths.py outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-01-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-02-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-04-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-05-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-06-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-08-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/clean/page-09-clean.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md
git commit -m "art: complete sharing picturebook clean pages"
```

预期：提交包含 11 张无字图的最终集合和更新后的 QA，不包含记录文件或其他绘本。

## 任务 7：创建可编辑排版、带字图和联系表

**文件：**
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/layout/text-layout.json`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/layout/editable-layout.pptx`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/cover-final.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-01-final.png` 至 `page-10-final.png`
- 创建：`outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/storyboard-contact-sheet.png`

- [ ] **步骤 1：写入精确排版 JSON**

使用 `apply_patch` 创建以下完整配置：

```json
{
  "title": "一把铲子，两座桥",
  "canvas": { "width": 1536, "height": 2048, "aspect_ratio": "3:4" },
  "font": {
    "family": "Noto Sans SC",
    "file": "C:\\Windows\\Fonts\\NotoSansSC-VF.ttf",
    "body_size_px": 56,
    "cover_title_size_px": 132,
    "cover_credit_size_px": 42,
    "fill": "#24383A",
    "stroke": "#F8FBF6",
    "stroke_width": 2,
    "line_spacing_px": 16
  },
  "cover": {
    "source": "artwork/clean/cover-clean.png",
    "output": "artwork/composited/cover-final.png",
    "title_text": "一把铲子，\n两座桥",
    "credit_text": "图/文：小葫芦",
    "title_box": { "x": 100, "y": 90, "width": 860, "height": 330, "align": "left" },
    "credit_box": { "x": 105, "y": 420, "width": 500, "height": 90, "align": "left" }
  },
  "pages": [
    { "page": 1, "source": "artwork/clean/page-01-clean.png", "output": "artwork/composited/page-01-final.png", "text": "小米在沙池里，\n挖一座弯弯的小桥。", "box": { "x": 95, "y": 95, "width": 760, "height": 250, "align": "left" } },
    { "page": 2, "source": "artwork/clean/page-02-clean.png", "output": "artwork/composited/page-02-final.png", "text": "乐乐也想挖。\n他蹲下来看看。", "box": { "x": 740, "y": 95, "width": 700, "height": 250, "align": "right" } },
    { "page": 3, "source": "artwork/clean/page-03-clean.png", "output": "artwork/composited/page-03-final.png", "text": "小米把铲子收近一点：\n“我还在用。”", "box": { "x": 95, "y": 95, "width": 720, "height": 250, "align": "left" } },
    { "page": 4, "source": "artwork/clean/page-04-clean.png", "output": "artwork/composited/page-04-final.png", "text": "乐乐有一点点失望。", "box": { "x": 740, "y": 95, "width": 700, "height": 220, "align": "right" } },
    { "page": 5, "source": "artwork/clean/page-05-clean.png", "output": "artwork/composited/page-05-final.png", "text": "“你先帮我装沙，好吗？”", "box": { "x": 95, "y": 95, "width": 720, "height": 230, "align": "left" } },
    { "page": 6, "source": "artwork/clean/page-06-clean.png", "output": "artwork/composited/page-06-final.png", "text": "一铲，一桶。\n第一座桥慢慢长高。", "box": { "x": 710, "y": 90, "width": 730, "height": 260, "align": "right" } },
    { "page": 7, "source": "artwork/clean/page-07-clean.png", "output": "artwork/composited/page-07-final.png", "text": "小米停了一小会儿：\n“挖好啦，轮到你。”", "box": { "x": 700, "y": 90, "width": 740, "height": 260, "align": "right" } },
    { "page": 8, "source": "artwork/clean/page-08-clean.png", "output": "artwork/composited/page-08-final.png", "text": "哗啦！桥边滑下来一点。", "box": { "x": 95, "y": 95, "width": 720, "height": 230, "align": "left" } },
    { "page": 9, "source": "artwork/clean/page-09-clean.png", "output": "artwork/composited/page-09-final.png", "text": "还差一点点。\n我们一起来。", "box": { "x": 250, "y": 90, "width": 1036, "height": 220, "align": "center" } },
    { "page": 10, "source": "artwork/clean/page-10-clean.png", "output": "artwork/composited/page-10-final.png", "text": "两座桥碰到一起，\n变成一条长长的路。", "box": { "x": 95, "y": 95, "width": 880, "height": 260, "align": "left" } }
  ]
}
```

- [ ] **步骤 2：运行排版工具**

运行：

```powershell
python scripts\render_picturebook_layout.py --root outputs\picturebooks\pinge-yangcheng\yiba-chanzi-liangzuo-qiao
```

预期：退出码 `0`，生成 11 张带字 PNG、`editable-layout.pptx` 和 `storyboard-contact-sheet.png`。如果文字超出框或画布不符，脚本必须失败并报告具体页面，不得缩小到 56 px 以下绕过。

- [ ] **步骤 3：检查联系表和 11 张带字图**

使用 `view_image` 查看原始尺寸的 `storyboard-contact-sheet.png`，再逐张抽查封面、第 3、7、9、10 页带字图。确认：

- 标题、署名和正文无错字、乱码或截断
- 文字不遮挡脸、手、脚、铲子交接和桥中心
- 文字区与设计锁定一致
- 无固定大背板，2 px 浅描边不破坏画面
- PPTX 共 11 页，背景与 PNG 页序一致

- [ ] **步骤 4：验证排版产物**

运行：

```powershell
python -c "from pathlib import Path; from PIL import Image; root=Path(r'outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao'); files=[root/'artwork/composited/cover-final.png',*sorted((root/'artwork/composited').glob('page-*-final.png'))]; assert len(files)==11; assert all(Image.open(p).size==(1536,2048) for p in files); assert (root/'layout/editable-layout.pptx').exists(); assert (root/'bible/storyboard-contact-sheet.png').exists(); print('11 composited images, editable PPTX, contact sheet: OK')"
```

预期：输出 `11 composited images, editable PPTX, contact sheet: OK`。

- [ ] **步骤 5：提交排版产物**

运行：

```powershell
git add -- outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/layout outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/storyboard-contact-sheet.png
git diff --cached --check
python scripts\assert_staged_paths.py outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/layout/text-layout.json outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/layout/editable-layout.pptx outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/cover-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-01-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-02-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-03-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-04-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-05-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-06-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-07-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-08-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-09-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/artwork/composited/page-10-final.png outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/bible/storyboard-contact-sheet.png
git commit -m "feat: add editable sharing picturebook layout"
```

预期：提交只包含排版 JSON、PPTX、联系表和 11 张带字图。

## 任务 8：完成全书 QA、记录更新与交付验证

**文件：**
- 修改：`story/story-package.md`
- 修改：`qa/story-and-text-qa.md`
- 修改：`qa/visual-consistency-qa.md`
- 修改：`qa/ai-artifact-audit.md`
- 修改但不提交：`records/picturebook_records.sqlite`
- 修改但不提交：`records/records.json`

- [ ] **步骤 1：把故事包状态更新为实际完成范围**

更新为：

- 当前状态：`排版完成，质检完成，PDF/PPT 导出未执行`
- 实际图片生成：`是`
- 生成方式：`内置 imagegen 生成无字插画，人工逐页审查，Pillow 与 python-pptx 后期加入可编辑中文`
- 11 张无字路径、11 张带字路径、参考图、PPTX、联系表和 QA 路径均写精确相对路径
- `export/` 明确写 `未生成；本计划不包含 PDF/PPT 最终导出`

- [ ] **步骤 2：完成故事、视觉和 AI 审计**

`story-and-text-qa.md` 必须给出 10 页汉字数、朗读结论和禁用语言检查。`visual-consistency-qa.md` 必须逐页写角色/服装/道具/空间/光线/镜头/文字区结果。`ai-artifact-audit.md` 必须逐图写手部、解剖、持握、重心、乱码、同质化、P0/P1/P2 和最终可交付结论。

任何 P0 必须回到对应图像步骤重做；任何 P1 必须修正后复检。不得在审计表中把未处理问题标成通过。

- [ ] **步骤 3：运行完整自动验证**

运行：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

预期：所有现有测试与新增 2 项排版测试通过，输出末尾为 `OK`。

运行：

```powershell
python -c "from pathlib import Path; from PIL import Image; root=Path(r'outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao'); clean=[root/'artwork/clean/cover-clean.png',*sorted((root/'artwork/clean').glob('page-*-clean.png'))]; final=[root/'artwork/composited/cover-final.png',*sorted((root/'artwork/composited').glob('page-*-final.png'))]; refs=sorted((root/'bible/reference').glob('*.png')); assert len(clean)==11; assert len(final)==11; assert len(refs)==3; assert all(Image.open(p).size==(1536,2048) for p in clean+final+refs); print('25 PNG assets have exact canvas')"
```

预期：输出 `25 PNG assets have exact canvas`。

运行：

```powershell
python -c "from pathlib import Path; root=Path(r'outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao'); required=['story/story-package.md','story/page-script.md','story/parent-guide.md','bible/character-bible.md','bible/environment-map.md','bible/color-and-style-bible.md','bible/continuity-matrix.md','bible/storyboard-contact-sheet.png','layout/text-layout.json','layout/editable-layout.pptx','qa/story-and-text-qa.md','qa/visual-consistency-qa.md','qa/ai-artifact-audit.md']; missing=[p for p in required if not (root/p).exists()]; assert not missing, missing; print('required package files: OK')"
```

预期：输出 `required package files: OK`。

- [ ] **步骤 4：刷新 SQLite 草稿记录**

再次运行任务 3 的 `add` 命令，保持 `--status "draft"`，随后运行 `export`。再运行：

```powershell
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py check --series "品格养成系列" --theme "分享" --title "一把铲子，两座桥"
```

预期：`duplicate: true`，唯一匹配 ID 为 `3d8e7e8b12b7102a`，状态为 `draft`，摘要、角色、风格和输出路径完整。最终 PDF/PPT 尚未导出，因此不得改为 `completed`。

- [ ] **步骤 5：提交最终 QA 与故事包状态**

运行：

```powershell
git add -- outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/story-package.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/story-and-text-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git diff --cached --check
python scripts\assert_staged_paths.py outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/story/story-package.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/story-and-text-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/visual-consistency-qa.md outputs/picturebooks/pinge-yangcheng/yiba-chanzi-liangzuo-qiao/qa/ai-artifact-audit.md
git commit -m "docs: complete sharing picturebook QA"
```

预期：提交不包含 `records/`、`.superpowers/`、`outputs/picturebooks/anquan-jiaoyu/` 或其他无关路径。

- [ ] **步骤 6：最终人工核对与交付说明**

最终回复必须列出：

- 故事包、联系表、无字图、带字图和可编辑 PPTX 的项目内绝对路径
- 内置 `imagegen` 的使用说明和实际参考图路径
- 自动测试与尺寸验证的实际输出
- P0/P1/P2 最终数量
- 草稿记录仍为 `draft`，原因是未执行 `picturebook-export-pdf-ppt`
- 仍未提交的记录文件和用户原有工作区内容，不得暗示工作区完全干净

## 计划自检

- 已覆盖批准规格中的故事、儿童主体性、角色、道具、空间、色彩、版式、关键样张、全书出图、中文后期排版和 QA。
- 每个图像资产都有精确目标路径、独立调用规则、参考图顺序、完整基线提示词和页面覆盖段。
- 第 8 页已明确工具落点、双手修沙和页末一掌宽缺口；第 9 页承接一致。
- 全部 10 页正文、汉字数、文字框坐标与 56 px 字号已锁定。
- 排版脚本使用标准库 `unittest` 做失败与通过验证，不依赖当前缺失的 pytest。
- 记录更新保持 `draft`，与“PDF/PPT 完成后才标记 completed”的项目规则一致。
- 所有提交命令都使用精确路径，避免纳入现有脏工作区中的无关修改。
- 计划中没有未决设计项、未定义目标文件名或省略式实现步骤；运行时文件枚举仅用于数量与尺寸验证。
