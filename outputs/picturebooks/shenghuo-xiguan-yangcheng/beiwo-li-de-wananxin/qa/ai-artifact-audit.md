# 《被窝里的晚安信》AI 插画瑕疵审计

## 生成与排版方法

- 无字插画：使用内置图像生成能力，先建立角色/道具与环境参考，再制作封面及内页。
- 中文文字：使用 `layout/text-layout.json` 与 `layout/render_book.py` 后期叠加；图像模型不负责生成书名、正文或任何可读文字。
- 交付规格：所有 clean 图与 composited 图均归一为 `1536×2048`、3:4 竖版 PNG。

## 硬性审计条件

```text
no readable text, no Chinese characters, no letters, no pseudo-text, no logos, no watermark;
no nightlight, no door-slit light, no stars, no moon, no yellow or amber cast, no sepia;
no coercion, no shaming, no adult looming, no forced hug, no reward ceremony;
no extra fingers, missing fingers, fused hands, extra limbs, malformed anatomy,
duplicated people, inconsistent faces, outfit changes, hairstyle changes, floating objects,
warped furniture, plastic skin, identical smiles, random clutter
```

## 最终审计结果

| 范围 | 文字 / 水印 | 人物、手脚与道具 | 主题与画面约束 | 结论 |
|---|---|---|---|---|
| 角色与环境参考图 | 未见可读文字 | 角色、兔子、卡、信封与空间结构可辨 | 冷调、无夜灯与门缝光 | 通过 |
| 封面与第 01–05 页 | 未见可读文字或伪文字 | 人数、服装、兔子、床窗方向合理 | 无催促姿势、无星月/小夜灯 | 通过 |
| 第 06 页 | 未见可读文字或伪文字 | 团团、妈妈局部、卡、三支蜡笔与单只兔子均合理 | 无接管式成人动作 | 通过（见修正记录） |
| 第 07 页 | 未见可读文字或伪文字 | 手指、握笔、卡与信封接触自然 | 卡面仅有约定的手形与色点 | 通过 |
| 第 08–10 页 | 未见可读文字或伪文字 | 信封交接、放置与拉被动作均自然 | 无夜灯、门缝光、星月或黄色滤镜 | 通过 |
| 11 张后期排版图 | 仅含计划内中文文字层 | 正文不遮挡关键动作 | 文字对比、留白与安全边距合格 | 通过 |

## 修正记录

| 编号 | 发现 | 处置 | 结果 |
|---|---|---|---|
| P0-06 | 第 06 页首次候选图中出现重复小兔，不符合 P01“仅一只”的锁定。 | 已重新生成并替换 clean 图，再重新合成最终文字层。 | 已解决；最终第 06 页仅一只小兔。 |
| P1-TEXT | 初次合成中个别页面存在中文标点单独换行的风险。 | 在 `text-layout.json` 中改为显式换行，重新渲染全书。 | 已解决；最终联系表和单页图均无孤立标点。 |

## 结论

最终成图没有遗留 P0/P1 瑕疵；可进入 PDF/PPT 导出流程（若后续需要）。
