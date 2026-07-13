# 《被窝里的晚安信》逐页脚本与无字插画提示词

## 全书生成锁定

- 画布：`1536×2048`、3:4 竖版、全部无字 `clean artwork`。
- 参考图：已生成 `artwork/reference/character-sheet.png` 与 `artwork/reference/environment-sheet.png`，内页均复用二者。
- 共通视觉底稿：当代中文绘本，哑光干刷水粉平涂与少量彩铅轮廓，轻微自然纸感，真实但不杂乱的现代儿童卧室；冷调雾蓝、云白、灰紫与鼠尾草绿为主，砖珊瑚只作小面积信封/发夹强调；不泛黄、不复古、不 3D。
- C01 锁定：3-4 岁团团，浅暖肤色、下巴长度深黑棕短发和轻直刘海、**画面自身左侧**一枚砖珊瑚布发夹；烟青绿圆领长袖睡衣、云白滚边、蓝灰睡裤、赤脚。
- A01 锁定：妈妈，深棕低发髻，雾蓝针织开衫、云白家居上衣、灰蓝长裤、深灰蓝袜；必须在团团视线高度回应。
- P01 锁定：米白棉布小兔，薄荷绿内耳，深灰刺绣眼。
- D01/D02 锁定：云白无字方形折纸卡 + 砖珊瑚无字小信封；完成后的卡仅有稚拙蓝色小手和三个色点，绝不出现任何文字或符号。

### 共通负面提示词

```text
no readable text, no Chinese characters, no letters, no logos, no watermark, no pseudo-text; no nightlight, no door-slit light, no stars, no moon, no celestial motifs, no yellow or amber cast, no sepia, no vintage paper filter, no glitter; no coercion, no shaming, no adult looming over child, no forced hug, no reward ceremony; no extra fingers, malformed hands, extra limbs, duplicated people, floating objects, inconsistent face, inconsistent outfit, hairstyle change, plastic skin, identical smiles, warped room perspective, decorative clutter
```

## 封面

- 封面中心意思：被窝里仍可有孩子自己选择的连接；团团把无字晚安信放在枕边，妈妈远处读书，不剧透妈妈按约定珍惜这封信的后续。
- 出场角色锁定：C01 团团、A01 妈妈（客厅背景小比例）、P01 小兔、D01/D02。
- 构图与光线：卧室前景的团团坐在画面下部偏右，枕边信封为叙事焦点；远景客厅的妈妈是小比例、非主角。床保持左侧，窗桌在右后。中性夜晚室内光，左上窗帘附近留 18% 自然低细节标题区。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: clean text-free portrait preschool picture-book cover, 1536x2048. A 3-4 year old Chinese child, C01 Tuantuan, with chin-length dark brown-black bob, short straight bangs, a small brick-coral fabric hair clip on her own left side, wearing a muted teal-green pajama top with cloud-white trim and blue-gray pajama pants, barefoot. She sits gently on the right side of her small bed, holding a cream cloth bunny with pale mint inner ears. A single small brick-coral envelope and a square off-white folded card with a simple blue child hand drawing rest by the pillow. In the distant connected living room, her mother in a mist-blue cardigan sits quietly reading an unmarked dark blue book, small and secondary. Bed stays left, window desk right-rear; modern lived-in Chinese home, matte dry-gouache fills and sparse colored-pencil lines, cool mist-blue, cloud-white, gray-lavender, sage palette with limited coral accent, peaceful connection without yellow light. Reserve a natural low-detail area in the upper left for later title, but render absolutely no text.
```

- 标题与署名后期方案：左上书名 `被窝里的\n晚安信`；左下 `图/文：小葫芦`；均为可编辑文字层。
- 图片路径：无字 `artwork/clean/cover-clean.png`；排版 `artwork/composited/cover-final.png`；状态：已完成并通过最终复检。

---

## 第 01 页

- 本页中心意思：团团在熟悉的睡前流程里走向自己的小床。
- 本页故事文字：夜里，团团洗好脸，抱着小兔。
- 汉字数：13。
- 朗读检查：两处自然停顿，具体、顺口，无评价性语言。
- 情绪变化：熟悉 → 平静。
- 儿童主体性：团团自己抱着小兔走向床；无额外推动。
- 成人/同伴支持：无。
- 文字与画面分工：文字只交代睡前动作；画面补足床、窗桌、略歪地毯和兔子的归属。
- 页间推进 / 视觉新增量：建立卧室主空间、服装、玩偶和夜色；下一页让孩子注意到画桌上的纸。
- 出场角色锁定：C01 团团 1 名，烟青睡衣、赤脚；P01 小兔 1 个，双手抱在胸前。
- 道具状态：D01/D02 与三支蜡笔在窗桌上，尚未被拿起；P01 在团团手中。
- 空间连续性校验：主机位东南向西北，床在左、窗桌在右后、书架在后；团团从右侧画桌方向走向床。
- 景别 / 机位：远中景、平视。
- 画面构图与动作真实性：团团在下部中右，脚踩地毯边缘、身体略向床倾，双手真实托住兔子；左上窗帘邻近区为正文低细节区。
- 色彩 / 光线：雾蓝墙、云白床品、烟青睡衣；上方偏右中性暖白漫反射光，不泛黄。
- 文字融入方案：左上，约 13% 画面，后期深可可色两行以内，四周留 92px 安全边距。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: text-free 3:4 portrait interior page, 1536x2048. C01 Tuantuan, locked appearance and teal pajamas, barefoot, walks from the right toward her small bed on the left after washing her face, holding P01 cream cloth bunny with pale mint inner ears against her chest. Establish the fixed bedroom: bed left, low bookcase on rear wall, window and small desk on right-rear; one off-white blank folded card, one brick-coral envelope and exactly three short crayons rest on the desk. A slightly rumpled blue-gray rug shows lived-in use. Matte dry gouache and sparse colored-pencil contours, cool clean evening interior, natural anatomy. Leave the upper-left curtain area low detail for later text. No words anywhere.
```

- 参考与输出：角色/环境参考图已生成；无字 `artwork/clean/page-01-clean.png`；排版 `artwork/composited/page-01-final.png`。
- 单页 QA：安全、人物数量、兔子、床左窗右、双脚着地、无文字均通过；最终复检通过。

## 第 02 页

- 本页中心意思：团团看见小床边可用来表达心意的小纸和蜡笔。
- 本页故事文字：小床边，有蜡笔和小纸。
- 汉字数：10。
- 朗读检查：短促、可指认，适合 3-4 岁。
- 情绪变化：平静 → 好奇。
- 儿童主体性：团团自己看向纸和蜡笔；不要求她立刻做什么。
- 成人/同伴支持：无。
- 文字与画面分工：文字点出物件；画面表现团团的目光、兔子夹在臂弯和桌上无字物件。
- 页间推进 / 视觉新增量：从走向床转为发现可选择的表达材料；为第 03 页的犹豫留出停顿。
- 出场角色锁定：C01 团团 1 名、P01 小兔 1 个；A01 不出场。
- 道具状态：D01 云白空白卡、D02 珊瑚信封、三支蜡笔仍在窗桌；P01 在团团左臂内侧。
- 空间连续性校验：同一卧室，床仍在左；轻俯镜头保留床角、窗桌与书架，团团坐到床沿朝右后看。
- 景别 / 机位：中景、轻微俯视。
- 画面构图与动作真实性：团团坐稳床沿，脚尖可碰地或自然悬于床边；右手轻搭被褥，眼神指向桌上物件，不出现拿不住的漂浮纸。
- 色彩 / 光线：与第 01 页一致，桌面云白卡和少量珊瑚信封成为细小焦点。
- 文字融入方案：右上墙面，约 12% 画面，两行以内。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: text-free 3:4 portrait interior page, 1536x2048. In the fixed bedroom, C01 Tuantuan sits naturally on the left-side bed edge, cream bunny tucked in her left arm, and looks with mild curiosity toward the right-rear desk. On that desk are exactly one blank off-white folded card, one brick-coral envelope, and exactly three short crayons; no writing, symbols, labels or logos. Preserve bed left, window desk right-rear, rear bookcase. Gentle slightly overhead medium shot, matte dry gouache, sparse colored-pencil edgework, cool mist-blue and cloud-white palette with small coral accent, genuine thoughtful expression not a standard smile. Keep the upper-right wall low detail for later text.
```

- 参考与输出：无字 `artwork/clean/page-02-clean.png`；排版 `artwork/composited/page-02-final.png`；状态：已完成并通过最终复检。

## 第 03 页

- 本页中心意思：上床前的停顿被看见，而不是被催过去。
- 本页故事文字：躺下时，团团把小兔抱紧了。
- 汉字数：13。
- 朗读检查：节奏自然，`抱紧了`有明确可见动作。
- 情绪变化：好奇 → 犹豫。
- 儿童主体性：团团用抱紧小兔表达身体信号；无需解释或纠正。
- 成人/同伴支持：A01 妈妈蹲到同高，安静看见团团，不伸手拉她躺下。
- 文字与画面分工：文字说明身体信号；画面表现妈妈保持可接受距离、开放等待。
- 页间推进 / 视觉新增量：第一次亲子同框；由发现纸转为说出需要前的安全停顿。
- 出场角色锁定：C01 团团、A01 妈妈、P01 小兔各 1；团团仍为烟青睡衣，妈妈为雾蓝开衫。
- 道具状态：D01/D02、蜡笔留在右后窗桌；P01 被团团双手抱住。
- 空间连续性校验：团团在床沿，妈妈在床边地毯上蹲低，床左窗桌右的轴线不变。
- 景别 / 机位：近景、平视亲子反打。
- 画面构图与动作真实性：团团双肩略收、脚自然触地；妈妈双手放在膝上，身体朝孩子微倾，距离不贴近；右上为低细节文字区。
- 色彩 / 光线：略降低饱和度，但墙、床、人物仍清楚可读；不以黑暗制造害怕。
- 文字融入方案：右上墙面，12%-15%，深可可字。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: text-free 3:4 portrait preschool picture-book page, 1536x2048. Bedside intimate medium-close scene in the locked bedroom: C01 Tuantuan sits on the left bed edge and holds P01 cream bunny tightly with both hands, shoulders slightly drawn in, calm but hesitant rather than crying. A01 mother in the locked mist-blue cardigan crouches on the rug at child eye level a comfortable distance away, hands resting quietly on her knees, listening and not touching or directing. Keep card, coral envelope and three crayons on the right-rear desk, bed left and window desk right. Matte dry gouache, gentle cool interior light, natural hands and believable feet. Reserve low-detail upper-right wall area; absolutely no text.
```

- 参考与输出：无字 `artwork/clean/page-03-clean.png`；排版 `artwork/composited/page-03-final.png`；状态：已完成并通过最终复检。

## 第 04 页

- 本页中心意思：团团主动把“还想说晚安”的需要说出来。
- 本页故事文字：“我还想和妈妈说晚安。”
- 汉字数：10。
- 朗读检查：第一人称直接、短句可模仿，无成人腔。
- 情绪变化：犹豫 → 被听见。
- 儿童主体性：团团用自己的话表达需要。
- 成人/同伴支持：妈妈继续蹲低，用专注目光与开放手势回应，不替团团定义感受。
- 文字与画面分工：文字交给团团说；画面重点放在相互的视线、妈妈耐心等待和小兔在腿边。
- 页间推进 / 视觉新增量：从身体信号推进为语言表达；下一页才给选择，不抢在孩子说完前解决。
- 出场角色锁定：C01、A01、P01 各 1；D01/D02 仍在窗桌。
- 道具状态：P01 靠在团团腿边；纸、信封、蜡笔未移动。
- 空间连续性校验：同一床沿和地毯；亲子视线高度一致，保留后墙书架作反打锚点。
- 景别 / 机位：中景、与团团齐平的亲子反打。
- 画面构图与动作真实性：团团一只手轻触兔耳，另一只手放在被子上；妈妈掌心向上但不伸手拿走玩偶；右上留白。
- 色彩 / 光线：云白床品映出脸部，珊瑚发夹仍作为小焦点；中性漫反射光不变。
- 文字融入方案：右上低细节处，单行或两行，最大 15% 画面。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: clean text-free 3:4 portrait page, 1536x2048. Eye-level two-person medium shot in the fixed bedroom. C01 Tuantuan, still seated on the left bed edge in locked teal pajamas, looks toward A01 mother and speaks with a small earnest open mouth, one hand touching the cream bunny at her side. Mother remains crouched at the same height, calm focused face and one open palm, not touching or prompting. Preserve rear low bookcase and the right-rear desk holding one blank card, one coral envelope, three crayons. Emotional focus is the child being heard, not a smile or a hug. Matte dry gouache, sparse color-pencil linework, cool neutral palette, low-detail upper-right space for later Chinese text, no text in image.
```

- 参考与输出：无字 `artwork/clean/page-04-clean.png`；排版 `artwork/composited/page-04-final.png`；状态：已完成并通过最终复检。

## 第 05 页

- 本页中心意思：妈妈给出两种可选的小办法，团团仍能自己决定。
- 本页故事文字：妈妈问：“画信，还是坐一会儿？”
- 汉字数：13。
- 朗读检查：问句自然、没有催促；`还是`清楚给出选择。
- 情绪变化：被听见 → 有主意。
- 儿童主体性：选择权明确在团团手中；她可以画信，也可以先坐一会儿。
- 成人/同伴支持：妈妈问而不命令，身体保持低姿态和开放手势。
- 文字与画面分工：文字提供选择；画面表现两种选项对应的画桌和床沿，不把任何一种画成正确答案。
- 页间推进 / 视觉新增量：从表达需要推进为可退一步的支持；下一页团团自己指向画信。
- 出场角色锁定：C01、A01、P01 各 1；D01/D02 与三支蜡笔在窗桌。
- 道具状态：P01 在床边；D01/D02 未改变，蜡笔仍只有三支。
- 空间连续性校验：妈妈转到窗桌附近坐/蹲，团团仍面向桌子；保留床尾和窗帘，避免空间翻转。
- 景别 / 机位：中近景、与团团齐平。
- 画面构图与动作真实性：妈妈一手轻指画桌、另一手指向床边空位，不用手指逼近孩子；团团身体向桌子略转。
- 色彩 / 光线：青灰、云白基调不变，珊瑚信封与三支短蜡笔提供克制焦点。
- 文字融入方案：左上窗帘低细节区，约 16%，两行。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: clean text-free 3:4 portrait page, 1536x2048. In the locked bedroom, A01 mother sits or crouches beside the right-rear desk at child eye level, calmly offering two visible possibilities with a relaxed open gesture: the blank folded card and three crayons on the desk, and a clear comfortable space beside C01 Tuantuan on the left bed. C01 looks toward the desk, deciding for herself; cream bunny rests nearby on the bed. Do not make either option look like a reward. Bed left, window desk right, rear bookcase fixed. Contemporary dry gouache with sparse colored-pencil lines, cool clear interior light, natural hands. Reserve a soft low-detail upper-left curtain area for later text; no text or symbols.
```

- 参考与输出：无字 `artwork/clean/page-05-clean.png`；排版 `artwork/composited/page-05-final.png`；状态：已完成并通过最终复检。

## 第 06 页

- 本页中心意思：团团自己选定“画晚安信”这一个小步骤。
- 本页故事文字：团团说：“我想画晚安信。”
- 汉字数：11。
- 朗读检查：主动句、发音顺畅；`想画`是孩子可完成的小行动。
- 情绪变化：有主意 → 主动。
- 儿童主体性：团团明确选择并指向纸和蜡笔。
- 成人/同伴支持：妈妈在画面边缘耐心等待，不接过蜡笔、不替画。
- 文字与画面分工：文字说出决定；画面呈现团团伸手取蜡笔的起始动作。
- 页间推进 / 视觉新增量：选择不再停留在提问，转为孩子自己发起的动作；下一页进入手部特写。
- 出场角色锁定：C01 团团 1 名、A01 可见局部或不出镜、P01 小兔 1 个；D01/D02、三支蜡笔。
- 道具状态：D01 云白卡在桌面正中，D02 珊瑚信封在其右侧，三支蜡笔在卡的上侧；团团右手去拿蓝色蜡笔。
- 空间连续性校验：机位轻俯，保留床尾和窗桌边缘；团团从床沿移动到右后画桌，行动方向合理。
- 景别 / 机位：中景、轻微俯视。
- 画面构图与动作真实性：团团一只脚踩地、一只脚微向画桌跨出；右手拇指和手指真实握住短蜡笔，左手轻压卡纸边角。
- 色彩 / 光线：云白卡成为明亮焦点，蓝色蜡笔与珊瑚信封呼应色板；上方中性光保持一致。
- 文字融入方案：左上墙面，12%-15%，一到两行。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: text-free 3:4 portrait preschool picture-book page, 1536x2048. Slight overhead medium scene in the locked bedroom: C01 Tuantuan has moved to the right-rear desk and independently reaches for exactly one short slate-blue crayon with her right hand while her left hand steadies one blank off-white folded card. The single brick-coral envelope lies to the card’s right, with the other two short crayons above it. P01 cream bunny rests at the nearby bed edge. A01 mother may be only a soft cropped knee/hand at a respectful distance, waiting and not taking over. Preserve bed left and window desk right. Matte dry gouache, sparse colored-pencil contours, natural small hands and grounded feet, cool blue-gray and cloud-white palette. Leave an upper-left low-detail wall zone; no text, no symbols, no readable markings.
```

- 参考与输出：无字 `artwork/clean/page-06-clean.png`；排版 `artwork/composited/page-06-final.png`；状态：已完成并通过最终复检。

## 第 07 页

- 本页中心意思：团团把一只小手和一张小床画进信里。
- 本页故事文字：小手、小床，画进信里。
- 汉字数：10。
- 朗读检查：重复节奏清楚，画面可直接指认。
- 情绪变化：主动 → 专注。
- 儿童主体性：团团自己画出图案；无需写字或画得像。
- 成人/同伴支持：无额外推动；妈妈不在特写中替画。
- 文字与画面分工：文字概括两项图案；画面展示一只正在画的手、三支固定蜡笔和无字卡。
- 页间推进 / 视觉新增量：从“拿起”到“完成”，为把信交给妈妈做好准备。
- 出场角色锁定：仅 C01 双手局部；P01 可在画桌边缘模糊出现；A01 不出镜。
- 道具状态：D01 上有简单蓝色小手和三个色点；D02 信封在右侧等待；三支蜡笔仍为蓝、珊瑚、鼠尾草绿。
- 空间连续性校验：孩子视角特写必须保留木桌边缘、睡衣衣袖或窗桌一角，不让物件悬浮。
- 景别 / 机位：特写、孩子视角俯视。
- 画面构图与动作真实性：团团右手握珊瑚蜡笔在纸上画一条弧线；左手指尖压住纸边；手指数量、手腕和桌面接触必须清楚。
- 色彩 / 光线：卡纸云白、蓝手形、珊瑚点、鼠尾草点构成唯一高注意力区域，背景减细节。
- 文字融入方案：上方桌面低细节区约 14%，后期两行以内，不遮挡手、卡或蜡笔。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: clean text-free 3:4 portrait close-up, 1536x2048. Child-eye slightly top-down close-up of C01 Tuantuan’s small natural hands at the fixed wooden desk: her right hand uses a short brick-coral crayon to make a simple childlike drawing on one off-white folded card; the finished drawing must show only one simple blue hand shape and exactly three small colored dots, never letters, numbers, or symbols. Her left fingertips gently hold the card flat. Exactly three short crayons—slate-blue, brick-coral, sage-green—and one coral envelope are visible. A soft corner of teal pajama sleeve and wood desk edge anchor the space. Matte dry gouache and sparse colored-pencil contour, highly believable anatomy, no extra fingers, no text. Reserve a low-detail top edge for later text without blocking the drawing hand.
```

- 参考与输出：无字 `artwork/clean/page-07-clean.png`；排版 `artwork/composited/page-07-final.png`；状态：已完成并通过最终复检。

## 第 08 页

- 本页中心意思：团团把自己画好的晚安信交给妈妈，并说出想把它放在哪里。
- 本页故事文字：“请放在你的书边。”团团说。
- 汉字数：12。
- 朗读检查：主动请求、短句清楚；不把照料者变成任务执行者。
- 情绪变化：专注 → 放心。
- 儿童主体性：团团决定信交给谁、要放在哪里；她用自己的话提出约定。
- 成人/同伴支持：妈妈保持同高、张开双手接信，不抢走、不追问、不增加条件。
- 文字与画面分工：文字交给团团表达；画面突出两人之间真实的递交动作。
- 页间推进 / 视觉新增量：从画纸特写回到亲子中景，信从团团手中移动到妈妈手中；下一页才展示妈妈执行约定。
- 出场角色锁定：C01、A01、P01、D01、D02 各 1；D03 不出镜。
- 道具状态：D01 装入 D02；团团双手递出，妈妈双手接住；P01 在团团左臂内侧。
- 空间连续性校验：仍在卧室，床在左、窗桌在右后；不可提前切到客厅。
- 景别 / 机位：中景、平视。
- 画面构图与动作真实性：团团与妈妈同高或近同高，四只手共同稳住一封信，手指、手腕和遮挡清楚；不拥抱、不拍手。
- 色彩 / 光线：中性卧室光，云白卡与珊瑚信封成为克制焦点；左上窗帘留字区。
- 文字融入方案：左上窗帘旁，约 15%，两行以内。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: clean text-free 3:4 portrait picture-book page, 1536x2048. Eye-level medium scene in the fixed bedroom: C01 Tuantuan in locked teal pajamas holds one finished off-white folded card inside one brick-coral envelope, and deliberately places it into A01 mother’s two open hands. Mother wears the locked mist-blue cardigan and crouches at child eye level, receiving rather than reaching. P01 cream bunny stays in Tuantuan’s left arm. Keep bed left, window desk right-rear and rear bookcase. Four hands must be anatomically believable and truly support one envelope; no hug, no applause, no adult pressure. Matte dry gouache with sparse colored-pencil contours, cool neutral interior light, low-detail upper-left curtain zone for later text. No words, letters, symbols, labels or logos.
```

- 参考与输出：无字 `artwork/clean/page-08-clean.png`；排版 `artwork/composited/page-08-final.png`；状态：已完成并通过最终复检。

## 第 09 页

- 本页中心意思：妈妈按团团的约定，把晚安信放到自己的书边。
- 本页故事文字：妈妈把信放到书边。
- 汉字数：9。
- 朗读检查：动作清楚，长度适合停顿后的翻页。
- 情绪变化：放心 → 被连接。
- 儿童主体性：团团上一页提出的位置被可靠执行；她不需出镜来证明或接受表扬。
- 成人/同伴支持：妈妈把唯一一封信轻放在无字深蓝书边，不再增加条件或指令。
- 文字与画面分工：文字说明成人动作；画面以单人、信和书表现“我会做到”的可见回应。
- 页间推进 / 视觉新增量：从卧室亲子交接切至相邻客厅；珊瑚信封和深蓝书成为跨空间锚点，下一页回到孩子自己的床。
- 出场角色锁定：A01 妈妈 1 名；C01、P01 不出镜；D01、D02、D03 各 1。
- 道具状态：D01 装入 D02；妈妈放在小边几深蓝书左侧，信封正面朝上但无字；D03 平放。
- 空间连续性校验：这是唯一客厅页，不可误画为卧室；单人椅在左、边几在右，窗帘仍是雾蓝灰，但床不出现。
- 景别 / 机位：远中景、客厅侧视。
- 画面构图与动作真实性：妈妈站或坐在单人椅边，右手把信封放下，左手自然扶书页或椅背；信封与边几真实接触，不能漂浮。
- 色彩 / 光线：中性云白墙、雾蓝开衫、深石板蓝书，珊瑚信封是唯一小面积重点；上方偏左柔和光。
- 文字融入方案：右上云白墙面，约 15%，一行或两行。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: clean text-free 3:4 portrait picture-book page, 1536x2048. Quiet side-view medium-wide scene in the fixed adjacent living room, not a bedroom. A01 mother with dark low bun, mist-blue cardigan, gray-blue home trousers and dark socks calmly places one single brick-coral envelope containing the off-white child drawing next to the left side of one unmarked dark slate-blue hardcover book on a small side table. A simple armchair is on the left, side table on the right, a softly rumpled rug and blue-gray curtain give lived-in realism. Her hand makes real contact with the table and envelope. No child, no bunny, no reward or applause. Matte dry gouache with sparse colored-pencil contour, cool neutral indoor light, upper-right cloud-white wall left low detail for later text. Absolutely no writing, book title, letters or logos.
```

- 参考与输出：无字 `artwork/clean/page-09-clean.png`；排版 `artwork/composited/page-09-final.png`；状态：已完成并通过最终复检。

## 第 10 页

- 本页中心意思：团团带着知道约定已做到的安心，选择先自己躺一会儿。
- 本页故事文字：团团拉好小被子：“我先躺一会儿。”
- 汉字数：15。
- 朗读检查：一句动作、一句主动表达，停顿自然；不要求“立刻睡着”。
- 情绪变化：被连接 → 安静。
- 儿童主体性：团团自己拉好被子并说出可行的小目标。
- 成人/同伴支持：本页不出现成人；支持已经通过上一页的可靠执行发生。
- 文字与画面分工：文字给出团团的选择；画面表现孩子独处但不孤立，兔子、固定房间与可读夜色提供安全场。
- 页间推进 / 视觉新增量：从客厅约定回到卧室；镜头由成人单人切换为团团自己的身体动作，温柔收束故事。
- 出场角色锁定：C01 团团 1 名、P01 小兔 1 个；A01、D01、D02、D03 均不出镜。
- 道具状态：P01 在枕头旁，耳朵朝上；信与书只在客厅，不可凭空回到卧室。
- 空间连续性校验：床左、窗帘右后、书架后墙不变；由床侧平视拍摄，团团朝枕头方向躺下，脚/被褥不可反向。
- 景别 / 机位：中景、床侧平视。
- 画面构图与动作真实性：团团侧躺，双手把雾蓝被子拉到肩下，不遮脸；一条腿在被褥下形成自然重心，小兔靠在手肘旁。
- 色彩 / 光线：低饱和石板蓝、灰紫和云白夜色；明暗降低但面部、床、兔子仍可辨；无小夜灯、门缝光、星月意象。
- 文字融入方案：左上窗帘低细节区，约 16%，正文两行，不遮挡脸或拉被子的手。
- 无字插画提示词：

```text
Use case: illustration-story. Asset type: clean text-free 3:4 portrait preschool picture-book page, 1536x2048. Calm bedside eye-level medium view in the same locked bedroom at readable blue-gray night ambience. C01 Tuantuan in locked teal pajamas lies naturally on her side in the left bed and independently pulls the muted blue quilt up to just below her shoulders with both believable hands. P01 cream bunny with pale mint ears rests beside her elbow on the cloud-white pillow, ears up. No mother, no card, no envelope, no book in this room. Keep the fixed bed left, blue-gray curtain right-rear and rear bookcase, with no moon, stars, lamp or door-slit light. Matte dry gouache, sparse colored-pencil lines, gentle quiet expression with eyes beginning to relax, not a performance smile. Reserve low-detail upper-left curtain area for later Chinese text; no text.
```

- 参考与输出：无字 `artwork/clean/page-10-clean.png`；排版 `artwork/composited/page-10-final.png`；状态：已完成并通过最终复检。

## 逐页生成顺序与质检门槛

1. 角色/道具参考表 → 环境参考图 → 封面、04、07、09 四类关键页样张。
2. 样张通过角色、空间、色彩、文字区及手部检查后，再生成 01-10 全部无字内页。
3. 任一页出现伪中文、主要角色换脸/换装、人数错误、多肢缺肢、手未接触信封、床窗翻转或黄色夜灯意象，按 P0 重做。
4. 完成 clean 图后，才依据 `layout/text-layout.json` 后期叠加中文，不让图像模型生成文字。
