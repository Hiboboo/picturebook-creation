# 《爸爸带我去冒险》逐页脚本与出图提示词

## 全书通用负面提示词

no mature content, no child-inappropriate content, no violence, no blood, no weapons, no scary horror, no sexual content, no nudity, no dangerous behavior, no climbing high, no jumping from furniture, no child trapped alone, no shaming, no coercion, no forced bravery, no adult pulling or pushing child, no reward chart, no prize, no clapping as proof of courage, no readable text, no letters, no numbers, no pseudo-Chinese characters, no logos, no watermark, no extra fingers, no missing fingers, no fused hands, no extra limbs, no malformed anatomy, no duplicated people, no inconsistent character face, no outfit changes, no changing hairstyle, no shoes on child, no shoes on dad, no changing wall art frame, no floating objects, no warped perspective, no impossible furniture, no random decorative clutter, no plastic skin, no identical smiles.

## 封面提示词

Use case: illustration-story
Asset type: wordless cover concept for a preschool picturebook
Primary request: Create a 3:4 vertical wordless cover for the Chinese preschool picturebook "爸爸带我去冒险"; do not draw any text.
Scene/backdrop: a bright lived-in family living room after rain, left-side window light, round blue-green rug, low gray sofa, one consistent light-wood framed teal-and-cream abstract landscape picture above the sofa, a few low soft cushions and a safe blanket tunnel in the background.
Subject: C01 Xiao He, 3-4 year old child with round face, soft black short hair with one side curl, moss-green pullover, denim-blue overalls, terracotta indoor socks, no shoes, small muted-mustard canvas adventure backpack with a simple leaf icon; A01 Dad, adult male caregiver with short black hair, deep teal sweatshirt, charcoal soft pants, light gray socks, no shoes, kneeling at child eye level.
Style/medium: refined preschool watercolor and colored-pencil illustration, light paper grain, natural body language, publication-quality, no glossy AI look.
Composition/framing: Dad opens a blank little map on the round rug, Xiao He leans in curiously, cushion mountain and blanket cave hint at a safe indoor pretend adventure; leave a natural low-detail title area on the upper wall.
Lighting/mood: soft natural window light, playful, safe, quiet affection.
Color palette: teal, moss green, denim blue, terracotta, cream, light gray; avoid yellow-beige dominance and random rainbow colors.
Constraints: no text, no readable map marks, no danger, no forced hugging, no adult pulling child, no outdoor mountain, both characters wear socks only and no shoes, keep the same single wall art frame design across pages.
Avoid: use the global negative prompt.

## 页面总表

| 页码 | 正文 | 汉字数 | 中心意思 | 无字图状态 |
|---|---:|---:|---|---|
| 1 | 爸爸铺开小地图。 | 7 | 打开游戏入口 | 已生成：`artwork/clean/page-01-clean.png`；原始图：`artwork/raw/page-01-raw.png` |
| 2 | 今天去客厅冒险吗？ | 8 | 爸爸邀请 | 已生成：`artwork/clean/page-02-clean.png`；原始图：`artwork/raw/page-02-raw.png` |
| 3 | 我背上小小包。 | 6 | 孩子准备参与 | 已生成：`artwork/clean/page-03-clean.png`；原始图：`artwork/raw/page-03-raw.png` |
| 4 | 枕头山，软软高高。 | 7 | 第一个小障碍 | 已生成：`artwork/clean/page-04-clean.png`；原始图：`artwork/raw/page-04-raw.png` |
| 5 | 我说：“我想慢一点。” | 7 | 表达节奏 | 已生成：`artwork/clean/page-05-clean.png`；原始图：`artwork/raw/page-05-raw.png` |
| 6 | 爸爸给我一根手指。 | 8 | 低压力支持 | 已生成：`artwork/clean/page-06-clean.png`；原始图：`artwork/raw/page-06-raw.png` |
| 7 | 一步，一步，过山啦。 | 7 | 完成小动作 | 已生成：`artwork/clean/page-07-clean.png`；原始图：`artwork/raw/page-07-raw.png` |
| 8 | 毛毯洞里有点黑。 | 7 | 再次犹豫 | 已生成：`artwork/clean/page-08-clean.png`；原始图：`artwork/raw/page-08-raw.png` |
| 9 | 爸爸在洞口等我。 | 7 | 看见爸爸等待 | 已生成：`artwork/clean/page-09-clean.png`；原始图：`artwork/raw/page-09-raw.png` |
| 10 | 我钻出来，爸爸还在。 | 8 | 安全收束 | 已生成：`artwork/clean/page-10-clean.png`；原始图：`artwork/raw/page-10-raw.png` |

## 分页提示词

### 第 1 页

正文：爸爸铺开小地图。

Prompt: 3:4 vertical watercolor preschool picturebook page, no text, bright lived-in family living room after rain, left-side window, round blue-green rug, low gray sofa, one consistent light-wood framed teal-and-cream abstract landscape picture above the sofa. A01 Dad in deep teal sweatshirt, charcoal soft pants, light gray socks and no shoes sits low on the rug and spreads a blank little map with only simple non-readable lines. C01 Xiao He, 3-4 year old child with soft black short hair side curl, moss-green pullover, denim-blue overalls, terracotta indoor socks and no shoes, leans in curiously. Natural low-detail wall area upper left for later Chinese text. Avoid: use the global negative prompt.

### 第 2 页

正文：今天去客厅冒险吗？

Prompt: 3:4 vertical watercolor close page, no text, same living room and round blue-green rug, same single light-wood framed teal-and-cream abstract landscape picture above the sofa. Dad wears light gray socks and no shoes, kneels at child eye level with open hand and calm expression, inviting Xiao He without touching. Xiao He wears terracotta indoor socks and no shoes, looks from Dad to the blank map, curious and expectant. A few low cushions are visible in the background as a safe pretend route. Leave clean wall area upper left. Avoid: use the global negative prompt, no pressure, no readable map text.

### 第 3 页

正文：我背上小小包。

Prompt: 3:4 vertical watercolor page, no text, Xiao He stands on the round rug in terracotta indoor socks and no shoes, putting on a small muted-mustard canvas adventure backpack with a simple leaf icon, moss-green pullover and denim-blue overalls unchanged. Dad waits nearby in light gray socks and no shoes, sitting low and not helping too much. Blank map lies on rug. Same single light-wood framed teal-and-cream abstract landscape picture above the sofa. Soft morning-afternoon window light, calm play start. Avoid: use the global negative prompt, no logos, no readable symbols.

### 第 4 页

正文：枕头山，软软高高。

Prompt: 3:4 vertical watercolor page, no text, child-height view of a very low safe cushion mountain on the round rug, highest cushions below Xiao He's knee, soft and stable. Xiao He pauses before it, terracotta indoor socks visible and no shoes, one hand holding backpack strap; Dad waits to the side at low height in light gray socks and no shoes. Same left window, sofa anchors, and same single light-wood framed teal-and-cream abstract landscape picture. Leave upper wall for later text. Avoid: use the global negative prompt, no climbing high, no jumping, no dangerous height.

### 第 5 页

正文：我说：“我想慢一点。”

Prompt: 3:4 vertical watercolor emotional close page, no text, Xiao He near the cushion mountain holding the backpack strap, terracotta indoor socks and no shoes, hesitant but safe, mouth slightly open as if speaking. Dad kneels nearby at eye level in light gray socks and no shoes, listening with calm open posture, hands low and not touching. Cushion edge, blue-green rug, and the same single wall art frame remain visible. Avoid: use the global negative prompt, no shaming, no urging, no forced bravery.

### 第 6 页

正文：爸爸给我一根手指。

Prompt: 3:4 vertical watercolor hand-detail page, no text, close view of Dad offering exactly one finger for Xiao He to hold, child small hand reaching by choice, backpack strap and terracotta indoor sock visible, no shoes on child or dad, cushion edge and rug as spatial anchors, same single wall art frame softly visible in background. Gentle window light, clear anatomy and real hand contact, no pulling motion. Avoid: use the global negative prompt, no extra fingers, no fused hands, no adult dragging child.

### 第 7 页

正文：一步，一步，过山啦。

Prompt: 3:4 vertical watercolor action page, no text, Xiao He steps slowly over the low soft cushion mountain with stable bent knees and both feet grounded in terracotta indoor socks, no shoes, gently holding one of Dad's fingers for balance. Dad follows at child's pace, low and calm, light gray socks and no shoes. The cushion is clearly safe and low, round rug, sofa, and same single wall art frame consistent. Avoid: use the global negative prompt, no jumping, no falling, no high climbing.

### 第 8 页

正文：毛毯洞里有点黑。

Prompt: 3:4 vertical watercolor page, no text, same living room right side with the same single light-wood framed teal-and-cream abstract landscape picture visible above the sofa. A safe open blanket tunnel made from blue-green blanket over a low cardboard box and low table, wide entrance, not closed. Xiao He stands at the entrance looking in, hesitant but curious, terracotta indoor socks and no shoes. Dad is visible beside the entrance holding a small flashlight pointed down at the floor, not into the child's face, light gray socks and no shoes. Avoid: use the global negative prompt, no horror, no trapped child, no dark scary tunnel.

### 第 9 页

正文：爸爸在洞口等我。

Prompt: 3:4 vertical watercolor subjective page, no text, view from inside the soft blanket tunnel looking out. The tunnel fabric frames the image gently, not scary; Dad kneels outside the entrance in deep teal sweatshirt, light gray socks and no shoes, face visible, calm eyes, one open hand low, small flashlight glow on the rug. The same single light-wood framed teal-and-cream abstract landscape picture is faintly visible beyond the sofa. Xiao He's shoulder or small hand may be visible in foreground. Avoid: use the global negative prompt, no scary lighting, no adult grabbing child, no unreadable marks.

### 第 10 页

正文：我钻出来，爸爸还在。

Prompt: 3:4 vertical watercolor ending page, no text, outside the blanket tunnel. Xiao He crawls out calmly with small relaxed expression, backpack still on, terracotta indoor socks and no shoes; Dad kneels nearby waiting at eye level in light gray socks and no shoes, not pulling. Blank little map lies on the rug with one simple non-readable route line, cushion mountain in background, same single wall art frame and left window light return. Warm but not yellow-dominant safe ending. Avoid: use the global negative prompt, no prize, no clapping, no victory pose, no readable text.

## 角色参考图提示词

状态：已生成：`bible/character-reference-sheet.png`；原始图：`bible/raw/character-reference-sheet-raw.png`。初检通过，用于锁定角色服装、发型、比例和“亲子都只穿室内袜、不穿鞋”规则。

Prompt: Use case: illustration-story. Asset type: character reference sheet. Create one wordless 3:4 vertical character reference sheet for "爸爸带我去冒险"; no text, labels, letters, numbers, logos, or pseudo-writing. Show C01 Xiao He front, three-quarter, side, back, plus expressions calm, curious, hesitant, relaxed. Xiao He wears moss-green pullover, denim-blue overalls, terracotta indoor socks, no shoes. Show A01 Dad standing and kneeling with open hand and one-finger support pose; Dad wears deep teal sweatshirt, charcoal soft pants, light gray socks, no shoes. Use locked clothing, colors, proportions, and style from `bible/character-bible.md`. Avoid: use the global negative prompt.

## 四格关键样张提示词

状态：已完成整本联系表：`bible/storyboard-contact-sheet.png`。当前联系表由无字封面和第 1-10 页无字内页合成，用于跨页检查；下方四格提示词保留为后续重新生成关键样张时的备用提示。

Prompt: Create a 3:4 vertical wordless four-panel contact sheet for "爸爸带我去冒险". No text, no labels, no letters, no numbers, no pseudo-Chinese. Panel 1: Dad opens blank map on living room rug, Xiao He leans in. Panel 2: low soft cushion mountain, Xiao He pauses, Dad kneels and offers one finger without pulling. Panel 3: safe blanket tunnel, Xiao He looks in, Dad visible at entrance with flashlight pointed down. Panel 4: Xiao He crawls out, Dad still waiting, blank map on rug. Use locked character and color rules from `character-bible.md` and `color-and-style-bible.md`. Avoid: use the global negative prompt.
