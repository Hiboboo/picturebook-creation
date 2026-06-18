# picturebook-creation

> 面向 2-6 岁幼儿绘本创作的本地工作流与 Codex 技能包，用于从选题、查重、故事设计到 PDF/PPTX 交付的完整流程管理。

## 项目用途

这个仓库整理了一套幼儿绘本创作方法和可复用的 Codex 技能，适合用于：

- 规划原创幼儿绘本系列和选题方向。
- 在创作前检查本地绘本记录，避免重复标题或重复主题。
- 生成符合低龄儿童阅读特点的故事包，包括封面、内页页表、图像提示词、亲子互动和适读年龄。
- 将完成后的故事包导出为 PDF 和 PPTX 交付物。

仓库中的 `绘本创作源.md` 记录了幼儿绘本常见主题方向，包括生活习惯、情绪管理、入园社交、认知启蒙、自然科普、传统文化、安全教育、亲情表达、想象冒险和品格养成等。

## 目录结构

```text
.
├── README.md
├── 绘本创作源.md
└── skills/
    ├── picturebook-check-local-record/
    ├── picturebook-story-design/
    └── picturebook-export-pdf-ppt/
```

## 技能说明

| 技能 | 用途 |
| --- | --- |
| `picturebook-check-local-record` | 在创作前查询和登记本地绘本记录，避免重复创作。 |
| `picturebook-story-design` | 设计幼儿绘本故事包，包含故事设定、角色设定、页表、构图说明和安全自检。 |
| `picturebook-export-pdf-ppt` | 将完成的故事包整理并导出为 PDF 和 PPTX。 |

## 使用方式

### 1. 安装技能

将 `skills/` 下的三个技能目录复制到你的 Codex 技能目录：

```powershell
Copy-Item -Recurse -Force .\skills\picturebook-check-local-record $env:USERPROFILE\.codex\skills\
Copy-Item -Recurse -Force .\skills\picturebook-story-design $env:USERPROFILE\.codex\skills\
Copy-Item -Recurse -Force .\skills\picturebook-export-pdf-ppt $env:USERPROFILE\.codex\skills\
```

如果你在当前仓库中直接维护技能，可以把这里作为技能源目录，再按需同步到 Codex 的技能目录。

### 2. 创作前查重

当你准备创建新的绘本故事时，先使用 `picturebook-check-local-record` 检查本地记录。默认记录文件位于：

```text
~/.codex/picturebook-records/picturebook-records.json
```

也可以通过环境变量指定项目内记录文件：

```powershell
$env:PICTUREBOOK_RECORDS_PATH = "D:\codex-projects\picturebook-creation\picturebook-records.json"
```

### 3. 设计故事包

使用 `picturebook-story-design` 生成完整故事包。故事包应包含：

- 故事设定卡。
- 角色设定卡。
- 封面和每页内页的构图说明。
- 每页故事文字及文字嵌入位置。
- 图像提示词和安全负面提示词。
- 这个故事想告诉孩子什么。
- 亲子互动建议。
- 适合幼儿年龄。

### 4. 导出 PDF/PPTX

故事包完成后，使用 `picturebook-export-pdf-ppt` 输出交付物。默认输出目录约定为：

```text
output/picturebooks/<series-slug>/<title-slug>/
```

导出阶段应直接使用已经完成的封面和内页图片，不重新生成或替换图片。PDF 与 PPTX 的页序、图片和文字应保持一致。

## 推荐工作流

1. 从 `绘本创作源.md` 选择系列方向和主题。
2. 使用 `picturebook-check-local-record` 查重并登记草稿。
3. 使用 `picturebook-story-design` 生成故事包。
4. 自检儿童安全、故事节奏、角色一致性和页面构图。
5. 使用 `picturebook-export-pdf-ppt` 生成 PDF 和 PPTX。
6. 将本地记录更新为 `completed`，并写入输出目录。

## 创作原则

- 面向 2-6 岁幼儿，语言要短、清楚、适合朗读。
- 一本故事只聚焦一个核心主题，避免说教和过高知识密度。
- 每页只承载一个明确动作或情绪，并保持页与页之间有推进。
- 画面和角色必须保持一致，避免每页重新发明角色或场景。
- 内容必须温和、安全，不包含暴力、恐吓、危险模仿或儿童不宜内容。

## 版本管理

本仓库适合使用 `main` 作为主分支。推荐提交信息使用约定式格式，例如：

```text
docs: add project readme
```

新增技能、修改故事规范或调整导出流程时，建议分别提交，保持历史记录清晰。
