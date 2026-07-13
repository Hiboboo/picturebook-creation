# 色板与风格圣经

## Visual Direction Card

- 故事核心情绪：短暂紧张、停住、被看见、安全求助、安心重逢。
- 视觉关键词：清晨图书馆、清爽公共空间、固定安全点、轻微紧张、可信求助、安静重逢。
- 艺术方向：透明水彩 + 彩铅细线；低饱和蓝绿与浅木色；手绘纸感；儿童真实比例；不追求高饱和动画感。
- 视觉禁区：恐怖阴影、泛黄滤镜、陌生人威胁、拥挤压迫、随机发光粒子、伪文字、过度商业卡通风。

## 出版级视觉精修规则

本轮精修不改变故事结构、角色设定和色彩体系，目标是从“高质量 AI 水彩绘本”提升到“接近人工绘本插画师完成的商业出版级绘本”。所有后续页面提示词必须叠加以下规则。

### 人物自然化规则

```text
Avoid perfect symmetry.
Characters should feel hand-drawn by a children's book illustrator.
Allow subtle imperfections in hair, clothing folds, facial asymmetry and natural body posture.
Avoid AI-perfect faces and mannequin-like expressions.
```

执行要点：

- 小米保留圆脸、短黑发、大眼睛、珊瑚红开衫、浅米背带裤和海军蓝鞋，但表情随剧情变化，不使用模板式微笑。
- 手部动作要服务情节：第 4 页握卡片有轻微用力感，第 6 页站稳，第 10 页主动靠近妈妈。
- 成人角色避免“标准救援者”或“标准服务人员”姿态，妈妈蹲低等待孩子靠近，工作人员可有轻微年龄感、马甲褶皱和自然前倾。

### 环境自然化规则

```text
The library should feel like a real children's library that is used every day.
Include small imperfections:
slightly uneven books, natural object placement, subtle wear, small life details.
Avoid showroom-like perfection.
```

执行要点：

- 环境随机性控制在约 10%-15%：少量书本突出、角度不同、高低不齐或有空位。
- 阅读区可以有翻过的绘本、轻微折角、小坐垫偏移、地毯边缘自然弯曲。
- 植物叶片需有遮挡和方向差异，不要每片叶子都朝向镜头。
- 不新增人物、广告牌、复杂装饰和任何可读文字。

### 水彩绘本规则

```text
Traditional children's picture book illustration style.
Soft watercolor and colored pencil texture.
Visible hand-drawn line variation.
Natural paper texture.
Avoid digital AI smoothness.
Avoid 3D rendering.
Avoid glossy surfaces.
```

执行要点：

- 前景人物和关键动作清晰，背景线条降低精度并允许轻微虚化。
- 线条有粗细变化，衣服边缘和头发走向允许轻微不规则。
- 避免统一水彩滤镜、塑料皮肤、过度锐化、3D 渲染感和样板间式整洁。

## 主色与功能

- 浅木色：图书馆地板和书架，提供真实、稳定的公共空间。
- 清水蓝：服务台和工作人员马甲，作为可信求助线索。
- 低饱和蓝绿：公共空间背景和情绪稳定色。
- 珊瑚红：小米开衫，帮助跨页识别主角。
- 浅蓝：小熊脚印和联系卡，连接“安全点”和“求助工具”。

## Whole Book Color Arc

| 阶段 | 页码 | 情绪 | 色彩方向 |
|---|---|---|---|
| 约定与看书 | 1-2 | 平静、专注 | 浅木色 + 清水蓝，明亮平衡 |
| 看不见妈妈 | 3-4 | 疑惑、紧张 | 蓝绿略降饱和，珊瑚红仍清楚 |
| 站回安全点 | 5-6 | 想起来、站稳 | 浅蓝脚印更明确，光线保持清楚 |
| 求助等待 | 7-8 | 被陪伴 | 清水蓝和服务台光稳定画面 |
| 重逢收束 | 9-10 | 放松、安心 | 浅木色和暖白光回升 |

## 版式规则

- 全书 `3:4` 竖版，`1536x2048`。
- 正文后期可编辑文本层加入，通常 1 行，最多 2 行。
- 文字安全边距至少 6%。
- 文字区优先使用上方低细节墙面、服务台侧面或书架上方空白，不添加固定不透明大背板。
- 封面书名最多 2 行；署名固定 `图/文：小葫芦`。

## 负面视觉约束

no mature content, no child-inappropriate content, no violence, no blood, no weapons, no scary horror, no dangerous stranger, no kidnapping, no traffic, no escalator, no coercion, no shaming, preschool-safe; no extra fingers, no missing fingers, no fused hands, no extra limbs, no malformed anatomy, no duplicated people, no outfit changes, no changing hairstyle, no floating objects, no warped perspective, no impossible furniture, no illegible text, no pseudo-Chinese characters, no readable signs, no random decorative clutter, no plastic skin, no identical smiles.
