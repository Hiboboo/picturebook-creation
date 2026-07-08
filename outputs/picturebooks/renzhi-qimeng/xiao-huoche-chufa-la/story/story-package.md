# 《小火车出发啦》故事包 v2

## 1. 交付状态

- 当前状态：全书出图、排版完成、PDF/PPTX 导出完成。
- 实际图片生成：是，已生成新版封面和第 1-8 页无字内页，路径位于 `artwork/clean/v2/`；排版完成图位于 `artwork/composited/v2/`。
- 生成方式：AI 辅助故事设计；无字插画由内置 `image_gen` 生成后复制到项目目录；中文标题、正文和家长页由本地后期文本层合成；PDF 由本地 ReportLab 导出，PPTX 由本地 OpenXML 包装导出。
- 本次未完成项：无。若用于正式印刷，建议另做人工校色、出血版和印前审校。
- 需要用户确认项：最终排版文字位置、是否继续做印刷规格版本或更多重绘备选图。

## 2. 基本信息

- 系列：认知启蒙系列
- 书名：小火车出发啦
- 主题：交通工具：火车
- 图/文：小葫芦
- 主要适合年龄：2-3 岁
- 可延伸年龄：3-4 岁
- 核心主题：孩子按照自己的节奏认识公园小火车。
- 孩子的生活入口：在公园小火车站台等车、看车、听声音、观察车门和车窗，再慢慢坐上小火车。
- 目标情绪变化：从好奇张望，到停一停、听一听、靠近一点，再到坐稳观察，最后看着小火车走远并回味。
- 故事页数：8 页，不含封面。
- 画面风格：清爽明亮水彩和彩铅线条，轻微纸面颗粒，人物真实幼儿比例，公园小火车场景。
- 视觉细节密度：适中偏简洁。
- 色彩设计策略：主色为晴空蓝、草地绿和火车红；辅助色为奶白站台、浅灰轨道；强调色为安全黄线、红鞋和车头圆灯。温暖来自陪伴关系，不依赖黄色滤镜。
- 图片比例：固定 `3:4` 竖版。
- 锁定像素尺寸：`1086x1448`。
- 文字安全边距：至少画布宽高的 `6%`；封面和内页均由后期文本层加字。
- 固定输出目录：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/`

## 3. 儿童发展与情绪安全策略

- 孩子可能感受到的情绪：好奇、专注、轻微犹豫、安心、满足和回味。
- 故事如何接纳这种情绪：小葫芦可以停一下、听一下、先看看里面，再决定靠近和坐下。
- 孩子拥有的选择：观察、牵手、停一停、看车门、看座位、坐稳后看窗外、下车后回头看。
- 成人如何提供支持：妈妈蹲下或坐在旁边，保持开放手势和等待姿态，不递任务、不催促、不替孩子决定。
- 故事中的最小可行尝试：小葫芦只要站在黄线后听见“呜呜”、看见车门和座位，就已经在用自己的节奏认识火车。
- 结尾如何避免“必须克服”：结尾不是“成功坐车”，而是小火车走远后，小葫芦还在看，留下“我认识了一点点”的余韵。
- 奖励、掌声或贴纸的处理：不出现奖励、掌声或贴纸。
- 禁用表达：不写“勇敢”“克服”“挑战”“成功了”“不怕了”“快一点”“别怕”“大家都等你”“你真棒”。

## 4. 故事设定卡

- 背景：晴朗上午的公园小火车站台，一辆低速观光小火车沿固定轨道进站、停靠、出发、走远。
- 儿童视角：小葫芦通过声音、颜色、车厢、车轮、车门、扶手、车窗和远去的轨道认识小火车。
- 故事弧线：生活入口 → 停下听声音 → 看见车头 → 数车厢 → 看车轮 → 看车门里面 → 坐稳看窗外 → 看小火车走远。
- 重复结构：低龄动词重复：“停一停、听一听、看一看、数一数、慢慢走、还在看”。拟声词“呜呜”“咔哒咔哒”作为声音钩子。
- 页间推进：每页新增一个可见动作或观察对象，同时推进小葫芦的心理节奏。
- 温暖结尾：小火车走远，小葫芦没有立刻离开，而是回头看远处轨道，画面留给孩子回味。
- 故事禁改项：不改成大型真实铁路，不出现跨轨道、摸车轮、探出车窗、强迫上车或完成任务式结尾。

## 5. 视觉圣经与连续性锁定

### 5.1 角色圣经

#### C01-小葫芦

- 名称与身份：幼儿主角
- 年龄感 / 物种：约 3 岁人类幼儿
- 身高与头身比例：成人腰部高度，约 3.5 头身，幼儿真实比例
- 脸型与核心五官：圆脸，黑色圆眼，短鼻，小嘴
- 发型与发色：黑色短发，额前一小撮自然翘起
- 上衣：明亮黄色长袖上衣
- 下装：浅蓝牛仔背带裤
- 鞋袜：白袜，红色帆布鞋
- 固定配色：黄色、浅蓝、红鞋、蓝背包
- 标志性配件或道具：D01 小蓝背包
- 常见表情范围：好奇观察、专注听、发现、犹豫观察、安心、满足回味；禁止每页固定开心笑。
- 禁改项：发型、黄色上衣、浅蓝背带裤、红鞋、小蓝背包、幼儿身高比例。
- 可变项：停下、侧头听、伸手数、微微后退观察、坐稳扶扶手、回头看。
- 角色参考图路径或状态：已整理，见 `outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/character-reference-sheet-v2.png`。

#### A01-妈妈

- 名称与身份：陪伴者
- 年龄感 / 物种：年轻成人女性
- 身高与头身比例：约 C01 两倍高，自然成人比例
- 脸型与核心五官：椭圆脸，温和眼神
- 发型与发色：深棕黑色低马尾
- 上衣：浅青绿色开衫，白色内搭
- 下装：米白长裤
- 鞋袜：浅灰平底鞋
- 固定配色：浅青绿、白、米白
- 标志性配件或道具：无固定手持物
- 常见表情范围：等待、注视、陪伴、轻微微笑；减少持续标准微笑。
- 禁改项：低马尾、浅青绿开衫、米白长裤、非催促姿态。
- 可变项：蹲下、站在稍后位置、坐在旁边、自然看向孩子或远处轨道。
- 角色参考图路径或状态：已整理，见 `outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/character-reference-sheet-v2.png`。

#### T01-公园小火车

- 名称与身份：低速观光小火车，不拟人化
- 车头：红色圆润车头，天蓝车顶，奶白窗框，圆形头灯，小烟囱
- 车厢：两节浅黄色短车厢
- 车轮与轨道：深灰小车轮，浅灰固定轨道
- 固定配色：红车头、天蓝车顶、奶白窗框、两节浅黄色车厢
- 禁改项：无拟人脸、无车身文字、无编号、两节车厢、低速公园小火车属性。
- 可变项：进站、停靠、车门打开、车内、弯轨行驶、远去。
- 角色参考图路径或状态：已整理，见 `outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/character-reference-sheet-v2.png`。

### 5.2 演员表

- 固定角色总表：C01 每页常驻；A01 每页出现或局部出现；T01 第 2-8 页出现。
- 配角人数与身份锁定：不设置固定配角；可有极远景模糊游客，但不得抢视觉。
- 身高关系：A01 约为 C01 两倍高；T01 车门略高于 C01。
- 不得互换或替代的角色：C01 不得换发型、服装或背包；A01 不得变成其他成人；T01 不得变成大型铁路列车。

### 5.3 环境与空间连续性地图

- 时间与天气：晴朗上午，柔和自然光。
- 核心场景：公园小火车站台、弯轨、小桥、草地与树。
- 起点：站台入口右侧，黄线后。
- 目标点：车门、座位、车窗，再到远处弯轨。
- 行动路线和路径轴线：轨道从画面左后方向右前方弯入，再向右侧小桥延伸；人物始终在黄线内侧或车厢内。
- 固定地标：黄色安全线、绿色站台棚、弯轨、小桥、两棵圆冠树。
- 角色进入/离开方向：小葫芦和妈妈从右侧站台进入；火车从左后方进站，向右侧出发并远去。
- 镜头主侧与越轴线：默认从站台内侧看向轨道，不随意翻转轨道左右关系。
- 主光源方向：左上方自然日光，柔和阴影向右下。
- 允许变化项：景别、人物距离、车头位置、车内/车外视角、远处桥与树的显隐。
- 禁改项：黄线在人物与轨道之间；轨道不能穿过人物脚下；不得出现真实危险铁路。
- 环境参考图或平面图路径：已整理，见 `outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/environment-reference-sheet-v2.png`。

### 5.4 道具状态表

#### D01-小蓝背包

- 归属角色：C01
- 颜色、尺寸和图案：蓝色圆角小背包，白色小扣，无文字。
- 初始位置：C01 背在身后。
- 每页状态变化：第 1-5 页背着；第 6 页放在孩子腿边或座位旁；第 7 页车内可见，仍在座位旁；第 8 页重新背上或由 C01 自然手提。
- 持握手或摆放方向：第 6-7 页不可悬空，需真实靠在座位或腿边。
- 禁改项：蓝色、圆角、小尺寸、无文字。

#### D03-黄色安全线

- 归属角色：环境
- 颜色、尺寸和图案：平整黄色线条，无文字。
- 初始位置：站台边缘，轨道前。
- 每页状态变化：第 1-5 页明显；第 8 页再次出现；第 6-7 页不出现或仅从窗外隐约可见。
- 持握手或摆放方向：不适用。
- 禁改项：出现时必须在人物与轨道之间；人物不能踩线、跨线或站在线外。

### 5.5 风格、色板与版式锁定

- 媒介与线条：透明水彩底色，彩铅轻线，边缘柔和但结构清楚。
- 颗粒与纹理：轻微纸纹和水彩晕染，不使用厚重油画、矢量硬边或塑料感 3D。
- 人物比例和面部风格：真实幼儿绘本比例，表情有细微变化，不全员同款大笑。
- 主色：晴空蓝、草地绿、火车红。
- 辅助色：奶白站台、浅木色栅栏、浅灰轨道。
- 强调色：安全黄线、红鞋、车头圆灯。
- 禁用色彩倾向：过度黄滤镜、随机彩虹色、阴森低照度、全画面高饱和、游戏插画式高光。
- 文字字体层级：书名为清晰圆体或黑体大字；正文为普通清楚中文字体；署名小字号深灰。
- 文字区规则：画面上方或侧上方自然低细节区域；不得用固定不透明卡片。
- 无字插画规则：图像模型不得生成中文书名、正文、标签、站牌文字、车身编号、车票文字或可读墙面文字。

### 5.6 Natural Imperfection Rules

- avoid perfect symmetry
- avoid overly clean vector edges
- maintain handmade watercolor feeling
- allow slight variation in facial expression
- allow natural clothing wrinkles
- allow subtle watercolor pigment spreading
- avoid plastic 3D rendering feeling
- avoid identical smiles across pages
- avoid overly perfect character poses
- allow small pauses in body posture, such as a tilted head, relaxed hand, shifted weight, or slightly uneven clothing folds
- keep visual richness tied to story objects, not random decoration

### 5.7 绘本真实性要求

所有无字插画提示词都必须包含或等价表达：

```text
Illustration should feel like a hand-painted children's picture book.
Avoid cinematic lighting, 3D animation style, ultra sharp edges, perfect symmetry, overly polished characters, plastic skin, game illustration style.
Keep natural watercolor pigment spread, colored-pencil line variation, gentle paper texture, natural clothing wrinkles, and varied child expressions.
```

## 6. 全书镜头与翻页计划

| 页码 | 叙事节点 | 情绪起点→终点 | 景别 | 视角/机位 | 出场角色 ID | 核心动作 | 空间锚点 | 文字区 | 相比上一页的视觉新增量 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 停下等车 | 好奇→安静听 | 远中景 | 平视站台侧 | C01, A01 | 停在黄线后，侧头听 | 黄线、站台棚、弯轨 | 左上天空 | 建立站台和“停一停” |
| 2 | 车头来了 | 安静听→专注看 | 中景 | 低幼儿视角 | C01, A01, T01 | 视线追向红车头 | 红车头、轨道、黄线 | 右上棚下 | 首次出现车头和声音 |
| 3 | 数车厢 | 专注→发现连接 | 中景 | 轻微俯视 | C01, A01, T01 | 手指数两节车厢 | 两节车厢、车钩 | 左上树冠空区 | 出现“跟着”的结构 |
| 4 | 看车轮 | 好奇→理解一点 | 特写 | 儿童主观低机位 | C01 局部, A01 局部, T01 | 鞋尖停在线后，看车轮 | 车轮、轨道、黄线 | 上方浅地面 | 第一次部件特写 |
| 5 | 看车门里面 | 犹豫→愿意再看 | 近景 | 平视 | C01, A01, T01 | 看打开的门、座位、车窗 | 车门、座位、黄线 | 右上车厢外侧 | 去掉车票，突出观察空间 |
| 6 | 坐好看窗外 | 谨慎→安心 | 中景 | 车厢内平视 | C01, A01, T01 | 坐稳，手扶扶手，看窗外 | 车窗、扶手、背包 | 左上车窗外天空 | 背包放座位旁，进入车内 |
| 7 | 弯轨慢走 | 安心→愉快观察 | 远中景 | 轻微俯视 | C01, A01, T01 | 小火车沿弯轨走 | 小桥、两棵树、弯轨 | 上方天空 | 外部环境移动 |
| 8 | 走远回味 | 满足→还想看 | 中远景 | 平视站台侧 | C01, A01, T01 | 小火车走远，C01 回头看 | 远处轨道、小桥、黄线 | 左上天空 | 从告别转为余韵 |

## 7. 封面图片

- 封面状态：新版已生成并排版完成。
- 无字封面图片文件路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/cover-clean.png`
- 排版完成封面图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/cover-final.png`
- 图片比例与像素尺寸：固定 `3:4`，`1086x1448`
- 封面中心意思：小葫芦在安全线后主动观察小火车，妈妈在旁边陪伴但不抢视觉。
- 封面构图说明：保留左侧小火车、右侧人物、中间安全线和顶部留白；将火车视觉占比比旧版缩小约 10%-15%；小葫芦略放大，身体姿态更主动，视线明确看向火车；妈妈略后移或退到第二视觉层级。
- 角色锁定：C01 黄色上衣、浅蓝背带裤、红鞋、小蓝背包；A01 浅青绿开衫；T01 红车头、天蓝车顶、两节浅黄色车厢。
- 书名排版：后期添加，顶部 2 行以内，清晰普通中文字体。
- 署名排版：后期添加 `图/文：小葫芦`，深灰小字。
- 标题安全区：顶部天空低细节区，不遮挡小葫芦脸、视线和黄线。
- 无字封面图像提示词：清爽水彩和彩铅风格，3:4 竖版，公园小火车站台；C01 小葫芦略大于旧版，站在黄色安全线后，身体微微前倾但脚不踩线，专注看向左侧小火车；A01 妈妈站或蹲在稍后位置，陪伴但不是第一视觉；T01 红色圆润公园小火车从左后方慢慢进站，火车比旧版小 10%-15%，两节浅黄色车厢，顶部自然留出低细节文字区；无任何文字、数字、标志或站牌文字。Illustration should feel like a hand-painted children's picture book; avoid cinematic lighting, 3D animation style, ultra sharp edges, perfect symmetry, plastic skin, overly polished characters, game illustration style.
- 封面负面提示词：no mature content, no violence, no danger, no real railway hazard, no child crossing tracks, no child touching train, no text, no train numbers, no pseudo-Chinese, no extra fingers, no malformed hands, no duplicated child, no identical smiles, no random clutter, no plastic skin.
- 使用的角色/环境参考图、模型、版本、种子或引用信息：内置 `image_gen` 新版 v2；旧版样张仅作风格对照。
- 封面 QA 结果：通过。火车视觉权重降低，小葫芦更突出，妈妈后移，无文字、无编号、无越线动作。

## 8. 内页图片与文字

### 第 1 页

- 页码：1
- 本页中心意思：小葫芦停在黄线后，先听一听。
- 本页故事文字：停一停，听一听。
- 汉字数：6
- 朗读检查：两个重复动作，适合低龄朗读。
- 情绪变化：好奇张望 → 安静听。
- 儿童主体性：小葫芦选择先停下，不急着靠近。
- 成人/同伴支持：妈妈站在稍后位置，手自然垂下或轻指黄线，不催促。
- 文字与画面分工：文字写动作节奏；画面补充站台、安全线和远处轨道。
- 页间推进：为第 2 页“呜呜”声音和车头出现做铺垫。
- 视觉新增量：建立站台、黄线、孩子停下的身体姿态。
- 出场角色锁定：C01、A01。
- 道具状态：D01 背在 C01 身后；D03 黄线在人物前方。
- 空间连续性校验：C01 与 A01 位于站台内侧，轨道在黄线外侧。
- 镜头切换理由：建立场景，无越轴。
- 景别：远中景
- 视角与机位：平视站台侧
- 画面构图：C01 略偏右前，A01 更后，左侧轨道延伸，顶部天空留字。
- 人物调度与动作真实性：C01 双脚落地，头稍侧向轨道，身体重心自然偏一侧。
- 画面细节与规整度：保留黄线、站台棚、弯轨；删去站牌文字和无关乘客。
- 色彩设计：蓝绿清爽，黄线清楚但不刺眼。
- 光线设计：左上自然光，透明阴影。
- 文字融入方案：左上天空低细节区，1 行。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：3:4 portrait watercolor and colored-pencil preschool picture book illustration, park mini-train station platform, C01 toddler in yellow shirt, light blue denim overalls, red canvas shoes, small blue backpack, standing safely behind a plain yellow safety line, pausing and tilting head slightly as if listening; A01 mother in light teal cardigan stands slightly behind with calm waiting posture; empty curved track in background, green station canopy, morning light, upper-left low-detail sky for later text, no text anywhere. Illustration should feel like a hand-painted children's picture book; avoid cinematic lighting, 3D animation style, ultra sharp edges, perfect symmetry, plastic skin, identical smiles.
- 负面提示词：preschool-safe; no child on tracks, no coercion, no shaming, no text, no signs with letters, no pseudo-Chinese, no extra fingers, no fused hands, no duplicated people, no random clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-01-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-01-final.png`
- 单页 QA：通过。无文字乱码，C01 在线内侧，D01 背在身后，A01 为等待陪伴姿态。
- 单页状态：通过。

### 第 2 页

- 页码：2
- 本页中心意思：小葫芦听见声音，看见红车头。
- 本页故事文字：呜呜，红车头来了。
- 汉字数：7
- 朗读检查：拟声词在前，有翻页动力。
- 情绪变化：安静听 → 专注看。
- 儿童主体性：小葫芦视线追向车头，身体仍在线后。
- 成人/同伴支持：妈妈保持等待姿态，不伸手推孩子。
- 文字与画面分工：文字说声音和车头；画面补充距离、速度和安全线。
- 页间推进：从听声音推进到看见车头。
- 视觉新增量：首次出现红色车头。
- 出场角色锁定：C01、A01、T01。
- 道具状态：D01 背在 C01 身后；D03 黄线清晰。
- 空间连续性校验：T01 从左后方进站，人物仍在右前方黄线内侧。
- 镜头切换理由：中景突出车头和孩子专注表情。
- 景别：中景
- 视角与机位：幼儿平视略低机位
- 画面构图：车头在左中，C01 在右侧，A01 略后。
- 人物调度与动作真实性：C01 脚不越线，肩膀略向车头转。
- 画面细节与规整度：车头圆润，头灯清楚，不画浓烟和车身文字。
- 色彩设计：火车红成为焦点，背景蓝绿保持清爽。
- 光线设计：车头左上受光。
- 文字融入方案：右上站台棚下或天空低细节区，1 行。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：Preschool watercolor and colored-pencil illustration, C01 toddler safely behind plain yellow platform line, watching a rounded red park mini-train engine T01 with sky-blue roof slowly entering from the left background on curved track; A01 mother slightly behind, calm and attentive, not smiling broadly; child expression focused and curious, no readable signs, no letters, upper-right low-detail area for later text. Hand-painted children's picture book feeling, natural clothing wrinkles, subtle watercolor pigment spread; avoid 3D animation, cinematic lighting, ultra sharp edges, perfect symmetry, plastic skin.
- 负面提示词：no child on rail, no fast train, no smoke cloud, no text, no pseudo-Chinese, no extra limbs, no outfit changes, no random decorations, no identical smiles.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-02-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-02-final.png`
- 单页 QA：通过。红车头进站，C01 在线内侧专注看，未出现文字、编号或危险动作。
- 单页状态：通过。

### 第 3 页

- 页码：3
- 本页中心意思：小葫芦发现车厢一节一节跟着车头。
- 本页故事文字：一节，两节，车厢跟上啦。
- 汉字数：9
- 朗读检查：数数节奏清楚，“跟上啦”有动作感。
- 情绪变化：专注 → 发现。
- 儿童主体性：小葫芦伸出手指数车厢。
- 成人/同伴支持：妈妈在旁边等待，不替孩子数完。
- 文字与画面分工：文字说数数和跟随；画面补充车钩、两节车厢和孩子的发现表情。
- 页间推进：从车头推进到车厢关系。
- 视觉新增量：两节车厢和车钩连接。
- 出场角色锁定：C01、A01、T01。
- 道具状态：D01 背在 C01 背后；D03 黄线仍在人物前。
- 空间连续性校验：T01 已停靠更近，车厢沿同一弯轨排列。
- 镜头切换理由：轻微俯视帮助看清“一节，两节”。
- 景别：中景
- 视角与机位：轻微俯视
- 画面构图：车头左侧，两节车厢向后延伸，C01 在右下数。
- 人物调度与动作真实性：C01 一只手指向车厢，脚仍在线后。
- 画面细节与规整度：只画两节车厢，车窗无文字或编号。
- 色彩设计：浅黄色车厢与红车头区分。
- 光线设计：上午自然光。
- 文字融入方案：左上树冠与天空低细节区，1 行或 2 行。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：Watercolor colored-pencil preschool scene, C01 toddler behind yellow line, pointing with one finger while counting exactly two pale-yellow passenger cars connected behind a red mini-train engine, A01 mother nearby in quiet waiting posture, curved track and platform visible, clear coupling, no letters or numbers on train, reserved low-detail top-left area for later text. Hand-painted picture book feeling, slight expression variation, natural clothing wrinkles, subtle watercolor spread; avoid perfect symmetry, 3D animation style, ultra sharp edges, plastic skin, identical smiles.
- 负面提示词：no text, no numbers, no more than two passenger cars, no unsafe crossing, no extra fingers, no fused hands, no inconsistent clothing.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2；第 3 页曾因与第 2 页过近而重生成一次。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-03-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-03-final.png`
- 单页 QA：通过。两节浅黄色车厢清楚，C01 有数数动作，构图与第 2 页区分明确。
- 单页状态：通过。

### 第 4 页

- 页码：4
- 本页中心意思：小葫芦看见车轮在轨道上走。
- 本页故事文字：小车轮，咔哒咔哒。
- 汉字数：7
- 朗读检查：拟声词顺口，适合模仿。
- 情绪变化：好奇 → 理解一点。
- 儿童主体性：小葫芦在线后看，不触碰车轮。
- 成人/同伴支持：妈妈手部可在远处自然垂放，不抓拉。
- 文字与画面分工：文字说声音；画面说明车轮和轨道关系。
- 页间推进：从车厢关系推进到车轮如何贴着轨道移动。
- 视觉新增量：车轮/轨道特写。
- 出场角色锁定：C01 局部、A01 局部可选、T01 车轮。
- 道具状态：D03 黄线边缘进入画面，D01 可不显著但不能矛盾。
- 空间连续性校验：镜头仍在站台安全侧，黄线在前景。
- 镜头切换理由：特写服务认知对象，保留黄线避免误读。
- 景别：特写
- 视角与机位：儿童主观低机位
- 画面构图：下方黄线，中央车轮与轨道，右侧 C01 小鞋在安全线后。
- 人物调度与动作真实性：鞋尖不越线，手不伸进轨道区域。
- 画面细节与规整度：只保留车轮、轨道、黄线、小鞋和必要车体下缘。
- 色彩设计：灰轨道、红车体、黄线形成清楚分层。
- 光线设计：低角度局部阴影真实但不压迫。
- 文字融入方案：上方浅色站台地面低细节区，1 行。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：Close-up preschool-safe watercolor illustration from child viewpoint, red mini-train wheel rolling on a simple gray rail, plain yellow safety line in foreground, C01 small red canvas shoes clearly behind the line, no touching the wheel, clean composition, top area simple for later text, no text. Hand-painted children's picture book feeling, colored-pencil line variation, natural watercolor pigment spread; avoid cinematic lighting, 3D animation, ultra sharp edges, perfect symmetry, plastic rendering.
- 负面提示词：no dangerous contact, no child on tracks, no fingers near wheel, no realistic industrial train, no text, no extra limbs, no warped wheel, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-04-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-04-final.png`
- 单页 QA：通过。车轮和轨道关系清楚，C01 鞋尖在线内侧，无手部靠近车轮；文字放在下方浅地面空区。
- 单页状态：通过。

### 第 5 页

- 页码：5
- 本页中心意思：小葫芦先看车门里面，再决定靠近。
- 本页故事文字：门开啦，先看看里面。
- 汉字数：8
- 朗读检查：动作清楚，语气温和，不催促。
- 情绪变化：犹豫观察 → 愿意再看一眼。
- 儿童主体性：孩子看车门、座位和车窗，而不是完成乘车流程。
- 成人/同伴支持：妈妈蹲在孩子身边，开放手势指向车门内侧，不递票、不拉孩子。
- 文字与画面分工：文字说“门开”和“先看”；画面补充座位、扶手、车窗和孩子的观察。
- 页间推进：从外部部件观察推进到车内空间观察。
- 视觉新增量：打开的车门、车内座位、扶手和车窗。
- 出场角色锁定：C01、A01、T01。
- 道具状态：D01 背在 C01 背后；D03 黄线仍在人物与轨道之间；无 D02 车票。
- 空间连续性校验：T01 停在站台旁，车门面向人物，人物仍在黄线内侧。
- 镜头切换理由：近景强调“按自己的节奏观察”。
- 景别：近景
- 视角与机位：平视
- 画面构图：C01 居中偏左或偏右，A01 在稍后侧蹲下，打开的车门和座位在后方。
- 人物调度与动作真实性：A01 手掌开放，不接触孩子身体；C01 可微微后停或一手扶背包肩带。
- 画面细节与规整度：突出车门、座位、扶手、车窗；删除车票和成人乘车流程道具。
- 色彩设计：车门内为奶白和浅黄，外部蓝绿清爽。
- 光线设计：车门内柔和，站台自然光承接。
- 文字融入方案：右上车厢外侧或天空低细节区，1-2 行。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：Gentle preschool watercolor and colored-pencil illustration, C01 toddler in yellow shirt and blue overalls standing safely behind yellow platform line, looking into an open mini-train door with slight hesitation and curiosity; inside the carriage show simple seat, rounded handrail, and window; A01 mother crouches slightly behind and beside the child with open guiding hand toward the doorway, not holding ticket, not pulling or pushing; red engine and exactly two pale-yellow cars, no readable signs, no ticket, upper-right low-detail area for later text. Hand-painted children's picture book feeling, natural clothing wrinkles, varied expressions, subtle watercolor spread; avoid cinematic lighting, 3D animation style, ultra sharp edges, perfect symmetry, plastic skin, game illustration style.
- 负面提示词：no ticket, no text, no labels, no train numbers, no pseudo-Chinese, no child crossing track, no foot on yellow line, no coercion, no pulling child, no extra fingers, no identical smiles, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2；旧样张含车票，仅作反例记录。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-05-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-05-final.png`
- 单页 QA：通过。无车票、无递票动作；画面重点为打开车门、座位、扶手、车窗和孩子观察；A01 开放手势，不拉拽。
- 单页状态：通过。

### 第 6 页

- 页码：6
- 本页中心意思：小葫芦坐稳，扶着扶手看窗外。
- 本页故事文字：坐好啦，扶稳稳。
- 汉字数：6
- 朗读检查：口语化，节奏稳定。
- 情绪变化：谨慎 → 安心。
- 儿童主体性：小葫芦自己坐好，一手扶扶手，一边看窗外。
- 成人/同伴支持：妈妈坐在旁边陪伴，不指导、不指挥。
- 文字与画面分工：文字说坐好扶稳；画面补充背包放下、车窗外风景和安心表情。
- 页间推进：从看车门推进到坐在车内。
- 视觉新增量：车厢内部、扶手、车窗、背包放座位旁。
- 出场角色锁定：C01、A01、T01 内部。
- 道具状态：D01 从背上取下，放在 C01 腿边或座位旁；D03 不出现。
- 空间连续性校验：从站台侧进入车厢内，窗外可见同一站台棚或绿树。
- 镜头切换理由：车内中景让孩子读懂“坐稳”和“可以看窗外”。
- 景别：中景
- 视角与机位：车厢内平视
- 画面构图：C01 坐左侧或中间，A01 坐旁边稍后，扶手横向清楚，窗外蓝绿风景。
- 人物调度与动作真实性：C01 臀部坐实，双脚在车内，一只手真实扶住扶手；背包有重量地靠在腿边或座位旁。
- 画面细节与规整度：保留扶手、座椅、窗框和背包；避免车厢内部杂乱。
- 色彩设计：车内奶白与浅黄，窗外蓝绿清爽。
- 光线设计：窗外左上光进入车厢，温和不昏暗。
- 文字融入方案：左上车窗外天空低细节区，1 行。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：Inside a small park mini-train carriage, preschool watercolor and colored-pencil illustration, C01 toddler seated securely, one hand naturally holding a simple rounded handrail, looking out the window with calm interest; small blue backpack removed from back and placed beside child's leg or on the seat, visibly resting with weight; A01 mother seated beside child, calm companion posture, not teaching or pointing; window shows same green park and station canopy, low-detail top-left window sky area for later text, no text. Hand-painted children's picture book feeling, natural child posture, clothing wrinkles, subtle watercolor pigment spread; avoid cinematic lighting, 3D animation style, ultra sharp edges, perfect symmetry, plastic skin, overly polished characters.
- 负面提示词：no backpack on child's back in this page, no standing while train moves, no unsafe leaning, no child outside window, no missing fingers, no fused hand on rail, no text, no pseudo letters, no outfit changes.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2；旧样张仅作构图对照。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-06-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-06-final.png`
- 单页 QA：通过。C01 坐稳扶扶手，D01 已从背上取下并放在座位旁，A01 陪坐不指导。
- 单页状态：通过。

### 第 7 页

- 页码：7
- 本页中心意思：小火车沿着弯弯轨道慢慢走。
- 本页故事文字：弯弯轨道，小火车慢慢走。
- 汉字数：10
- 朗读检查：有重复节奏和移动感。
- 情绪变化：安心 → 愉快观察。
- 儿童主体性：小葫芦从车窗看外面的弯轨和小桥。
- 成人/同伴支持：妈妈坐在旁边陪看，无额外推动。
- 文字与画面分工：文字说轨道和速度；画面补充小桥、树和车窗内的孩子。
- 页间推进：从坐好推进到真正移动观察。
- 视觉新增量：外部全景展示火车、弯轨、小桥。
- 出场角色锁定：C01、A01 通过车窗可见，T01 全车。
- 道具状态：D01 在车内座位旁，可通过车窗隐约可见。
- 空间连续性校验：T01 从站台右侧出发，沿弯轨经过小桥，仍为一车头两车厢。
- 镜头切换理由：远中景让幼儿看到火车和轨道关系。
- 景别：远中景
- 视角与机位：轻微俯视
- 画面构图：弯轨从下方引向小桥，红车头在弯道中央，两棵树作为锚点。
- 人物调度与动作真实性：C01 和 A01 坐在车窗内，不探出身体。
- 画面细节与规整度：保留小桥、树、弯轨；删去动物、招牌和随机装饰。
- 色彩设计：蓝绿公园主导，红车头跳出但不刺眼。
- 光线设计：日光从左上照亮车顶和树冠。
- 文字融入方案：上方天空低细节区，1-2 行。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：Wide-medium preschool watercolor scene, the same red park mini-train with sky-blue roof and exactly two pale-yellow carriages moves slowly along a curved gray track over a small low bridge in a sunny green park, C01 and A01 visible safely seated through the carriage window, no one leaning out, small blue backpack resting inside near child, two round trees as fixed landmarks, top sky reserved for later text, no signs or letters. Hand-painted children's picture book feeling, watercolor pigment spread, colored-pencil line variation, natural imperfect tree shapes; avoid cinematic lighting, 3D animation style, ultra sharp edges, perfect symmetry, plastic skin, game illustration style.
- 负面提示词：no fast motion, no danger, no derailment, no child outside train, no text, no random animals, no clutter, no inconsistent train colors, no more than two passenger cars.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-07-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-07-final.png`
- 单页 QA：通过。小火车沿弯轨慢走，车窗内 C01/A01 坐稳，未探出窗外；一车头两车厢关系清楚。
- 单页状态：通过。

### 第 8 页

- 页码：8
- 本页中心意思：小火车走远，小葫芦还在看。
- 本页故事文字：小火车走远啦，小葫芦还在看。
- 汉字数：12
- 朗读检查：收束自然，有余韵，不说教。
- 情绪变化：满足 → 回味。
- 儿童主体性：小葫芦自己回头看远处轨道和小火车。
- 成人/同伴支持：妈妈站在稍后位置等待，跟着孩子一起看，不催走。
- 文字与画面分工：文字说“走远”和“还在看”；画面补充背包重新背上、身体回头和远处小火车。
- 页间推进：从坐车观察回到站台，结束在回味而非完成任务。
- 视觉新增量：远去的小火车、回头看的动作、余白天空。
- 出场角色锁定：C01、A01、T01。
- 道具状态：D01 重新背在 C01 背后或由 C01 自然手提；D03 黄线在人物与轨道之间。
- 空间连续性校验：人物回到站台安全侧，小火车沿右侧弯轨走远。
- 镜头切换理由：中远景保留余白，突出孩子和远去火车之间的联系。
- 景别：中远景
- 视角与机位：平视站台侧
- 画面构图：C01 在前景偏左，背包可见，身体回头看；A01 在稍后位置；T01 变小，沿远处弯轨离开。
- 人物调度与动作真实性：C01 站稳在线内侧，手可轻扶背包带或自然垂下，头和视线追向远处火车。
- 画面细节与规整度：保留黄线、小桥、两棵树和远处小火车；不加掌声、奖品、贴纸或围观人群。
- 色彩设计：蓝绿明亮，远处红车头成为小小回忆点。
- 光线设计：与开头一致的上午自然光，略更多天空留白。
- 文字融入方案：左上或上方天空低细节区，2 行以内。
- 图片比例与像素尺寸：`3:4`，`1086x1448`
- 无字插画图像提示词：Ending page in sunny park mini-train station, watercolor and colored-pencil preschool picture book style, C01 toddler safely behind plain yellow line on platform, small blue backpack back on shoulders or naturally held, body gently turned and still looking at the small red park mini-train far away on the curved track; A01 mother stands slightly behind, quietly waiting and looking in the same direction, not urging; T01 appears smaller in the distance, exactly one red engine and two pale-yellow passenger cars, distant low bridge and two round trees, large calm sky area for later text, no rewards, no applause, no text. Hand-painted children's picture book feeling, natural clothing wrinkles, subtle watercolor pigment spreading, varied expressions, no perfect symmetry.
- 负面提示词：no child on tracks, no crossing rail, no touching train wheels, no prizes, no applause crowd, no text, no pseudo-Chinese, no train numbers, no more than two passenger cars, no extra fingers, no duplicated child, no plastic skin, no identical smiles, no random clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 `image_gen` 新版 v2；第 8 页曾因远处车厢不够清楚而重生成一次。
- 无字图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-08-clean.png`
- 排版完成图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-08-final.png`
- 单页 QA：通过。C01 回头看远去小火车，A01 稍后等待；一车头两节车厢清楚，无掌声、奖品、贴纸或完成任务式庆祝。
- 单页状态：通过。

## 9. 全书质量审计

### 9.1 故事与文字 QA

- 单一核心主题：通过。聚焦孩子按自己的节奏认识公园小火车。
- 年龄适配和字数：通过。每页 6-12 个汉字，拟声词和重复动作明确。
- 儿童视角：通过。全部来自听、看、数、坐稳、看远处等幼儿可理解动作。
- 情绪接纳与选择权：通过。第 1/5/8 页分别体现停下、先看、回味。
- 是否存在催促、比较、羞辱、条件式奖励或说教：无。
- 重复结构是否每次推进：通过。停听 → 看车头 → 数车厢 → 听车轮 → 看里面 → 坐稳 → 看弯轨 → 还在看。
- 出声朗读检查：通过。短句可分行朗读，无成人价值词。
- 结尾是否允许慢慢来并避免价值评判：通过。结尾停在“还在看”，不是“完成任务”。

### 9.2 跨页连续性 QA

- 角色脸型、发型、服装、鞋袜和身高关系：通过。C01 黄色上衣、浅蓝背带裤、红鞋、小蓝背包稳定；A01 浅青绿开衫和低马尾稳定。
- 固定配角人数与身份：通过。不设置固定配角。
- 道具颜色、大小、位置和持握状态：通过。D01 状态已按 1-5 背着、6-7 放旁边、8 重新背上调整。
- 门窗、站台、道路和家具位置：通过。站台、黄线、轨道、小桥和树已锁定。
- 镜头轴线、行动方向和光源：通过。默认站台内侧看向轨道，左上自然光。
- 色板、线条、颗粒和人物比例：通过。新增 Natural Imperfection Rules 和绘本真实性要求。
- 画幅、像素尺寸和页码命名：通过。统一 `1086x1448`，3:4。

### 9.3 AI 瑕疵审计

- P0 问题及重做页码：无未解决项。旧第 5 页车票问题已通过 v2 第 5 页解决；旧第 8 页余韵不足已通过 v2 第 8 页解决。
- P1 问题及修正页码：无未解决项。第 3 页因与第 2 页构图过近已重生成；第 6 页背包状态已修正；第 8 页车厢数量已重生成确认。
- P2 已记录差异：第 4 页为低机位部件特写，车轮视觉更接近局部观察页，接受为认知重点页面。
- 整本联系表检查结果：通过。无字联系表为 `outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/storyboard-contact-sheet-v2.png`；排版完成联系表为 `outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/storyboard-contact-sheet-final-v2.png`。
- 最终可交付结论：v2 已具备完整故事包、无字图、排版完成图、家长页、PDF 和 PPTX，可进入人工终审或印刷规格扩展。

## 10. 给家长的文字

- 这个故事想让孩子感受到什么：孩子可以慢慢认识新的交通工具；先停一停、听一听、看一看，也是认识世界的方式。
- 共读提醒：不要用故事催孩子必须坐车、必须勇敢或必须马上尝试；可以把“还在看”当作孩子正在吸收和回味。
- 亲子互动：
  1. 读“停一停，听一听”时，一起安静听一秒。
  2. 读“呜呜”时，轻轻学火车声音。
  3. 读“一节，两节”时，用手指数车厢。
  4. 读最后一页时，问：“小葫芦还在看什么？”
- 可使用的支持性语言：“你想先看一看吗？”“我们慢慢来。”“你还想再看一会儿吗？”
- 不建议使用的语言：“快上去。”“别怕。”“你坐了才勇敢。”“坐完就成功了。”
- 适合幼儿年龄：2-3 岁为主，3-4 岁可延展到交通工具观察。

## 11. 交付准备

- 故事包文本路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/story/story-package.md`
- 逐页脚本路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/story/page-script.md`
- 家长指南路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/story/parent-guide.md`
- 角色圣经路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/character-bible.md`
- 环境地图路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/environment-map.md`
- 色板与风格圣经路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/color-and-style-bible.md`
- 连续性矩阵路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/continuity-matrix.md`
- 整本缩略联系表路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/storyboard-contact-sheet-v2.png`
- 无字封面图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/cover-clean.png`
- 无字内页图片路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/clean/v2/page-01-clean.png` 至 `page-08-clean.png`
- 排版完成封面路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/cover-final.png`
- 排版完成内页路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/artwork/composited/v2/page-01-final.png` 至 `page-08-final.png`
- 可编辑排版源文件路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/layout/editable-layout-v2.json`
- 故事与文字 QA 路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/qa/story-and-text-qa.md`
- 视觉连续性 QA 路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/qa/visual-consistency-qa.md`
- AI 瑕疵审计路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/qa/ai-artifact-audit.md`
- 导出文件路径：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/export/renzhi-qimeng-xiao-huoche-chufa-la-v2.pdf`；`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/export/renzhi-qimeng-xiao-huoche-chufa-la-v2.pptx`
- 固定输出目录：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/`
