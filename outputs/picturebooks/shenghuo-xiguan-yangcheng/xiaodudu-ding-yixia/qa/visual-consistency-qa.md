# 《小肚肚叮一下》视觉连续性 QA

## 当前状态

- 实际图片生成：是，已生成封面 + 8 页无字内页 v2。
- 可检查内容：角色、道具、空间、色板、镜头计划、提示词和全书 v2 样张初检。

## 文本锁定检查

- 角色外观：通过，C01 和 A01 已固定服装、发型、比例和禁改项。
- 演员人数：通过，无同伴、无围观者。
- 道具状态：通过，小兔、小马桶、积木、训练裤均有跨页状态。
- 空间地图：通过，客厅左、浴室右，行动轴线明确。
- 镜头变化：通过，8 页包含远中景、中景、近景、特写和反向收束；第 3 页用未完成积木增加轻微犹豫，第 8 页避免裤裤胜利展示。
- 色板：通过，奶油白、浅木色、薄荷绿、暖黄、浅蓝、苹果红少量强调。
- 文字区：通过，每页均有自然低细节文字区。
- 无字规则：通过，提示词明确禁止模型生成文字。

## 出图后必须检查

- C01 是否保持黑色短发、暖黄色上衣、浅蓝训练裤。
- A01 是否保持低马尾、奶油色上衣、浅橄榄绿长裤。
- 浴室是否一直在客厅右侧，小马桶是否固定在门内。
- 第 6-7 页是否完全隐私安全，无私密部位、尿液、马桶内部内容，并能表达“坐一坐、等一等”和“小肚肚轻轻的”。
- 妈妈是否没有拉、按、催、围观或奖励。
- 是否出现奖励贴纸、排行榜、羞耻文字、公共厕所标识或伪中文。

## 全书样张初检

- 封面：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/cover-clean-v2.png`。客厅左、浴室右、小马桶可见，妈妈蹲低陪伴；无文字、无尿液、无隐私暴露；孩子轻微疑惑感和半成品积木信息更明确。
- 第 1 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-01-clean-v2.png`。建立客厅左、浴室右的路线；小葫芦专注搭积木，小兔在旁，小马桶在浴室远景中可见。
- 第 2 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-02-clean-v2.png`。搭积木的手形成停顿感，轻触肚肚动作自然，未画成疼痛或害怕；浴室门作为右侧背景线索保留。
- 第 3 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-03-clean-v2.png`。孩子一手靠近小肚肚、一手仍靠近积木，轻微犹豫感清楚；妈妈蹲低倾听，没有替孩子判断或催促。
- 第 4 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-04-clean-v2.png`。孩子抱小兔自己慢慢走向浴室，妈妈保持跟随距离；没有拉、抱、催或路线遮挡。
- 第 5 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-05-clean-v2.png`。小马桶和脚凳友好清楚，孩子先看一看；浴室明亮干净，不像公共厕所或医院。
- 第 6 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-06-clean-v2.png`。已修正“训练裤完整穿着坐马桶”的误读；隐私区域由侧面机位、衣摆和马桶边缘共同遮挡，无私密暴露、无尿液、无马桶内部细节，姿势稳定。
- 第 7 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-07-clean-v2.png`。用放松表情、手部和脚踩小凳表达“小肚肚轻轻的”；无尿液、无马桶内部内容、无私密暴露。
- 第 8 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-08-clean-v2.png`。孩子轻松回到游戏垫，未做裤裤胜利展示；背景小马桶统一为奶油白主体 + 薄荷绿坐圈，小兔耳朵内侧统一为浅蓝。
- 尺寸一致性：封面和 8 页 clean v2 样张均已规范化为 `1536x2048`、`3:4`。

## 当前结论

封面 + 8 页无字样张 v2 已完成初检，可进入全书联系表、后期文字排版和 PDF/PPT 导出前复核。第 6/7 页为隐私敏感页，正式排版前仍建议人工终审。
