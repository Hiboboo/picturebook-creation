# 《花开了》逐页脚本与图像提示词

## 统一生成规则

- 用例分类：`illustration-story`
- 画布：`3:4` 竖版，最终统一为 `1536×2048`
- 媒介：透明水彩铺色 + 彩色铅笔植物纹理，轻纸感
- 参考：`bible/character-reference-sheet.png`、`bible/environment-reference.png`
- 统一约束：每页只有同一株 S01 的一个生长阶段；D01 左、D02 右；主光右上；保留自然低细节文字区；无字画面
- 统一避让：no text, no letters, no numbers, no labels, no watermark, no pseudo-Chinese, no cartoon face on the sun or raindrops, no eyes or limbs on the plant, no duplicated plant, no multiple growth stages on one page, no wrong root direction, no wrong shoot direction, no extra flower heads, no random flowers, no glowing particles, no plastic 3D look, no yellow filter, no oversaturated colors, no warped botany, no impossible roots, preschool-safe

## 无字封面

- 中心意思：雨后清晨，同一花圃中的向日葵刚刚开放。
- 构图：S01 单株位于中下部，花盘偏中上；D01 左、D02 右弱化；左上留标题区，底部留署名区。
- 色彩与光线：清澈浅蓝天空、叶绿、低饱和向日葵黄；右上自然晨光，无泛黄滤镜。
- 图片提示词：Use case: illustration-story. Asset type: wordless preschool picturebook cover. A single fully grown sunflower S01 in the same small garden bed after gentle rain, one main stem and one flower head, warm brown center and low-saturation golden-yellow petals, broad slightly serrated green leaves with a few natural raindrops. The blue-gray pebble D01 stays on the left ground and the unmarked pale wooden stake D02 stays on the right. Transparent watercolor washes with colored-pencil botanical texture, subtle paper grain, natural hand-painted edges, fresh spring morning, soft light from upper right. Vertical 3:4 composition, flower centered slightly above middle, generous quiet pale-sky space in upper left for later Chinese title, clear bottom safe area for later credit. No printed text or symbols anywhere.
- 参考图：计划引用两张项目参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/cover-clean.png`
- 排版图片路径：`artwork/composited/cover-final.png`
- 状态：未生成

## 第 1 页

- 页码：1
- 本页中心意思：小种子安静地待在泥土中。
- 本页故事文字：泥土里，小种子睡着了。
- 汉字数：9
- 朗读检查：顺口；“睡着”是低龄可理解的拟人化，不改变植物事实。
- 情绪变化：安静 → 留下好奇伏笔。
- 儿童主体性：无行为推动；孩子可自由观察种子位置。
- 成人/同伴支持：无。
- 文字与画面分工：文字说“睡着”；画面补充种子形状、土层和地表锚点。
- 页间推进：建立起点；下一页让雨水进入。
- 视觉新增量：首次出现地下空间与 S01。
- 出场角色锁定：S01 未萌发种子 1 粒；无其他角色。
- 道具状态：D01/D02 仅在地表边缘弱化可辨，左右关系正确。
- 空间连续性校验：种子在固定种植点，尖端朝右上。
- 镜头切换理由：地下侧向剖面让孩子先看到通常看不见的起点。
- 景别：近景。
- 视角与机位：地下侧向剖面，平视。
- 画面构图：地表线位于上方约 1/5；种子在中下部；左上保留低细节土层。
- 人物调度与动作真实性：种子自然嵌在松软土粒间，不漂浮。
- 画面细节与规整度：保留少量根须残痕与土粒层次，不堆叠昆虫或装饰。
- 色彩设计：湿土棕、低饱和灰绿。
- 光线设计：雨前漫射光从地表柔和透入。
- 文字融入方案：左上，1 行或 2 行，安全边距 ≥6%，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. Side cutaway of the same small garden bed, showing one warm-brown sunflower seed S01 resting naturally in loose soil at the fixed center planting point. The seed is slightly flattened and oval, pointed end angled upper right, with one pale cream longitudinal stripe. The surface line occupies the upper fifth; a small edge of blue-gray pebble D01 appears on the left surface and an unmarked wooden stake D02 appears on the right surface. Transparent watercolor and colored-pencil botanical texture, soft paper grain, quiet safe mood, restrained soil detail, dim natural reflected light. Vertical 3:4, generous low-detail soil area in upper left for later Chinese text.
- 负面提示词：使用统一避让；额外禁止发根、嫩芽、昆虫和第二粒种子。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用两张项目参考图；内置 imagegen；无固定种子。
- 无字图片路径：`artwork/clean/page-01-clean.png`
- 排版完成图片路径：`artwork/composited/page-01-final.png`
- 单页 QA：待生成后检查安全、种子数量、方向、地标和文字区。
- 单页状态：未生成

## 第 2 页

- 页码：2
- 本页中心意思：雨水从地表慢慢渗向种子。
- 本页故事文字：滴答，滴答。雨点来敲门。
- 汉字数：9
- 朗读检查：拟声词清楚；“敲门”由水滴接近种子的画面承接。
- 情绪变化：安静 → 感受到外界。
- 儿童主体性：无行为推动；孩子可沿水迹寻找路径。
- 成人/同伴支持：无。
- 文字与画面分工：文字说雨声；画面说明水如何进入土中。
- 页间推进：雨水到来；下一页种子吸水鼓起。
- 视觉新增量：地上、地下联合剖面和渗水路径。
- 出场角色锁定：S01 种子 1 粒；W01 自然雨点。
- 道具状态：D01 左侧表面变深并带水珠；D02 右侧无字。
- 空间连续性校验：固定种植点和 D01/D02 左右关系不变。
- 镜头切换理由：拉远同时看见雨和地下结果，建立因果。
- 景别：远中景。
- 视角与机位：地上、地下联合侧剖面。
- 画面构图：天空和雨占上方约 1/3，土层占下方；细小水迹向 S01 渗入。
- 人物调度与动作真实性：水分以土色加深和细小渗流表现，不画粗大水管或洪水。
- 画面细节与规整度：少量雨滴和湿土层次，不画卡通水滴脸。
- 色彩设计：雨蓝、湿土棕、蓝灰石色。
- 光线设计：阴雨漫射光，安全明亮，不阴森。
- 文字融入方案：右上浅雨天空，1–2 行，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. A wider side cutaway of the exact same small garden bed during gentle rain. Above ground: soft rain falls on low grass, blue-gray pebble D01 fixed on the left and unmarked pale wooden stake D02 fixed on the right. Below ground: one sunflower seed S01 at the center planting point, still intact but beginning to absorb moisture; subtle darker damp pathways and tiny water beads move downward through realistic soil toward it. Transparent watercolor with colored-pencil soil and plant textures, calm spring rain, no flooding, clear educational cause-and-effect without labels. Vertical 3:4, quiet pale rain-sky space in upper right for later text.
- 负面提示词：使用统一避让；额外禁止洪水、闪电、种皮完全裂开和根芽出现。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用两张项目参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-02-clean.png`
- 排版完成图片路径：`artwork/composited/page-02-final.png`
- 单页 QA：待生成后检查渗水逻辑、地标、无脸雨点和文字区。
- 单页状态：未生成

## 第 3 页

- 页码：3
- 本页中心意思：种子吸水鼓起，种皮出现裂缝。
- 本页故事文字：喝饱水，小种子裂开啦。
- 汉字数：9
- 朗读检查：顺口；“喝饱水”由吸水鼓起的微距画面支撑。
- 情绪变化：感受到外界 → 发现身体变化。
- 儿童主体性：无行为推动。
- 成人/同伴支持：无。
- 文字与画面分工：文字说变化结果；画面展示种皮膨胀和裂缝。
- 页间推进：种皮裂开；下一页从裂缝中出现白根。
- 视觉新增量：首次使用微距，显示种皮纹理。
- 出场角色锁定：S01 吸水种子 1 粒。
- 道具状态：D01/D02 不入镜；以种子纵纹维持身份。
- 空间连续性校验：同一土层，种子尖端仍朝右上。
- 镜头切换理由：微距让孩子看清肉眼不易发现的裂缝。
- 景别：微距特写。
- 视角与机位：地下平视。
- 画面构图：种子偏右下，裂缝清楚；左上留低细节土色区域。
- 人物调度与动作真实性：种子略膨胀、种皮张开，不像爆炸或破碎蛋壳。
- 画面细节与规整度：清楚种皮与湿土材质，避免过度微纹理。
- 色彩设计：深浅土棕、奶油色裂缝。
- 光线设计：柔和地下反射光，裂缝可辨但不发光。
- 文字融入方案：左上，1–2 行，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. Macro underground view of the same single sunflower seed S01 after absorbing water. The warm-brown slightly flattened seed is visibly plumper, its pale cream longitudinal stripe still recognizable, and the seed coat has one small natural opening at the pointed end. Moist loose soil surrounds and supports it. No root has emerged yet. Transparent watercolor washes and careful colored-pencil seed texture, subtle paper grain, scientifically plausible gentle germination, calm discovery mood. Vertical 3:4, seed placed lower right with a natural low-detail brown area in upper left for later Chinese text.
- 负面提示词：使用统一避让；额外禁止爆炸裂纹、蛋壳造型、白根、绿芽、多个种子和发光裂缝。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用 S01 参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-03-clean.png`
- 排版完成图片路径：`artwork/composited/page-03-final.png`
- 单页 QA：待生成后检查种皮裂缝、无根芽、单一种子和文字区。
- 单页状态：未生成

## 第 4 页

- 页码：4
- 本页中心意思：白色胚根先向下生长。
- 本页故事文字：小白根，先往下伸一伸。
- 汉字数：9
- 朗读检查：节奏清楚；“先”强调真实顺序。
- 情绪变化：发现变化 → 方向变得清楚。
- 儿童主体性：孩子可用手指向下模仿。
- 成人/同伴支持：无。
- 文字与画面分工：文字说方向；画面显示根尖和土粒接触。
- 页间推进：根向下；下一页嫩芽向上。
- 视觉新增量：白根首次出现，形成上下对照伏笔。
- 出场角色锁定：S01 裂种发根阶段 1 株。
- 道具状态：D01/D02 不入镜。
- 空间连续性校验：种子尖端与纵纹承接第 3 页；根向画面下方。
- 镜头切换理由：轻俯特写清楚显示根尖路径。
- 景别：特写。
- 视角与机位：地下轻微俯视。
- 画面构图：种子在中上部，白根弯曲向下；右上留文字区。
- 人物调度与动作真实性：根尖贴着土粒间隙生长，不漂浮、不分叉过度。
- 画面细节与规整度：保留少量细根毛暗示，不画成熟庞大根系。
- 色彩设计：土棕、奶油白根尖。
- 光线设计：柔和反射光，根不发光。
- 文字融入方案：右上低细节土层，1 行，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. Close underground view of the same cracked sunflower seed S01, with its warm-brown coat and cream stripe unchanged. One pale embryonic root has emerged from the opening and curves clearly downward through small gaps in moist soil; the root tip touches and passes between soil grains. No green shoot is above ground yet, no mature branching root system. Transparent watercolor and colored-pencil botanical texture, scientifically plausible, calm gentle motion. Vertical 3:4, seed in upper middle, root leading downward, quiet upper-right soil area for later Chinese text.
- 负面提示词：使用统一避让；额外禁止根向上、绿芽出土、成熟根团、发光根和重复种子。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用 S01 参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-04-clean.png`
- 排版完成图片路径：`artwork/composited/page-04-final.png`
- 单页 QA：待生成后检查根方向、阶段和物理接触。
- 单页状态：未生成

## 第 5 页

- 页码：5
- 本页中心意思：绿色嫩芽向上顶出泥土。
- 本页故事文字：小嫩芽，再往上顶一顶。
- 汉字数：9
- 朗读检查：与第 4 页形成“先下、再上”的朗读对应。
- 情绪变化：地下方向清楚 → 第一次接触天空。
- 儿童主体性：孩子可用手掌向上模仿顶出的动作。
- 成人/同伴支持：无。
- 文字与画面分工：文字说动作；画面补充土面裂口、弯曲芽钩和雨后水珠。
- 页间推进：嫩芽出土；下一页子叶展开。
- 视觉新增量：从地下切到地表低机位。
- 出场角色锁定：S01 出土幼芽 1 株。
- 道具状态：D01 固定在左侧；D02 可在右后方弱化。
- 空间连续性校验：嫩芽从同一种植点向上，D01/D02 关系不变。
- 镜头切换理由：贴地低机位让出土动作显得清楚而有力量，不夸张英雄化。
- 景别：近景。
- 视角与机位：地表低机位，平视略仰。
- 画面构图：嫩芽位于下方中央，弯曲芽尖正顶开土面；左上留天空文字区。
- 人物调度与动作真实性：嫩芽与土面真实接触，茎有自然弯曲和重心。
- 画面细节与规整度：少量湿土块和水珠，不添加昆虫和额外植物。
- 色彩设计：嫩叶绿、湿土棕、天青。
- 光线设计：雨后柔和天光从右上来。
- 文字融入方案：左上浅天空，1 行，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. Ground-level close view in the exact same garden bed after rain. One young sunflower shoot S01 emerges from the fixed center planting point, its small green hypocotyl naturally curved like a hook as it gently pushes apart damp soil. Blue-gray pebble D01 remains on the left; the unmarked wooden stake D02 is softly visible on the right rear. A few realistic water beads, no extra plants. Transparent watercolor with colored-pencil botanical detail, fresh safe spring mood, soft natural light from upper right. Vertical 3:4, shoot lower center, generous quiet pale-sky area upper left for later Chinese text.
- 负面提示词：使用统一避让；额外禁止 fully open leaves、flower、multiple sprouts、heroic glow、flying soil 和昆虫。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用两张项目参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-05-clean.png`
- 排版完成图片路径：`artwork/composited/page-05-final.png`
- 单页 QA：待生成后检查单芽、出土接触、地标和文字区。
- 单页状态：未生成

## 第 6 页

- 页码：6
- 本页中心意思：两片子叶在阳光下张开。
- 本页故事文字：太阳照一照，两片小叶张开了。
- 汉字数：12
- 朗读检查：顺口；正文用“小叶”，家长指南说明这是子叶。
- 情绪变化：新鲜 → 舒展。
- 儿童主体性：孩子可张开双手模仿两片子叶。
- 成人/同伴支持：无。
- 文字与画面分工：文字说张开；画面通过芽的主观仰视表现第一次见光。
- 页间推进：子叶展开；下一页出现形状不同的真叶。
- 视觉新增量：主观仰视和两片对生子叶。
- 出场角色锁定：S01 子叶幼苗 1 株；L01 自然光。
- 道具状态：D02 右缘可辨，无文字。
- 空间连续性校验：同一种植点，茎向上，D02 仍在右侧。
- 镜头切换理由：主观仰视让孩子感受嫩芽第一次接触天空和光线。
- 景别：中近景。
- 视角与机位：贴近幼苗的轻微仰视。
- 画面构图：两片圆润子叶在中下部向两侧打开；右上光线与文字区分开。
- 人物调度与动作真实性：子叶与细茎连接自然，不出现成熟锯齿真叶。
- 画面细节与规整度：天空简洁，光线自然，无太阳脸和发光粒子。
- 色彩设计：嫩叶绿、浅天青、少量奶油晨光。
- 光线设计：右上柔和晨光，阴影透明。
- 文字融入方案：右上浅天空，2 行以内，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. Intimate low-angle view beside the same newly emerged sunflower seedling S01. Exactly two smooth rounded green cotyledons open naturally to either side on one slender stem; no serrated true leaves yet. The unmarked wooden stake D02 remains softly at the right edge, confirming the same garden. Clear pale blue spring sky and soft natural sunlight from upper right, no visible cartoon sun. Transparent watercolor washes, colored-pencil leaf veins, subtle paper grain, quiet sense of first light. Vertical 3:4, cotyledons in lower middle, calm pale-sky text space upper right without covering the light direction.
- 负面提示词：使用统一避让；额外禁止 serrated mature leaves、flower bud、extra cotyledons、cartoon sun 和 glowing rays。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用两张项目参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-06-clean.png`
- 排版完成图片路径：`artwork/composited/page-06-final.png`
- 单页 QA：待生成后检查恰好两片子叶、无真叶和无太阳脸。
- 单页状态：未生成

## 第 7 页

- 页码：7
- 本页中心意思：向日葵真叶一片片长出来。
- 本页故事文字：雨点来，太阳照。真叶一片片长。
- 汉字数：12
- 朗读检查：两处自然停顿；“真叶”与画面清楚对应。
- 情绪变化：舒展 → 稳定生长。
- 儿童主体性：孩子可比较子叶和真叶形状。
- 成人/同伴支持：无。
- 文字与画面分工：文字点出环境和真叶；画面展示叶形差异与更高植株。
- 页间推进：真叶出现；下一页茎更高并形成花苞。
- 视觉新增量：平视中景、宽卵形轻锯齿真叶。
- 出场角色锁定：S01 真叶幼苗 1 株；W01/L01 为自然痕迹。
- 道具状态：D01 左、D02 右完整可辨。
- 空间连续性校验：固定种植点不变，根系可在浅剖面中弱化暗示。
- 镜头切换理由：回到平视中景，便于比较植株整体和地标关系。
- 景别：中景。
- 视角与机位：平视。
- 画面构图：植株居中略偏下；左右地标稳定；左上留文字区。
- 人物调度与动作真实性：茎直立但略有自然弧度；真叶角度不完全对称。
- 画面细节与规整度：保留少量雨后水珠和轻微土壤使用痕迹，不添加花朵。
- 色彩设计：草绿、天青、少量雨蓝。
- 光线设计：雨后柔和自然光，右上来光。
- 文字融入方案：左上天空与低细节背景，2 行以内，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. Mid shot of the exact same sunflower seedling S01 in the same fixed garden bed, now taller with the original two smooth cotyledons lower down and several new broad ovate true leaves above, their edges gently serrated and veins visible. One main stem only. Blue-gray pebble D01 remains left, unmarked wooden stake D02 remains right. A few natural raindrops on leaves and soft sunlight from upper right suggest rain and sun without characters. Transparent watercolor and colored-pencil botanical texture, natural asymmetry, fresh green and pale blue palette. Vertical 3:4, plant lower center, quiet upper-left area for later Chinese text.
- 负面提示词：使用统一避让；额外禁止花苞、花、过多成熟叶片、完全对称叶序和额外幼苗。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用两张项目参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-07-clean.png`
- 排版完成图片路径：`artwork/composited/page-07-final.png`
- 单页 QA：待生成后检查子叶/真叶差异、单一主茎和地标。
- 单页状态：未生成

## 第 8 页

- 页码：8
- 本页中心意思：茎长高，顶端形成花苞。
- 本页故事文字：茎长高了，小花苞也来了。
- 汉字数：10
- 朗读检查：顺口；两个现象属于同一生长阶段的整体发现。
- 情绪变化：稳定生长 → 期待。
- 儿童主体性：孩子可猜花苞里会出现什么颜色。
- 成人/同伴支持：无。
- 文字与画面分工：文字说花苞到来；画面补充高度、叶片和轻风。
- 页间推进：花苞形成；下一页花瓣完全打开。
- 视觉新增量：显著高度变化、轻微仰视和紧闭花苞。
- 出场角色锁定：S01 高茎花苞阶段 1 株；B01 轻风。
- 道具状态：D01/D02 在下方弱化；S01 高于 D02。
- 空间连续性校验：同一花圃与单一主茎，D01 左、D02 右。
- 镜头切换理由：轻微仰视强调长高和顶端花苞，为翻页开花蓄势。
- 景别：远中景。
- 视角与机位：轻微仰视。
- 画面构图：高茎从下方中心上升，闭合花苞位于中上；右上留文字区，不遮花苞。
- 人物调度与动作真实性：茎有支撑感，叶片受轻风略微偏转，花苞不提前开放。
- 画面细节与规整度：少量花萼和黄绿色边缘，不出现完整黄色花瓣。
- 色彩设计：深浅叶绿、天青、少量黄绿色。
- 光线设计：右上明亮自然光，仍无金黄滤镜。
- 文字融入方案：右上浅天空，1–2 行，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook page. Slight low-angle wider view of the same single sunflower S01 in the fixed garden bed. One sturdy but naturally curved green main stem has grown taller than the unmarked wooden stake D02 on the right; blue-gray pebble D01 remains left. Broad slightly serrated leaves grow at plausible intervals. At the top is one closed green sunflower bud with sepals and only the faintest yellow-green hint at the edges, not yet open. A light breeze gently changes leaf angles. Transparent watercolor and colored-pencil botanical texture, pale blue sky, natural light from upper right. Vertical 3:4, bud in upper middle-left and quiet upper-right sky for later Chinese text.
- 负面提示词：使用统一避让；额外禁止 open flower、multiple buds、branching stems、oversaturated yellow、bent broken stem 和额外 plants。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用两张项目参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-08-clean.png`
- 排版完成图片路径：`artwork/composited/page-08-final.png`
- 单页 QA：待生成后检查单花苞、株高、地标和安全区。
- 单页状态：未生成

## 第 9 页

- 页码：9
- 本页中心意思：向日葵花瓣一片片完全打开。
- 本页故事文字：一片，两片……花开了！
- 汉字数：7
- 朗读检查：节奏明快，省略号提供打开的等待感。
- 情绪变化：期待 → 明亮满足。
- 儿童主体性：孩子可跟读“一片，两片”并观察完整花盘。
- 成人/同伴支持：无。
- 文字与画面分工：文字表达发现；画面呈现完全开放、同一花圃和清晨空间。
- 页间推进：完成从种子到花的生长弧线。
- 视觉新增量：开阔远景、黄色花盘和满足性留白。
- 出场角色锁定：S01 完全开放成株 1 株；B01 轻风。
- 道具状态：D01 左、D02 右在下方弱化；D02 被高茎部分遮挡。
- 空间连续性校验：同一种植点、单一主茎、单一花盘，主光右上。
- 镜头切换理由：拉远给结尾呼吸感，同时让孩子确认这仍是同一座花圃。
- 景别：远景。
- 视角与机位：平视略仰。
- 画面构图：S01 位于中下部，花盘中上；左上浅蓝天空为文字区。
- 人物调度与动作真实性：茎承重合理，花盘略向右上自然光，叶片与花瓣轻微自然偏差。
- 画面细节与规整度：花瓣数量自然丰富但不机械重复，背景不堆叠其他花。
- 色彩设计：低饱和向日葵黄成为强调色，叶绿和清澈浅蓝平衡。
- 光线设计：雨后清晨柔光，右上来光，无过度光晕。
- 文字融入方案：左上浅天空，1 行，后期文本层。
- 图片比例与像素尺寸：`3:4`，`1536×2048`
- 无字插画图像提示词：Use case: illustration-story. Asset type: wordless preschool picturebook ending page. Open wider view of the exact same single sunflower S01, now fully blooming in the fixed garden bed. One main stem, one broad flower head with a natural warm-brown center and low-saturation golden-yellow petals, broad slightly serrated leaves, subtle natural asymmetry. The flower turns slightly toward soft light from upper right. Blue-gray pebble D01 remains at the lower left and the unmarked wooden stake D02 remains at the lower right, partly obscured by the taller stem. Transparent watercolor washes and colored-pencil botanical texture, fresh pale blue morning sky, gentle breeze, peaceful satisfying ending. Vertical 3:4, plant centered lower, generous quiet upper-left sky for later Chinese text.
- 负面提示词：使用统一避让；额外禁止 second flower、multiple heads、other flower species、cartoon smile、perfect radial symmetry 和 glowing halo。
- 使用的参考图、模型、版本、种子或角色引用信息：计划引用两张项目参考图；内置 imagegen。
- 无字图片路径：`artwork/clean/page-09-clean.png`
- 排版完成图片路径：`artwork/composited/page-09-final.png`
- 单页 QA：待生成后检查单花盘、物种、地标、色彩和文字区。
- 单页状态：未生成

