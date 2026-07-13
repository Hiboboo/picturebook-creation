# 《第一次上幼儿园》逐页脚本与出图提示词

## 全书通用负面提示词

no mature content, no child-inappropriate content, no violence, no blood, no weapons, no scary horror, no sexual content, no nudity, no dangerous behavior, no shaming, no coercion, no forced separation, no adult pulling or pushing child, no crowd pressure, no reward chart, no clapping as proof of bravery, no readable text, no letters, no pseudo-Chinese characters, no logos, no watermark, no extra fingers, no missing fingers, no fused hands, no extra limbs, no malformed anatomy, no duplicated people, no inconsistent character face, no outfit changes, no changing hairstyle, no floating objects, no warped perspective, no impossible furniture, no random decorative clutter, no plastic skin, no identical smiles.

## 封面提示词

Use case: illustration-story
Asset type: wordless cover concept for a preschool picturebook
Primary request: Create a 3:4 vertical wordless cover for the Chinese preschool picturebook "第一次上幼儿园"; do not draw any text.
Scene/backdrop: morning outside a low rounded blue-green kindergarten gate with soft tree shadows, a glimpse of a bright classroom doorway inside.
Subject: C01 Xiao You, 3-4 year old child with black short bob, muted-coral side clip, blue-green cardigan, white shirt, soft coral pants, white socks, teal backpack, holding a sky-blue cloud handkerchief; A01 Mom kneels beside the child at eye level, waiting gently without pulling.
Style/medium: refined preschool watercolor and colored-pencil illustration, light paper grain, natural child posture, publication-quality.
Composition/framing: Xiao You stands between Mom and the open gate, feet paused, one hand holding the handkerchief; leave a natural low-detail title area above the gate.
Lighting/mood: fresh morning light, calm, supportive, first-day hesitation.
Color palette: morning blue, fresh green, muted coral, navy, cream white; avoid yellow-beige dominance.
Constraints: no text, no readable school signs, no crowd, no forced bravery.
Avoid: use the全书通用负面提示词.

## 页面总表

| 页码 | 正文 | 汉字数 | 中心意思 | 无字图状态 |
|---|---:|---:|---|---|
| 1 | 轻轻背上可爱的小书包。 | 10 | 出发 | 已生成：`artwork/clean/page-01-clean.png`；已排版：`artwork/composited/page-01-final.png` |
| 2 | 好漂亮的幼儿园。 | 7 | 到门口停住 | 已生成：`artwork/clean/page-02-clean.png`；已排版：`artwork/composited/page-02-final.png` |
| 3 | 妈妈蹲下来。 | 5 | 妈妈陪着慢一点 | 已生成：`artwork/clean/page-03-clean.png`；已排版：`artwork/composited/page-03-final.png` |
| 4 | 老师说，进来看一看吧。 | 9 | 老师给选择 | 已生成：`artwork/clean/page-04-clean.png`；已排版：`artwork/composited/page-04-final.png` |
| 5 | 小格子，等我哟。 | 6 | 找到自己的位置 | 已生成：`artwork/clean/page-05-clean.png`；已排版：`artwork/composited/page-05-final.png` |
| 6 | 我坐边边看一看。 | 7 | 先观察 | 已生成：`artwork/clean/page-06-clean.png`；已排版：`artwork/composited/page-06-final.png` |
| 7 | 圆圆球，咕噜咕噜跑过来。 | 10 | 同伴低压力邀请 | 已生成：`artwork/clean/page-07-clean.png`；已排版：`artwork/composited/page-07-final.png` |
| 8 | 我也咕噜回去。 | 6 | 做一个小回应 | 已生成：`artwork/clean/page-08-clean.png`；已排版：`artwork/composited/page-08-final.png` |
| 9 | 妈妈来接我啦。 | 6 | 照顾者回来 | 已生成：`artwork/clean/page-09-clean.png`；已排版：`artwork/composited/page-09-final.png` |
| 10 | 明天，我还要来幼儿园。 | 9 | 允许持续适应 | 已生成：`artwork/clean/page-10-clean.png`；已排版：`artwork/composited/page-10-final.png` |

## 分页提示词

### 第 1 页

正文：轻轻背上可爱的小书包。

Prompt: 3:4 vertical watercolor preschool picturebook page, no text, morning at home doorway, C01 Xiao You wearing blue-green cardigan, white shirt, soft coral pants, white socks, muted-coral hair clip, teal backpack, holding sky-blue cloud handkerchief, A01 Mom kneels beside child gently adjusting backpack strap without pulling, calm departure mood, low-detail wall area upper left for later Chinese text. Avoid: use the global negative prompt.

### 第 2 页

正文：好漂亮的幼儿园。

Prompt: 3:4 vertical watercolor page, no text, kindergarten entrance with low rounded blue-green gate and morning tree shadows, C01 Xiao You pauses before the gate holding sky-blue cloud handkerchief, teal backpack on shoulders, A01 Mom nearby at a respectful distance, child looks small but safe, natural title-free low-detail area above gate. Avoid: use the global negative prompt, no crowd, no school sign text.

### 第 3 页

正文：妈妈蹲下来。

Prompt: 3:4 vertical watercolor close page, no text, beside blue-green kindergarten gate, A01 Mom kneels at C01 Xiao You's eye level with calm open posture, Xiao You holds the sky-blue cloud handkerchief close, teal backpack visible, child hesitant but safe, no pulling, low-detail wall area upper left. Avoid: use the global negative prompt.

### 第 4 页

正文：老师说，进来看一看吧。

Prompt: 3:4 vertical watercolor page, no text, classroom doorway with round window and child-height cubbies behind, T01 Teacher Lin crouches at child eye level in sage green apron, C01 Xiao You stands by A01 Mom holding cloud handkerchief and looking in, teacher waits warmly, no pressure, no readable classroom signs. Avoid: use the global negative prompt.

### 第 5 页

正文：小格子，等我哟。

Prompt: 3:4 vertical watercolor page, no text, child-height cubbies inside classroom, C01 Xiao You gently places teal backpack into one cubby with blank simple shape tag, sky-blue cloud handkerchief still nearby, T01 Teacher Lin waits at respectful distance, warm but not yellow-dominant morning classroom, no readable name labels. Avoid: use the global negative prompt.

### 第 6 页

正文：我坐边边看一看。

Prompt: 3:4 vertical watercolor page, no text, inside classroom near left window, round blue rug in center, C01 Xiao You sits at the quiet edge of the rug holding sky-blue cloud handkerchief, T01 Teacher Lin nearby but not crowding, a quiet chair by the window, low shelves behind, calm observation moment. Avoid: use the global negative prompt, no crowd staring.

### 第 7 页

正文：圆圆球，咕噜咕噜跑过来。

Prompt: 3:4 vertical watercolor low-angle page, no text, coral soft fabric ball gently rolling across the round blue rug toward C01 Xiao You sitting at the edge, C02 An An waits on the other side with natural curious expression, Xiao You watches while holding cloud handkerchief, teacher only softly in background, low-pressure social invitation. Avoid: use the global negative prompt, no throwing, no clapping.

### 第 8 页

正文：我也咕噜回去。

Prompt: 3:4 vertical watercolor page, no text, C01 Xiao You at the edge of the round blue rug gently rolls the coral soft fabric ball back to C02 An An, one hand still near the sky-blue cloud handkerchief, Xiao You shows a small relaxed expression, T01 Teacher Lin waits quietly in background, no applause or reward, low-pressure preschool social moment. Avoid: use the global negative prompt.

### 第 9 页

正文：妈妈来接我啦。

Prompt: 3:4 vertical watercolor page, no text, classroom doorway with round window and cubbies, A01 Mom kneels at doorway to pick up C01 Xiao You, Xiao You walks toward Mom holding sky-blue cloud handkerchief, T01 Teacher Lin waits gently nearby, calm reunion after first kindergarten day, no report-card feeling. Avoid: use the global negative prompt.

### 第 10 页

正文：明天，我还要来幼儿园。

Prompt: 3:4 vertical watercolor ending page, no text, outside the same low rounded blue-green kindergarten gate, C01 Xiao You holds A01 Mom's hand and walks out calmly while looking back at the gate with a small relaxed expression, sky-blue cloud handkerchief visible, teal backpack returned, morning-blue and fresh-green palette, gentle open ending, no victory display. Avoid: use the global negative prompt.

## 四格关键样张提示词

状态：全书无字封面、10 页无字内页、排版完成图、整本联系表、PDF 和 PPTX 已生成。所有 clean/final 图片均为 `1536x2048`。

已生成关键样张：

- 封面：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/cover-clean.png`
- 第 6 页：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-06-clean.png`
- 第 8 页：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-08-clean.png`
- 第 10 页：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/artwork/clean/page-10-clean.png`
- 关键样张联系表：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/storyboard-contact-sheet-key-samples.png`
- 整本联系表：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/bible/storyboard-contact-sheet.png`
- PDF：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/export/ruyuan-shiying-yu-shejiao-diyici-shang-youeryuan.pdf`
- PPTX：`outputs/picturebooks/ruyuan-shiying-yu-shejiao/diyici-shang-youeryuan/export/ruyuan-shiying-yu-shejiao-diyici-shang-youeryuan.pptx`

Prompt: Create a 3:4 vertical wordless contact sheet for "第一次上幼儿园". Four equal panels, no readable text, no labels, no letters, no numbers, no pseudo-Chinese. Panel 1: outside a low rounded blue-green kindergarten gate, Xiao You pauses with cloud handkerchief, Mom kneels and waits, no pulling. Panel 2: classroom doorway with round window and cubbies, Teacher Lin crouches at eye level, Xiao You holds Mom's sleeve and looks in. Panel 3: quiet edge seat near left window, Xiao You sits at rug edge and watches, teacher nearby but not crowding. Panel 4: near round rug, An An gently rolls coral fabric ball to Xiao You, Xiao You rolls it back with a small relaxed smile; Mom visible at doorway for pickup warmth. Use the locked character and color rules from `character-bible.md` and `color-and-style-bible.md`.
