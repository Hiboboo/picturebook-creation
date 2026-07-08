# 《小肚肚叮一下》故事包

## 1. 交付状态

- 当前状态：故事草案 + 视觉设定 + 插画提示词已完成；封面与 8 页无字内页样张均已完成 v2 生成并初检。
- 实际图片生成：是，已生成封面 + 8 页无字内页 v2。
- 生成方式：人工文本设计 + AI 辅助插画提示词规划 + 图像模型生成全书样张；原始图保存在 `artwork/raw/`，规范化无字样张保存在 `artwork/clean/`，v1 旧样张保留不覆盖。
- 本次未完成项：角色参考图、环境参考图、后期文字排版、PDF/PPT 导出。
- 需要用户确认项：书名《小肚肚叮一下》、主角沿用“小葫芦”、主要年龄定位为 2-3 岁、故事中不展示尿液和私密部位。
- 本次修订：根据反馈强化“叮一下”的重复钩子，加入“不想停下玩”的轻微犹豫，减少正文中的成人指导，把结尾从“干干的结果”转为“听见身体后的轻松感”。
- 本次样张精修：根据四张样张精修意见单生成 v2，重点修正第 6 页“像穿着训练裤坐马桶”的误读，并统一第 8 页小马桶与小兔耳朵连续性；随后补齐第 1/3/4/5/7 页，形成全书无字内页样张。
- 本地记录：新标题未发现重复，已登记草稿；旧标题《尿尿来啦》已归档为改名前记录。SQLite：`records/picturebook_records.sqlite`；导出 JSON：`records/records.json`。

## 2. 基本信息

- 系列：生活习惯养成系列。
- 书名：小肚肚叮一下。
- 主题：听见尿意信号，慢慢练习坐小马桶。
- 图/文：小葫芦。
- 主要适合年龄：2-3 岁。
- 可延伸年龄：2-4 岁亲子共读。
- 核心主题：孩子可以听见身体发出的“叮一下”，再慢慢去小马桶坐一坐。
- 孩子的生活入口：玩积木时突然感觉小肚肚有一点点提示。
- 目标情绪变化：从专注玩耍，到听见身体信号但有点不想停，再到愿意抱着小兔慢慢走、坐一坐，最后感到“我听见啦，真轻松”。
- 故事页数：8 页，不含封面。
- 画面风格：温柔水彩和彩铅线条，轻纸感颗粒，幼儿比例圆润；明亮家庭浴室和客厅，不使用医院式、训练营式或羞耻化视觉。
- 视觉细节密度：适中偏简洁。
- 色彩设计策略：奶油白和浅木色提供安全感，柔和薄荷绿表现清洁，暖黄色表现成人陪伴，苹果红作为小马桶按钮/小标识的少量强调色。
- 图片比例：固定 `3:4` 竖版。
- 锁定像素尺寸：`1536x2048`。
- 文字安全边距：至少画布宽高的 `6%`；印刷项目另列出血。
- 固定输出目录：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/`

## 3. 儿童发展与情绪安全策略

- 孩子可能感受到的情绪：专注、被打断的不愿意、好奇、急一点、需要妈妈陪、等待时的专心、身体放松后的轻松。
- 故事如何接纳这种情绪：故事不说“不能尿裤子”“羞羞脸”，而是把如厕写成听见身体信号后的一个小动作。
- 孩子拥有的选择：停一停、抱小兔一起去、慢慢走、坐一小会儿、没来就先起来、下次再试。
- 成人如何提供支持：妈妈蹲到孩子视线高度，听见孩子的表达，给出安静陪伴和可退回的空间；正文不依赖妈妈口令推动，画面中妈妈在旁边等待。
- 故事中的最小可行尝试：孩子只需要走到小马桶并坐一坐；是否每次都尿出来不作为价值判断。
- 结尾如何避免“必须克服”：结尾停在孩子听见身体、感觉轻松，不扩展为“以后再也不会尿裤子”，也不把“干干的”作为唯一成绩。
- 奖励、掌声或贴纸的处理：不出现奖励、贴纸、掌声或排行榜。
- 禁用表达：“这么大了还尿裤子”“憋住”“快点快点”“羞羞脸”“乖孩子才会坐马桶”“坐好了才有奖励”“你看别人都不会尿裤子”。

## 4. 故事设定卡

- 背景：白天的家里，客厅铺着游戏垫，右侧通向明亮小浴室，小马桶放在浴室门内侧。
- 儿童视角：故事来自孩子能理解的身体感受和动作经验：玩着玩着，小肚肚“叮一下”，积木还没搭完，但可以抱小兔慢慢走，坐一坐、等一等。
- 故事弧线：生活入口 -> 身体信号 -> 轻微犹豫 -> 自己选择抱小兔慢慢走 -> 看到小马桶 -> 坐一坐、等一等 -> 身体真实回应 -> 温暖收束。
- 重复结构：“叮”作为全书记忆钩子：第 2 页身体叮一下，第 3 页孩子确认“叮？”，第 8 页孩子说“我听见啦”；第 6 页用“等一等”降低必须立刻成功的压力。
- 页间推进：从客厅玩耍，到身体信号出现和不想停下玩的犹豫，再到去浴室、坐马桶等待，最后回到身体轻松感。
- 温暖结尾：孩子不是展示“成功成绩”，而是知道自己听见了身体的小铃铛，感觉轻松。
- 故事禁改项：不展示私密部位；不展示尿液细节；不把意外尿湿写成羞耻；不让成人强行抱起、按住或围观孩子坐马桶。

## 5. 视觉圣经与连续性锁定

### 5.1 角色圣经

- 角色 ID：C01-小葫芦
- 名称与身份：小葫芦，正在练习坐小马桶的幼儿。
- 年龄感 / 物种：2-3 岁人类幼儿。
- 身高与头身比例：约 3.5 头身，圆润幼儿比例。
- 脸型与核心五官：圆脸，黑色眼睛，短鼻小嘴，表情细微。
- 发型与发色：黑色短发，柔软刘海，耳侧自然碎发。
- 上衣：暖黄色短袖上衣，胸前一个小白圆点。
- 下装：浅蓝训练裤，苹果小图案；坐马桶页必须用长上衣、侧身和遮挡保证私密安全。
- 鞋袜：室内浅灰防滑袜。
- 固定配色：暖黄色、浅蓝、奶油白。
- 标志性配件或道具：P01-小兔抱偶可陪同去浴室。
- 常见表情范围：专注、疑惑、急一点、专心、轻松、开心一点；不默认全程大笑。
- 禁改项：黑色短发、暖黄色上衣、浅蓝训练裤、幼儿比例。
- 可变项：坐姿、走路姿态、抱小兔力度、看向妈妈或小马桶的方向。
- 角色参考图路径或状态：未生成。

- 角色 ID：A01-妈妈
- 名称与身份：妈妈，温和照顾者。
- 年龄感 / 物种：成人女性，人类。
- 身高与头身比例：成人比例，明显高于小葫芦；同框时蹲低或坐小凳。
- 脸型与核心五官：柔和脸型，深棕眼睛，自然倾听表情。
- 发型与发色：深棕色低马尾。
- 上衣：奶油色棉麻衬衫。
- 下装：浅橄榄绿居家长裤。
- 鞋袜：米色居家拖鞋。
- 固定配色：奶油白、浅橄榄绿、暖灰。
- 标志性配件或道具：无固定手持物；可在第 4 页轻轻伸出开放手势。
- 常见表情范围：平静、倾听、等待、温和提示、放松。
- 禁改项：低马尾、奶油色上衣、蹲低支持、不强迫。
- 可变项：蹲在游戏垫边、站在浴室门旁、侧身等待。
- 角色参考图路径或状态：未生成。

### 5.2 演员表

- 固定角色总表：C01-小葫芦全书常驻；A01-妈妈第 3-8 页出现或局部出现。
- 配角人数与身份锁定：无其他家庭成员、同伴或围观者。
- 身高关系：妈妈约为小葫芦 2.3 倍身高；支持时降低身体高度。
- 不得互换或替代的角色：不得把妈妈替换成老师、陌生成人或同伴；不得新增孩子形成比较。

### 5.3 环境与空间连续性地图

- 时间与天气：晴朗白天，室内自然光。
- 核心场景：客厅游戏垫、客厅右侧的浴室门、小浴室内的小马桶区域。
- 起点：客厅左侧游戏垫，小葫芦在搭积木。
- 目标点：浴室右侧的小马桶。
- 行动路线和路径轴线：从客厅左下游戏垫向右侧浴室门移动，再进入浴室坐小马桶；镜头主侧保持客厅在左、浴室在右。
- 固定地标：浅木地板、圆角游戏垫、蓝黄积木、右侧浴室门、浴室白色小瓷砖、薄荷绿毛巾、小马桶、脚边小脚凳。
- 角色进入/离开方向：小葫芦从左向右移动；妈妈从客厅后侧蹲下，再跟到浴室门边等待。
- 镜头主侧与越轴线：不越过客厅到浴室的行动轴线；反打时保留浴室门框或游戏垫边缘作为锚点。
- 主光源方向：左侧窗户柔和日光；浴室顶部漫反射白光；全书保持明亮安全。
- 允许变化项：小葫芦从游戏垫到浴室的位置、妈妈蹲下或门边等待、训练裤穿脱状态用安全遮挡处理。
- 禁改项：不得把小浴室画成公共厕所、医院场景、阴暗空间或封闭惩罚空间；不得出现马桶成人化过大或脏乱。
- 环境参考图或平面图路径：未生成。

### 5.4 道具状态表

- 道具 ID 与名称：D01-小马桶
- 归属角色：家庭浴室固定物。
- 颜色、尺寸和图案：奶油白小马桶，薄荷绿坐圈，前方一个小苹果红圆点。
- 初始位置：第 5 页明确出现，前几页可在浴室门内远处隐约可见。
- 每页状态变化：第 5 页被看见；第 6-7 页小葫芦坐在上面；第 8 页留在浴室门内背景。
- 持握手或摆放方向：不手持，正面略朝向客厅。
- 禁改项：不得变成成人马桶、不得变色、不得出现脏污或夸张拟人脸。

- 道具 ID 与名称：P01-小兔抱偶
- 归属角色：C01-小葫芦。
- 颜色、尺寸和图案：奶油白布兔，浅蓝耳朵内侧，小葫芦前臂长度。
- 初始位置：第 1 页在游戏垫边。
- 每页状态变化：第 3 页小葫芦可抓兔耳；第 4-5 页可抱着走；第 6-7 页放在脚边小凳或妈妈手边；第 8 页回到怀里。
- 持握手或摆放方向：多用左手抱或靠在脚边，兔耳朝上。
- 禁改项：不得变色、变大、变成其他动物或无故消失。

- 道具 ID 与名称：D02-积木
- 归属角色：C01-小葫芦。
- 颜色、尺寸和图案：蓝、黄、浅木色大颗粒积木。
- 初始位置：第 1 页在游戏垫中央。
- 每页状态变化：第 1-4 页在客厅；第 8 页小葫芦回到游戏垫边，可见积木还在。
- 持握手或摆放方向：第 1 页右手放积木，第 2 页手停住，第 3 页放下。
- 禁改项：不得变成小颗粒危险玩具；不得堵住去浴室路线。

- 道具 ID 与名称：D03-浅蓝训练裤
- 归属角色：C01-小葫芦。
- 颜色、尺寸和图案：浅蓝色，苹果小图案。
- 初始位置：第 1 页穿在身上。
- 每页状态变化：第 6-7 页用长上衣、侧身、马桶遮挡和画外处理；第 8 页穿好且整洁，但不是画面焦点。
- 持握手或摆放方向：第 8 页可见腰头平整。
- 禁改项：不得展示私密部位；不得把裤裤湿掉画成羞耻焦点。

### 5.5 风格、色板与版式锁定

- 媒介与线条：温柔水彩底色，彩铅细线勾边。
- 颗粒与纹理：轻纸感颗粒，避免塑料皮肤和过度纹理。
- 人物比例和面部风格：幼儿圆润，成人自然，表情细微。
- 主色：奶油白、浅木色、柔和薄荷绿。
- 辅助色：暖黄色、浅蓝、浅橄榄绿。
- 强调色：苹果红小圆点，仅用于小马桶标识或训练裤图案。
- 禁用色彩倾向：医院冷白、脏乱灰褐、随机彩虹色、过度高饱和、阴暗低照度。
- 文字字体层级：书名大字号；正文中字号；署名小字号。
- 文字区规则：使用墙面、浴室门上方、游戏垫外侧地面等低细节自然区域；不得用固定卡片或不透明大背板。
- 无字插画规则：图像模型不得生成中文书名、正文、标签、厕所标识文字或可读墙面文字。

## 6. 全书镜头与翻页计划

| 页码 | 叙事节点 | 情绪起点->终点 | 景别 | 视角/机位 | 出场角色 ID | 核心动作 | 空间锚点 | 文字区 | 相比上一页的视觉新增量 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 客厅玩积木 | 专注->投入 | 远中景 | 幼儿视角平视 | C01 | 小葫芦搭积木 | 游戏垫、浴室门 | 左上墙面 | 建立客厅到浴室路线 |
| 2 | 身体信号出现 | 投入->注意身体 | 近景 | 平视 | C01 | 手停在积木上，另一手轻碰肚肚 | 游戏垫边、积木 | 右上 | 身体信号和动作暂停 |
| 3 | 听见叮并有点犹豫 | 注意身体->想确认但不想停 | 中近景 | 低平视 | C01, A01 | 小葫芦一手靠肚肚，一手还挨着积木 | 妈妈蹲下、浴室门 | 左上 | 身体信号和未完成积木同框 |
| 4 | 自己抱小兔慢慢走 | 犹豫->开始行动 | 远中景 | 从客厅看浴室门 | C01, A01 | 小葫芦抱小兔迈小步 | 游戏垫、浴室门框 | 上方墙面 | 空间移动开始，妈妈不拉不催 |
| 5 | 看见小马桶 | 有陪伴->愿意试 | 中景 | 浴室门口平视 | C01, A01 | 小葫芦站在小马桶前看一看 | 小马桶、薄荷毛巾 | 右上瓷砖空区 | 目标物出现 |
| 6 | 坐一坐，等一等 | 愿意试->专心等待 | 近景 | 侧面平视 | C01, A01 局部 | 小葫芦安全坐在小马桶上等一等 | 小马桶、脚凳、门框 | 左上 | 如厕动作但保持隐私，并降低成功压力 |
| 7 | 小肚肚轻轻的 | 专心等待->小肚肚放松 | 特写 | 手脚局部/脸部近景 | C01 局部 | 肩膀放松，脚踩稳 | 小脚凳、小兔、马桶边 | 右上 | 小肚肚回应，不展示尿液 |
| 8 | 听见身体，真轻松 | 放松->有把握 | 中景 | 从浴室看回客厅 | C01, A01 | 小葫芦回到游戏垫边，表情轻松 | 浴室门、游戏垫、积木 | 左上 | 回到生活，温暖收束 |

## 7. 封面图片

- 封面状态：无字样张 v2 已生成，待后期标题排版。
- 无字封面图片文件路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/cover-clean-v2.png`
- 排版完成封面图片路径：未生成。
- 图片比例与像素尺寸：固定 `3:4`，`1536x2048`。
- 封面中心意思：小葫芦玩积木时听见小肚肚“叮一下”，一手轻碰肚肚，一手抱小兔，正准备慢慢走向明亮小浴室。
- 封面构图说明：左下是未搭完的积木和游戏垫，右侧浴室门内可见小马桶；小葫芦站在两者之间，有一点舍不得停下玩但不慌张，妈妈蹲低在后方或侧边，用开放手势等待；上方墙面预留书名区。
- 角色锁定：C01 暖黄色上衣、浅蓝训练裤、浅灰防滑袜；A01 低马尾、奶油色衬衫、浅橄榄绿居家裤；P01 小兔抱偶。
- 书名排版：后期可编辑文本层，建议两行“小肚肚 / 叮一下”，圆润清楚，不使用装饰性过强字体。
- 副标题排版：可选小副标题“练习坐小马桶的故事”，放在书名下方或封底说明区，字号明显小于主书名；仅由后期可编辑文本层添加。
- 署名排版：固定 `图/文：小葫芦`；普通字体、深灰、小字号、舒适间距。
- 标题安全区：距离边缘至少 6%，不遮挡小葫芦脸、手、小兔和浴室路线。
- 无字封面图像提示词：见“封面提示词”。
- 封面负面提示词：安全、隐私、解剖、一致性、乱码和过度装饰约束已写入提示词。
- 使用的角色/环境参考图、模型、版本、种子或引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/cover-raw-v2.png`。
- 封面 QA 结果：v2 初检通过。无可读文字、无尿液、无私密暴露；客厅左、浴室右、小马桶可见，妈妈陪伴关系温和；孩子“听见身体信号”的轻微疑惑感和半成品积木信息比 v1 更明确。

## 8. 内页图片与文字

### 第 1 页

- 页码：1
- 本页中心意思：小葫芦正在专注玩积木。
- 本页故事文字：小葫芦搭呀搭。
- 汉字数：6。
- 朗读检查：顺口，重复节奏适合 2-3 岁。
- 情绪变化：专注 -> 投入。
- 儿童主体性：孩子自由玩耍，没有被任务打断。
- 成人/同伴支持：无额外推动。
- 文字与画面分工：文字说玩耍动作；画面交代游戏垫和浴室门位置。
- 页间推进：建立“玩着玩着”的生活入口，为身体信号出现做铺垫。
- 视觉新增量：完整客厅和通向浴室的路线。
- 出场角色锁定：C01 1 人，暖黄色上衣、浅蓝训练裤、浅灰防滑袜。
- 道具状态：D02 积木在游戏垫中央；P01 小兔在游戏垫边；D01 小马桶可在浴室门内远处隐约可见。
- 空间连续性校验：客厅在左，浴室门在右。
- 镜头切换理由：建立场景。
- 景别：远中景。
- 视角与机位：幼儿视角平视。
- 画面构图：小葫芦在左下游戏垫，浴室门在右后方，行动路线保持清楚。
- 人物调度与动作真实性：小葫芦坐在地垫上，右手拿积木，脚接触地垫。
- 画面细节与规整度：保留积木、浴室门、小兔；删减无关玩具。
- 色彩设计：浅木色和暖黄色表现家里安全感。
- 光线设计：左侧窗光柔和照入。
- 文字融入方案：左上墙面低细节区，1 行，安全边距 6%。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor preschool picturebook page, no text, bright cozy living room in daytime, child-eye-level view, C01 Xiao Hulu is a 2-3-year-old child with black short hair, round face, warm yellow short-sleeve top, light blue training pants with tiny apple pattern, light gray non-slip socks, sitting on a round-corner play mat and stacking large safe blue, yellow and wood blocks, P01 cream bunny plush near the mat, bathroom door visible on the right side with a small cream potty faintly inside, soft natural window light, low-detail text area on upper wall, gentle colored pencil linework, light paper grain.
- 负面提示词：no text, no pseudo-Chinese, no nudity, no exposed private parts, no shaming, no toilet use shown, no small choking-hazard blocks, no extra fingers, no missing fingers, no malformed anatomy, no duplicated child, no clutter, no plastic skin.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-01-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-01-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。客厅左、浴室右的路线清楚，孩子专注搭积木，小兔和小马桶远景锚点到位；无文字、无如厕动作、无隐私风险。
- 单页状态：无字样张 v2 已生成，待人工终审。

### 第 2 页

- 页码：2
- 本页中心意思：身体信号出现，小葫芦停一下。
- 本页故事文字：小肚肚，叮一下。
- 汉字数：6。
- 朗读检查：顺口，“叮一下”将身体信号具体化。
- 情绪变化：投入 -> 注意身体。
- 儿童主体性：孩子感到信号并暂停动作。
- 成人/同伴支持：无额外推动。
- 文字与画面分工：文字说身体提示；画面补充手停住、积木未继续搭。
- 页间推进：从玩耍转向如厕需要。
- 视觉新增量：手部动作停顿和肚肚提示。
- 出场角色锁定：C01 1 人，服装不变。
- 道具状态：D02 积木塔停在半高；P01 仍在游戏垫边。
- 空间连续性校验：仍在客厅游戏垫，浴室门保持右侧远景锚点。
- 镜头切换理由：近景服务身体信号。
- 景别：近景。
- 视角与机位：平视略近。
- 画面构图：小葫芦上半身和积木在前景，浴室门只作为远处锚点。
- 人物调度与动作真实性：一只手停在积木上，另一只手轻轻碰肚子，不夸张捂痛。
- 画面细节与规整度：背景简洁，不画夸张符号。
- 色彩设计：暖黄保持安全，薄荷绿浴室门框作为下一步线索。
- 光线设计：延续左侧窗光。
- 文字融入方案：右上低细节墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, same living room and play mat, closer view of C01 Xiao Hulu in warm yellow top and light blue training pants, one small hand pauses on a large block while the other hand lightly touches the tummy, expression curious and noticing a body signal, not painful, P01 bunny plush near the knee, bathroom doorway still visible softly on the right, bright safe daytime home, natural blank text area upper right.
- 负面提示词：no text, no pseudo-Chinese, no pain, no fear, no shaming, no exposed private parts, no toilet use, no extra fingers, no fused hands, no malformed wrist, no duplicated toys, no random decorative clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-02-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-02-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。搭积木的手停顿感更明确，轻触肚肚动作自然，表情为轻微察觉而非疼痛；无可读文字、无如厕细节，浴室门保持右侧背景线索。
- 单页状态：无字样张 v2 已生成，待人工终审。

### 第 3 页

- 页码：3
- 本页中心意思：小葫芦听见“叮”，也看见积木还没搭完。
- 本页故事文字：叮？尿尿来啦？
- 汉字数：5。
- 朗读检查：短句顺口，“叮？”延续身体信号钩子。
- 情绪变化：注意身体 -> 想确认但不想停下玩。
- 儿童主体性：孩子主动确认身体信号，也保留对未完成游戏的牵挂。
- 成人/同伴支持：妈妈蹲低倾听，不替孩子判断。
- 文字与画面分工：文字是孩子的确认；画面补充未搭完的积木和妈妈蹲低等待。
- 页间推进：身体信号和“还想玩”的轻微犹豫同时出现，为下一页自己慢慢走提供动力。
- 视觉新增量：妈妈加入画面但保持低压力，未完成积木仍在孩子手边。
- 出场角色锁定：C01、A01。
- 道具状态：D02 积木在小葫芦身旁；P01 可被小葫芦轻抓兔耳。
- 空间连续性校验：客厅左侧，浴室门右侧；妈妈从后侧蹲下。
- 镜头切换理由：中近景呈现孩子和妈妈的视线连接。
- 景别：中近景。
- 视角与机位：低平视。
- 画面构图：小葫芦居中偏左，一手靠肚肚，一手仍挨着积木；妈妈蹲在右后方，浴室门框在更右侧。
- 人物调度与动作真实性：妈妈双手开放，身体略后退，不拉孩子。
- 画面细节与规整度：只保留积木、小兔和浴室门。
- 色彩设计：妈妈奶油色上衣和浅橄榄绿裤子柔和稳定。
- 光线设计：窗光照亮孩子脸，浴室光柔和。
- 文字融入方案：左上墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, same home layout, C01 Xiao Hulu looks up from the play mat with a questioning expression and one hand near tummy, the other hand still close to an unfinished block tower to show a tiny reluctance to stop playing, A01 mother with deep brown low ponytail, cream cotton-linen shirt and light olive home pants kneels at child height with gentle listening posture and open hands, bathroom doorway on right as the next destination, P01 bunny plush near the child, no pressure, no rushing, soft natural daylight, low-detail wall area for later Chinese text.
- 负面提示词：no text, no pseudo-Chinese, no shaming, no pointing pressure, no adult pulling child, no panic, no nudity, no exposed private parts, no extra fingers, no malformed hands, no duplicated people.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-03-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-03-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。孩子一手靠近小肚肚、一手仍在积木旁，轻微犹豫感成立；妈妈蹲低倾听，没有拉拽或催促；浴室门和小马桶保持右侧线索。
- 单页状态：无字样张 v2 已生成，待人工终审。

### 第 4 页

- 页码：4
- 本页中心意思：小葫芦慢慢走向浴室。
- 本页故事文字：抱小兔，慢慢走。
- 汉字数：6。
- 朗读检查：顺口，以孩子行动代替成人口令。
- 情绪变化：想确认但不想停下玩 -> 开始行动。
- 儿童主体性：孩子自己迈步走向浴室，可抱小兔。
- 成人/同伴支持：妈妈在画面里保持一步距离跟随，不拉、不催、不挡路。
- 文字与画面分工：文字说孩子选择的行动；画面显示妈妈安静陪着。
- 页间推进：从犹豫进入行动路线。
- 视觉新增量：客厅到浴室的移动。
- 出场角色锁定：C01、A01。
- 道具状态：P01 被小葫芦抱在左臂；D02 积木留在游戏垫；D01 小马桶在门内更清楚。
- 空间连续性校验：行动方向左到右，门框作为锚点。
- 镜头切换理由：远中景展示路线和成人距离。
- 景别：远中景。
- 视角与机位：从客厅看向浴室门。
- 画面构图：小葫芦在中间向右走，抱着小兔；妈妈在左后方稍低，浴室门内有明亮光。
- 人物调度与动作真实性：小葫芦双脚落地，步幅小；妈妈不牵拉，只跟在后面。
- 画面细节与规整度：保持路线无遮挡。
- 色彩设计：浴室薄荷绿和奶油白引导视线。
- 光线设计：浴室光比客厅略亮，形成目标点。
- 文字融入方案：上方墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, child-eye-level wide-medium view from living room toward bathroom, C01 Xiao Hulu chooses to hug P01 cream bunny plush and walks slowly from the play mat toward the bright bathroom doorway, A01 mother follows one step behind at a calm distance with open supportive posture, not leading or pulling, unfinished large blocks remain on the play mat, small cream potty with mint seat partly visible inside bathroom, clear left-to-right movement path, soft daylight and clean warm home palette, natural blank text area above.
- 负面提示词：no text, no pseudo-Chinese, no running, no rushing, no adult pulling or carrying child, no panic, no nudity, no exposed private parts, no slippery floor, no clutter blocking the path, no extra limbs.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-04-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-04-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。孩子抱小兔自行从客厅走向浴室，步幅小且路线无遮挡；妈妈在后方陪同，没有牵拉、抱起或催促。
- 单页状态：无字样张 v2 已生成，待人工终审。

### 第 5 页

- 页码：5
- 本页中心意思：小葫芦看见小马桶。
- 本页故事文字：小马桶，在这里。
- 汉字数：6。
- 朗读检查：顺口，目标物明确。
- 情绪变化：有陪伴 -> 愿意试。
- 儿童主体性：孩子先看一看，不被强迫坐下。
- 成人/同伴支持：妈妈站在浴室门旁等待。
- 文字与画面分工：文字说小马桶位置；画面补充小马桶尺寸友好、脚凳稳定。
- 页间推进：目标点出现，为坐一坐准备。
- 视觉新增量：浴室空间和小马桶完整出现。
- 出场角色锁定：C01、A01。
- 道具状态：D01 小马桶在浴室内侧；P01 在小葫芦怀里；D04 小脚凳在小马桶前。
- 空间连续性校验：从客厅进入浴室门口，仍可看见门框。
- 镜头切换理由：中景确认环境安全。
- 景别：中景。
- 视角与机位：浴室门口平视。
- 画面构图：小马桶在右下，小葫芦在左侧看向它，妈妈在门边。
- 人物调度与动作真实性：小葫芦站稳，身体略前倾观察。
- 画面细节与规整度：保留小马桶、脚凳、毛巾；删减其他浴室杂物。
- 色彩设计：奶油白与薄荷绿突出干净柔和。
- 光线设计：浴室漫反射光，没有刺眼冷白。
- 文字融入方案：右上瓷砖低细节区，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, bright small home bathroom viewed from doorway, C01 Xiao Hulu stands safely near a child-sized cream potty with mint green seat and tiny apple-red dot on front, small stable footstool in front, P01 bunny plush in child's arm, A01 mother waits gently by the door at a respectful distance, mint towel and simple white tiles as fixed anchors, child is looking first before sitting, calm and clean, no public restroom feeling, blank low-detail tile area upper right for later text.
- 负面提示词：no text, no pseudo-Chinese, no adult toilet, no dirty bathroom, no public restroom, no coercion, no adult touching pants, no nudity, no exposed private parts, no extra fingers, no distorted potty, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-05-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-05-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。小马桶和脚凳位置清楚，孩子只是先看一看，没有被迫坐下；浴室干净明亮，未出现公共厕所感、尿液或隐私内容。
- 单页状态：无字样张 v2 已生成，待人工终审。

### 第 6 页

- 页码：6
- 本页中心意思：小葫芦坐在小马桶上试一试。
- 本页故事文字：坐一坐，等一等。
- 汉字数：6。
- 朗读检查：顺口，动作和等待都很轻，不催结果。
- 情绪变化：愿意试 -> 专心等待。
- 儿童主体性：孩子坐一小会儿；可随时起身。
- 成人/同伴支持：妈妈在门边等待，可把小兔放在脚边陪伴。
- 文字与画面分工：文字说坐一坐、等一等；画面用侧身和遮挡保护隐私。
- 页间推进：从看见目标进入实际小动作。
- 视觉新增量：如厕动作出现但不展示隐私，同时表达没来也可以慢慢等。
- 出场角色锁定：C01；A01 可局部出现。
- 道具状态：D01 被使用；D04 小脚凳在脚下；P01 在脚凳旁或妈妈手边；D03 训练裤状态用构图遮挡，不直接展示。
- 空间连续性校验：浴室门框保留在左侧背景，薄荷毛巾位置不变。
- 镜头切换理由：侧面近景保护隐私，同时表达坐稳。
- 景别：近景。
- 视角与机位：侧面平视。
- 画面构图：小葫芦侧坐在小马桶上，长上衣自然遮住腰腿隐私区域，脚踩小脚凳，妈妈只露出温和等待的手或膝盖。
- 人物调度与动作真实性：脚踩稳，身体重心自然，手可放在膝上或抱小兔。
- 画面细节与规整度：不展示尿液，不展示裤子脱下细节。
- 色彩设计：薄荷绿与暖黄保持轻松。
- 光线设计：柔和浴室光，脸部清楚。
- 文字融入方案：左上门框外墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor page, no text, privacy-safe side view in the same bright home bathroom, C01 Xiao Hulu sits steadily on the child-sized cream potty with mint seat and waits calmly, the same warm yellow short-sleeve top drapes low enough to safely cover the lap area, light blue training pants are not explicitly shown during use, no private parts visible, feet rest on a small footstool, P01 bunny plush sits nearby, A01 mother only partially visible by the doorway waiting calmly without pressure, soft clean bathroom anchors, child focused and calm, natural blank area upper left for text.
- 负面提示词：no text, no pseudo-Chinese, no nudity, no exposed private parts, no urine stream, no liquid, no adult holding child down, no pressure, no shaming, no anatomical detail, no extra fingers, no malformed legs, no awkward potty pose, no dirty bathroom.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-06-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-06-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。已修正 v1 中“像训练裤完整穿着坐上去”的误读，隐私区域由侧面机位、上衣下摆和马桶边缘共同遮挡；无私密暴露、无尿液、无马桶内部细节，脚踩小凳且姿势稳定。正式页仍需人工终审隐私安全。
- 单页状态：无字安全样张 v2 已生成，待人工终审。

### 第 7 页

- 页码：7
- 本页中心意思：小肚肚回应了，小葫芦放松下来。
- 本页故事文字：嘘——小肚肚轻轻的。
- 汉字数：7。
- 朗读检查：拟声词自然，“小肚肚”与书名呼应，低幼可理解。
- 情绪变化：专心 -> 小肚肚放松。
- 儿童主体性：孩子感受到小肚肚轻松。
- 成人/同伴支持：妈妈在旁边等待，不用掌声或奖励评价。
- 文字与画面分工：文字用声音和小肚肚感受表现回应；画面只呈现放松表情和稳定身体。
- 页间推进：坐一坐、等一等后，身体有了真实回应。
- 视觉新增量：情绪近景和脚踩稳的身体安全感。
- 出场角色锁定：C01 局部，A01 可用门边剪影。
- 道具状态：D01 继续被使用；D04 脚凳在脚下；P01 在脚边。
- 空间连续性校验：浴室薄荷毛巾和门框位置不变。
- 镜头切换理由：特写避免展示隐私，强调放松。
- 景别：特写。
- 视角与机位：脸部、手部或脚部局部近景。
- 画面构图：小葫芦脸部轻松、手放在膝上、脚踩小凳；小马桶边缘和小兔作为锚点。
- 人物调度与动作真实性：身体自然坐稳，不漂浮，不夸张扭动。
- 画面细节与规整度：不画尿液、马桶内部或裤子细节。
- 色彩设计：暖黄光在孩子脸上更柔和。
- 光线设计：浴室光均匀，情绪明亮。
- 文字融入方案：右上瓷砖空区，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor close-up page, no text, privacy-safe close composition in the same bathroom, show C01 Xiao Hulu's relaxed face, dropped shoulders, and small hands resting calmly, feet stable on the small footstool, edge of the mint-seat potty and P01 bunny plush visible as anchors, A01 mother only softly suggested near doorway, the moment communicates the tummy feeling light and relieved without showing urine, liquid, toilet bowl contents, or private body parts, warm gentle clean palette, low-detail tile area upper right for later text.
- 负面提示词：no text, no pseudo-Chinese, no nudity, no exposed private parts, no urine, no liquid stream, no toilet bowl contents, no shame, no reward sticker, no clapping crowd, no extra fingers, no malformed hands or feet, no dirty bathroom.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-07-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-07-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。画面以放松表情、手部和脚踩小凳表达“小肚肚轻轻的”；没有尿液、马桶内部内容、私密暴露或奖励羞耻元素。正式页仍建议人工终审隐私安全。
- 单页状态：无字安全样张 v2 已生成，待人工终审。

### 第 8 页

- 页码：8
- 本页中心意思：孩子发现自己听见了身体信号，轻松回到生活里。
- 本页故事文字：我听见啦，真轻松。
- 汉字数：7。
- 朗读检查：顺口，结尾强调自我觉察和身体感受。
- 情绪变化：身体放松 -> 有把握。
- 儿童主体性：孩子穿好裤裤，自己走回游戏垫。
- 成人/同伴支持：妈妈在旁边自然陪伴，不奖励、不比较。
- 文字与画面分工：文字说自我觉察和轻松感；画面补充回到积木游戏和妈妈的平静陪伴。
- 页间推进：故事回到生活入口，形成闭环。
- 视觉新增量：从浴室回望客厅，空间闭合；画面不做“胜利展示裤裤”。
- 出场角色锁定：C01、A01。
- 道具状态：D03 训练裤穿好且保持整洁但不是画面焦点；P01 回到小葫芦怀里；D02 积木仍在游戏垫；D01 小马桶在浴室背景。
- 空间连续性校验：浴室门在后侧，客厅游戏垫在前方，路线与第 4 页相反。
- 镜头切换理由：中景收束，保留生活感。
- 景别：中景。
- 视角与机位：从浴室门口看回客厅。
- 画面构图：小葫芦站在浴室门口或游戏垫边，身体放松，训练裤完整穿好但不被突出展示，妈妈蹲在旁边，积木在前景。
- 人物调度与动作真实性：孩子站稳，裤裤腰头平整；不刻意指私密部位。
- 画面细节与规整度：只保留必要道具，避免像奖励展示或裤裤展示。
- 色彩设计：暖黄与浅蓝回到平衡，苹果红点作为轻微呼应。
- 光线设计：自然光更明亮，情绪松动。
- 文字融入方案：左上墙面，1 行。
- 图片比例与像素尺寸：`3:4`，`1536x2048`。
- 无字插画图像提示词：3:4 vertical watercolor ending page, no text, view from the bathroom doorway back toward the living room play mat, C01 Xiao Hulu is fully dressed again in warm yellow top and light blue training pants with tiny apple pattern, holding P01 bunny plush and standing relaxed near the play mat, with a subtly proud and relaxed expression, as if noticing a body signal, large unfinished blocks still waiting, A01 mother kneels nearby with calm natural companionship, the small potty remains in the bathroom background, do not emphasize the pants as a victory display, no reward chart, no clapping, gentle sense of returning to play, bright safe home palette, low-detail wall area upper left for text.
- 负面提示词：no text, no pseudo-Chinese, no nudity, no exposed private parts, no pointing at crotch, no shame, no reward sticker, no prize, no clapping, no comparison, no extra fingers, no malformed anatomy, no clutter.
- 使用的参考图、模型、版本、种子或角色引用信息：AI 图像模型生成样张；v2 原始输出：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/raw/page-08-raw-v2.png`。
- 无字图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-08-clean-v2.png`
- 排版完成图片路径：未生成。
- 单页 QA：文本安全通过；v2 样张初检通过。背景小马桶已统一为奶油白主体 + 薄荷绿坐圈，小兔耳朵内侧统一为浅蓝；孩子轻松回到游戏垫，没有裤裤胜利展示、奖励贴纸或掌声。
- 单页状态：无字样张 v2 已生成，待人工终审。

## 封面提示词

Use case: illustration-story
Asset type: wordless cover concept for a preschool picturebook
Primary request: create a 3:4 vertical, wordless cover for the Chinese preschool picturebook "小肚肚叮一下"; do not draw any text.
Scene/backdrop: bright cozy home interior in daytime, living room play mat on the left with a few large safe blocks, bathroom doorway on the right with a child-sized cream potty with mint green seat visible inside, clean warm family environment.
Subject: C01 Xiao Hulu, a 2-3-year-old child with black short hair, round face, warm yellow short-sleeve top, light blue training pants with tiny apple pattern, light gray non-slip socks, one hand lightly touching the tummy as if noticing a tiny body bell, the other arm holding P01 cream bunny plush, standing between the unfinished blocks and the bathroom route; A01 mother with deep brown low ponytail, cream cotton-linen shirt and light olive home pants kneels at child height nearby with an open gentle hand, waiting rather than pushing.
Style/medium: warm watercolor and colored pencil linework, light paper grain, rounded preschool picturebook proportions, simple clean shapes.
Composition/framing: Xiao Hulu stands between play mat and bathroom doorway, showing both the unfinished play and the route from play to potty; small potty is friendly but secondary; leave a natural low-detail title area in the upper wall; no text, no labels, no bathroom signs.
Lighting/mood: soft natural daylight, calm, clean, supportive, not clinical.
Color palette: cream white, light wood, soft mint green, warm yellow, light blue, tiny apple red accent.
Constraints: no toilet use shown on the cover; child is fully dressed; mother is supportive and low, not pulling or rushing; keep living room left and bathroom right.
Avoid: no text, no pseudo-Chinese, no letters, no nudity, no exposed private parts, no urine, no toilet contents, no dirty bathroom, no public restroom, no shaming, no reward chart, no clapping, no extra fingers, no missing fingers, no malformed hands, no duplicated people, no changed outfit, no random decorative clutter, no plastic skin.

## 9. 全书质量审计

### 9.1 故事与文字 QA

- 单一核心主题：通过，围绕“听见身体叮一下后坐小马桶”。
- 年龄适配和字数：通过，每页 5-7 个汉字，适合 2-3 岁朗读。
- 儿童视角：通过，全部来自玩、肚肚提示、舍不得停下、抱小兔走、坐一坐等一等、身体轻松等具体经验。
- 情绪接纳与选择权：通过，孩子可以停一停、保留不想停下玩的感受、抱小兔、慢慢走、坐一小会儿、等一等。
- 是否存在催促、比较、羞辱、条件式奖励或说教：无。
- 重复结构是否每次推进：通过，“叮一下”作为身体信号钩子，第 2、3、8 页形成记忆闭环。
- 出声朗读检查：通过，短句自然。
- 结尾是否允许慢慢来并避免价值评判：通过，没有写“以后再也不尿裤子”。

### 9.2 跨页连续性 QA

- 角色脸型、发型、服装、鞋袜和身高关系：通过，8 页 v2 初检整体保持小葫芦黑色短发、暖黄色上衣、浅蓝训练裤/隐私遮挡处理和浅灰袜；妈妈低马尾、奶油色上衣、橄榄绿裤装保持一致。
- 固定配角人数与身份：通过，无配角。
- 道具颜色、大小、位置和持握状态：通过，小兔、积木、小马桶和脚凳在 8 页中承担连续锚点；小马桶保持奶油白主体与薄荷绿坐圈。
- 门、游戏垫、浴室、小马桶和脚凳位置：通过，客厅左、浴室右的路线在第 1-5 页清楚，第 8 页完成回到游戏垫的空间闭环。
- 镜头轴线、行动方向和光源：通过，客厅左、浴室右。
- 色板、线条、颗粒和人物比例：通过，整体为明亮水彩和彩铅线条，未出现明显跨页风格跳变。
- 画幅、像素尺寸和页码命名：通过，封面和 8 页内页 v2 均统一 `3:4` 和 `1536x2048`。

### 9.3 AI 瑕疵审计

- P0 问题及重做页码：封面 + 8 页 v2 初检未见 P0。
- P1 问题及修正页码：暂无必须重做项。第 6 页已由 v1 的“穿着训练裤坐马桶”误读修正为隐私遮挡式如厕尝试画面；第 6/7 页仍建议正式排版前人工终审隐私安全。
- P2 已记录差异：全书内页 v2 原始输出为图像模型默认尺寸，均已等比规范化为 `1536x2048`；v1 文件保留作比较。
- 整本联系表检查结果：8 页无字内页 v2 已完成初检；整本缩略联系表仍未生成。
- 最终可交付结论：封面 + 8 页无字样张 v2 已可供方向确认，可进入全书联系表、后期文字排版和 PDF/PPT 导出前复核。

## 10. 给家长的文字

- 这个故事想让孩子感受到什么：尿尿来之前，身体会像小铃铛一样“叮一下”；听见提示后，即使还想玩，也可以抱着小兔慢慢去小马桶坐一坐。
- 共读提醒：不要用故事催孩子“必须不尿裤子”。如厕训练会有反复，尿湿不是羞耻，也不是失败。
- 亲子互动：
  - 读第 2 页时，可以和孩子一起轻轻碰肚肚，说“我听一听”。
  - 读第 3 页时，可以问：“积木还没搭完，小葫芦想先做什么？”
  - 读第 4 页时，可以一起做抱小兔、慢慢走的小步子。
  - 读第 6 页时，可以说“坐一小会儿，没来也可以起来”。
  - 读第 8 页时，可以和孩子一起说：“我听见啦。”
- 可使用的支持性语言：
  - “你觉得尿尿来了吗？我们去看看。”
  - “慢慢走，我在旁边。”
  - “没来没关系，等身体再告诉你。”
  - “裤裤湿了也没关系，我们换一条。”
- 不建议使用的语言：
  - “怎么又尿裤子了？”
  - “快点憋住。”
  - “坐好了才是乖孩子。”
  - “你看别人都不用换裤子。”
- 适合幼儿年龄：2-3 岁，2-4 岁可由主要照顾者亲子共读。

## 11. 交付准备

- 故事包文本路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/story/story-package.md`
- 逐页脚本路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/story/page-script.md`
- 家长指南路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/story/parent-guide.md`
- 角色圣经路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/bible/character-bible.md`
- 环境地图路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/bible/environment-map.md`
- 色板与风格圣经路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/bible/color-and-style-bible.md`
- 连续性矩阵路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/bible/continuity-matrix.md`
- 整本缩略联系表路径：未生成。
- 无字封面图片路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/cover-clean-v2.png`
- 无字内页图片路径：第 1 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-01-clean-v2.png`；第 2 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-02-clean-v2.png`；第 3 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-03-clean-v2.png`；第 4 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-04-clean-v2.png`；第 5 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-05-clean-v2.png`；第 6 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-06-clean-v2.png`；第 7 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-07-clean-v2.png`；第 8 页 `outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-08-clean-v2.png`。
- 排版完成封面路径：未生成。
- 排版完成内页路径：未生成。
- 可编辑排版源文件路径：未生成。
- 故事与文字 QA 路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/qa/story-and-text-qa.md`
- 视觉连续性 QA 路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/qa/visual-consistency-qa.md`
- AI 瑕疵审计路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/qa/ai-artifact-audit.md`
- 四张关键样张 v2 精修记录路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/qa/key-sample-v2-refinement.md`
- 剩余页 v2 生成记录路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/qa/remaining-pages-v2-generation.md`
- 导出文件路径：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/export/`
- 固定输出目录：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/`
