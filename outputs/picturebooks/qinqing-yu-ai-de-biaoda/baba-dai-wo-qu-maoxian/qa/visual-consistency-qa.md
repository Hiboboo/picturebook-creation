# 《爸爸带我去冒险》视觉连续性 QA

## 当前状态

- 实际图片生成：是，已生成角色参考图、无字封面、10 页无字内页和整本联系表。
- 角色参考图：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/baba-dai-wo-qu-maoxian/bible/character-reference-sheet.png`
- 环境参考图：未单独生成；空间连续性由 `bible/environment-map.md` 和整本联系表共同控制。
- 封面与内页：封面 `outputs/picturebooks/qinqing-yu-ai-de-biaoda/baba-dai-wo-qu-maoxian/artwork/clean/cover-clean.png`；第 1-10 页 `artwork/clean/page-01-clean.png` 至 `page-10-clean.png`。
- 整本联系表：`outputs/picturebooks/qinqing-yu-ai-de-biaoda/baba-dai-wo-qu-maoxian/bible/storyboard-contact-sheet.png`

## 文本锁定检查

- 角色脸型、发型、服装、鞋袜和身高关系：已在 `bible/character-bible.md` 锁定；根据用户反馈，亲子二人全书都只穿室内袜、不穿鞋。
- 固定角色人数与身份：已锁定为 C01-小禾、A01-爸爸，无配角。
- 道具颜色、大小、位置和持握状态：已在 `story/story-package.md` 与 `bible/continuity-matrix.md` 锁定。
- 窗、沙发、圆地毯、软垫、纸箱、毛毯洞和沙发上方单一壁画相框位置：已在 `bible/environment-map.md` 锁定。
- 镜头轴线、行动方向和光源：已锁定为左窗光，行动从地毯左侧向右推进。
- 色板、线条、颗粒和人物比例：已在 `bible/color-and-style-bible.md` 锁定。
- 画幅、像素尺寸和页码命名：角色参考图、无字封面和第 1-10 页无字内页均为 `1536x2048`，按 `cover-clean.png` 与 `page-01-clean.png` 至 `page-10-clean.png` 命名。

## 出图后初检

- 每页无可读正文、无伪中文；地图只保留简单线条。
- 爸爸没有拉扯、推、催促或强迫；支持动作保持低压力。
- 枕头山保持低矮、安全，不像真实高山或跳台。
- 毛毯洞开放、可见爸爸，不阴森、不封闭。
- 第 6 页手指支架关系清楚，无强拉动作；排版前建议放大复核手部细节。
- 小禾服装、小包和发型跨页一致。
- 客厅固定地标整体一致；沙发、圆地毯、窗光和毛毯洞位置可读。
- 墙上壁画保持单一浅木框青绿色抽象画；少数页内部笔触略有差异，属于 P2 级精修项。
- 小禾和爸爸均只穿室内袜、不穿鞋。

## 结论

无字图初稿通过当前阶段检查。用户指出的两项旧样图问题已处理：墙上壁画统一为单一浅木框青绿色抽象画；爸爸和小禾全书均只穿室内袜、不穿鞋。当前剩余为 P2 级精修项：第 9-10 页爸爸脸部略显成熟，壁画内部笔触有轻微差异；不影响进入排版审阅。
