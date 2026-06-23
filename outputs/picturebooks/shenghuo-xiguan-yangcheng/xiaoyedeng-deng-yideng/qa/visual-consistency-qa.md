# 《小夜灯，等一等》视觉连续性 QA

## 当前状态

- 角色参考图：未生成。
- 环境参考图：未生成。
- 封面：已生成修订版无字封面 `artwork/clean/cover-clean.png`，排版封面 `artwork/composited/cover-final.png`；旧版备份 `artwork/clean/cover-clean-before-review.png`。
- 内页：已生成 10 张无字内页和 10 张带文字成品图。
- 联系表：无字内页联系表 `bible/storyboard-contact-sheet.png`；带文字内页联系表 `bible/storyboard-final-contact-sheet.png`。
- 本文件为生成前连续性检查基准 + 当前全书初检记录。

## 已锁定项

- 画幅：`3:4` 竖版。
- 像素尺寸：`1536x2048`。
- 主要场景：卧室 + 右侧门口。
- 空间轴线：床左、房门右、窗边椅后侧。
- 主光源：床头小夜灯 + 第 7 页后门缝光。
- 角色：C01-小葫芦、A01-妈妈、P01-小兔抱偶。
- 风格：温柔水彩 + 彩铅线条 + 轻纸感颗粒。

## 跨页风险点

| 风险 | 处理要求 |
|---|---|
| 影子被画得恐怖或像第三个人 | 必须保持柔和，可看出来源是椅背小外套 |
| 妈妈位置变成离开 | 第 8-10 页妈妈必须在门口可回应范围 |
| 门缝光消失或过强 | 第 7 页后持续保留，但不得压过小夜灯 |
| 小兔无故消失或变色 | 全书保持奶油白、浅蓝耳朵 |
| 卧室左右翻转 | 床左、门右关系不变 |
| 夜晚过暗 | 保持暖光可读，不使用恐怖低照度 |
| 模型生成文字 | 出现中文、假字母或乱码必须重做 |

## 生成后逐页检查项

- 角色脸型、发型、服装、鞋袜是否一致。
- 妈妈是否蹲低、坐低或保持非压迫姿态。
- 小兔是否被真实抱住，手指是否正常。
- 夜灯和门缝光是否符合页码状态。
- 影子是否温和、可解释为小外套，不像第三个人。
- 文本安全区是否清楚，未遮挡脸、手、眼神、小兔、夜灯。
- 是否存在重复人物、漂浮家具、穿插、透视错误。

## 封面样张初检

- 画幅与像素：通过，`1536x2048`。
- 无字插画：通过，未见中文、英文、假字或标签。
- 角色关系：通过，小葫芦抱小兔坐床边，妈妈在门口可回应。
- 光源：通过。修订版小夜灯成为第一视觉暖光，门口光收窄为辅助。
- 影子：通过。修订版能看出小外套袖子和下摆，不像第三个人。
- 文字安全区：通过，上方墙面可承载后期标题。
- 记录项：标题测试图可用，未遮挡人物和关键道具；颜色偏低调，正式排版可略提亮。

## 全书内页与排版初检

| 页码 | 无字图 | 排版图 | 初检结论 | 备注 |
|---|---|---|---|---|
| 1 | `artwork/clean/page-01-clean.png` | `artwork/composited/page-01-final.png` | 通过 | 建立卧室，床左门右，文字不遮挡人物。 |
| 2 | `artwork/clean/page-02-clean.png` | `artwork/composited/page-02-final.png` | 通过 | 夜灯成为安全光源，妈妈动作温和。 |
| 3 | `artwork/clean/page-03-clean.png` | `artwork/composited/page-03-final.png` | 通过 | 墙影柔和，情绪是“有点紧”，未恐怖化。 |
| 4 | `artwork/clean/page-04-clean.png` | `artwork/composited/page-04-final.png` | 通过 | 妈妈坐低陪看，指向动作无压迫。 |
| 5 | `artwork/clean/page-05-clean.png` | `artwork/composited/page-05-final.png` | 通过 | 新版影子能读成椅背上的小外套；旧版 P1 样张已备份。 |
| 6 | `artwork/clean/page-06-clean.png` | `artwork/composited/page-06-final.png` | 通过 | 小葫芦抱近小兔，安抚物接触关系清楚。 |
| 7 | `artwork/clean/page-07-clean.png` | `artwork/composited/page-07-final.png` | 通过 | 门只留一点点，门缝光清楚但未压过夜灯。 |
| 8 | `artwork/clean/page-08-clean.png` | `artwork/composited/page-08-final.png` | 通过 | 床到门口的距离、妈妈可回应、夜灯和门缝光同时在场。 |
| 9 | `artwork/clean/page-09-clean.png` | `artwork/composited/page-09-final.png` | 通过 | 三颗星星小练习可见，文字不遮挡手部。 |
| 10 | `artwork/clean/page-10-clean.png` | `artwork/composited/page-10-final.png` | 通过 | 小葫芦先躺一会儿，妈妈仍在门口，结尾没有强迫独睡或抛下感。 |

## 结论

文本、空间和光源连续性通过当前初检。旧版封面仅保留为修订前备份和色调参考；第 5 页旧版影子问题已修正并备份旧图。当前可进入导出前人工确认；若后续需要重批量生成，仍建议补齐角色参考图和环境参考图，以降低跨页漂移风险。

