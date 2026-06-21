# 《小松鼠追着风看彩虹》故事包实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 基于已批准规格，创建《小松鼠追着风看彩虹》的完整文本故事包、视觉圣经、连续性矩阵、QA 文件，并更新本地记录摘要。

**架构：** 输出集中在 `outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/`。故事正文、逐页脚本和家长指南放在 `story/`；角色、环境、色板和连续性放在 `bible/`；故事与视觉 QA 放在 `qa/`。不生成实际图片，只提供无字插画提示词和明确的未生成状态。

**技术栈：** Markdown 文档、项目内 SQLite 记录脚本、Python unittest/pytest 验证。

---

## 文件结构

- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/story/story-package.md`
  - 职责：按故事输出契约整合交付状态、基本信息、儿童安全策略、故事设定、镜头计划、封面与逐页详情、QA 和素材清单。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/story/page-script.md`
  - 职责：提供可直接用于后续排版和插画制作的逐页正文、画面重点和无字插画提示词。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/story/parent-guide.md`
  - 职责：给家长的共读提醒、互动问题和支持性语言。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/character-bible.md`
  - 职责：锁定主角、配件和表情范围。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/environment-map.md`
  - 职责：锁定林边小路空间、行动路线、天气变化和镜头轴线。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/color-and-style-bible.md`
  - 职责：锁定画面风格、色板、版式和无字插画规则。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/continuity-matrix.md`
  - 职责：逐页列出角色、道具、空间、天气和镜头连续性。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/qa/story-and-text-qa.md`
  - 职责：检查年龄、字数、朗读、安全语言和单一主题。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/qa/visual-consistency-qa.md`
  - 职责：检查角色、道具、空间、色板、镜头和文字区规则。
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/qa/ai-artifact-audit.md`
  - 职责：标明图片未生成，并列出后续出图必须审计的 P0/P1/P2 项。
- 修改：`records/picturebook_records.sqlite`
  - 职责：保留 draft 状态，补充摘要、主角、风格和输出目录。
- 修改：`records/records.json`
  - 职责：导出 SQLite 记录，便于人工审查。

## 任务 1：创建故事文本文件

**文件：**
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/story/story-package.md`
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/story/page-script.md`
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/story/parent-guide.md`

- [ ] **步骤 1：写入故事包总文档**

写入完整契约字段：交付状态、基本信息、儿童发展策略、故事设定卡、全书镜头表、封面说明、8 个内页字段、全书质量审计、家长文字、交付准备。

- [ ] **步骤 2：写入逐页脚本文档**

每页包含：正文、汉字数、画面中心、镜头、文字区、角色锁定、道具状态、无字插画提示词和负面提示词。

- [ ] **步骤 3：写入家长指南**

包含 3 条共读提醒、4 个亲子互动、3 句支持性语言和 3 句不建议语言。

- [ ] **步骤 4：验证故事文件存在**

运行：`Test-Path outputs\picturebooks\dongwu-yu-ziran-kepu\tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong\story\story-package.md`
预期：`True`

## 任务 2：创建视觉圣经文件

**文件：**
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/character-bible.md`
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/environment-map.md`
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/color-and-style-bible.md`
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/bible/continuity-matrix.md`

- [ ] **步骤 1：写入角色圣经**

锁定 `C01-小松鼠`、`D01-小绿围巾`、`D02-树洞口`，明确禁改项和可变项。

- [ ] **步骤 2：写入环境地图**

锁定林边小路、左侧大树树洞、右上开阔草坡、左到右行动方向、主光源和天气变化。

- [ ] **步骤 3：写入色板和版式圣经**

锁定水彩质感、色板、文字安全边距、3:4 竖版、`1536x2048`、无字插画规则。

- [ ] **步骤 4：写入连续性矩阵**

逐页列出角色、围巾、树洞、天气、镜头、文字区和禁止漂移项。

- [ ] **步骤 5：验证 bible 文件存在**

运行：`Get-ChildItem outputs\picturebooks\dongwu-yu-ziran-kepu\tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong\bible -File | Measure-Object`
预期：`Count` 为 `4`。

## 任务 3：创建 QA 文件并更新记录

**文件：**
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/qa/story-and-text-qa.md`
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/qa/visual-consistency-qa.md`
- 创建：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/qa/ai-artifact-audit.md`
- 修改：`records/picturebook_records.sqlite`
- 修改：`records/records.json`

- [ ] **步骤 1：写入故事与文字 QA**

检查 8 页正文汉字数、朗读顺口性、禁用表达、单一主题、情绪接纳和结尾边界。

- [ ] **步骤 2：写入视觉连续性 QA**

检查角色、围巾、树洞、天气、色板、镜头变化、文字区和画幅。

- [ ] **步骤 3：写入 AI 瑕疵审计**

明确实际图片未生成，并列出后续封面与 8 页出图时必须检查的 P0/P1/P2 项。

- [ ] **步骤 4：更新 SQLite 记录摘要**

运行：
`python .\skills\picturebook-check-local-record\scripts\picturebook_records.py add --series "动物与自然科普系列" --theme "天气" --title "小松鼠追着风看彩虹" --status "draft" --summary "小松鼠顺着风的线索观察雨、雷声和雨后彩虹，理解天气会慢慢变化。" --characters "C01-小松鼠" --style "温柔水彩质感，适中偏简洁，3:4竖版" --output-dir "outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong"`
预期：返回 JSON 中 `status` 为 `draft`，`output_dir` 为目标输出目录。

- [ ] **步骤 5：导出记录**

运行：`python .\skills\picturebook-check-local-record\scripts\picturebook_records.py export`
预期：返回 JSON 中 `records` 为 `1` 或更多，且命令退出码为 `0`。

## 任务 4：验证与提交

**文件：**
- 验证：`outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong/**`
- 验证：`records/records.json`
- 测试：`tests/test_picturebook_output_paths.py`
- 测试：`tests/test_picturebook_records_sqlite.py`

- [ ] **步骤 1：检查必需文件数量**

运行：`Get-ChildItem outputs\picturebooks\dongwu-yu-ziran-kepu\tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong -Recurse -File | Measure-Object`
预期：`Count` 至少为 `10`。

- [ ] **步骤 2：检查未生成图片状态**

运行：`rg -n "实际图片生成：否|图片状态：未生成|无字图片路径：未生成" outputs\picturebooks\dongwu-yu-ziran-kepu\tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong`
预期：至少在 `story-package.md` 和 `ai-artifact-audit.md` 中命中。

- [ ] **步骤 3：运行测试**

运行：`python -m pytest`
预期：所有测试通过，退出码 `0`。

- [ ] **步骤 4：只暂存本轮文件**

运行：
`git add docs/superpowers/plans/2026-06-21-xiao-songshu-story-package.md outputs/picturebooks/dongwu-yu-ziran-kepu/tianqi-xiao-songshu-zhui-zhe-feng-kan-caihong records/picturebook_records.sqlite records/records.json`

- [ ] **步骤 5：提交**

运行：`git commit -m "feat: add squirrel weather picturebook package"`
预期：提交成功，且未包含已有无关删除或技能文件修改。
