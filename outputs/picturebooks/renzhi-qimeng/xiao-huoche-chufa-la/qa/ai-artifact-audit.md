# 《小火车出发啦》AI 瑕疵审计 v2

## 当前状态

- 实际图片生成：是，已生成新版无字封面和第 1-8 页无字内页。
- 审计范围：`artwork/clean/v2/`、`artwork/composited/v2/`、联系表和导出文件。
- 当前 P0：无未解决项。
- 当前 P1：无未解决项。
- 当前 P2：第 4 页为低机位部件特写，车轮局部更接近认知观察页，接受。

## 逐页结论

- 封面：通过。小葫芦为第一视觉，火车视觉权重降低，妈妈后移，无文字。
- 第 1 页：通过。站台、黄线和听的动作清楚。
- 第 2 页：通过。红车头进站，人物未越线。
- 第 3 页：通过。重生成后车厢数量和数数动作更明确。
- 第 4 页：通过。无触摸车轮、无越线；文字避开车轮和鞋尖。
- 第 5 页：通过。无车票，无递票或拉拽动作。
- 第 6 页：通过。背包放座位旁，孩子坐稳扶扶手。
- 第 7 页：通过。小火车沿弯轨慢走，人物未探出窗外。
- 第 8 页：通过。小火车远去，孩子仍在看，两节车厢可读。

## 文本与导出

- clean 图：未发现可读中文、伪中文、车身编号或站牌文字。
- final 图：中文由本地后期文本层合成，曾修复 PowerShell 管道导致的问号替代问题。
- PDF：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/export/renzhi-qimeng-xiao-huoche-chufa-la-v2.pdf`
- PPTX：`outputs/picturebooks/renzhi-qimeng/xiao-huoche-chufa-la/export/renzhi-qimeng-xiao-huoche-chufa-la-v2.pptx`

## 结论

v2 已达到当前项目交付标准。正式印刷前建议进行人工校色、出血设置和纸张适配检查。
