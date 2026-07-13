# 《被窝里的晚安信》素材清单

## 交付根目录

`outputs/picturebooks/shenghuo-xiguan-yangcheng/beiwo-li-de-wananxin/`

## 文字与策划

- `story/story-package.md`：故事包、儿童发展安全策略与全书翻页设计。
- `story/page-script.md`：封面与 10 页分镜、无字插画提示词、文字区说明。
- `story/parent-guide.md`：亲子共读建议。
- `bible/character-bible.md`、`environment-map.md`、`color-and-style-bible.md`、`continuity-matrix.md`：连续性锁定资料。

## 插画资产

- 参考图：`artwork/reference/character-sheet.png`、`artwork/reference/environment-sheet.png`。
- 无字图：`artwork/clean/cover-clean.png` 及 `artwork/clean/page-01-clean.png` 至 `page-10-clean.png`（共 11 张）。
- 排版成图：`artwork/composited/cover-final.png` 及 `artwork/composited/page-01-final.png` 至 `page-10-final.png`（共 11 张）。
- 联系表：`bible/storyboard-contact-sheet.png`（无字）与 `bible/storyboard-final-contact-sheet.png`（排版完成）。

## 可编辑排版与验收

- `layout/text-layout.json`：中文书名、署名与每页正文的可编辑文本、位置及样式。
- `layout/editable-layout.html`：浏览器中的版式预览。
- `layout/render_book.py`：尺寸归一、文字合成、联系表和规格验证脚本。
- `qa/story-and-text-qa.md`、`qa/visual-consistency-qa.md`、`qa/ai-artifact-audit.md`：最终 QA 记录。

## 规格状态

- 无字图：11 张；排版图：11 张。
- 已验证：`clean=11 composited=11 size=1536x2048`。
- 本次未导出 PDF/PPT；如需导出，可将本目录直接交给 `picturebook-export-pdf-ppt` 流程。
