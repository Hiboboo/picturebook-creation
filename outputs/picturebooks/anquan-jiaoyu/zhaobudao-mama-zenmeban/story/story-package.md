# 《找不到妈妈怎么办》故事包

## 1. 交付状态

- 当前状态：故事草案 + 视觉设定 + 角色/环境参考图 + 四张关键页无字样张已完成。
- 实际图片生成：是，已生成角色参考表、环境参考图、封面、第 4 页、第 6 页、第 10 页无字样张，并统一规范化为 `1536x2048`。
- 生成方式：人工故事设计 + AI 辅助插画提示词规划 + 图像模型生成关键样张；中文文字仍未排版，后续必须由可编辑文本层加入。
- 本次未完成项：第 1-3、5、7-9 页无字插画、全书缩略联系表、后期文字排版、PDF/PPT 导出。
- 需要用户确认项：是否接受当前角色参考、环境参考和四张关键样张方向；第 6 页批量出图时是否按 QA 建议强化为“双脚分别踩在两个小脚印上”。
- 本地记录：沿用已有草稿记录。SQLite：`records/picturebook_records.sqlite`；导出 JSON：`records/records.json`。

## 2. 基本信息

- 系列：安全教育系列。
- 书名：找不到妈妈怎么办。
- 主题：在公共场所暂时找不到妈妈时，停在安全点，找可信成人帮忙。
- 图/文：小葫芦。
- 主要适合年龄：3-4 岁。
- 可延伸年龄：3-5 岁亲子共读。
- 核心主题：找不到妈妈时，先停住，再找固定安全点和可信成人帮忙。
- 孩子的生活入口：孩子在儿童图书馆亲子阅读区看绘本，妈妈去旁边还书，孩子一回头暂时看不见妈妈。
- 目标情绪变化：从好奇看书，到有点慌，再到停住、回到安全点、开口求助，最后被妈妈接住。
- 故事页数：10 页，不含封面。
- 画面风格：清爽水彩和彩铅线条，儿童图书馆真实生活感，低饱和蓝绿与浅木色为主，少量珊瑚红和蓝色作为识别点；不使用恐吓、阴暗或泛黄滤镜。
- 视觉细节密度：适中偏简洁。
- 色彩设计策略：浅木色和清水蓝建立明亮公共空间，低饱和蓝绿表达短暂不确定，珊瑚红主角外套保持可识别，蓝马甲工作人员提供安全线索；结尾回到柔和明亮的浅木色和暖白光。
- 图片比例：固定 `3:4` 竖版。
- 锁定像素尺寸：`1536x2048`。
- 文字安全边距：至少画布宽高的 `6%`；如印刷另加出血。
- 固定输出目录：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/`

## 3. 儿童发展与情绪安全策略

- 孩子可能感受到的情绪：好奇、专注、发现妈妈不在眼前时的紧张、想跑去找的冲动、站住后的不确定、被听见后的安心。
- 故事如何接纳这种情绪：正文允许小米小手抓紧、声音变小；不说“别怕”“你要勇敢”，而是让她用一个小步骤找回把握。
- 孩子拥有的选择：停住、回到约定安全点、抱住联系卡、观察工作人员、开口求助、在原地等待、慢慢抱一抱。
- 成人如何提供支持：妈妈提前约定“小熊脚印”；图书馆工作人员蹲低、保持距离、先问“你想在这里等妈妈吗？”再帮忙联系；妈妈回来后接住情绪，不责备。
- 故事中的最小可行尝试：小米站回小熊脚印，说出“请帮我找妈妈”。
- 结尾如何避免“必须克服”：结尾是妈妈回来后一起重新确认安全点，不要求孩子表现得不害怕，也不把求助写成“真勇敢”的奖励。
- 奖励、掌声或贴纸的处理：不出现奖励、掌声、贴纸或价值评判。
- 禁用表达：“别哭”“你怎么乱跑”“你要勇敢”“妈妈不要你了”“陌生人都很危险”“再不听话就找不到妈妈”“你看别人都不会走丢”。

## 4. 故事设定卡

- 背景：上午的儿童图书馆亲子阅读区，左侧是圆形阅读地毯和低矮书架，中间有小熊脚印地贴，右后方是服务台，右侧远处是入口但不作为行动目标。
- 儿童视角：故事来自孩子能理解的公共空间经验：看书、转身找妈妈、看见地贴、看见穿蓝马甲和工作牌的工作人员、在原地等妈妈。
- 故事弧线：生活入口 -> 妈妈短暂离开视线 -> 孩子发现不见妈妈 -> 身体紧张信号 -> 回到安全点 -> 看到可信成人 -> 开口求助 -> 工作人员陪同等待 -> 妈妈回来 -> 温暖收束。
- 重复结构：“停一停”作为安全动作钩子；第 1 页由妈妈约定，第 6 页由小米执行，第 10 页由亲子一起确认。
- 页间推进：约定安全点 -> 看书 -> 找不到妈妈 -> 紧张 -> 看见脚印 -> 站回脚印 -> 看见工作人员 -> 说出求助 -> 等到妈妈 -> 复盘安全动作。
- 温暖结尾：妈妈蹲下接住小米的情绪，说“你站在这里等我，我找到你了”，让孩子感到求助有效、自己没有做错。
- 故事禁改项：不把妈妈短暂离开写成遗弃；不写危险陌生人接近；不让孩子追出门、跑向马路或乘电梯；不让成人责备孩子。

## 5. 视觉圣经与连续性锁定

### 5.1 角色圣经

- 角色 ID：C01-小米
- 名称与身份：小米，3-4 岁幼儿。
- 年龄感 / 物种：人类幼儿。
- 身高与头身比例：约 3.5 头身，小体型，圆润幼儿比例。
- 脸型与核心五官：圆脸，黑色眼睛，短鼻小嘴，表情细微。
- 发型与发色：黑色短发，柔软齐刘海，耳侧少量碎发。
- 上衣：珊瑚红轻薄连帽开衫，里面奶油白圆领衫。
- 下装：浅米色背带裤，裤脚微卷。
- 鞋袜：白色短袜，海军蓝软底鞋。
- 固定配色：珊瑚红、奶油白、浅米、海军蓝。
- 标志性配件或道具：D02-小蓝联系卡，挂在黄色圆扣短绳上，卡面不出现可读文字。
- 常见表情范围：好奇、专注、犹豫、紧张一点、认真求助、放松、安心；不默认全程微笑。
- 禁改项：短黑发、珊瑚红开衫、浅米背带裤、海军蓝鞋、小蓝联系卡。
- 可变项：站姿、抱卡动作、看向脚印/服务台/妈妈的方向、表情强度。
- 角色参考图路径或状态：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/character-reference-sheet.png`

- 角色 ID：A01-妈妈
- 名称与身份：小米的妈妈，温和照顾者。
- 年龄感 / 物种：成人女性，人类。
- 身高与头身比例：成人比例，明显高于小米；同框支持时蹲低。
- 脸型与核心五官：柔和脸型，深棕眼睛，表情自然。
- 发型与发色：深棕色低马尾。
- 上衣：浅鼠尾草绿针织开衫，内搭白色上衣。
- 下装：浅卡其长裤。
- 鞋袜：米色平底鞋。
- 固定配色：鼠尾草绿、白色、浅卡其。
- 标志性配件或道具：D03-浅棕布包，装待还绘本。
- 常见表情范围：平静、说明、寻找、松一口气、接纳、安心。
- 禁改项：低马尾、鼠尾草绿开衫、浅棕布包、蹲低回应。
- 可变项：走向还书台、从书架后回来、蹲下拥抱距离。
- 角色参考图路径或状态：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/character-reference-sheet.png`

- 角色 ID：A02-蓝马甲阿姨
- 名称与身份：儿童图书馆工作人员，可信成人。
- 年龄感 / 物种：成人女性，人类。
- 身高与头身比例：成人比例；靠近孩子时蹲低或坐低。
- 脸型与核心五官：温和脸型，清楚但不夸张的微笑。
- 发型与发色：黑色中长发，低丸子头。
- 上衣：清水蓝工作马甲，内搭白色长袖。
- 下装：深灰长裤。
- 鞋袜：白色软底工作鞋。
- 固定配色：清水蓝、白色、深灰。
- 标志性配件或道具：D04-空白工作牌、服务台电话；图像中工作牌不可有可读文字。
- 常见表情范围：观察、温和询问、认真倾听、陪伴等待。
- 禁改项：蓝色工作马甲、空白工作牌、蹲低距离、不过度触碰孩子。
- 可变项：站在服务台后、蹲在小熊脚印旁、拿起电话。
- 角色参考图路径或状态：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/character-reference-sheet.png`

### 5.2 演员表

- 固定角色总表：C01-小米全书常驻；A01-妈妈第 1-2、9-10 页出现，第 3-8 页通过布包、还书台方向或等待目标存在；A02-蓝马甲阿姨第 7-9 页出现。
- 配角人数与身份锁定：背景可有 1-2 组模糊亲子读者，但不得围观小米或成为情节角色；不新增陌生人搭话。
- 身高关系：妈妈和工作人员约为小米 2.2 倍身高；靠近小米时必须蹲低或隔着服务台保持温和距离。
- 不得互换或替代的角色：A02 不得换成路人、保安威吓形象或陌生成人；A01 不得换成其他照顾者。

### 5.3 环境与空间连续性地图

- 时间与天气：上午，晴天，自然光透过图书馆高窗。
- 核心场景：儿童图书馆亲子阅读区。
- 起点：左下圆形浅蓝阅读地毯，小米和妈妈一起看绘本。
- 目标点：中景的小熊脚印地贴，是约定等待点；右后方服务台是可信求助点。
- 行动路线和路径轴线：小米从阅读地毯走到低书架前，发现妈妈不在眼前后不向右侧入口移动，而是回到中间小熊脚印，再面向右后方服务台求助。
- 固定地标：圆形阅读地毯、低矮绘本架、红色还书车、小熊脚印地贴、蓝色服务台、入口玻璃门、窗边绿植。
- 角色进入/离开方向：妈妈从地毯右上方走向还书车；小米从书架前回到脚印；工作人员从服务台方向来到脚印旁；妈妈从还书车/书架方向回来。
- 镜头主侧与越轴线：保持阅读地毯在左、小熊脚印在中、服务台在右后方、入口在最右；不随意翻转入口和服务台位置。
- 主光源方向：左上高窗柔和自然光；服务台有冷白台灯；结尾整体明度提高。
- 允许变化项：背景读者轻微移动、还书车上绘本数量、妈妈布包位置。
- 禁改项：入口不得变成行动目标；不能出现马路、电梯、楼梯、安检口或拥挤商场压迫感；服务台不得有可读文字。
- 环境参考图或平面图路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/environment-reference.png`

### 5.4 道具状态表

- 道具 ID 与名称：D01-小熊脚印地贴
- 归属角色：图书馆固定安全点。
- 颜色、尺寸和图案：浅蓝地贴，上面两个圆润小熊脚印，无文字。
- 初始位置：第 1 页妈妈指给小米看，位于阅读地毯和服务台之间。
- 每页状态变化：第 1 页被约定；第 4-6 页成为小米回去站住的位置；第 8-10 页作为等待和重逢锚点。
- 持握手或摆放方向：固定在地面，小熊脚尖朝服务台。
- 禁改项：不得消失、变色、变成箭头或出口标识。

- 道具 ID 与名称：D02-小蓝联系卡
- 归属角色：C01-小米。
- 颜色、尺寸和图案：浅蓝小卡，黄色圆扣短绳，卡面只有无字色块，不生成可读个人信息。
- 初始位置：挂在小米开衫内侧或手中。
- 每页状态变化：第 1-2 页挂在身前；第 5 页小米轻轻抓住；第 9 页拿给工作人员看。
- 持握手或摆放方向：多由小米左手握住。
- 禁改项：不得出现真实电话号码、姓名或伪文字；不得变成玩具卡片。

- 道具 ID 与名称：D03-妈妈布包
- 归属角色：A01-妈妈。
- 颜色、尺寸和图案：浅棕帆布包，装 2-3 本绘本，无文字图案。
- 初始位置：第 1 页妈妈肩上。
- 每页状态变化：第 2 页随妈妈去还书；第 9 页妈妈回来时仍背着。
- 持握手或摆放方向：妈妈右肩或左手拎着，方向保持自然。
- 禁改项：不得变成购物袋、背包或遗失物。

- 道具 ID 与名称：D04-工作人员空白工作牌
- 归属角色：A02-蓝马甲阿姨。
- 颜色、尺寸和图案：白色小牌，蓝色边框，无可读文字。
- 初始位置：第 7 页出现在工作人员胸前。
- 每页状态变化：第 7-9 页保持在胸前，帮助小米识别可信成人。
- 持握手或摆放方向：挂绳垂直，不能遮挡脸或手。
- 禁改项：不得出现可读文字、警徽、夸张权威标志。

### 5.5 风格、色板与版式锁定

- 媒介与线条：透明水彩底色，彩铅细线，边缘轻微手绘抖动。
- 颗粒与纹理：轻纸感颗粒，控制在低强度；不使用塑料皮肤、高光堆叠或 3D 渲染质感。
- 人物比例和面部风格：幼儿圆润自然，成人温和真实，表情有层次。
- 主色：浅木色、清水蓝、低饱和蓝绿。
- 辅助色：奶油白、浅鼠尾草绿、浅卡其。
- 强调色：珊瑚红开衫、蓝色马甲、浅蓝脚印。
- 禁用色彩倾向：阴森低照度、过度黄色滤镜、随机彩虹色、商业卡通高饱和、恐吓式深色阴影。
- 文字字体层级：书名大字号；正文中字号；署名小字号，固定 `图/文：小葫芦`。
- 文字区规则：使用书架上方墙面、窗光下低细节墙面、服务台侧面或地毯外侧低细节区域；不得用固定卡片或不透明大背板。
- 无字插画规则：图像模型不得生成中文书名、正文、服务台文字、工作牌文字、标识牌文字或伪文字。

## 6. 全书镜头与翻页计划

| 页码 | 叙事节点 | 情绪起点→终点 | 景别 | 视角/机位 | 出场角色 ID | 核心动作 | 空间锚点 | 文字区 | 相比上一页的视觉新增量 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 约定安全点 | 平静→有准备 | 远中景 | 幼儿视角平视 | C01, A01 | 妈妈指给小米看小熊脚印 | 地毯、脚印、服务台 | 左上墙面 | 建立安全点和空间关系 |
| 2 | 看绘本 | 有准备→专注 | 中景 | 平视 | C01, A01 | 小米看见喜欢的小红书 | 低书架、还书车 | 右上 | 妈妈去还书的方向 |
| 3 | 妈妈不在眼前 | 专注→疑惑 | 近景 | 平视 | C01 | 小米回头找妈妈 | 书架、红书 | 左上 | 情绪近景 |
| 4 | 身体紧张 | 疑惑→有点慌 | 特写 | 手部/脚部近景 | C01 局部 | 小手抓住小蓝卡 | 联系卡、地面 | 右上 | 紧张身体信号 |
| 5 | 看见安全点 | 有点慌→想起来 | 中景 | 孩子主观视角 | C01 局部 | 小米看见小熊脚印 | 脚印、地毯边 | 左上 | 安全点重新出现 |
| 6 | 站回脚印 | 想起来→站稳 | 远中景 | 平视 | C01 | 小米站到小熊脚印上 | 脚印、入口远景 | 右上 | 安全动作完成，不跑向门 |
| 7 | 识别工作人员 | 站稳→敢开口 | 中景 | 平视 | C01, A02 | 工作人员蹲低询问 | 服务台、工作牌 | 左上 | 可信成人出现 |
| 8 | 一起等待 | 敢开口→被陪伴 | 中近景 | 平视 | C01, A02 | 工作人员陪小米在脚印旁等 | 脚印、服务台电话 | 右上 | 等待支架 |
| 9 | 妈妈回来 | 被陪伴→放松 | 远中景 | 平视 | C01, A01, A02 | 妈妈从还书方向回来 | 脚印、还书车 | 左上 | 重逢但不责备 |
| 10 | 温暖收束 | 放松→安心 | 近景 | 幼儿高度平视 | C01, A01 | 小米主动靠一靠 | 脚印、书架 | 右上 | 亲子复盘安全动作 |

## 7. 封面图片

- 封面状态：已生成无字 v2 样张，并已作为全书视觉基准继续出图。
- 无字封面图片文件路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/cover-clean.png`
- 排版完成封面图片路径：未生成。
- 图片比例与像素尺寸：固定 `3:4`，`1536x2048`。
- 封面中心意思：小米站在儿童图书馆的小熊脚印上，一只手握着小蓝联系卡，远处可见蓝色服务台和妈妈回来的方向，整体气质明亮、安全、不惊吓。
- 封面构图说明：小米居中偏下站在浅蓝小熊脚印上，珊瑚红开衫提供第一视觉识别；右后方蓝色服务台和蓝马甲工作人员形成可信求助线索，左侧低书架和浅木色地板保留图书馆生活感；上方留出书名区。
- 角色锁定：C01-小米，珊瑚红开衫、浅米背带裤、海军蓝鞋、小蓝联系卡；A02 可在服务台后方以温和小比例出现；A01 可在远处书架边形成回来的方向线索。
- 书名排版：上方低细节墙面，最多 2 行，大字号，清楚普通，不用花哨特效。
- 署名排版：固定 `图/文：小葫芦`；深灰或黑色，小字号。
- 标题安全区：距离边缘至少 6%，不得遮挡小米脸部、联系卡、脚印或服务台方向。
- 无字封面图像提示词：3:4 vertical watercolor preschool picturebook cover, no text, bright children's library reading area in the morning, child-eye-level view, C01 Xiaomi, a 3-4-year-old child with black short hair, coral red hoodie cardigan, cream shirt, light beige overalls, white socks, navy soft shoes, stands calmly on two pale blue bear-paw floor decals, one small hand holding a pale blue contact card with a yellow round button, no readable words on the card, blue service desk in the background, A02 librarian in a clear blue vest and blank badge standing softly behind the service desk, low picturebook shelves and round rug, safe public place feeling, calm but attentive expression, natural low-detail title area on upper wall, transparent watercolor and colored pencil, soft paper grain, clean composition.
- 封面负面提示词：no text, no pseudo-Chinese, no readable signs, no scary mood, no abandonment, no dangerous stranger, no kidnapping, no running into street, no escalator, no traffic, no coercion, no shaming, no crying panic, no extra fingers, no missing fingers, no malformed hands, no duplicated child, no inconsistent outfit, no plastic skin, no random decorative clutter.
- 使用的角色/环境参考图、模型、版本、种子或引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/cover-raw.png`。
- 封面 QA 结果：通过。无可读文字，主角、脚印、服务台和妈妈回来的方向清楚；画面明亮，不含恐吓或遗弃感。

## 8. 内页图片与文字

### 第 1 页

- 页码：1
- 本页中心意思：妈妈和小米先约定安全点。
- 本页故事文字：妈妈说：“小熊脚印在这里。”
- 汉字数：10
- 朗读检查：顺口；具体、生活化。
- 情绪变化：平静 → 有准备。
- 儿童主体性：小米可以看见并记住一个具体位置。
- 成人/同伴支持：妈妈蹲低指向脚印，提前说明，不吓唬。
- 文字与画面分工：文字说约定；画面补充图书馆空间和脚印位置。
- 页间推进：建立安全点，下一页进入看书活动。
- 视觉新增量：阅读区、服务台、小熊脚印同时建立。
- 出场角色锁定：C01 小米；A01 妈妈；服装按角色圣经。
- 道具状态：D01 初次出现；D02 挂在小米身前；D03 在妈妈肩上。
- 空间连续性校验：地毯左侧，脚印中间，服务台右后方。
- 镜头切换理由：建立场景。
- 景别：远中景。
- 视角与机位：幼儿视角平视。
- 画面构图：妈妈蹲低，手指向脚印；小米看向脚印，服务台在远处但清楚可识别。
- 人物调度与动作真实性：妈妈保持可接受距离，不拉扯；小米站稳。
- 画面细节与规整度：保留脚印、地毯、低书架、服务台；删减无关读者。
- 色彩设计：浅木色、清水蓝、珊瑚红建立明亮安全感。
- 光线设计：左上窗光柔和。
- 文字融入方案：左上低细节墙面，1-2 行，安全边距 6%。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor preschool picturebook page, no text, bright children's library reading area, child-eye-level view, A01 mother with low ponytail and sage green cardigan kneels beside C01 Xiaomi and gently points to pale blue bear-paw floor decals, Xiaomi wears coral red cardigan, cream shirt, light beige overalls, navy shoes, pale blue contact card on a yellow button cord, round reading rug on the left, low picturebook shelves, blue service desk in the right background, calm preparation mood, natural low-detail text area upper left, transparent watercolor, colored pencil linework.
- 负面提示词：no text, no pseudo-Chinese, no readable signs, no scary warning, no coercion, no shaming, no adult pulling child, no extra fingers, no malformed hands, no duplicated people, no outfit changes, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/cover-clean.png`、`artwork/clean/page-10-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/fullbook-v2/page-01-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-01-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 初检通过。妈妈蹲低指向脚印，服务台和小熊脚印清楚；无文字、无强迫动作、无安全违规。
- 单页状态：无字内页已按 v2 视觉基准生成。

### 第 2 页

- 页码：2
- 本页中心意思：小米专注看书，妈妈去旁边还书。
- 本页故事文字：小米看见一本红书。
- 汉字数：8
- 朗读检查：顺口；符合幼儿生活经验。
- 情绪变化：有准备 → 专注。
- 儿童主体性：小米自己选择一本书看。
- 成人/同伴支持：妈妈在画面边缘向还书车走，保持同一空间。
- 文字与画面分工：文字说小米的兴趣；画面补充妈妈移动方向。
- 页间推进：妈妈暂时离开视线的原因出现，下一页小米回头找。
- 视觉新增量：低书架和红书成为视觉焦点。
- 出场角色锁定：C01；A01 侧背影或局部。
- 道具状态：D02 挂在小米身前；D03 随妈妈移动；D01 在背景中可见。
- 空间连续性校验：小米从地毯旁来到低书架，妈妈向右后方还书车走。
- 镜头切换理由：中景聚焦小米看书。
- 景别：中景。
- 视角与机位：平视。
- 画面构图：红书在低书架上，小米伸手取书；妈妈在背景去还书，脚印仍在中景。
- 人物调度与动作真实性：小米一手扶书架，一手拿红书；妈妈没有离开建筑空间。
- 画面细节与规整度：书架书脊不出现可读文字，只用色块。
- 色彩设计：红书与小米开衫呼应，蓝绿环境保持平静。
- 光线设计：自然光稳定。
- 文字融入方案：右上低细节墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, same children's library, child-eye-level, C01 Xiaomi reaches for a simple red picturebook on a low shelf, no readable book titles, A01 mother in sage green cardigan walks gently toward a red return cart in the background with a canvas bag, pale blue bear-paw floor decals still visible between rug and service desk, calm everyday movement, low-detail text area upper right, soft watercolor and colored pencil.
- 负面提示词：no text, no pseudo-Chinese, no readable book titles, no abandonment, no crowded panic, no adult pulling, no extra fingers, no missing fingers, no malformed hands, no duplicated child, no outfit changes.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/page-01-clean.png`、`artwork/clean/page-04-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/fullbook-v2/page-02-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-02-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 初检通过。小米取红书、妈妈在还书方向，脚印和服务台仍为背景锚点；无文字和遗弃恐吓感。
- 单页状态：无字内页已按 v2 视觉基准生成。

### 第 3 页

- 页码：3
- 本页中心意思：小米回头时看不见妈妈。
- 本页故事文字：一回头，妈妈不在眼前。
- 汉字数：10
- 朗读检查：顺口；不夸大成“妈妈不见了”。
- 情绪变化：专注 → 疑惑。
- 儿童主体性：小米主动回头寻找。
- 成人/同伴支持：无额外推动；妈妈只是暂时在书架/还书车方向被遮挡。
- 文字与画面分工：文字说看不见；画面补充妈妈可能在遮挡后方，避免遗弃感。
- 页间推进：引出紧张情绪和安全动作。
- 视觉新增量：小米表情近景。
- 出场角色锁定：C01。
- 道具状态：D02 在胸前；红书在小米手中；D01 背景中隐约可见。
- 空间连续性校验：小米仍在低书架前，服务台方向不变。
- 镜头切换理由：近景呈现轻微疑惑。
- 景别：近景。
- 视角与机位：平视。
- 画面构图：小米抱着红书回头，眼睛看向妈妈刚才的方向；背景书架遮挡一部分还书车。
- 人物调度与动作真实性：小米脚站稳，没有奔跑。
- 画面细节与规整度：背景简洁，避免拥挤人群。
- 色彩设计：环境蓝绿略降饱和，珊瑚红仍清楚。
- 光线设计：自然光不变，不制造阴暗恐惧。
- 文字融入方案：左上低细节墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, close child-height view, C01 Xiaomi holds a simple red picturebook and turns her head toward where mother walked, expression curious and slightly unsure, pale blue contact card visible, low picturebook shelf behind her, soft library light, background partially blocks the return cart so mother is not visible in frame, no scary atmosphere, small low-detail text area upper left.
- 负面提示词：no text, no pseudo-Chinese, no panic crying, no dark scary shadows, no dangerous stranger, no running, no extra fingers, no malformed hands, no duplicated people, no outfit changes.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/page-02-clean.png`、`artwork/clean/page-04-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/fullbook-v2/page-03-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-03-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 初检通过。小米抱红书回头，疑惑但不恐慌；服务台、脚印和书架空间关系清楚，无文字。
- 单页状态：无字内页已按 v2 视觉基准生成。

### 第 4 页

- 页码：4
- 本页中心意思：小米有点慌，抓住联系卡。
- 本页故事文字：小手抓紧小蓝卡。
- 汉字数：7
- 朗读检查：顺口；身体信号具体，不贴负面标签。
- 情绪变化：疑惑 → 有点慌。
- 儿童主体性：小米抓住自己的联系卡，这是可用的小支架。
- 成人/同伴支持：无额外推动。
- 文字与画面分工：文字说动作；画面补充脚停住、没有乱跑。
- 页间推进：从情绪信号转向想起安全动作。
- 视觉新增量：手部和联系卡特写。
- 出场角色锁定：C01 局部。
- 道具状态：D02 被左手握住，卡面不出现文字。
- 空间连续性校验：地面仍是图书馆浅木地板，远处可隐约看见脚印颜色。
- 镜头切换理由：特写让“紧张”和“可用支架”可见。
- 景别：特写。
- 视角与机位：手部近景。
- 画面构图：小手握住小蓝卡，红书靠在身体旁，海军蓝鞋停在原地。
- 人物调度与动作真实性：手指数量正常，握卡真实，不勒脖子。
- 画面细节与规整度：联系卡无文字，背景只保留地板和一点脚印色块。
- 色彩设计：浅蓝卡与脚印呼应，降低慌乱感。
- 光线设计：清楚柔和，无强阴影。
- 文字融入方案：右上地面低细节区域，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor close-up page, no text, privacy-safe child detail, C01 Xiaomi's small hand gently grips a pale blue contact card on a yellow round button cord, no readable words on the card, coral red cardigan sleeve, red picturebook edge, navy shoes planted on pale wood library floor, faint pale blue bear-paw decal visible in the distance, gentle tension but no panic, low-detail text area upper right.
- 负面提示词：no text, no pseudo-Chinese, no readable personal information, no choking cord, no panic, no extra fingers, no missing fingers, no fused hand, no malformed wrist, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/cover-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/page-04-raw.png`，出版级视觉精修 v2 原始图保存在 `artwork/raw/ai-denoise-v2/page-04-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-04-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：通过。联系卡无可读文字，手部动作清楚，脚印在远处作为空间锚点；未见安全违规。
- 单页状态：无字关键样张已完成出版级视觉精修 v2，并作为全书视觉基准。

### 第 5 页

- 页码：5
- 本页中心意思：小米想起并看见小熊脚印。
- 本页故事文字：小熊脚印在那边。
- 汉字数：8
- 朗读检查：顺口；具体位置帮助幼儿理解。
- 情绪变化：有点慌 → 想起来。
- 儿童主体性：小米自己看向安全点。
- 成人/同伴支持：无额外推动。
- 文字与画面分工：文字指向安全点；画面补充小米视角看见脚印。
- 页间推进：为第 6 页站回脚印做准备。
- 视觉新增量：孩子主观视角。
- 出场角色锁定：C01 局部。
- 道具状态：D01 重新成为视觉焦点；D02 仍在手中。
- 空间连续性校验：脚印在地毯和服务台之间，入口在更右侧远处。
- 镜头切换理由：主观视角帮助幼儿跟随“看见安全点”。
- 景别：中景。
- 视角与机位：孩子主观视角。
- 画面构图：前景有小米手和红书边，画面中间是小熊脚印，服务台在右后方。
- 人物调度与动作真实性：小米还未跑动，只是转向脚印。
- 画面细节与规整度：入口弱化，脚印明确。
- 色彩设计：脚印浅蓝提升可见度。
- 光线设计：窗光照亮脚印。
- 文字融入方案：左上书架上方低细节墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, subjective child-height view from near a low shelf, pale blue bear-paw floor decals clearly visible between the round rug and the blue service desk, C01 Xiaomi's coral sleeve and red book edge in foreground, pale wood floor, entrance glass door far right but visually secondary, safe point is the clear focus, calm library light, low-detail text area upper left.
- 负面提示词：no text, no pseudo-Chinese, no arrows, no exit sign, no scary empty hall, no running, no crowd, no warped perspective, no random decorations.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/page-04-clean.png`、`artwork/clean/page-06-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/fullbook-v2/page-05-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-05-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 初检通过。小米看见脚印和服务台，仍未完成站上脚印动作；无文字、无跑动、无入口诱导。
- 单页状态：无字内页已按 v2 视觉基准生成。

### 第 6 页

- 页码：6
- 本页中心意思：小米站回小熊脚印，没有往门口跑。
- 本页故事文字：小米站回脚印上。
- 汉字数：8
- 朗读检查：顺口；安全动作明确，不说教。
- 情绪变化：想起来 → 站稳。
- 儿童主体性：小米主动完成“回到安全点”的小动作。
- 成人/同伴支持：无额外推动。
- 文字与画面分工：文字说站回；画面补充入口在远处但不是行动方向。
- 页间推进：从独自处理进入可求助状态。
- 视觉新增量：完整身体站在脚印上。
- 出场角色锁定：C01。
- 道具状态：D01 被小米双脚踩在上方；D02 左手握住；红书抱在右臂。
- 空间连续性校验：小米在中间脚印位置，服务台右后方，入口远右。
- 镜头切换理由：远中景清楚展示安全动作和空间边界。
- 景别：远中景。
- 视角与机位：平视。
- 画面构图：小米站在脚印中央，身体朝服务台方向，入口玻璃门只在背景边缘。
- 人物调度与动作真实性：双脚踩地，肩膀略紧但身体稳定。
- 画面细节与规整度：背景读者模糊，不围观。
- 色彩设计：浅蓝脚印和蓝色服务台形成安全路线。
- 光线设计：清爽明亮，情绪开始稳定。
- 文字融入方案：右上低细节墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, C01 Xiaomi stands with both feet on pale blue bear-paw floor decals, holding the pale blue contact card and red picturebook, body facing the blue service desk, coral red cardigan and beige overalls consistent, entrance glass door far right and secondary, no running, no panic, child appears a little tense but steady, round rug and low shelves maintain spatial continuity, natural low-detail text area upper right.
- 负面提示词：no text, no pseudo-Chinese, no running out the door, no traffic, no escalator, no scary stranger, no crying panic, no extra limbs, no malformed feet, no duplicated child, no outfit changes, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/cover-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/page-06-raw.png`，出版级视觉精修 v2 原始图保存在 `artwork/raw/ai-denoise-v2/page-06-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-06-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 通过。孩子没有跑向入口，身体和眼神朝服务台方向；左右脚分别踩在两个小熊脚印上，人物完整、无文字；旧版“脚踩一个大脚印垫”的 P2 已解决。
- 单页状态：无字关键样张已完成出版级视觉精修 v2，并作为全书视觉基准。

### 第 7 页

- 页码：7
- 本页中心意思：小米识别到蓝马甲工作人员。
- 本页故事文字：蓝马甲阿姨走过来。
- 汉字数：9
- 朗读检查：顺口；以可见服装识别可信成人。
- 情绪变化：站稳 → 敢开口。
- 儿童主体性：小米看向工作人员，可选择开口求助。
- 成人/同伴支持：工作人员蹲低，先问“你想在这里等妈妈吗？”。
- 文字与画面分工：文字说谁来了；画面补充工作牌、服务台和温和距离。
- 页间推进：可信成人支架出现，为求助句做铺垫。
- 视觉新增量：工作人员从服务台方向出现。
- 出场角色锁定：C01；A02 蓝马甲阿姨。
- 道具状态：D04 工作牌出现但无文字；D01 在两人脚下附近；D02 在小米手里。
- 空间连续性校验：工作人员从服务台方向来，不从入口或陌生角落来。
- 镜头切换理由：中景展示双方距离和识别线索。
- 景别：中景。
- 视角与机位：平视。
- 画面构图：工作人员蹲在小米侧前方，保持一臂距离；小米站在脚印上，服务台在背景。
- 人物调度与动作真实性：工作人员不牵手、不拉拽；手掌开放。
- 画面细节与规整度：工作牌无字，表情温和。
- 色彩设计：清水蓝马甲与服务台呼应。
- 光线设计：均匀自然光。
- 文字融入方案：左上书架上方低细节区域，1-2 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, same library safe point, A02 librarian in a clear blue vest, white shirt, dark gray pants, blank badge with no words, comes from the blue service desk direction and kneels at child height near C01 Xiaomi, keeping a respectful distance with open hands, Xiaomi remains on pale blue bear-paw decals holding contact card, calm attentive expressions, no touching or pulling, service desk visible behind, low-detail text area upper left.
- 负面提示词：no text, no pseudo-Chinese, no readable badge, no police intimidation, no dangerous stranger, no adult grabbing child, no coercion, no shaming, no extra fingers, no malformed hands, no duplicated people, no outfit changes.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/page-06-clean.png`、`artwork/clean/page-10-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/fullbook-v2/page-07-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-07-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 初检通过。工作人员从服务台方向蹲低靠近，手掌开放，未牵拉或带离脚印；工作牌无可读文字。
- 单页状态：无字内页已按 v2 视觉基准生成。

### 第 8 页

- 页码：8
- 本页中心意思：工作人员陪小米在安全点等待。
- 本页故事文字：她说：“我陪你等。”
- 汉字数：7
- 朗读检查：顺口；支持语言具体、低压力。
- 情绪变化：敢开口 → 被陪伴。
- 儿童主体性：小米可以选择站在脚印上等。
- 成人/同伴支持：工作人员蹲低陪同，不带小米离开安全点。
- 文字与画面分工：文字说陪伴；画面补充服务台电话和原地等待。
- 页间推进：从识别可信成人到被稳定支持。
- 视觉新增量：电话/服务台作为联系妈妈的工具出现。
- 出场角色锁定：C01；A02。
- 道具状态：D01 在小米脚下；D02 在小米手里；D04 在工作人员胸前；服务台电话在背景。
- 空间连续性校验：两人仍在脚印附近，服务台就在右后方。
- 镜头切换理由：中近景突出安全陪伴。
- 景别：中近景。
- 视角与机位：平视。
- 画面构图：小米站在脚印上，工作人员半蹲在旁边，身体朝向服务台电话。
- 人物调度与动作真实性：工作人员一手指向服务台电话，一手自然放低；不拉小米。
- 画面细节与规整度：背景简化，电话无数字可读。
- 色彩设计：蓝绿稳定，珊瑚红弱化紧张。
- 光线设计：服务台台灯轻微增强安全感，但不刺眼。
- 文字融入方案：右上服务台侧面低细节区域，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, C01 Xiaomi stands on bear-paw decals while A02 librarian in blue vest kneels beside her and calmly indicates the nearby blue service desk phone, staying with Xiaomi at the safe point, no walking away, blank badge and phone with no readable numbers, respectful distance, quiet library background, soft blue-green palette, low-detail text area upper right.
- 负面提示词：no text, no pseudo-Chinese, no readable phone numbers, no adult leading child away, no grabbing, no panic, no reward sticker, no crowd watching, no extra fingers, no malformed hands, no duplicated people.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/page-06-clean.png`、`artwork/clean/page-07-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/fullbook-v2/page-08-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-08-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 初检通过。工作人员在脚印旁陪等，服务台电话可见；无牵拉、无带离、无可读文字。
- 单页状态：无字内页已按 v2 视觉基准生成。

### 第 9 页

- 页码：9
- 本页中心意思：小米开口求助后，妈妈回来了。
- 本页故事文字：小米说：“请帮我找妈妈。”
- 汉字数：10
- 朗读检查：顺口；求助句清楚可模仿。
- 情绪变化：被陪伴 → 放松。
- 儿童主体性：小米主动说出求助需求。
- 成人/同伴支持：工作人员听见并联系妈妈；妈妈从还书方向回来。
- 文字与画面分工：文字呈现求助句；画面补充妈妈回来的方向和工作人员陪同。
- 页间推进：安全动作产生真实回应。
- 视觉新增量：妈妈重新进入画面。
- 出场角色锁定：C01；A01；A02。
- 道具状态：D01 仍在脚下；D02 小米拿出给工作人员看；D03 妈妈肩上；D04 工作牌无字。
- 空间连续性校验：妈妈从还书车/书架方向回到脚印，不从入口外突然出现。
- 镜头切换理由：远中景恢复完整空间和关系。
- 景别：远中景。
- 视角与机位：平视。
- 画面构图：小米和工作人员在脚印旁，妈妈从左后方还书车方向走来，三者形成稳定三角关系。
- 人物调度与动作真实性：妈妈手臂打开但不扑抱；工作人员略退一步让亲子连接。
- 画面细节与规整度：背景读者不围观。
- 色彩设计：浅木色和暖白光回升，蓝色安全线索保留。
- 光线设计：整体明度提高。
- 文字融入方案：左上窗光墙面低细节区域，1-2 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, bright library reading area, C01 Xiaomi stands on bear-paw decals and holds out a pale blue contact card toward A02 librarian, A01 mother in sage green cardigan and canvas book bag returns from the red return cart and low shelf direction, warm relief but no dramatic panic, respectful librarian steps slightly aside, clear triangle between child, librarian, and mother, soft natural light, no readable signs, low-detail text area upper left.
- 负面提示词：no text, no pseudo-Chinese, no readable personal information, no blame, no scolding, no forced hug, no crowd watching, no running, no extra fingers, no malformed hands, no duplicated people, no outfit changes.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/page-08-clean.png`、`artwork/clean/page-10-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/fullbook-v2/page-09-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-09-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：v2 初检通过。小米主动出示小蓝卡，工作人员蹲低倾听，妈妈从还书方向回来；没有提前进入夸张拥抱或救援姿态。
- 单页状态：无字内页已按 v2 视觉基准生成。

### 第 10 页

- 页码：10
- 本页中心意思：妈妈接住小米的情绪，一起确认“停一停”。
- 本页故事文字：妈妈来了，抱一抱。
- 汉字数：7
- 朗读检查：顺口；温暖收束，不说教。
- 情绪变化：放松 → 安心。
- 儿童主体性：小米主动靠近妈妈；亲密动作由孩子发起。
- 成人/同伴支持：妈妈蹲低接住小米，轻声确认“你站在这里等我，我找到你了”。
- 文字与画面分工：文字说重逢；画面补充妈妈蹲低、脚印仍在、工作人员在背景温和离开。
- 页间推进：温暖收束。
- 视觉新增量：近景亲子关系和安全点闭环。
- 出场角色锁定：C01；A01；A02 背景小比例。
- 道具状态：D01 在两人脚边；D02 放松垂在小米身前；D03 在妈妈身侧；D04 背景。
- 空间连续性校验：仍在脚印旁，没有离开安全点。
- 镜头切换理由：近景收束情绪，保留脚印锚点。
- 景别：近景。
- 视角与机位：幼儿高度平视。
- 画面构图：妈妈蹲低，小米轻轻靠过去，脚印在下方可见，蓝马甲工作人员在服务台方向微笑点头。
- 人物调度与动作真实性：妈妈不强拉，小米主动靠一靠；手和身体接触自然。
- 画面细节与规整度：保留脚印、书架、联系卡；删减多余背景。
- 色彩设计：浅木色、奶油白和珊瑚红柔和融合。
- 光线设计：窗光柔和包住亲子，保持真实公共空间光线。
- 文字融入方案：右上书架上方低细节区域，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor ending page, no text, child-height close view near the pale blue bear-paw decals, A01 mother kneels low and receives C01 Xiaomi as Xiaomi gently leans in by choice, calm relieved expressions, no forced hug, Xiaomi's pale blue contact card relaxes at her chest, bear-paw decals visible near their feet, A02 librarian in blue vest softly in the background near service desk, low shelves and warm natural library light, gentle safe ending, low-detail text area upper right.
- 负面提示词：no text, no pseudo-Chinese, no scolding, no forced hug, no exaggerated praise, no reward sticker, no crying panic, no extra fingers, no missing fingers, no malformed hands, no duplicated people, no outfit changes, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：参考 `bible/character-reference-sheet.png`、`bible/environment-reference.png`、`artwork/clean/cover-clean.png`；内置 imagegen；无固定种子记录；原始图保存在 `artwork/raw/page-10-raw.png`，出版级视觉精修 v2 原始图保存在 `artwork/raw/ai-denoise-v2/page-10-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/page-10-clean.png`
- 排版完成图片路径：未生成。
- 单页 QA：通过。妈妈蹲低，小米主动靠近，脚印仍在，工作人员在背景退后；无责备、强迫拥抱或奖励暗示。
- 单页状态：无字关键样张已完成出版级视觉精修 v2，并作为全书视觉基准。

## 9. 全书质量审计

### 9.1 故事与文字 QA

- 单一核心主题：通过，始终围绕“找不到妈妈时先停住并求助”。
- 年龄适配和字数：通过，每页正文约 7-10 个汉字，适合 3-4 岁朗读。
- 儿童视角：通过，线索来自图书馆、脚印地贴、联系卡、蓝马甲工作人员等可见经验。
- 情绪接纳与选择权：通过，小米可以紧张、停住、抓卡、站回脚印、开口求助。
- 是否存在催促、比较、羞辱、条件式奖励或说教：无。
- 重复结构是否每次推进：通过，“小熊脚印/停一停”从约定到执行再到收束。
- 出声朗读检查：通过；句子短，停顿自然。
- 结尾是否允许慢慢来并避免价值评判：通过，不表扬“勇敢”，不责备“走丢”。

### 9.2 跨页连续性 QA

- 角色脸型、发型、服装、鞋袜和身高关系：关键样张初检通过；剩余页待生成后复检。
- 固定配角人数与身份：通过，只有妈妈和蓝马甲工作人员；背景读者不参与情节。
- 道具颜色、大小、位置和持握状态：文本锁定通过，小熊脚印和小蓝联系卡是连续锚点。
- 门窗、舞台、地毯、道路和家具位置：通过，阅读地毯、脚印、服务台、入口位置已锁定。
- 镜头轴线、行动方向和光源：通过，阅读地毯左、脚印中、服务台右后、入口右侧。
- 色板、线条、颗粒和人物比例：文本锁定通过。
- 画幅、像素尺寸和页码命名：通过，统一 `3:4` 和 `1536x2048`，计划使用 `page-01` 到 `page-10`。

### 9.3 AI 瑕疵审计

- 多指、少指、粘连手、反向手掌、多肢、缺肢：全书无字图初检未见 P0 级问题。
- 眼睛、耳朵、牙齿、头发和衣领异常：全书无字图初检未见 P0 级问题；后续排版前仍需逐页大图复检。
- 人物漂浮、脚不着地、重心不稳、物体未被真实握住：关键动作可读，第 6 页安全脚印动作已通过 v2 修正。
- 重复人物、无故换装、角色变脸、道具复制或消失：初检通过，服装、联系卡、红书、小熊脚印、服务台方向保持连续。
- 透视、遮挡、阴影、门窗和家具结构异常：初检未见必须重做项；图书馆空间骨架保持一致。
- 乱码、伪中文、假字母和模型生成文字：全书无字图初检未见可读文字；工作牌、联系卡、书脊和服务台区域后续仍需排版前复检。
- 同款微笑、塑料皮肤、过量纹理、随机装饰和模板化构图：v2 已按出版级降 AI 感规则处理，增加生活化随机细节与前后景层次。
- P0 问题及重做页码：暂无。
- P1 问题及修正页码：暂无必须修正项。
- P2 已记录差异：无。
- 整本联系表检查结果：关键样张联系表已生成：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/storyboard-contact-sheet-key-samples.png`；全书内页联系表已生成：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/storyboard-contact-sheet.png`。
- 最终可交付结论：封面和第 1-10 页无字 clean artwork 已按 v2 视觉基准补齐；可进入文字排版前检查。排版完成图、PDF 和 PPT 尚未生成。

## 10. 给家长的文字

- 这个故事想让孩子感受到什么：在外面暂时看不见妈妈时，害怕和紧张都可以出现；孩子可以先停住，回到约定位置，找穿工作服、在服务台的可信成人帮忙。
- 共读提醒：不要用故事吓孩子“走丢很可怕”，也不要要求孩子证明自己勇敢。重点是反复练习一个可执行的小动作。
- 亲子互动：
  - 和孩子一起在画面中找“小熊脚印”“蓝马甲”“服务台”。
  - 读到第 6 页时，一起做“停一停，脚站稳”的动作。
  - 读到第 9 页时，练一句求助话：“请帮我找妈妈/爸爸。”
  - 出门前可约定一个真实安全点，例如服务台、收银台或入口内侧固定标志。
- 可使用的支持性语言：
  - “如果你一回头看不见我，先停在我们说好的地方。”
  - “你可以找穿工作服、在服务台的人帮忙。”
  - “你说‘请帮我找妈妈’，我会来找你。”
- 不建议使用的语言：
  - “你再乱跑妈妈就不要你了。”
  - “外面的人都很可怕。”
  - “你看你，怎么连妈妈都看不住。”
- 适合幼儿年龄：3-4 岁，3-5 岁可由主要照顾者亲子共读。

## 11. 交付准备

- 故事包文本路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/story/story-package.md`
- 逐页脚本路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/story/page-script.md`
- 家长指南路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/story/parent-guide.md`
- 角色圣经路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/character-bible.md`
- 环境地图路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/environment-map.md`
- 色板与风格圣经路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/color-and-style-bible.md`
- 连续性矩阵路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/continuity-matrix.md`
- 整本缩略联系表路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/storyboard-contact-sheet.png`；关键样张联系表为 `outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/bible/storyboard-contact-sheet-key-samples.png`
- 无字封面图片路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/artwork/clean/cover-clean.png`
- 无字内页图片路径：已生成 `artwork/clean/page-01-clean.png` 至 `artwork/clean/page-10-clean.png`。
- 排版完成封面路径：未生成。
- 排版完成内页路径：未生成。
- 可编辑排版源文件路径：未生成。
- 故事与文字 QA 路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/qa/story-and-text-qa.md`
- 视觉连续性 QA 路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/qa/visual-consistency-qa.md`
- AI 瑕疵审计路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/qa/ai-artifact-audit.md`
- 导出文件路径：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/export/`
- 固定输出目录：`outputs/picturebooks/anquan-jiaoyu/zhaobudao-mama-zenmeban/`
