# 《妈妈一直在》故事包实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 基于已批准规格，创建《妈妈一直在》的完整文本故事包、视觉圣经、连续性矩阵、QA 文件，并更新本地记录摘要。

**架构：** 输出集中在 `outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/`。故事正文、逐页脚本和家长指南放在 `story/`；角色、环境、色板和连续性放在 `bible/`；故事与视觉 QA 放在 `qa/`。不生成实际图片，只提供无字插画提示词和明确的未生成状态。

**技术栈：** Markdown 文档、项目内 SQLite 记录脚本、PowerShell 路径检查。

---

## 文件结构

- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/story/story-package.md`
  - 职责：按故事输出契约整合交付状态、基本信息、儿童安全策略、故事设定、镜头计划、封面与逐页详情、QA 和素材清单。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/story/page-script.md`
  - 职责：提供可直接用于后续排版和插画制作的逐页正文、画面重点和无字插画提示词。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/story/parent-guide.md`
  - 职责：给家长的共读提醒、互动问题和支持性语言。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/bible/character-bible.md`
  - 职责：锁定小米、妈妈、服装、表情范围和禁改项。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/bible/environment-map.md`
  - 职责：锁定客厅到厨房的空间、行动路线、门口安全边界和镜头轴线。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/bible/color-and-style-bible.md`
  - 职责：锁定温暖水彩家庭感、色板、版式和无字插画规则。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/bible/continuity-matrix.md`
  - 职责：逐页列出角色、道具、空间、光线和镜头连续性。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/qa/story-and-text-qa.md`
  - 职责：检查年龄、字数、朗读、安全语言和单一主题。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/qa/visual-consistency-qa.md`
  - 职责：检查角色、道具、空间、色板、镜头和文字区规则。
- 创建：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai/qa/ai-artifact-audit.md`
  - 职责：标明图片未生成，并列出后续出图必须审计的 P0/P1/P2 项。
- 修改：`records/picturebook_records.sqlite`
  - 职责：保留 draft 状态，补充摘要、主角、风格和输出目录。
- 修改：`records/records.json`
  - 职责：导出 SQLite 记录，便于人工审查。

## 任务 1：创建故事文本文件

- [x] **步骤 1：写入故事包总文档**

写入完整契约字段：交付状态、基本信息、儿童发展策略、故事设定卡、全书镜头表、封面说明、10 个内页字段、全书质量审计、家长文字、交付准备。

- [x] **步骤 2：写入逐页脚本文档**

每页包含：正文、汉字数、画面中心、镜头、文字区、角色锁定、道具状态、无字插画提示词和负面提示词。

- [x] **步骤 3：写入家长指南**

包含共读提醒、亲子互动、支持性语言和不建议语言。

- [ ] **步骤 4：验证故事文件存在**

运行：`Test-Path outputs\picturebooks\qinqing-yu-ai-de-biaoda\mama-yizhi-zai\story\story-package.md`
预期：`True`

## 任务 2：创建视觉圣经文件

- [x] **步骤 1：写入角色圣经**

锁定 `C01-小米`、`A01-妈妈` 和连续道具，明确禁改项和可变项。

- [x] **步骤 2：写入环境地图**

锁定客厅、厨房门口、行动路线、门口安全边界和主光源方向。

- [x] **步骤 3：写入色板和版式圣经**

锁定水彩质感、色板、文字安全边距、3:4 竖版、`1536x2048`、无字插画规则。

- [x] **步骤 4：写入连续性矩阵**

逐页列出角色、道具、空间、光线、镜头和禁止漂移项。

- [ ] **步骤 5：验证 bible 文件存在**

运行：`Get-ChildItem outputs\picturebooks\qinqing-yu-ai-de-biaoda\mama-yizhi-zai\bible -File | Measure-Object`
预期：`Count` 为 `4`。

## 任务 3：创建 QA 文件并更新记录

- [x] **步骤 1：写入故事与文字 QA**

检查 10 页正文汉字数、朗读顺口性、禁用表达、单一主题、情绪接纳和结尾边界。

- [x] **步骤 2：写入视觉连续性 QA**

检查角色、道具、空间、色板、镜头变化、文字区和画幅。

- [x] **步骤 3：写入 AI 瑕疵审计**

明确实际图片未生成，并列出后续封面与 10 页出图时必须检查的 P0/P1/P2 项。

- [ ] **步骤 4：更新 SQLite 记录摘要**

运行：
`python .\skills\picturebook-check-local-record\scripts\picturebook_records.py add --series "亲情与爱的表达系列" --theme "妈妈的爱" --title "妈妈一直在" --status "draft" --summary "小米在客厅短暂看不见妈妈，通过声音、围裙、香味和妈妈的回应感到妈妈一直在。" --characters "C01-小米; A01-妈妈" --style "温暖水彩家庭感，适中偏简洁，3:4竖版" --output-dir "outputs/picturebooks/qinqing-yu-ai-de-biaoda/mama-yizhi-zai"`
预期：返回 JSON 中 `status` 为 `draft`，`output_dir` 为目标输出目录。

- [ ] **步骤 5：导出记录**

运行：`python .\skills\picturebook-check-local-record\scripts\picturebook_records.py export`
预期：返回 JSON 中 `records` 为 `2` 或更多，且命令退出码为 `0`。

## 任务 4：验证

- [ ] **步骤 1：检查必需文件数量**

运行：`Get-ChildItem outputs\picturebooks\qinqing-yu-ai-de-biaoda\mama-yizhi-zai -Recurse -File | Measure-Object`
预期：`Count` 至少为 `10`。

- [ ] **步骤 2：检查未生成图片状态**

运行：`rg -n "实际图片生成：否|图片状态：未生成|无字图片路径：未生成" outputs\picturebooks\qinqing-yu-ai-de-biaoda\mama-yizhi-zai`
预期：至少在 `story-package.md` 和 `ai-artifact-audit.md` 中命中。

- [ ] **步骤 3：检查故事安全语言**

运行：`rg -n "别哭|你要勇敢|不要打扰|妈妈不要你了|真乖" outputs\picturebooks\qinqing-yu-ai-de-biaoda\mama-yizhi-zai`
预期：只在“禁用表达”或“不建议使用的语言”章节命中，不出现在正文中。
