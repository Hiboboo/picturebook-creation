# 《小火车出发啦》视觉连续性 QA v2

## 锁定检查

- 画幅：通过。封面和 8 页内页均为 `3:4` 竖版，`1086x1448`。
- 主角服装：通过。C01 保持黄色上衣、浅蓝背带裤、红鞋、小蓝背包。
- 妈妈服装：通过。A01 保持浅青绿开衫、白色内搭、米白长裤和低马尾。
- 小火车：通过。T01 为红车头、天蓝车顶、浅黄色车厢，无文字编号。
- 场景：通过。公园小火车站台、黄线、弯轨、小桥和树形成连续空间。
- 光源：通过。整体为晴朗上午自然光。
- 文字：通过。clean 图无模型文字；中文只出现在 `artwork/composited/v2/` 后期文本层。

## 重点页复检

- 第 3 页：通过。已重生成，数车厢动作比第 2 页更明确。
- 第 5 页：通过。无车票、无递票；车门、座位、扶手、车窗成为画面重点。
- 第 6 页：通过。背包从背上取下并放在座位旁，孩子坐稳扶手。
- 第 8 页：通过。小火车远去，小葫芦回头看；无掌声、奖品或完成任务式庆祝。

## 当前结论

新版无字联系表：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/storyboard-contact-sheet-v2.png`

排版完成联系表：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/bible/storyboard-contact-sheet-final-v2.png`

视觉连续性通过，可进入人工终审或印刷规格扩展。
