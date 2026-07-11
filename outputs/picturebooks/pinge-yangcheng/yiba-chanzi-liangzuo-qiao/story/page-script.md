# 《一把铲子，两座桥》逐页脚本

## 全书锁定

- 系列：品格养成系列
- 主题：分享
- 主要年龄：3-4 岁
- 故事页数：10 页，不含封面
- 画布：`1536×2048`，3:4 竖版
- 文字安全边距：至少 6%
- 角色：C01-小米、C02-乐乐
- 场景：上午 10 点的幼儿园沙池
- 实际图片：未生成

## 全局无字插画提示词

每一页的实际调用提示词必须由“全局提示词 + 本页追加提示词”组成，不得省略全局约束。

```text
Use case: illustration-story
Asset type: clean preschool picturebook artwork, exact 3:4 portrait canvas, 1536x2048
Input images: Image 1 is the locked C01 Xiaomi character reference; Image 2 is the locked C02 Lele character reference; Image 3 is the locked kindergarten sandpit environment and style reference.
Scene/backdrop: a real Chinese kindergarten sandpit at about 10 a.m.; pale blue rounded metal fence on the north side, muted green shrubs behind it, one tree on the west/left side, one low wooden bench on the east/right side, rounded rubber sandpit border on the south side.
Characters: preserve the exact faces, hair, proportions, outfits, shoes, height relationship, and identifying details from the character references. Xiaomi stays on the left side of the action axis; Lele stays on the right side.
Style/medium: transparent watercolor washes with light colored-pencil contours, subtle natural paper variation, moderate-to-simple detail, believable preschool body weight and hand contact, hand-drawn irregularity without visual noise.
Lighting/mood: clear natural morning light from upper right toward lower left, soft transparent shadows, safe and emotionally observant, no dramatic spotlight.
Color palette: clear pale blue, muted leaf green, natural sand beige, Xiaomi coral red and gray-blue, Lele blue-green and mustard khaki, coral-red shovel and sky-blue bucket as controlled accents.
Text: no text of any kind in the generated artwork.
Constraints: preserve the left-right action axis, fixed fence/tree/bench positions, realistic sand contact, natural clothing folds, lightly sandy knees and shoe edges, a natural low-detail text area in the specified position, at least 6 percent safe margin around faces, hands, feet, tool exchange, and bridge connection.
Avoid: mature or child-inappropriate content, violence, scary imagery, coercion, shaming, grabbing, throwing sand, dangerous behavior, extra fingers, missing fingers, fused hands, extra limbs, malformed anatomy, duplicated people, face drift, outfit changes, hairstyle changes, height drift, floating bodies, impossible grip, warped perspective, flipped environment, duplicated shovel or bucket, premature bridge connection, readable signs, letters, numbers, pseudo-Chinese, logos, watermark, plastic skin, identical smiles, yellow filter, orange skin, excessive glow, random stars, decorative clutter, template-like symmetry.
```

## 封面

- 中心意思：两名孩子和两座尚未连接的桥，一眼呈现“两个需要正在靠近”
- 角色：C01 左、C02 右
- 道具：小米持 D01；D02 位于乐乐旁
- 构图：两座未完成沙桥指向中央小缺口，不剧透完成结局
- 文字区：上方 22% 自然低细节天空与围栏；右下保留署名区
- 无字图片：`artwork/clean/cover-clean.png`
- 带字图片：`artwork/composited/cover-final.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: clean front cover artwork. Xiaomi is on the left beside S01, holding the coral-red shovel; Lele is on the right beside S02 with the sky-blue bucket. The two unfinished sand bridges angle toward a visible center gap but are not connected. Their eyes and body directions gently lead toward the gap. Xiaomi looks focused with a small softening, Lele looks hopeful and patient; neither has a broad standard smile. Keep the upper 22 percent as a natural pale-sky and low-detail fence title area and reserve a small lower-right credit area. Do not show the ending and do not generate any text.
```

## 第 1 页

- 正文：小米在沙池里，挖一座弯弯的小桥。
- 汉字数：14
- 中心意思：小米沉浸在自己的桥计划里
- 情绪：平静 → 专注
- 儿童主体性：小米自主决定玩法和节奏
- 画面新增量：建立沙池、角色、红铲子和 S01
- 出场：C01；C02 不出场
- 道具：D01 由小米持握；D02 不出现；S01 半成
- 景别 / 机位：远中景，儿童平视，主机位南侧
- 构图：小米在左下工作，树与围栏提供锚点，中间留出桥延伸方向
- 文字区：左上，1-2 行
- 色彩 / 光线：清浅蓝绿与自然沙色平衡，右上自然光
- 朗读检查：顺口；一个动作；无说教
- 无字图片：`artwork/clean/page-01-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 1 establishing medium-wide child-eye view. Xiaomi alone on the left is absorbed in digging S01 with the red shovel; S01 is only half formed and points toward the empty center. Lele and the blue bucket are absent. Show the fixed fence and west tree, with the east bench secondary. Natural upper-left text area. Her posture shows concentration and ownership without posing for the viewer.
```

## 第 2 页

- 正文：乐乐也想挖。他蹲下来看看。
- 汉字数：11
- 中心意思：乐乐先观察，再靠近表达愿望
- 情绪：好奇 → 期待
- 儿童主体性：乐乐没有抢，先蹲下看
- 画面新增量：C02 从右侧入场，D02 出现
- 出场：C01 左、C02 右
- 道具：D01 仍由小米持握；D02 在乐乐右后方；S01 未变
- 景别 / 机位：中景，乐乐右肩后视角
- 构图：乐乐前景右、小米中景左，视线落到红铲子
- 文字区：右上，2 行
- 色彩 / 光线：延续第 1 页，保持开放感
- 朗读检查：顺口；因果清楚；不替孩子评价
- 无字图片：`artwork/clean/page-02-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 2 relationship medium view from just behind Lele's right shoulder. Lele enters from the right and crouches to look before asking; his blue bucket sits just behind his right side. Xiaomi remains left with the red shovel and unfinished S01. Both bodies remain on their locked sides. Natural upper-right text area, fence and east bench visible.
```

## 第 3 页

- 正文：小米把铲子收近一点：“我还在用。”
- 汉字数：13
- 中心意思：小米表达边界
- 情绪：专注 → 防守
- 儿童主体性：小米可以说自己还没有用完
- 画面新增量：手、铲柄、鞋尖与嘴角显出真实舍不得
- 出场：C01 主导；C02 可仅为右侧软边缘
- 道具：D01 收近身体；D02 不突出；S01 未变
- 景别 / 机位：近景，南侧平视
- 构图：小米左下，铲柄形成内收线，保留树或围栏锚点
- 文字区：左上，2 行
- 色彩 / 光线：轻微降饱和，不变暗
- 朗读检查：像孩子会说的话；无羞辱或成人腔
- 无字图片：`artwork/clean/page-03-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 3 emotional close view. Xiaomi remains on the left, drawing the shovel handle slightly closer to her body; her navy shoe toe presses gently into the sand, mouth corners tighten a little, shoulders are not aggressive. Lele is only a soft partial presence at the far right edge or just outside frame. Keep the first unfinished bridge direction and one tree-or-fence anchor visible. Natural upper-left low-detail text area. The emotion is protective hesitation, not anger, greed, or villainy.
```

## 第 4 页

- 正文：乐乐有一点点失望。
- 汉字数：8
- 中心意思：乐乐的愿望暂时没有实现
- 情绪：期待 → 失落
- 儿童主体性：乐乐可以失望，不必立刻表现懂事
- 画面新增量：肩膀垂下，手指在沙面画短线
- 出场：C02；C01 可不入画
- 道具：D02 在乐乐身侧；D01 画外仍归小米；S01 未变
- 景别 / 机位：近景，轻微俯视
- 构图：乐乐右侧偏下，长椅为锚点
- 文字区：右上，1 行
- 色彩 / 光线：全书最低饱和段，但保持儿童友好
- 朗读检查：具体、简短，不否定情绪
- 无字图片：`artwork/clean/page-04-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 4 quiet reaction close view. Lele is on the right with shoulders slightly lowered, using one finger to draw a short line in the sand; he looks mildly disappointed, not devastated and not instantly cheerful. The blue bucket remains beside him. Xiaomi and the shovel may stay outside frame. Preserve the east bench as a spatial anchor and leave a natural upper-right text area.
```

## 第 5 页

- 正文：“你先帮我装沙，好吗？”
- 汉字数：8
- 中心意思：小米提出一个不必立刻放手的共同办法
- 情绪：防守 → 松动
- 儿童主体性：提议带有“好吗”，乐乐可以选择回应
- 同伴支持：双方的需要都获得位置
- 画面新增量：D02 从旁边进入两人共同视线
- 出场：C01 左、C02 右
- 道具：D01 小米持握；D02 在两人之间偏右；S01 待完成
- 景别 / 机位：双人中景，平视
- 构图：两人之间留有呼吸空间，视线连接蓝桶
- 文字区：左上，1 行
- 色彩 / 光线：自然绿增加，情绪开始松动
- 朗读检查：邀请式、口语化，无命令感
- 无字图片：`artwork/clean/page-05-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 5 balanced two-child medium view. Xiaomi on the left still holds the shovel but looks toward the blue bucket and makes a small open invitation gesture. Lele on the right listens; the bucket sits between them but slightly right. S01 is still unfinished. Their expressions show cautious possibility, not instant harmony. Natural upper-left text area.
```

## 第 6 页

- 正文：一铲，一桶。第一座桥慢慢长高。
- 汉字数：12
- 中心意思：两人用不同工具完成第一座桥
- 情绪：试探 → 合作
- 儿童主体性：乐乐选择参与装沙，小米继续完成当前计划
- 画面新增量：铲沙和倒沙形成节奏，S01 完成
- 出场：C01 左、C02 右
- 道具：D01 小米铲沙；D02 乐乐倒沙；S01 完成但粗糙
- 景别 / 机位：中近景，轻微俯视，单一构图
- 构图：前景放大工具真实接触，同时保留两人和桥
- 文字区：右上，2 行
- 色彩 / 光线：沙色略明亮，右上主光不变
- 朗读检查：重复有节奏，第二句带来真实推进
- 无字图片：`artwork/clean/page-06-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 6 medium-close view with a slight overhead angle. In the foreground, Xiaomi's red shovel makes real contact with sand while Lele tips the blue bucket so sand actually lands on S01; both full torsos and the rough first bridge remain readable in one single composition. S01 becomes complete but naturally uneven. Keep upper-right text space and preserve the fixed fence.
```

## 第 7 页

- 正文：小米停了一小会儿：“挖好啦，轮到你。”
- 汉字数：14
- 中心意思：小米在犹豫之后完成交接
- 情绪：犹豫 → 愿意
- 儿童主体性：分享不是瞬间服从，而是自己决定现在可以交接
- 画面新增量：两只手与铲柄形成关键动作
- 出场：C01 左、C02 右
- 道具：D01 柄朝右交接；D02 在右侧地面；S01 完成，S02 未开始
- 景别 / 机位：手部与表情近景
- 构图：D01 居中，双方脸与手完整可读
- 文字区：右上，2 行
- 色彩 / 光线：珊瑚红成为视觉焦点
- 朗读检查：停顿自然，保留“不完美懂事”的小拍子
- 无字图片：`artwork/clean/page-07-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 7 key handoff close view. Xiaomi on the left has paused for one small beat and turns the shovel handle toward Lele on the right. Lele reaches with one open hand; the handle, both hands, and both natural expressions are clearly visible, with correct fingers and believable distance. S01 is complete but rough, S02 has not started. The blue bucket rests on the right. Keep a natural upper-right low-detail text area. Show willingness after hesitation, not a ceremonial or overly perfect exchange.
```

## 第 8 页

- 正文：哗啦！桥边滑下来一点。
- 汉字数：9
- 中心意思：新尝试出现小挫折
- 情绪：专注 → 挫败 → 开始修复
- 儿童主体性：两人可以先皱眉，再停下工具用手修复
- 画面新增量：S02 塌一角，D01 / D02 明确放下
- 出场：C01 左、C02 右
- 道具：D01 平放乐乐右侧；D02 放小米左侧；S02 修稳后留一掌宽缺口
- 景别 / 机位：侧面中景，南侧儿童平视
- 构图：两人双手压沙，工具远离中心动作，长椅为锚点
- 文字区：左上，1 行
- 色彩 / 光线：不因挫折变暗，保持清爽基色
- 朗读检查：“哗啦”提供翻页节奏，不夸张成事故
- 无字图片：`artwork/clean/page-08-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 8 side medium view after a small collapse. S02 on the right has slipped at one edge. Lele has placed the red shovel flat on his far right; Xiaomi has placed the blue bucket on her far left. Both children use their free hands to press the bridge edge back into a stable shape, first wearing small frustrated frowns. At the end of the scene S02 remains one preschool palm-width away from S01. Keep upper-left text space and the east bench anchor.
```

## 第 9 页

- 正文：还差一点点。我们一起来。
- 汉字数：10
- 中心意思：两双手共同填合最后缺口
- 情绪：挫败 → 靠近
- 儿童主体性：共同动作来自两人的选择，不由成人安排
- 画面新增量：人物脸退出，手与两桥成为唯一焦点
- 出场：C01 双手从左、C02 双手从右
- 道具：D01 远右、D02 远左；S01 / S02 中央填合
- 景别 / 机位：俯视特写
- 构图：两桥从左右进入，中心缺口清楚，四只手不重叠混乱
- 文字区：上方居中，2 行
- 色彩 / 光线：蓝绿与沙色重新平衡，轻微提亮
- 朗读检查：邀请自然，不讲抽象道理
- 无字图片：`artwork/clean/page-09-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 9 overhead action close view. S01 enters from the left and S02 from the right, with a visible small center gap. Xiaomi's two hands enter from the left and Lele's two hands enter from the right to fill the gap together; all fingers are clearly separated and naturally pressing sand. The red shovel is far right and the blue bucket far left, outside the central action. Keep a clean top-center text zone. No faces are required; hands and bridge connection are the sole focus.
```

## 第 10 页

- 正文：两座桥碰到一起，变成一条长长的路。
- 汉字数：15
- 中心意思：两个需要都被保留，并产生新的共同玩法
- 情绪：靠近 → 满足
- 儿童主体性：结尾不评价谁更大方，只呈现共同结果
- 画面新增量：两桥稳定连接、工具放下、两个孩子自然坐近
- 出场：C01 左、C02 右
- 道具：D01 右侧靠近乐乐；D02 左侧靠近小米；两桥连接
- 景别 / 机位：开阔远景，南侧平视
- 构图：围栏、树、长椅全部回归；人物不是中央摆拍
- 文字区：左上，2 行
- 色彩 / 光线：全书最通透但不过度暖黄
- 朗读检查：具体可见，无品德口号
- 无字图片：`artwork/clean/page-10-clean.png`
- 状态：未生成
- 追加提示词：

```text
Page-specific direction: page 10 satisfying wide ending. S01 from the left and S02 from the right are now stably connected into one long sandy route. Xiaomi sits on the left and Lele sits on the right, naturally a little closer than before, with sandy knees and shoe edges, relaxed small smiles rather than cheering. The red shovel lies on the far right near Lele; the blue bucket rests on the far left near Xiaomi. Show the fixed fence, west tree, east bench, and consistent morning light. Keep a natural upper-left text area. No moral slogan and no text.
```

## 全书朗读结果

- 10 页均为 8-15 个汉字，符合 3-4 岁主要年龄带
- 每页一个中心动作或情绪变化
- “一铲，一桶”形成一次有推进的节奏重复
- 没有“真乖、不要小气、好孩子要分享”等评价
- 结尾不解释隐喻，由两座桥连接的画面承载
