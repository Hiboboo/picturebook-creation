# 《小碗自己排队》实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 基于已批准规格，创建《小碗自己排队》的完整故事包、视觉圣经、连续性矩阵、QA 文件、关键参考图/样张，并更新本地记录。

**架构：** 输出集中在 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/`。文本文件先完成故事、逐页脚本、家长指南、角色/空间/色彩/连续性锁定和 QA；图片阶段先生成角色参考、环境参考、缩略分镜和四类关键页样张，通过检查后再生成全书无字图。中文标题和正文只在后期排版层加入，不让图像模型生成文字。

**技术栈：** Markdown 文档、项目内 SQLite 记录脚本、PowerShell 验证命令、`rg` 文本检查、内置 `image_gen` 工具、Python/Pillow 可选图片尺寸检查。

---

## 文件结构

- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/story/story-package.md`
  - 职责：按故事输出契约整合交付状态、基本信息、儿童安全策略、故事设定、镜头计划、封面与逐页详情、QA 和素材清单。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/story/page-script.md`
  - 职责：提供可直接用于插画和排版的逐页正文、中心意思、画面重点、文字区和无字插画提示词。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/story/parent-guide.md`
  - 职责：给家长的共读提醒、亲子互动、支持性语言和不建议语言。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/character-bible.md`
  - 职责：锁定 `C01-小葫芦`、`A01-妈妈`、小碗、勺子、餐垫和水杯的外观、禁改项和可变项。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/environment-map.md`
  - 职责：锁定餐桌空间、角色座位、小碗队伍位置、行动路线、镜头轴线和光源。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/color-and-style-bible.md`
  - 职责：锁定透明水彩和彩铅线条、清爽晚饭色板、版式、安全边距和无字插画规则。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/continuity-matrix.md`
  - 职责：逐页列出角色、道具、空间、光线、镜头、文字区和禁止漂移项。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/story-and-text-qa.md`
  - 职责：检查年龄适配、字数、朗读、禁用表达、单一主题、主体性和结尾边界。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/visual-consistency-qa.md`
  - 职责：检查角色、道具、餐桌空间、色板、镜头变化、文字区和画幅。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/ai-artifact-audit.md`
  - 职责：记录图片生成状态、逐页 P0/P1/P2 检查、关键样张审核和全书联系表结论。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/character-reference-sheet.png`
  - 职责：角色参考表，包含小葫芦和妈妈的固定外观、比例与表情。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/environment-reference.png`
  - 职责：餐桌空间参考图，锁定小碗队伍、座位关系和光源。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/storyboard-contact-sheet.png`
  - 职责：全书缩略分镜联系表，用于检查镜头节奏与空间连续性。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/cover-clean.png`
  - 职责：无字封面插画。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-01-clean.png` 到 `page-10-clean.png`
  - 职责：10 页无字内页插画。
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/layout/text-layout.json`
  - 职责：记录封面和每页正文的文字层位置、字号、行数和安全边距。
- 修改：`records/picturebook_records.sqlite`
  - 职责：保持《小碗自己排队》为 `draft`，补充摘要、角色、风格和输出目录。
- 修改：`records/records.json`
  - 职责：导出 SQLite 记录，便于人工审查。

## 任务 1：创建故事文本文件

**文件：**
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/story/story-package.md`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/story/page-script.md`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/story/parent-guide.md`

- [ ] **步骤 1：创建故事目录**

运行：`New-Item -ItemType Directory -Force outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\story`
预期：命令退出码为 `0`，目录存在。

- [ ] **步骤 2：写入 `story-package.md`**

使用 `apply_patch` 创建 `story-package.md`。文档必须包含这些章节，且按 `story-output-contract.md` 填写完整字段：

```markdown
# 《小碗自己排队》故事包

## 1. 交付状态

- 当前状态：故事草案
- 实际图片生成：否
- 生成方式：AI 辅助文本设计；图片未生成
- 本次未完成项：角色参考图、环境参考图、缩略分镜、无字插画、后期排版、PDF/PPT 导出
- 需要用户确认项：10 页正文、角色设定、餐桌空间、视觉方向

## 2. 基本信息

- 系列：生活习惯养成系列
- 书名：小碗自己排队
- 主题：不挑食、自己吃饭
- 图/文：小葫芦
- 主要适合年龄：3-4 岁
- 可延伸年龄：2-5 岁亲子共读
- 核心主题：孩子自己选择并尝一小口不熟悉的食物。
- 孩子的生活入口：家中晚饭桌，孩子只想吃白饭，桌上有排队的小碗。
- 目标情绪变化：从只想吃熟悉食物，到有选择感，再到愿意自己舀一点。
- 故事页数：10 页，不含封面
- 画面风格：透明水彩和彩铅线条，清爽家庭餐桌，适中偏简洁
- 图片比例：固定 `3:4` 竖版
- 锁定像素尺寸：`1536x2048`
- 文字安全边距：至少画布宽高的 `6%`
- 固定输出目录：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/`
```

正文页表必须使用已批准规格中的 10 页正文方向，并扩展每页字段：汉字数、朗读检查、儿童主体性、成人支持、文字与画面分工、页间推进、角色锁定、道具状态、空间校验、镜头理由、文字区、无字插画提示词、负面提示词、路径状态和单页 QA。

- [ ] **步骤 3：写入 `page-script.md`**

使用 `apply_patch` 创建逐页脚本。每页必须包含：

```markdown
### 第 1 页

- 正文：小葫芦坐好啦。
- 汉字数：7
- 本页中心意思：晚饭开始，孩子坐到餐桌前。
- 景别：远中景
- 视角与机位：平视，餐桌前侧
- 出场角色：C01-小葫芦；A01-妈妈
- 道具状态：D01 在孩子面前；D02、D03、D04 尚在桌边队伍外侧；D05 在餐垫右侧
- 文字区：左上低细节墙面，1 行，安全边距 6%
- 无字插画提示词：透明水彩和彩铅线条，3:4 竖版，清爽家庭晚饭餐桌，小葫芦穿暖黄色长袖上衣和浅蓝背带裤坐在儿童椅上，妈妈坐在旁边，白饭小碗和小勺在餐垫上，浅木餐桌，柔和自然光，左上保留低细节文字区，无任何文字
- 负面提示词：no mature content, no coercion, no shaming, no forced feeding, no extra fingers, no missing fingers, no duplicated people, no illegible text, no pseudo-Chinese characters, no plastic food, no random decorative clutter
```

第 2-10 页按规格页表补齐同等字段。正文必须保留：

```text
1. 小葫芦坐好啦。
2. 三只小碗，排成队。
3. “我先吃白饭。”
4. 绿绿小碗来了。
5. “哪只小碗先来？”
6. “黄黄先来一点点。”
7. 小勺子，啊呜。
8. 绿绿也靠近一点。
9. 小葫芦舀了一点。
10. “下一口，我自己来。”
```

- [ ] **步骤 4：写入 `parent-guide.md`**

使用 `apply_patch` 创建家长指南，必须包含：

```markdown
# 《小碗自己排队》家长指南

## 这个故事想让孩子感受到什么

孩子可以先观察、先选择熟悉的食物，也可以只尝一点点。愿意自己拿勺尝一小口，已经是足够小、足够真实的一步。

## 共读提醒

不要用这本书催孩子“你也要像小葫芦一样吃菜”。共读时重点放在选择、闻一闻、舀一点这些小动作。

## 亲子互动

1. 让孩子指一指：哪只小碗先来？
2. 用手比一比：一点点有多小？
3. 读到“小勺子，啊呜”时，做一个慢慢舀的动作。
4. 饭桌上可以问：你想先看一看，还是先闻一闻？

## 可使用的支持性语言

- “你想让哪一口先来？”
- “一点点，也可以。”
- “你自己舀，我在旁边。”

## 不建议使用的语言

- “不吃菜就没有点心。”
- “你看别人都吃了。”
- “吃完才是好孩子。”
```

- [ ] **步骤 5：验证故事文件存在**

运行：`Get-ChildItem outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\story -File | Measure-Object`
预期：`Count` 为 `3`。

- [ ] **步骤 6：提交故事文本**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\story
git commit -m "feat: add xiaowan ziji paidui story text"
```

预期：提交成功，只包含 `story/` 下 3 个文件。若 Git 缺少作者信息，使用：

```powershell
git -c user.name="Codex" -c user.email="codex@openai.com" commit -m "feat: add xiaowan ziji paidui story text"
```

## 任务 2：创建视觉圣经文件

**文件：**
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/character-bible.md`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/environment-map.md`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/color-and-style-bible.md`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/continuity-matrix.md`

- [ ] **步骤 1：创建视觉圣经目录**

运行：`New-Item -ItemType Directory -Force outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\bible`
预期：命令退出码为 `0`，目录存在。

- [ ] **步骤 2：写入 `character-bible.md`**

使用 `apply_patch` 创建角色圣经。必须包含：

```markdown
# 角色圣经

## C01-小葫芦

- 年龄感 / 物种：3-4 岁幼儿
- 身高与头身比例：约 3.5 头身，小体型
- 脸型与核心五官：圆脸，黑色眼睛，小鼻子，表情自然
- 发型与发色：黑色短发，柔软刘海
- 上衣：暖黄色长袖上衣
- 下装：浅蓝背带裤
- 鞋袜：白袜，红色软底小鞋
- 固定配色：暖黄、浅蓝、红色鞋点缀
- 常见表情范围：平静、好奇、皱鼻犹豫、专注、尝试、放松
- 禁改项：短发、黄色上衣、浅蓝背带裤、红鞋、幼儿比例
- 可变项：坐姿、身体前后倾、握勺动作、视线方向
- 角色参考图路径或状态：`bible/character-reference-sheet.png`，未生成

## A01-妈妈

- 年龄感 / 身份：温和照顾者
- 发型与发色：深棕色低马尾
- 上衣：奶油色家居上衣
- 下装：浅棕长裤
- 固定配件：鼠尾草绿色围裙
- 支持方式：坐在旁边等待，给选择，不喂饭，不催促
- 禁改项：低马尾、绿色围裙、非夸张微笑、不把勺子送到孩子嘴边
```

道具卡必须覆盖 `D01` 到 `D06`，记录颜色、归属、初始位置、每页状态和禁改项。

- [ ] **步骤 3：写入 `environment-map.md`**

使用 `apply_patch` 创建环境地图。必须包含：

```markdown
# 环境与空间连续性地图

- 时间与天气：晚饭时间，室内自然余光加柔和餐区灯，整体清爽明亮
- 核心场景：家中浅木餐桌
- 起点：C01 坐在餐桌左前侧，D01 白饭碗在面前
- 目标点：孩子可以自己舀一点 D03 或 D04
- 行动路线和路径轴线：小碗从桌边队伍靠近孩子碗边，角色不离开座位
- 固定地标：浅木餐桌、圆角餐垫、低矮儿童椅、餐边柜、水杯、小勺
- 角色进入/离开方向：无离席动作；妈妈始终在旁边或远侧
- 镜头主侧与越轴线：主侧保持餐桌前侧；俯视和特写保留餐垫边缘或小碗队伍
- 主光源方向：画面左上或左侧窗光，餐区柔和补光
- 禁改项：小碗队伍顺序、白饭碗位置、妈妈不喂饭、小葫芦不离开餐桌
```

- [ ] **步骤 4：写入 `color-and-style-bible.md`**

使用 `apply_patch` 创建色板和风格圣经。必须包含视觉方向卡、主色/辅助色/强调色、情绪色彩弧线、禁用色彩倾向、版式、无字插画规则和负面提示词模板。

负面提示词模板必须包含：

```text
no mature content, no child-inappropriate content, no coercion, no shaming, no forced feeding, no conditional reward, preschool-safe; no extra fingers, no missing fingers, no fused hands, no malformed anatomy, no duplicated people, no inconsistent character face, no outfit changes, no changing hairstyle, no floating objects, no warped perspective, no impossible furniture, no illegible text, no pseudo-Chinese characters, no plastic skin, no plastic food, no identical smiles, no random decorative clutter, consistent character design, consistent dining table environment
```

- [ ] **步骤 5：写入 `continuity-matrix.md`**

使用 `apply_patch` 创建连续性矩阵。逐页列出：

```markdown
| 页码 | 出场角色 | 道具状态 | 空间锚点 | 镜头 | 光线 | 文字区 | 禁止漂移 |
|---|---|---|---|---|---|---|---|
| 1 | C01, A01 | D01 在孩子面前，D05 在餐垫右侧 | 餐桌前侧、儿童椅 | 远中景平视 | 左上自然光 | 左上 | 角色服装、餐桌大小 |
```

第 2-10 页必须各有一行，且小碗队伍顺序、白饭碗位置、勺子归属和妈妈支持姿态要连续。

- [ ] **步骤 6：验证视觉圣经文件存在**

运行：`Get-ChildItem outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\bible -File | Measure-Object`
预期：`Count` 至少为 `4`。

- [ ] **步骤 7：提交视觉圣经**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\bible
git commit -m "feat: add xiaowan ziji paidui visual bible"
```

预期：提交成功，只包含 `bible/` 下 Markdown 文件。

## 任务 3：创建 QA 文件并更新记录

**文件：**
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/story-and-text-qa.md`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/visual-consistency-qa.md`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/ai-artifact-audit.md`
- 修改：`records/picturebook_records.sqlite`
- 修改：`records/records.json`

- [ ] **步骤 1：创建 QA 目录**

运行：`New-Item -ItemType Directory -Force outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\qa`
预期：命令退出码为 `0`，目录存在。

- [ ] **步骤 2：写入 `story-and-text-qa.md`**

使用 `apply_patch` 创建故事与文字 QA。必须列出 10 页正文、汉字数和检查结论。检查结论必须包含：

```markdown
- 单一核心主题：通过
- 年龄适配和字数：通过
- 儿童视角：通过
- 情绪接纳与选择权：通过
- 是否存在催促、比较、羞辱、条件式奖励或说教：无
- 重复结构是否每次推进：通过
- 出声朗读检查：通过
- 结尾是否避免“必须吃完”：通过
```

- [ ] **步骤 3：写入 `visual-consistency-qa.md`**

使用 `apply_patch` 创建视觉连续性 QA。必须检查角色、服装、道具、餐桌空间、小碗顺序、镜头变化、色板、画幅、文字区和无字规则。每项填写 `通过` 或 `图片未生成，已锁定检查标准`。

- [ ] **步骤 4：写入 `ai-artifact-audit.md`**

使用 `apply_patch` 创建 AI 瑕疵审计。当前图片未生成，必须写：

```markdown
- 实际图片生成：否
- 当前 P0 问题：无实际图片可判定
- 当前 P1 问题：无实际图片可判定
- 当前 P2 差异：无实际图片可判定
- 后续封面和第 1-10 页出图后，必须逐页检查手指、握勺、嘴边动作、脚踩地、餐桌透视、食物质感、角色服装、伪文字和小碗顺序。
```

- [ ] **步骤 5：更新 SQLite 记录摘要**

运行：

```powershell
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py add --series "生活习惯养成系列" --theme "不挑食、自己吃饭" --title "小碗自己排队" --status "draft" --summary "小葫芦在晚饭桌前让三只小碗排队，自己选择先尝哪一碗，从只吃白饭到愿意自己舀一点不熟悉的食物。" --characters "C01-小葫芦; A01-妈妈; D01-白饭小碗; D02-红红小碗; D03-黄黄小碗; D04-绿绿小碗" --style "透明水彩和彩铅线条，清爽家庭晚饭餐桌，3:4竖版，适中偏简洁" --output-dir "outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui"
```

预期：返回 JSON 中 `title` 为 `小碗自己排队`，`status` 为 `draft`，`output_dir` 为目标输出目录。

- [ ] **步骤 6：导出记录**

运行：`python .\skills\picturebook-check-local-record\scripts\picturebook_records.py export`
预期：返回 JSON 中 `records` 大于等于 `1`，命令退出码为 `0`。

- [ ] **步骤 7：提交 QA 与记录**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\qa records\picturebook_records.sqlite records\records.json
git commit -m "feat: add xiaowan ziji paidui qa and records"
```

预期：提交成功。提交前用 `git diff --cached --name-only` 确认只包含本书 `qa/` 和 `records/` 文件；不要暂存已有无关删除。

## 任务 4：验证文本故事包

**文件：**
- 验证：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/**`
- 验证：`records/records.json`
- 测试：`tests/test_picturebook_output_paths.py`
- 测试：`tests/test_picturebook_records_sqlite.py`

- [ ] **步骤 1：检查必需 Markdown 文件数量**

运行：`Get-ChildItem outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui -Recurse -File -Include *.md | Measure-Object`
预期：`Count` 至少为 `10`。

- [ ] **步骤 2：检查图片未生成状态**

运行：`rg -n "实际图片生成：否|图片未生成|无字图片路径：未生成|排版完成图片路径：未生成" outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui`
预期：至少在 `story/story-package.md` 和 `qa/ai-artifact-audit.md` 中命中。

- [ ] **步骤 3：检查正文不含禁用表达**

运行：`rg -n "不许挑食|吃完才是好孩子|你看别人都吃了|不吃菜就没有点心|妈妈喂你|真乖" outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\story`
预期：只在 `parent-guide.md` 的“不建议使用的语言”或 `story-package.md` 的禁用表达章节命中，不出现在 10 页正文中。

- [ ] **步骤 4：运行项目测试**

运行：`python -m pytest`
预期：所有测试通过，退出码 `0`。

- [ ] **步骤 5：提交验证状态**

若任务 1-3 的提交已完成，本任务不创建新提交。若验证发现文档问题，修复后运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui records\picturebook_records.sqlite records\records.json
git commit -m "fix: refine xiaowan ziji paidui story package"
```

预期：提交成功，且 `git diff --cached --check` 无输出。

## 任务 5：生成角色、环境和缩略分镜参考

**文件：**
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/character-reference-sheet.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/environment-reference.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/bible/storyboard-contact-sheet.png`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/visual-consistency-qa.md`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/ai-artifact-audit.md`

- [ ] **步骤 1：生成角色参考表**

使用内置 `image_gen` 生成一张 `3:4` 角色参考表。提示词：

```text
Use case: illustration-story
Asset type: preschool picturebook character reference sheet
Primary request: Create a clean no-text character reference sheet for a 3-4 year old child named C01-Xiaohulu and mother A01 in a preschool picturebook.
Subject: C01-Xiaohulu is a small 3-4 year old child, 3.5-head proportion, round face, black short hair with soft bangs, warm yellow long sleeve top, light blue overalls, white socks, red soft shoes. Show front, three-quarter, side, back, and four expressions: calm, curious, hesitant wrinkled nose, focused trying. A01-Mother has deep brown low ponytail, cream home top, sage green apron, light brown pants, calm waiting expression. Show front and three-quarter.
Style/medium: transparent watercolor and colored pencil linework, gentle hand-drawn preschool picturebook style, clean white background, natural imperfections, no text.
Composition/framing: organized reference sheet with separated poses, full bodies visible, generous padding.
Constraints: no labels, no Chinese characters, no readable text, consistent outfit, consistent hairstyle, no forced feeding pose.
Avoid: plastic skin, identical smiles, high saturation cartoon look, random decorations, pseudo text, malformed hands, extra fingers.
```

将生成结果复制到 `bible/character-reference-sheet.png`。

- [ ] **步骤 2：生成环境参考图**

使用内置 `image_gen` 生成一张无字环境参考图。提示词：

```text
Use case: illustration-story
Asset type: preschool picturebook dining room environment reference
Primary request: Create a no-text environment reference for a family dinner table in the picturebook Xiaowan Ziji Paidui.
Scene/backdrop: refreshing home dining table at dinner time, pale wood table, child chair on left-front side, mother seat on right or far side, round-corner placemat, small white rice bowl in front of child, three small bowls queued left to right with red tomato/carrot, yellow pumpkin, green vegetable, child spoon and water cup as anchors.
Style/medium: transparent watercolor and colored pencil, clean natural light from upper left, light paper texture, suitable for 3-4 year old preschool picturebook.
Composition/framing: 3:4 portrait, slightly elevated view showing table layout and spatial anchors, natural low-detail area for text.
Constraints: no people required, no readable text, no menu labels, no forced symmetry, no glossy plastic food.
Avoid: warm yellow filter, clutter, random stars, pseudo-Chinese, impossible table perspective, overdecorated background.
```

将生成结果复制到 `bible/environment-reference.png`。

- [ ] **步骤 3：生成缩略分镜联系表**

使用内置 `image_gen` 生成 10 页缩略联系表。提示词：

```text
Use case: illustration-story
Asset type: no-text storyboard contact sheet
Primary request: Create a 10-panel no-text storyboard contact sheet for the preschool picturebook Xiaowan Ziji Paidui, showing clear composition thumbnails only, not final art.
Story beats: 1 child sits at dinner table; 2 three small bowls queue on table; 3 child chooses white rice first; 4 green bowl approaches and child hesitates; 5 mother offers choice while sitting beside child; 6 child chooses yellow bowl and scoops a tiny bit; 7 spoon close-up and small bite; 8 green bowl moves closer; 9 child scoops a tiny bit of green vegetable; 10 child relaxed, three bowls still queued, ready to try next bite.
Style/medium: loose watercolor and colored pencil thumbnail storyboard, consistent dining table layout, no text, no speech bubbles.
Composition/framing: 3:4 portrait contact sheet with 10 numbered-looking panels but no actual numerals or readable text; vary shot size across panels.
Constraints: no Chinese characters, no readable text, no final typography, consistent child outfit, mother never feeds child, spoon belongs to child.
Avoid: repeated identical camera, forced feeding, reward stickers, pseudo text, plastic food, malformed hands.
```

将生成结果复制到 `bible/storyboard-contact-sheet.png`。

- [ ] **步骤 4：检查参考图尺寸和存在性**

运行：`Get-ChildItem outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\bible -File *.png | Select-Object Name,Length`
预期：输出包含 `character-reference-sheet.png`、`environment-reference.png`、`storyboard-contact-sheet.png`，且 `Length` 均大于 `0`。

- [ ] **步骤 5：更新 QA 文件**

在 `qa/visual-consistency-qa.md` 中记录三张参考图路径和检查结论。在 `qa/ai-artifact-audit.md` 中记录是否存在 P0/P1 问题；若有 P0，重新生成对应参考图。

- [ ] **步骤 6：提交参考图**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\bible outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\qa
git commit -m "feat: add xiaowan ziji paidui reference art"
```

预期：提交成功，只包含本书 `bible/` 图片和 QA 更新。

## 任务 6：生成四类关键页样张

**文件：**
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/cover-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-01-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-04-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-09-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-10-clean.png`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/visual-consistency-qa.md`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/ai-artifact-audit.md`

- [ ] **步骤 1：创建无字插画目录**

运行：`New-Item -ItemType Directory -Force outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\artwork\clean`
预期：命令退出码为 `0`，目录存在。

- [ ] **步骤 2：生成无字封面样张**

使用角色和环境参考图作为参考，调用内置 `image_gen`。提示词：

```text
Use case: illustration-story
Asset type: no-text cover artwork
Primary request: Create a no-text cover illustration for the preschool picturebook Xiaowan Ziji Paidui.
Input images: character-reference-sheet.png as character reference; environment-reference.png as dining table reference.
Scene/backdrop: refreshing family dinner table, low-detail upper area reserved for later Chinese title text.
Subject: C01-Xiaohulu sits at the table, wearing warm yellow long sleeve top, light blue overalls, white socks, red soft shoes, holding his own child spoon. Three small bowls queue on the table: red bowl, yellow pumpkin bowl, green vegetable bowl; white rice bowl near the child.
Style/medium: transparent watercolor and colored pencil linework, gentle preschool picturebook, natural life traces, no text.
Composition/framing: 3:4 portrait, child and bowl queue are first visual signal, title-safe area does not cover face, spoon, or bowls.
Constraints: no readable text, no Chinese characters, mother may be absent or softly in background, no forced feeding, no reward sticker.
Avoid: pseudo text, plastic food, glossy skin, identical smiles, overdecorated background, warm yellow filter, malformed hands.
```

保存为 `artwork/clean/cover-clean.png`。

- [ ] **步骤 3：生成第 1 页建立场景样张**

使用 `page-script.md` 第 1 页提示词和参考图，生成 `artwork/clean/page-01-clean.png`。画面必须显示晚饭桌、孩子、妈妈和白饭碗，左上保留正文区，无文字。

- [ ] **步骤 4：生成第 4 页情绪转折样张**

使用 `page-script.md` 第 4 页提示词和参考图，生成 `artwork/clean/page-04-clean.png`。画面必须显示绿绿小碗靠近、小葫芦皱鼻或身体轻轻后靠，不夸张恐惧，不出现成人催促。

- [ ] **步骤 5：生成第 9 页关键动作样张**

使用 `page-script.md` 第 9 页提示词和参考图，生成 `artwork/clean/page-09-clean.png`。画面必须是手部或中近景，孩子自己握勺舀一点绿菜；勺子和食物必须真实接触。

- [ ] **步骤 6：生成第 10 页结尾样张**

使用 `page-script.md` 第 10 页提示词和参考图，生成 `artwork/clean/page-10-clean.png`。画面必须显示孩子放松、三只小碗仍在队里，结尾是“更有把握”，不是吃完后的胜利展示。

- [ ] **步骤 7：逐图 QA**

更新 `qa/ai-artifact-audit.md`，逐图检查：

```markdown
| 文件 | 安全 | 手/勺动作 | 角色一致性 | 小碗顺序 | 空间 | 文字乱码 | 结论 |
|---|---|---|---|---|---|---|---|
| cover-clean.png | 通过 | 通过 | 通过 | 通过 | 通过 | 通过 | 通过 |
```

出现 P0 时重新生成对应图片。出现 P1 时记录问题并生成修正版，不用裁切掩盖。

- [ ] **步骤 8：提交关键样张**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\artwork\clean outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\qa
git commit -m "feat: add xiaowan ziji paidui key samples"
```

预期：提交成功，只包含关键样张和 QA 更新。

## 任务 7：生成剩余无字内页

**文件：**
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-02-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-03-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-05-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-06-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-07-clean.png`
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/artwork/clean/page-08-clean.png`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/visual-consistency-qa.md`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/ai-artifact-audit.md`

- [ ] **步骤 1：确认关键样张通过**

运行：`rg -n "P0|必须重做|需修正" outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\qa\ai-artifact-audit.md`
预期：没有未解决的 P0；若有 P1，已有对应修正版和复检记录。

- [ ] **步骤 2：生成第 2 页**

使用 `page-script.md` 第 2 页提示词和参考图生成 `page-02-clean.png`。画面重点是三只小碗排队，轻微俯视，无文字。

- [ ] **步骤 3：生成第 3 页**

使用 `page-script.md` 第 3 页提示词和参考图生成 `page-03-clean.png`。画面重点是小葫芦自己拿勺靠近白饭，表达“先吃熟悉食物”。

- [ ] **步骤 4：生成第 5 页**

使用 `page-script.md` 第 5 页提示词和参考图生成 `page-05-clean.png`。画面重点是妈妈坐旁边给选择，勺子仍在孩子手边，妈妈不喂饭。

- [ ] **步骤 5：生成第 6 页**

使用 `page-script.md` 第 6 页提示词和参考图生成 `page-06-clean.png`。画面重点是黄黄小碗靠近，孩子自己舀一点。

- [ ] **步骤 6：生成第 7 页**

使用 `page-script.md` 第 7 页提示词和参考图生成 `page-07-clean.png`。画面重点是小勺子和小口动作，避免夸张张嘴或食物糊脸。

- [ ] **步骤 7：生成第 8 页**

使用 `page-script.md` 第 8 页提示词和参考图生成 `page-08-clean.png`。画面重点是绿绿小碗靠近一点，孩子再次犹豫但不恐惧。

- [ ] **步骤 8：全书联系表检查**

更新 `qa/visual-consistency-qa.md`，逐页检查角色服装、发型、妈妈围裙、小碗顺序、餐桌视角、光源、文字区和镜头变化。

- [ ] **步骤 9：提交剩余无字内页**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\artwork\clean outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\qa
git commit -m "feat: add xiaowan ziji paidui remaining clean pages"
```

预期：提交成功，`artwork/clean/` 包含封面和 `page-01-clean.png` 到 `page-10-clean.png`。

## 任务 8：创建文字层排版规范

**文件：**
- 创建：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/layout/text-layout.json`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/story/story-package.md`
- 修改：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/qa/visual-consistency-qa.md`

- [ ] **步骤 1：创建 layout 目录**

运行：`New-Item -ItemType Directory -Force outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\layout`
预期：命令退出码为 `0`，目录存在。

- [ ] **步骤 2：写入 `text-layout.json`**

使用 `apply_patch` 创建排版 JSON。结构：

```json
{
  "canvas": { "width": 1536, "height": 2048, "ratio": "3:4", "safe_margin_percent": 6 },
  "font": {
    "cover_title": { "family": "Noto Sans SC", "size": 112, "weight": 700, "color": "#333333" },
    "body": { "family": "Noto Sans SC", "size": 56, "weight": 500, "color": "#333333", "line_height": 1.25 },
    "credit": { "family": "Noto Sans SC", "size": 34, "weight": 400, "color": "#444444" }
  },
  "pages": [
    { "id": "cover", "text": "小碗自己排队", "credit": "图/文：小葫芦", "box": { "x": 120, "y": 120, "w": 700, "h": 260 } },
    { "id": "page-01", "text": "小葫芦坐好啦。", "box": { "x": 110, "y": 120, "w": 760, "h": 120 } }
  ]
}
```

补齐 `page-02` 到 `page-10`，每页使用 `page-script.md` 正文，文字框不遮挡脸、手、勺子、小碗队伍和关键动作。

- [ ] **步骤 3：更新故事包素材清单**

在 `story/story-package.md` 的交付准备中补入：

```markdown
- 可编辑排版源文件路径：`layout/text-layout.json`
```

- [ ] **步骤 4：验证 JSON 可解析**

运行：`python -m json.tool outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\layout\text-layout.json`
预期：格式化 JSON 输出，退出码 `0`。

- [ ] **步骤 5：提交排版规范**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\layout outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\story outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\qa
git commit -m "feat: add xiaowan ziji paidui text layout"
```

预期：提交成功，只包含本书 layout、story 更新和 QA 更新。

## 任务 9：最终验证与记录完成度

**文件：**
- 验证：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui/**`
- 修改：`records/picturebook_records.sqlite`
- 修改：`records/records.json`

- [ ] **步骤 1：检查全书素材数量**

运行：`Get-ChildItem outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui -Recurse -File | Measure-Object`
预期：`Count` 至少为 `22`，包含 10 个 Markdown/JSON 文档、3 个参考图、11 张无字图。

- [ ] **步骤 2：检查无字图文件名**

运行：`Get-ChildItem outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui\artwork\clean -File | Select-Object -ExpandProperty Name`
预期：输出包含 `cover-clean.png` 和 `page-01-clean.png` 到 `page-10-clean.png`，没有同一页的含义不明最终版文件。

- [ ] **步骤 3：运行文本安全检查**

运行：`rg -n "不许挑食|吃完才是好孩子|你看别人都吃了|不吃菜就没有点心|妈妈喂你|真乖" outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui`
预期：命中只出现在禁用表达或不建议语言章节。

- [ ] **步骤 4：运行项目测试**

运行：`python -m pytest`
预期：所有测试通过，退出码 `0`。

- [ ] **步骤 5：更新记录为当前草稿完整状态**

如果无字图、故事包和 QA 均通过，仍保持 `draft`，因为 PDF/PPT 尚未导出。运行：

```powershell
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py add --series "生活习惯养成系列" --theme "不挑食、自己吃饭" --title "小碗自己排队" --status "draft" --summary "小葫芦在晚饭桌前让三只小碗排队，自己选择先尝哪一碗，从只吃白饭到愿意自己舀一点不熟悉的食物；故事包、视觉圣经、参考图、无字封面和10页无字内页已完成。" --characters "C01-小葫芦; A01-妈妈; D01-白饭小碗; D02-红红小碗; D03-黄黄小碗; D04-绿绿小碗" --style "透明水彩和彩铅线条，清爽家庭晚饭餐桌，3:4竖版，适中偏简洁；中文文字后期排版" --output-dir "outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaowan-ziji-paidui"
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py export
```

预期：第一条命令返回 `status` 为 `draft`；第二条命令退出码为 `0`。

- [ ] **步骤 6：最终提交**

运行：

```powershell
git add outputs\picturebooks\shenghuo-xiguan-yangcheng\xiaowan-ziji-paidui records\picturebook_records.sqlite records\records.json
git diff --cached --check
git commit -m "feat: complete xiaowan ziji paidui picturebook package"
```

预期：`git diff --cached --check` 无输出；提交成功，且不包含已有无关删除或其他绘本目录。
