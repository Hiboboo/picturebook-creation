# 《第一次上幼儿园》故事包

## 1. 交付状态

- 当前状态：全书出图 + 排版完成 + 质检完成 + PDF/PPTX 导出完成。
- 实际图片生成：是，已生成角色参考图、环境参考图、无字封面、10 页无字内页、排版完成图、整本联系表、PDF 和 PPTX。
- 生成方式：人工文本设计 + AI 辅助插画生成 + 本地后期文字排版；中文正文与书名均由后期文本层添加。
- 本次未完成项：无。
- 需要用户确认项：最终 PDF/PPTX 是否进入后续印刷或发布版本微调。
- 本地记录：未发现重复，已登记草稿。SQLite：`records/picturebook_records.sqlite`；导出 JSON：`records/records.json`。

## 2. 基本信息

- 系列：入园适应与社交系列。
- 书名：第一次上幼儿园。
- 主题：第一次上幼儿园。
- 图/文：小葫芦。
- 主要适合年龄：3-4 岁。
- 可延伸年龄：3-5 岁亲子共读。
- 核心主题：第一次进入幼儿园时，孩子可以慢慢看、慢慢靠近，并完成一个适合自己的小动作。
- 孩子的生活入口：早晨背着小书包来到幼儿园门口，面对新门、新老师、新教室和新同伴。
- 目标情绪变化：从紧张停住，到感到有人陪，再到愿意坐在边边观察，最后做出一次小小回应。
- 故事页数：10 页，不含封面。
- 画面风格：水彩铺色 + 彩铅线条，轻纸感颗粒，幼儿比例自然圆润；清晨蓝、草叶绿与珊瑚色构成明亮但不过度甜腻的入园氛围。
- 视觉细节密度：适中偏简洁。
- 色彩设计策略：清晨蓝表现新环境，草叶绿表现安全与稳定，珊瑚色表现小小互动，奶白和木色只做环境中性色，避免整本偏黄。
- 图片比例：固定 `3:4` 竖版。
- 锁定像素尺寸：`1536x2048`。
- 文字安全边距：至少画布宽高的 `6%`；印刷项目另列出血。
- 固定输出目录：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/`

## 3. 儿童发展与情绪安全策略

- 孩子可能感受到的情绪：紧张、好奇、舍不得妈妈、想看但暂时不想进去、被同伴邀请时的小犹豫、完成回应后的轻松。
- 故事如何接纳这种情绪：故事不说“别怕”“要勇敢”，而是允许小柚牵手、停住、先看一看、坐边边、只做一个小动作。
- 孩子拥有的选择：牵手、抱安抚物、观察、坐在边缘、分步骤、换一种表达、明天再来。
- 成人如何提供支持：妈妈蹲到小柚视线高度等待；林老师在门口蹲下邀请；成人不拉、不推、不替孩子回答。
- 故事中的最小可行尝试：小柚不必马上加入集体活动，只需把软球轻轻滚回给同伴。
- 结尾如何避免“必须克服”：结尾停在“明天，我还要来幼儿园”，不写成“以后再也不害怕”。
- 奖励、掌声或贴纸的处理：不出现奖励、掌声、贴纸或“表现好”的评价。
- 禁用表达：“别哭”“你要勇敢”“大家都在等你”“别人都进去了”“真乖”“不进去就不是好孩子”“妈妈不要你了”。

## 4. 故事设定卡

- 背景：清晨，幼儿园入口、教室门口、储物格、圆地毯活动区和靠窗安静角。
- 儿童视角：故事来自孩子能看见和感受到的具体经验：新幼儿园、手想牵住妈妈、老师蹲下来、自己的小格子、坐在边边看、软球滚过来。
- 故事弧线：生活入口 -> 愿望/好奇 -> 犹豫信号 -> 安全支架 -> 一个小动作 -> 真实回应 -> 温暖收束。
- 重复结构：“看一看”和“咕噜”作为动作钩子：第 4 页老师邀请进来看，第 6 页小柚坐边边看一看，第 7-8 页软球来回滚动，第 10 页小柚愿意明天再来。
- 页间推进：从家门口到幼儿园门口，再到教室入口、个人小格子、边缘观察、同伴低压力互动，最后由妈妈接回。
- 温暖结尾：小柚没有被要求“完全适应”，而是知道自己可以被接住，也可以明天继续试。
- 故事禁改项：不强迫分离；不让成人拉扯孩子；不把入园成功定义为不哭、不想妈妈或立刻交朋友。

## 5. 视觉圣经与连续性锁定

### 5.1 角色圣经

- 角色 ID：C01-小柚
- 名称与身份：小柚，第一次上幼儿园的孩子。
- 年龄感 / 物种：3-4 岁人类幼儿。
- 身高与头身比例：约 3.7 头身；明显低于成人，略矮于教室门把手高度。
- 脸型与核心五官：圆脸，黑亮大眼，清晰双眼皮，较长但自然的上睫毛，短鼻小嘴，表情细微。
- 发型与发色：黑色短波波头，左侧小珊瑚色发夹。
- 上衣：蓝绿色针织开衫，内搭白色上衣。
- 下装：柔和珊瑚色长裤。
- 鞋袜：白色袜子与浅色软底鞋。
- 固定配色：蓝绿色、白色、珊瑚色、深青色书包。
- 标志性配件或道具：D01-天蓝色小云朵手帕；D02-深青色小书包，参考图含小云朵挂件。
- 常见表情范围：平静、好奇、犹豫、专注、放松；不默认全程微笑。
- 禁改项：短波波头、珊瑚色发夹、蓝绿色开衫、珊瑚色裤子、天蓝小云朵手帕。
- 可变项：牵手、抱手帕、站住、坐边边、滚球、回头看妈妈。
- 角色参考图路径或状态：优先使用 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-reference-sheet-v2-eyes.png`；原始版为 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-reference-sheet.png`

- 角色 ID：A01-妈妈
- 名称与身份：妈妈，主要照顾者。
- 年龄感 / 物种：成人女性，人类。
- 身高与头身比例：成人比例；与小柚互动时蹲下或半跪。
- 脸型与核心五官：柔和脸型，深色眼睛，表情安静。
- 发型与发色：深色低马尾。
- 上衣：浅石灰色针织外套，白色内搭。
- 下装：藏蓝色长裤。
- 鞋袜：浅色平底鞋。
- 固定配色：浅石灰、藏蓝、白色。
- 标志性配件或道具：无固定手持物。
- 常见表情范围：倾听、等待、温和、放松。
- 禁改项：低马尾、浅石灰外套、蹲低支持、不拉扯。
- 可变项：牵手、蹲下、在门口等待、接孩子。
- 角色参考图路径或状态：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-reference-sheet.png`

- 角色 ID：T01-林老师
- 名称与身份：幼儿园老师。
- 年龄感 / 物种：成人女性，人类。
- 身高与头身比例：成人比例；与孩子说话时蹲下或弯腰。
- 脸型与核心五官：自然脸型，眼神温和。
- 发型与发色：黑色短发，耳后收整。
- 上衣：白色上衣外搭鼠尾草绿色围裙。
- 下装：深蓝长裤。
- 鞋袜：浅色软底鞋。
- 固定配色：鼠尾草绿、白色、深蓝。
- 标志性配件或道具：可轻扶教室门框，不主动触碰小柚身体。
- 常见表情范围：等待、邀请、观察、轻微微笑。
- 禁改项：不替孩子回答、不催促入场、不把孩子推到集体中央。
- 可变项：蹲在门口、坐在地毯边、递出低压力邀请。
- 角色参考图路径或状态：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-reference-sheet.png`

- 角色 ID：C02-安安
- 名称与身份：同班孩子，低压力互动同伴。
- 年龄感 / 物种：3-4 岁人类幼儿。
- 身高与头身比例：与小柚接近，略高一点点。
- 脸型与核心五官：圆脸短发，表情自然。
- 发型与发色：黑色短发。
- 上衣：海蓝条纹上衣。
- 下装：赭黄色短裤。
- 鞋袜：白袜、蓝色软鞋。
- 固定配色：海蓝、赭黄、珊瑚色软球。
- 标志性配件或道具：D03-珊瑚色软布球。
- 常见表情范围：好奇、等待、专注、开心一点。
- 禁改项：不围观、不评价小柚、不抢球。
- 可变项：坐在地毯边、把软球滚过去、接住软球。
- 角色参考图路径或状态：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-reference-sheet.png`

### 5.2 演员表

- 固定角色总表：C01-小柚全书常驻；A01-妈妈第 1-4、9-10 页出现；T01-林老师第 4-8 页出现；C02-安安第 7-8 页出现。
- 配角人数与身份锁定：可出现 2-3 个模糊背景幼儿剪影，但不得形成围观压力；正式出场同伴仅 C02-安安。
- 身高关系：A01 与 T01 明显高于幼儿；成人支持时降低身体高度。C02 与 C01 身高相近。
- 不得互换或替代的角色：不得把妈妈替换成老师；不得把林老师替换成陌生成人；不得临时新增“评判型同伴”。

### 5.3 环境与空间连续性地图

- 时间与天气：晴朗清晨，自然日光。
- 核心场景：幼儿园入口、教室门口、储物格、圆地毯活动区、靠窗安静角。
- 起点：家门口/幼儿园外侧步道。
- 目标点：教室圆地毯边缘与靠窗安静角。
- 行动路线和路径轴线：从画面左侧步道到蓝绿色园门，再进入教室门；教室内部保持窗户在左、储物格在后、圆地毯在中、安静椅在边缘。
- 固定地标：蓝绿色圆洞园门、圆窗教室门、低矮储物格、圆形蓝地毯、珊瑚色软球篮、左侧窗户、靠窗安静椅。
- 角色进入/离开方向：小柚从左向右进入园门，再由门口进入教室；结尾从教室门口回到妈妈身边。
- 镜头主侧与越轴线：不随意反转入口与教室空间；反打时保留圆窗门或圆地毯作为锚点。
- 主光源方向：左侧窗光和入口树影；教室内为柔和自然光。
- 允许变化项：角色位置、站/坐/蹲姿、局部特写、安静角与活动区视角切换。
- 禁改项：不得画成阴暗封闭空间、拥挤公共机构、纪律化排队场景或成人控制场景。
- 环境参考图或平面图路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/environment-reference-sheet.png`

### 5.4 道具状态表

- 道具 ID 与名称：D01-小云朵手帕
- 归属角色：C01-小柚。
- 颜色、尺寸和图案：天蓝色小手帕，白色云朵图案，约小柚前臂长度。
- 初始位置：第 1 页握在手中。
- 每页状态变化：第 1-4 页手中；第 5 页放入或贴近自己的小格子；第 6-8 页握在膝边或手里；第 9-10 页带回身边。
- 持握手或摆放方向：多由左手握住，犹豫时贴近胸口。
- 禁改项：不得变成玩具奖励或老师发放物；不得无故消失。

- 道具 ID 与名称：D02-小书包
- 归属角色：C01-小柚。
- 颜色、尺寸和图案：深青色儿童小书包，参考图含小云朵挂件。
- 初始位置：第 1-4 页背在身上。
- 每页状态变化：第 5 页放进储物格；第 9 页可由妈妈帮忙拿起；第 10 页背回家或抱在妈妈手中。
- 持握手或摆放方向：背带在双肩；放入格子时正面朝外。
- 禁改项：不得变色、变大或换成其他背包。

- 道具 ID 与名称：D03-珊瑚色软布球
- 归属角色：C02-安安/教室活动区。
- 颜色、尺寸和图案：柔和珊瑚色布球，幼儿双手可抱。
- 初始位置：第 7 页在软球篮或安安手边。
- 每页状态变化：第 7 页滚向小柚；第 8 页小柚滚回安安。
- 持握手或摆放方向：沿地毯滚动，不抛掷。
- 禁改项：不得变成硬球、危险玩具或竞赛道具。

- 道具 ID 与名称：D04-小格子
- 归属角色：C01-小柚在教室的储物格。
- 颜色、尺寸和图案：低矮木色格子，空白简单形状标记，不含文字。
- 初始位置：第 4 页门内可见，第 5 页成为本页中心。
- 每页状态变化：第 5 页放入书包；后续作为背景锚点。
- 持握手或摆放方向：固定在教室门内右后方。
- 禁改项：不得出现可读姓名、拼音、数字或标签文字。

### 5.5 风格、色板与版式锁定

- 媒介与线条：水彩底色，彩铅细线，边缘保留轻微手绘变化。
- 颗粒与纹理：轻纸感颗粒；避免塑料皮肤和过度发光。
- 人物比例和面部风格：幼儿自然圆润，成人亲近但不过度卡通。
- 主色：清晨蓝、草叶绿。
- 辅助色：奶白、深青、浅木色。
- 强调色：柔和珊瑚色，用于发夹、裤子和软球。
- 禁用色彩倾向：随机彩虹色、过度高饱和、整页黄褐木色、阴森低照度。
- 文字字体层级：书名大字号；正文中字号；署名小字号。
- 文字区规则：门边墙面、窗边浅色墙、地毯外低细节地面或上方空气区；不得使用固定卡片或不透明大背板。
- 无字插画规则：图像模型不得生成中文书名、正文、标签、班级牌、姓名牌或可读墙面文字。

## 6. 全书镜头与翻页计划

| 页码 | 叙事节点 | 情绪起点->终点 | 景别 | 视角/机位 | 出场角色 ID | 核心动作 | 空间锚点 | 文字区 | 相比上一页的视觉新增量 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 早晨准备出发 | 平静->有点期待 | 中景 | 家门口平视 | C01, A01 | 小柚背上书包，握手帕 | 家门、书包、手帕 | 上方墙面 | 建立主角和安抚物 |
| 2 | 到幼儿园门口 | 期待->紧张停住 | 远中景 | 幼儿视角平视 | C01, A01 | 小柚在蓝绿园门前停住 | 圆洞园门、树影 | 天空/墙面 | 新环境变大 |
| 3 | 妈妈蹲下来 | 紧张->有人陪 | 近景 | 低平视 | C01, A01 | 妈妈蹲下，小柚握手帕 | 园门边、妈妈膝盖 | 左上墙面 | 成人降低高度支持 |
| 4 | 老师在门口邀请 | 犹豫->可以先看 | 中景 | 教室门口平视 | C01, A01, T01 | 老师蹲在圆窗门边等待 | 圆窗门、储物格 | 门侧墙面 | 新成人出现但不施压 |
| 5 | 找到自己的小格子 | 有陪伴->有一个位置 | 中近景 | 轻微俯视 | C01, T01 | 小柚把书包放进格子 | 低矮储物格 | 右上墙面 | 个人空间被建立 |
| 6 | 坐在边边观察 | 紧绷->可停一停 | 远中景 | 从地毯边看窗 | C01, T01 | 小柚坐在圆地毯边缘 | 左窗、圆地毯、安静椅 | 窗边空区 | 允许不立刻加入 |
| 7 | 软球滚过来 | 观察->被轻轻邀请 | 特写/低角 | 地毯低机位 | C01, C02 | 软球滚到小柚脚边 | 圆地毯、软球篮 | 上方地毯外 | 同伴低压力出现 |
| 8 | 小柚滚回去 | 犹豫->做一个小动作 | 中近景 | 幼儿低平视 | C01, C02, T01 | 小柚把球轻轻滚回 | 圆地毯、窗光 | 左上墙面 | 第一次互动完成 |
| 9 | 妈妈来接 | 放松->被接住 | 中景 | 教室门口反打 | C01, A01, T01 | 小柚看见妈妈 | 圆窗门、储物格 | 门上方空区 | 时间闭合，照顾者回来 |
| 10 | 明天我还要来 | 安心->有把握 | 远中景 | 从园门外回看 | C01, A01 | 小柚牵妈妈离开，回头看门 | 蓝绿园门、树影 | 天空/墙面 | 温暖收束，不强制克服 |

## 7. 封面图片

- 封面状态：无字封面和排版完成封面已生成，初检通过。
- 无字封面图片文件路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/cover-clean.png`
- 排版完成封面图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/cover-final.png`
- 图片比例与像素尺寸：固定 `3:4`，`1536x2048`。
- 封面中心意思：小柚第一次站在幼儿园蓝绿色园门前，手里握着小云朵手帕，妈妈蹲在身边等待，门里有温和的新空间。
- 封面构图说明：画面下半部为小柚与妈妈，右后方是蓝绿色圆洞园门，门内隐约可见明亮教室入口；上方保留自然标题区。
- 角色锁定：C01 蓝绿色开衫、珊瑚色裤子、珊瑚色发夹、深青书包、天蓝手帕；A01 低马尾、浅石灰外套、藏蓝裤。
- 书名排版：后期可编辑文本层，大字号，建议两行“第一次 / 上幼儿园”，普通清楚字体。
- 署名排版：固定 `图/文：小葫芦`；普通字体、深灰、小字号。
- 标题安全区：距离边缘至少 6%，不遮挡小柚脸、妈妈手势、手帕和园门。
- 无字封面图像提示词：见 `story/page-script.md` 的“封面提示词”。
- 封面负面提示词：全书安全负面提示词 + 无文字、无拉扯、无哭闹羞辱、无奖励标识。
- 使用的角色/环境参考图、模型、版本、种子或引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/cover-raw.png`，规范化无字图 `artwork/clean/cover-clean.png`。
- 封面 QA 结果：通过。无字图无可读文字、无拉扯、无围观；排版图书名和署名清楚，未遮挡小柚、妈妈、手帕和园门。

## 8. 内页图片与文字

### 第 1 页

- 页码：1
- 本页中心意思：早晨，小柚准备出发。
- 本页故事文字：轻轻背上可爱的小书包。
- 汉字数：10。
- 朗读检查：顺口；动作具体；无成人腔。
- 情绪变化：平静 -> 有点期待。
- 儿童主体性：小柚握着自己的小云朵手帕出门。
- 成人/同伴支持：妈妈在旁边整理书包，不催促。
- 文字与画面分工：文字说出发动作；画面补充手帕和书包。
- 页间推进：建立小柚和安抚物，为到园门口做铺垫。
- 视觉新增量：主角、妈妈和固定服装首次出现。
- 出场角色锁定：C01、A01；服装按角色圣经。
- 道具状态：D01 左手握住；D02 背在身上。
- 空间连续性校验：家门口作为出发点，下一页转到幼儿园门口。
- 镜头切换理由：中景建立人物关系。
- 景别：中景。
- 视角与机位：平视。
- 画面构图：小柚居中偏左，妈妈蹲在右侧，门口留出向外的行动方向。
- 人物调度与动作真实性：书包背带贴肩，妈妈手只扶书包肩带，不拉孩子身体。
- 画面细节与规整度：保留书包、手帕、鞋；删减无关玩具。
- 色彩设计：清晨蓝与奶白为主，珊瑚色作角色强调。
- 光线设计：门外柔和日光。
- 文字融入方案：左上墙面，1 行，安全边距 6%。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor preschool picturebook page, no text, morning at home doorway, C01 Xiao You wearing blue-green cardigan, white shirt, soft coral pants, white socks, muted-coral hair clip, teal backpack, holding sky-blue cloud handkerchief, A01 Mom kneels beside child gently adjusting backpack strap without pulling, calm departure mood, low-detail wall area upper left for later Chinese text.
- 负面提示词：全书安全负面提示词；no readable text, no pseudo-Chinese, no adult pulling child.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-01-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-01-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-01-final.png`
- 单页 QA：安全通过；无可读文字；妈妈只扶书包肩带，未拉扯小柚；小柚服装、发夹、书包和手帕符合角色锁定；文字区未遮挡脸、手和书包。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 2 页

- 页码：2
- 本页中心意思：幼儿园门口很新、很大，小柚停住。
- 本页故事文字：好漂亮的幼儿园。
- 汉字数：7。
- 朗读检查：顺口；符合幼儿身体感受。
- 情绪变化：有点期待 -> 紧张停住。
- 儿童主体性：小柚可以停在门口，不被立刻推进去。
- 成人/同伴支持：妈妈站在旁边，保持可牵手距离。
- 文字与画面分工：文字说幼儿园漂亮；画面补充脚步停住和手帕被握紧。
- 页间推进：从出发到达新环境。
- 视觉新增量：蓝绿色圆洞园门和树影。
- 出场角色锁定：C01、A01。
- 道具状态：D01 握紧；D02 背在身上。
- 空间连续性校验：进入幼儿园路线开始，园门为后续封面和结尾锚点。
- 镜头切换理由：远中景让“门大、人小”的感受成立。
- 景别：远中景。
- 视角与机位：幼儿视角平视。
- 画面构图：园门占画面后方，小柚站在前景偏左，妈妈半步后方。
- 人物调度与动作真实性：小柚双脚停住，身体微微靠向妈妈。
- 画面细节与规整度：保留园门、树影、步道；不加人群。
- 色彩设计：清晨蓝门和草叶绿树影。
- 光线设计：树叶投影，不阴森。
- 文字融入方案：上方浅墙或天空区，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, kindergarten entrance with low rounded blue-green gate and morning tree shadows, C01 Xiao You pauses before the gate holding sky-blue cloud handkerchief, teal backpack on shoulders, A01 Mom nearby at a respectful distance, child looks small but safe, natural title-free low-detail area above gate.
- 负面提示词：全书安全负面提示词；no crowd, no school sign text, no forced movement.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-02-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-02-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-02-final.png`
- 单页 QA：安全通过；无可读文字；蓝绿色园门、树影和教室入口清楚；妈妈蹲下等待，没有推拉；小柚停在门口的犹豫感明确。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 3 页

- 页码：3
- 本页中心意思：妈妈蹲下来陪小柚慢一点。
- 本页故事文字：妈妈蹲下来。
- 汉字数：5。
- 朗读检查：顺口；没有命令和评价。
- 情绪变化：紧张 -> 有人陪。
- 儿童主体性：小柚可以继续停住并握住手帕。
- 成人/同伴支持：妈妈蹲到视线高度，等待，不说催促话。
- 文字与画面分工：文字说妈妈的支持动作；画面补充小柚手帕和眼神。
- 页间推进：为下一页老师的邀请建立安全支架。
- 视觉新增量：成人降低高度的近景关系。
- 出场角色锁定：C01、A01。
- 道具状态：D01 贴近胸前；D02 背在身上。
- 空间连续性校验：仍在园门边，背景保留蓝绿门。
- 镜头切换理由：近景聚焦情绪安全。
- 景别：近景。
- 视角与机位：低平视。
- 画面构图：妈妈蹲在小柚侧前方，小柚在画面中央，园门边缘作为背景锚点。
- 人物调度与动作真实性：妈妈双手自然放在膝盖或开放手势，不抓孩子。
- 画面细节与规整度：不出现围观孩子或老师催促。
- 色彩设计：石灰灰与蓝绿降低紧张。
- 光线设计：柔和侧光。
- 文字融入方案：左上墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor close page, no text, beside blue-green kindergarten gate, A01 Mom kneels at C01 Xiao You's eye level with calm open posture, Xiao You holds the sky-blue cloud handkerchief close, teal backpack visible, child hesitant but safe, no pulling, low-detail wall area upper left.
- 负面提示词：全书安全负面提示词；no shaming, no forced hug, no adult grabbing.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-03-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-03-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-03-final.png`
- 单页 QA：安全通过；无可读文字；妈妈蹲在视线高度，手势开放；小柚抱着手帕，情绪可见；未出现围观和强迫。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 4 页

- 页码：4
- 本页中心意思：老师允许小柚先看一看。
- 本页故事文字：老师说，进来看一看吧。
- 汉字数：9。
- 朗读检查：顺口；支持语言具体、低压力。
- 情绪变化：有人陪 -> 可以先看。
- 儿童主体性：小柚可以牵着妈妈，不必马上进去。
- 成人/同伴支持：林老师蹲在门口，邀请而不催促。
- 文字与画面分工：文字给出选择；画面显示老师蹲下和教室门内空间。
- 页间推进：从园门进入教室入口。
- 视觉新增量：圆窗教室门、储物格、林老师。
- 出场角色锁定：C01、A01、T01。
- 道具状态：D01 手中；D02 背在身上；D04 门内可见。
- 空间连续性校验：从入口转入教室门，保留圆窗门和储物格。
- 镜头切换理由：中景呈现三人距离和不施压关系。
- 景别：中景。
- 视角与机位：门口平视。
- 画面构图：小柚在门外边缘，老师蹲在门内侧，妈妈在小柚身后半步。
- 人物调度与动作真实性：老师手心朝上或轻扶门框，不触碰小柚。
- 画面细节与规整度：保留门、格子、鞋凳；不加班级牌文字。
- 色彩设计：鼠尾草绿和清晨蓝协调。
- 光线设计：教室内窗光比门外更柔和。
- 文字融入方案：门侧浅墙，1-2 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, classroom doorway with round window and child-height cubbies behind, T01 Teacher Lin crouches at child eye level in sage green apron, C01 Xiao You stands by A01 Mom holding cloud handkerchief and looking in, teacher waits warmly, no pressure, no readable classroom signs.
- 负面提示词：全书安全负面提示词；no text labels, no adult reaching to pull child, no crowd.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-04-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-04-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-04-final.png`
- 单页 QA：安全通过；无可读文字；老师蹲下开放手势，未触碰小柚；妈妈在旁陪伴；门槛和圆窗门空间锚点清楚。P2：教室木色略多，但不影响叙事。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 5 页

- 页码：5
- 本页中心意思：小柚找到自己的小格子。
- 本页故事文字：小格子，等我哟。
- 汉字数：6。
- 朗读检查：顺口；给新空间一个具体安全点。
- 情绪变化：可以先看 -> 有一个位置。
- 儿童主体性：小柚把书包放到自己的格子。
- 成人/同伴支持：林老师在旁边等，不替小柚完成。
- 文字与画面分工：文字说格子在等；画面补充书包被放进去。
- 页间推进：从门口进入教室内部。
- 视觉新增量：个人小格子成为安全锚点。
- 出场角色锁定：C01、T01；A01 可在门口局部出现。
- 道具状态：D02 放进 D04；D01 仍在手中或格子边。
- 空间连续性校验：储物格位置与第 4 页一致。
- 镜头切换理由：中近景聚焦“自己的位置”。
- 景别：中近景。
- 视角与机位：轻微俯视，符合幼儿看格子的高度。
- 画面构图：小柚侧身放书包，老师在一旁留出空间。
- 人物调度与动作真实性：书包底部接触格子，双手动作自然。
- 画面细节与规整度：格子只用形状标记，不出现文字姓名。
- 色彩设计：浅木只作中性背景，蓝绿和珊瑚维持视觉识别。
- 光线设计：窗光从左侧照入。
- 文字融入方案：右上墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, child-height cubbies inside classroom, C01 Xiao You gently places teal backpack into one cubby with blank simple shape tag, sky-blue cloud handkerchief still nearby, T01 Teacher Lin waits at respectful distance, warm but not yellow-dominant morning classroom, no readable name labels.
- 负面提示词：全书安全负面提示词；no text, no names, no numbers, no adult taking over.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-05-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-05-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-05-final.png`
- 单页 QA：安全通过；无可读姓名或数字；小柚自己放书包，老师在旁等待；书包、手帕和储物格状态清楚。P2：墙面挂饰为非文字装饰，可接受。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 6 页

- 页码：6
- 本页中心意思：小柚先坐在边边观察。
- 本页故事文字：我坐边边看一看。
- 汉字数：7。
- 朗读检查：顺口；孩子主动表达位置选择。
- 情绪变化：有一个位置 -> 可停一停。
- 儿童主体性：小柚选择坐在地毯边缘。
- 成人/同伴支持：林老师在近处陪伴，不把小柚推到中间。
- 文字与画面分工：文字说位置选择；画面补充活动区和安静角关系。
- 页间推进：从整理物品转入集体活动，但允许边缘观察。
- 视觉新增量：圆地毯、窗、安静椅。
- 出场角色锁定：C01、T01；背景幼儿可模糊处理。
- 道具状态：D01 握在膝边；D02 已在格子内。
- 空间连续性校验：教室窗在左，地毯在中，安静椅在边缘。
- 镜头切换理由：远中景让“边边”位置清楚。
- 景别：远中景。
- 视角与机位：从地毯边平视。
- 画面构图：小柚坐在圆地毯外缘，老师在旁边不挡视线，活动区留出呼吸空间。
- 人物调度与动作真实性：小柚双脚落地或盘坐稳定，手帕在手里。
- 画面细节与规整度：背景幼儿不围观；玩具数量克制。
- 色彩设计：蓝地毯和绿椅稳定，珊瑚色只作小点缀。
- 光线设计：左窗柔光。
- 文字融入方案：窗边浅墙，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, inside classroom near left window, round blue rug in center, C01 Xiao You sits at the quiet edge of the rug holding sky-blue cloud handkerchief, T01 Teacher Lin nearby but not crowding, a quiet chair by the window, low shelves behind, calm observation moment.
- 负面提示词：全书安全负面提示词；no crowd staring, no teacher pushing child to center, no text posters.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-06-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-06-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-06-final.png`
- 单页 QA：安全通过；无可读文字；小柚坐在地毯边缘观察，老师在远处等待，未出现推动或围观。服装、手帕和书包状态基本符合连续性；文字区未遮挡人物。P2：室内木色略多，已记录。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 7 页

- 页码：7
- 本页中心意思：同伴用低压力方式邀请小柚。
- 本页故事文字：圆圆球，咕噜咕噜跑过来。
- 汉字数：10。
- 朗读检查：顺口；拟声词适合朗读。
- 情绪变化：观察 -> 被轻轻邀请。
- 儿童主体性：小柚可以先看球，不必马上回应。
- 成人/同伴支持：安安只把球滚过来，不催小柚；老师在背景等待。
- 文字与画面分工：文字说球滚来；画面补充安安与小柚之间的距离。
- 页间推进：从观察到第一次同伴互动的入口。
- 视觉新增量：软球和同伴进入故事。
- 出场角色锁定：C01、C02；T01 可在背景。
- 道具状态：D03 从安安方向滚到小柚脚边；D01 在小柚手中。
- 空间连续性校验：仍在圆地毯边，软球篮在背景。
- 镜头切换理由：低角特写强调低压力动作。
- 景别：特写/低角。
- 视角与机位：地毯低机位。
- 画面构图：珊瑚色软球在前景滚来，小柚脚边和手帕在中景，安安在对面。
- 人物调度与动作真实性：软球贴地滚动，不抛向小柚。
- 画面细节与规整度：不出现围观和掌声。
- 色彩设计：珊瑚球成为小互动强调色。
- 光线设计：窗光落在地毯上。
- 文字融入方案：上方低细节墙面或地毯外空区，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor low-angle page, no text, coral soft fabric ball gently rolling across the round blue rug toward C01 Xiao You sitting at the edge, C02 An An waits on the other side with natural curious expression, Xiao You watches while holding cloud handkerchief, teacher only softly in background, low-pressure social invitation.
- 负面提示词：全书安全负面提示词；no throwing, no crowd, no clapping, no reward, no text.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-07-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-07-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-07-final.png`
- 单页 QA：安全通过；无可读文字；软球贴地滚向小柚，安安等待，没有抛掷、围观或掌声；老师在背景不指挥。P2：第 7/8 页构图相近，但动作方向形成连续互动，可接受。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 8 页

- 页码：8
- 本页中心意思：小柚做出一个小回应。
- 本页故事文字：我也咕噜回去。
- 汉字数：6。
- 朗读检查：顺口；回应动作具体。
- 情绪变化：被邀请 -> 做一个小动作。
- 儿童主体性：小柚自己决定把球滚回去。
- 成人/同伴支持：安安等待接球；老师不评价、不奖励。
- 文字与画面分工：文字说回应动作；画面补充小柚的放松表情。
- 页间推进：故事的最小社交尝试完成。
- 视觉新增量：小柚从观察变为主动动作。
- 出场角色锁定：C01、C02、T01。
- 道具状态：D03 从小柚手边滚回安安；D01 可放在膝旁。
- 空间连续性校验：圆地毯和左窗保持第 6-7 页位置。
- 镜头切换理由：中近景呈现手、球、同伴回应。
- 景别：中近景。
- 视角与机位：幼儿低平视。
- 画面构图：小柚在前景轻推球，安安在对面接球，老师在侧后方微笑等待。
- 人物调度与动作真实性：小柚身体前倾有重心，手接触软球。
- 画面细节与规整度：不出现奖励贴纸、掌声或集体围观。
- 色彩设计：珊瑚球连接两位孩子，蓝绿环境稳定。
- 光线设计：柔和窗光加强轻松感。
- 文字融入方案：左上墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, C01 Xiao You at the edge of the round blue rug gently rolls the coral soft fabric ball back to C02 An An, one hand still near the sky-blue cloud handkerchief, Xiao You shows a small relaxed expression, T01 Teacher Lin waits quietly in background, no applause or reward, low-pressure preschool social moment.
- 负面提示词：全书安全负面提示词；no clapping, no stickers, no text, no crowd pressure, no malformed hands.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-08-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-08-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-08-final.png`
- 单页 QA：安全通过；无可读文字；小柚主动轻轻滚球，安安等待接球，老师在背景不指挥；无奖励、掌声和围观。P2：安安性别呈现偏男孩，但角色设定允许“同班孩子”，不影响叙事。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 9 页

- 页码：9
- 本页中心意思：妈妈按约定来接小柚。
- 本页故事文字：妈妈来接我啦。
- 汉字数：6。
- 朗读检查：顺口；让分离有稳定回路。
- 情绪变化：放松 -> 被接住。
- 儿童主体性：小柚看见妈妈，可以走过去。
- 成人/同伴支持：妈妈在门口蹲下接小柚；老师在旁边自然告别。
- 文字与画面分工：文字说接回；画面补充小柚带着手帕和小小轻松。
- 页间推进：从教室活动回到照顾者连接。
- 视觉新增量：妈妈重新出现，时间闭合。
- 出场角色锁定：C01、A01、T01。
- 道具状态：D01 在手中；D02 从格子中取回或妈妈手边。
- 空间连续性校验：圆窗教室门和储物格作为反向锚点。
- 镜头切换理由：中景让小柚和妈妈的距离明确。
- 景别：中景。
- 视角与机位：教室门口反打。
- 画面构图：妈妈在门口蹲下，小柚向门口走，老师在侧后方等待。
- 人物调度与动作真实性：没有冲撞拥抱，先看见、再靠近。
- 画面细节与规整度：不展示“成绩汇报”。
- 色彩设计：清晨蓝转为更柔和的蓝绿与珊瑚。
- 光线设计：门口光线明亮但不刺眼。
- 文字融入方案：门上方低细节区域，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, classroom doorway with round window and cubbies, A01 Mom kneels at doorway to pick up C01 Xiao You, Xiao You walks toward Mom holding sky-blue cloud handkerchief, T01 Teacher Lin waits gently nearby, calm reunion after first kindergarten day, no report-card feeling.
- 负面提示词：全书安全负面提示词；no text signs, no reward chart, no teacher evaluating child.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-09-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-09-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-09-final.png`
- 单页 QA：安全通过；无可读文字；妈妈蹲在门口接小柚，老师在侧边等待；没有成绩汇报、奖励或评价；书包和手帕状态清楚。
- 单页状态：无字图和排版图已完成，初检通过。

### 第 10 页

- 页码：10
- 本页中心意思：小柚知道明天还可以再来幼儿园。
- 本页故事文字：明天，我还要来幼儿园。
- 汉字数：9。
- 朗读检查：顺口；结尾不要求完全克服。
- 情绪变化：被接住 -> 有把握。
- 儿童主体性：小柚牵着妈妈离开，也可以回头看一眼幼儿园。
- 成人/同伴支持：妈妈牵手同行，不追问表现。
- 文字与画面分工：文字说未来节奏；画面补充小柚回头看门的轻松感。
- 页间推进：温暖收束，开放到明天。
- 视觉新增量：回到蓝绿色园门，形成首尾闭环。
- 出场角色锁定：C01、A01。
- 道具状态：D01 手中；D02 背回或妈妈手边。
- 空间连续性校验：园门与第 2-3 页一致，行动方向反向离开。
- 镜头切换理由：远中景给出余韵和空间闭合。
- 景别：远中景。
- 视角与机位：从园门外回看。
- 画面构图：小柚牵妈妈手往外走，身体放松，轻轻回头看门。
- 人物调度与动作真实性：牵手自然，不被拖走。
- 画面细节与规整度：不加“胜利”元素；不出现掌声或贴纸。
- 色彩设计：清晨蓝和草叶绿回到稳定，珊瑚小点呼应发夹。
- 光线设计：下午或柔和日光，保持安全。
- 文字融入方案：上方天空/墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor ending page, no text, outside the same low rounded blue-green kindergarten gate, C01 Xiao You holds A01 Mom's hand and walks out calmly while looking back at the gate with a small relaxed expression, sky-blue cloud handkerchief visible, teal backpack returned, morning-blue and fresh-green palette, gentle open ending, no victory display.
- 负面提示词：全书安全负面提示词；no text, no prize, no clapping, no forced bravery, no adult dragging child.
- 使用的参考图、模型、版本、种子或角色引用信息：内置 imagegen 生成；原始图 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/raw/page-10-raw.png`。
- 无字图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-10-clean.png`
- 排版完成图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-10-final.png`
- 单页 QA：安全通过；无可读文字；小柚牵妈妈离开并回头看园门，形成首尾闭环；没有胜利展示、奖励或强制克服。P2：妈妈面部为背侧视角，不影响结尾功能。
- 单页状态：无字图和排版图已完成，初检通过。

## 9. 全书质量审计

### 9.1 故事与文字 QA

- 单一核心主题：通过，围绕第一次上幼儿园时“慢慢进入新环境”。
- 年龄适配和字数：通过，每页约 5-10 个汉字，适合 3-4 岁亲子朗读。
- 儿童视角：通过，门口、牵手、格子、边边、球滚来均为幼儿可理解经验。
- 情绪接纳与选择权：通过，孩子可以停住、观察、坐边边、只做一个小回应。
- 是否存在催促、比较、羞辱、条件式奖励或说教：无。
- 重复结构是否每次推进：通过，“看一看”和“咕噜”从观察推进到小回应，再落到愿意明天再来。
- 出声朗读检查：通过，短句自然。
- 结尾是否允许持续适应并避免价值评判：通过。

### 9.2 跨页连续性 QA

- 角色脸型、发型、服装、鞋袜和身高关系：全书初检通过；小柚大眼、双眼皮、长睫毛、发夹、开衫、珊瑚色裤子、手帕和书包连续。
- 固定配角人数与身份：通过，正式互动同伴仅 C02。
- 道具颜色、大小、位置和持握状态：通过；手帕、书包、储物格和珊瑚色软球状态清楚。
- 门窗、地毯、储物格和家具位置：通过；园门、圆窗门、储物格、圆地毯和教室门口锚点连续。
- 镜头轴线、行动方向和光源：文本锁定通过。
- 色板、线条、颗粒和人物比例：通过；整体为统一水彩和彩铅质感，室内页木色略多但未破坏蓝绿主调。
- 画幅、像素尺寸和页码命名：通过；无字图和排版图均为 `1536x2048`，页码命名完整。

### 9.3 AI 瑕疵审计

- P0 问题及重做页码：未见。
- P1 问题及修正页码：未见必须修正项。
- P2 已记录差异：角色参考图中书包出现小云朵挂件，已纳入 D02 可用配件；第 4/5/6/7/8/9 页室内木色略多但不影响叙事；第 7/8 页构图相近但动作方向构成连续互动；第 8 页安安性别呈现偏男孩但不影响同伴角色功能；第 10 页妈妈面部为背侧视角。
- 整本联系表检查结果：通过；整本联系表路径 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/storyboard-contact-sheet.png`。
- 最终可交付结论：全书无字图、排版图、PDF 和 PPTX 已完成，可进入用户审阅或后续印刷微调。

## 10. 给家长的文字

- 这个故事想让孩子感受到什么：第一次上幼儿园紧张、停住、想先看一看，都是可以被理解的；适应可以从一个很小的动作开始。
- 共读提醒：不要用故事催孩子“明天不能哭”或“要像小柚一样交朋友”。孩子的节奏可能每天不同。
- 亲子互动：
  - 读第 2 页时，可以问：“小柚的脚为什么停住了？”
  - 读第 4 页时，可以一起说：“进来看一看吧”，再补一句“想慢一点也可以”。
  - 读第 6 页时，可以让孩子指一指“边边在哪里”。
  - 读第 8 页时，可以和孩子做一个轻轻滚球的动作。
- 可使用的支持性语言：
  - “你想先牵着我，还是先看一看？”
  - “我听见你说想慢一点。”
  - “今天做到这一小步，就可以了。”
- 不建议使用的语言：
  - “别怕，没什么好怕的。”
  - “别人都进去了，你也快点。”
  - “不哭才是勇敢。”
- 适合幼儿年龄：3-4 岁，3-5 岁可亲子共读。

## 11. 交付准备

- 故事包文本路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/story/story-package.md`
- 逐页脚本路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/story/page-script.md`
- 家长指南路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/story/parent-guide.md`
- 角色圣经路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-bible.md`
- 环境地图路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/environment-map.md`
- 色板与风格圣经路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/color-and-style-bible.md`
- 连续性矩阵路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/continuity-matrix.md`
- 整本缩略联系表路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/storyboard-contact-sheet.png`
- 角色参考图路径：优先使用 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-reference-sheet-v2-eyes.png`；原始版为 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/character-reference-sheet.png`
- 环境参考图路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/environment-reference-sheet.png`
- 无字封面图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/cover-clean.png`
- 无字内页图片路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-01-clean.png` 至 `page-10-clean.png`
- 排版完成封面路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/cover-final.png`
- 排版完成内页路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/composited/page-01-final.png` 至 `page-10-final.png`
- 可编辑排版源文件路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/layout/editable-layout.html`；渲染脚本 `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/layout/render_book.py`
- 故事与文字 QA 路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/qa/story-and-text-qa.md`
- 视觉连续性 QA 路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/qa/visual-consistency-qa.md`
- AI 瑕疵审计路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/qa/ai-artifact-audit.md`
- 素材清单路径：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/qa/materials-manifest.md`
- 导出文件路径：PDF `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/export/ruyuan-shiying-yu-shejiao-diyici-shang-youeryuan.pdf`；PPTX `outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/export/ruyuan-shiying-yu-shejiao-diyici-shang-youeryuan.pptx`
- 固定输出目录：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/`
