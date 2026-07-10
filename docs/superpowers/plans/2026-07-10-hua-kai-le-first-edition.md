# 《花开了》第一版实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 按已确认规格完成《花开了》第一版故事包、植物与环境参考、无字封面和 9 页内页、中文排版预览、联系表和 QA 记录。

**架构：** 先以 Markdown 固化故事、角色、空间、色彩和逐页导演信息，再以项目内参考图驱动每张无字插画。所有生成图统一裁切/缩放为 `1536×2048`，中文通过可重复运行的本地排版脚本叠加，最后用联系表和逐项审计验证跨页连续性。

**技术栈：** Markdown、内置 imagegen、Python 3 + Pillow、HTML 可编辑预览、项目 SQLite 记录脚本、Git。

---

## 文件结构

- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/story/story-package.md`：完整故事包与交付状态。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/story/page-script.md`：9 页正文、镜头、连续性和最终图像提示词。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/story/parent-guide.md`：亲子共读与科普延伸。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/bible/character-bible.md`：S01 生长形态与不可变项。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/bible/environment-map.md`：E01 花圃空间、地标和光源。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/bible/color-and-style-bible.md`：媒介、色板、版式和视觉禁区。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/bible/continuity-matrix.md`：逐页阶段、地标、镜头和色彩矩阵。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/bible/character-reference-sheet.png`：S01 六阶段无字参考表。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/bible/environment-reference.png`：地上/地下联合剖面环境参考。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/bible/storyboard-contact-sheet.png`：封面和 9 页联系表。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/artwork/clean/*.png`：统一尺寸的无字封面与内页。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/artwork/composited/*.png`：中文排版预览。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/layout/render_book.py`：尺寸统一、中文排版与联系表生成。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/layout/editable-layout.html`：可编辑正文、字体、位置和图片引用。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/qa/story-and-text-qa.md`：故事、字数和朗读检查。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/qa/visual-consistency-qa.md`：跨页阶段、空间和色彩检查。
- `outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/qa/ai-artifact-audit.md`：逐图 P0/P1/P2 审计。

### 任务 1：建立故事包和四本视觉圣经

- [ ] **步骤 1：创建固定输出目录**

创建 `story/`、`bible/`、`artwork/clean/`、`artwork/composited/`、`layout/`、`qa/` 和 `export/`，不写入仓库外目录。

- [ ] **步骤 2：写入故事与家长文件**

使用规格中已锁定的 9 页正文，完整填写故事输出契约要求的状态、基本信息、儿童安全、故事弧线、逐页推进和亲子互动。

- [ ] **步骤 3：写入角色、环境、色彩和连续性文件**

明确 S01、W01、L01、B01、D01、D02、每页生长阶段、镜头、地标、光源和文字区，确保无未决字段。

- [ ] **步骤 4：运行文本校验**

运行：

```powershell
rg -n "快点长大|别人都开花了|你要努力|真乖|最漂亮的花|未决项|占位内容" outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le
```

预期：无正文命中；若 QA 文件引用禁用表达，命中行必须明确标为“禁用”。

### 任务 2：生成并锁定参考图

- [ ] **步骤 1：生成 S01 六阶段参考表**

使用内置 imagegen 单独生成无字参考表，阶段从左到右、从上到下依次为吸水种子、裂种发根、出土子叶、真叶幼苗、花苞、完全开花；使用透明水彩和彩色铅笔植物纹理，不画卡通脸或标签。

- [ ] **步骤 2：保存并标准化参考表**

将生成结果复制到 `bible/character-reference-sheet.png`；保留原始比例，不将它作为故事页排版。

- [ ] **步骤 3：生成 E01 环境参考**

引用 S01 参考表，生成同一花圃的地上/地下联合剖面，锁定 D01 左、D02 右、主光右上和中间种植点；保存为 `bible/environment-reference.png`。

- [ ] **步骤 4：检查参考锁定**

放大检查种子纵纹、根/芽方向、向日葵叶形、单一主茎、单一花盘、D01/D02 左右关系和无字要求。任何 P0 立即单独重生成。

### 任务 3：生成四张关键样张

- [ ] **步骤 1：生成无字封面**

引用 S01 与 E01，生成清晨花圃中的刚开放向日葵；左上保留标题区，底部保留署名安全区，输出到 `artwork/clean/cover-clean.png`。

- [ ] **步骤 2：生成第 3 页种皮裂开微距**

引用 S01 与 E01，生成地下种子吸水后裂开、尚未出现错误方向根芽的微距，输出到 `artwork/clean/page-03-clean.png`。

- [ ] **步骤 3：生成第 5 页嫩芽出土**

引用 S01 与 E01，生成绿色嫩芽顶破同一种植点土面，D01 左侧可辨，输出到 `artwork/clean/page-05-clean.png`。

- [ ] **步骤 4：生成第 9 页完全开花**

引用 S01 与 E01，生成同一株向日葵完全开放的开阔晨光结尾，输出到 `artwork/clean/page-09-clean.png`。

- [ ] **步骤 5：关键样张内部验收**

逐图核验无文字、无重复植株、阶段正确、画面空间一致、黄色弧线成立和文字安全区可用；修复全部 P0/P1 后再继续。

### 任务 4：生成其余六张内页

- [ ] **步骤 1：生成第 1–2 页**

分别生成地下沉睡种子、雨水渗入的地上/地下联合剖面，输出 `page-01-clean.png` 和 `page-02-clean.png`。

- [ ] **步骤 2：生成第 4 页**

生成白色胚根向下伸展的地下特写，保持种子纵纹与第 3 页一致，输出 `page-04-clean.png`。

- [ ] **步骤 3：生成第 6–8 页**

分别生成子叶展开、真叶出现、高茎花苞三个连续阶段，输出 `page-06-clean.png`、`page-07-clean.png`、`page-08-clean.png`。

- [ ] **步骤 4：统一画幅和尺寸**

运行 `layout/render_book.py normalize`，对封面和 9 页执行中心安全裁切与 Lanczos 缩放，结果必须为 `1536×2048`、RGB 或 RGBA PNG。

### 任务 5：完成中文排版预览和可编辑布局

- [ ] **步骤 1：确定中文字体**

优先查找思源黑体或 Noto Sans CJK；若不可用，使用系统中可完整显示中文的微软雅黑。脚本记录实际字体路径。

- [ ] **步骤 2：实现排版脚本**

`render_book.py compose` 读取锁定正文和每页文字区坐标，在不透明度适当的自然明暗调整上直接绘制深灰中文；不添加固定白卡片。封面加入 `花开了` 和 `图/文：小葫芦`。

- [ ] **步骤 3：生成排版预览**

输出 `cover-final.png` 和 `page-01-final.png` 至 `page-09-final.png`，验证文本在 6% 安全边距内且不遮挡根尖、嫩芽、叶片或花苞。

- [ ] **步骤 4：创建可编辑 HTML**

`editable-layout.html` 使用绝对定位文本层引用 `../artwork/clean/*.png`，每一页的正文、位置、字号和颜色可直接编辑。

### 任务 6：视觉质检与联系表

- [ ] **步骤 1：生成联系表**

运行 `layout/render_book.py contact-sheet`，按“封面 + 1–9 页”顺序输出 `bible/storyboard-contact-sheet.png`，每格只在联系表边框区标注页码，不修改故事图片。

- [ ] **步骤 2：逐页视觉审计**

使用图像查看工具检查根/芽方向、单株数量、向日葵物种、D01/D02、光源、叶片阶段、文字乱码、AI 融化和裁切风险，将结论写入 `qa/ai-artifact-audit.md`。

- [ ] **步骤 3：跨页一致性审计**

通过联系表检查阶段无倒退、镜头不模板化、土棕→雨蓝→嫩叶绿→向日葵黄的色彩弧线和同一花圃识别度，将结论写入 `qa/visual-consistency-qa.md`。

- [ ] **步骤 4：尺寸与文件完整性验证**

运行：

```powershell
python outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le/layout/render_book.py verify
```

预期：报告 10 张 clean、10 张 composited，全部 `1536×2048`，无缺失文件，退出码为 0。

### 任务 7：更新故事包状态与本地记录

- [ ] **步骤 1：回填实际素材和 QA 状态**

更新 `story/story-package.md` 中的图片路径、生成方式、模型/参考信息和每页状态；不得把未通过页面标为通过。

- [ ] **步骤 2：更新 SQLite 草稿记录**

运行：

```powershell
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py add --series "动物与自然科普系列" --theme "植物生长" --title "花开了" --status "draft" --summary "一粒向日葵种子在雨水、阳光和时间中按真实顺序发根、出土、长叶并开花。" --output-dir "outputs/picturebooks/dongwu-yu-ziran-kepu/zhiwu-shengzhang-hua-kai-le"
python .\skills\picturebook-check-local-record\scripts\picturebook_records.py export
```

预期：记录仍为 `draft`，因为 PDF/PPTX 尚未完成；摘要和输出目录已回填，导出记录数不减少。

- [ ] **步骤 3：最终仓库检查**

运行 `git diff --check`，确认没有空白错误；检查 `git status --short`，仅包含本次输出、记录更新和计划文档，不提交 `.superpowers/` 视觉伴侣临时文件。

## 计划自检

- 规格中的故事、角色、空间、色彩、版式、图片、排版、QA 和记录更新均有对应任务。
- 所有资产路径、文件数量、图像尺寸、文本内容和验证命令已明确。
- 生成顺序先参考、再关键样张、再其余页面，符合四项锁定和视觉质检要求。
- 第一版不包含 PDF/PPTX，SQLite 保持 `draft`，与规格范围一致。
