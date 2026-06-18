---
name: picturebook-export-pdf-ppt
description: Use when a completed preschool picturebook story package, cover image, page images, story text, moral text, parent-child interaction text, or age guidance must be turned into PDF and PPT/PPTX deliverables, exported files, slide decks, print-ready pages, or matching storybook documents.
---

# 绘本 PDF/PPT 输出

## 前置条件

需要已有完整故事包：封面完整图片、每页完整图片、每页故事文字、故事想告诉孩子什么、亲子互动、适合幼儿年龄。缺少故事包时，先使用 `picturebook-story-design`。

导出前读取 `references/delivery-spec.md`。

## 输出原则

- 同时交付 PDF 和 PPTX。用户说 PPT 时，输出 `.pptx`。
- PDF 与 PPTX 的页序、文字、图片必须一致。
- 封面署名固定为 `图/文：小葫芦`；不要使用其他作者名或署名。
- 导出阶段不再生成、重绘、替换或扩写图片；直接引用 `picturebook-story-design` 已生成的封面完整图片和每页完整图片。
- 每张故事图片应作为对应页面的主画面完整放入文档，保持原图比例和核心内容，不裁掉书名、署名、角色脸部、故事文字或关键动作。
- 如果故事文字已经嵌入图片，默认不要另行重复叠加文字；仅在用户或故事包明确要求可编辑文本层时添加覆盖层。
- 末尾加入家长页：`这个故事想告诉孩子什么`、`亲子互动`、`适合幼儿年龄`。
- 文件放在当前仓库下：`outputs/picturebooks/<series-slug>/<title-slug>/`。

## 推荐工具

- PDF：优先使用 `minimax-pdf`，因为它适合重视视觉质量的绘本 PDF。
- PPTX：使用 `pptx-generator`。
- 如果需要从图片精确排版，使用本地脚本或 PptxGenJS/HTML 生成中间版，但只能整理已有图片和文字，不得调用图片生成工具重新生成画面。

## 导出流程

1. 规范化素材清单：封面完整图片、按页码排序的内页完整图片、页文、家长页文字。
2. 校验图片顺序：封面第一；内页按故事页码逐一排列；最后是家长页。优先使用故事包记录的顺序；没有记录时按文件名中的页码自然排序，如 `page-01`、`page-02`、`page-03`。
3. 逐页整理到最终文档：第 1 页放封面完整图片；第 2 页起依次放每一张内页完整图片；最后一页放家长页文字。
4. 输出 PDF。
5. 输出 PPTX。
6. 验证文件存在、页数/幻灯片数正确、封面书名和署名 `图/文：小葫芦` 正确、所有图片均按顺序出现且未被错误裁切。
7. 使用 `picturebook-check-local-record` 更新本地记录为 `completed`，写入输出目录。

## 完成回复

交付时用中文列出：

- PDF 文件路径。
- PPTX 文件路径。
- 页数/幻灯片数。
- 本地记录已更新的位置。
