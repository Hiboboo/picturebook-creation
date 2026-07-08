# 《小肚肚叮一下》AI 瑕疵审计

## 当前状态

- 实际图片生成：是，已生成封面 + 8 页无字内页 v2。
- 审计对象：提示词风险 + 全书 v2 样张初检。

## 提示词风险控制

- 文字乱码风险：已在每页提示词加入 `no text, no pseudo-Chinese`。
- 隐私风险：第 6-7 页加入 `privacy-safe composition, no nudity, no exposed private parts, no urine, no liquid stream, no toilet bowl contents`，且第 7 页改为“小肚肚轻轻的”的身体感受，不要求画尿液结果。
- 成人强迫风险：每页负面提示包含 no coercion/no adult pulling/no pressure 等约束。
- 奖励羞耻风险：结尾和坐马桶页明确 no reward sticker/no clapping/no shame，并要求第 8 页不展示裤裤胜利。
- 角色漂移风险：角色外观在每页提示词中复述，并在角色圣经锁定。
- 空间漂移风险：环境地图和连续性矩阵锁定客厅左、浴室右。

## 出图后 P0 检查项

- 任何私密部位、裸露、尿液、马桶内部内容。
- 成人拉拽、按住、围堵、催促或围观孩子。
- 主要角色换脸、换装、换发型。
- 多手指、少手指、多肢、缺肢、脚不着地。
- 浴室左右翻转导致空间路线混乱。
- 图像模型生成中文、伪中文、厕所标识或可读文字。

## 出图后 P1 检查项

- 小马桶颜色、大小或位置漂移。
- 小兔无故消失或变形。
- 文字区不足或遮挡关键动作。
- 浴室过冷、过暗、像公共厕所或医院。
- 角色表情过度兴奋、哭闹或羞耻化。

## 本轮成图审计

- 样张路径：
  - 封面：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/cover-clean-v2.png`
  - 第 1 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-01-clean-v2.png`
  - 第 2 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-02-clean-v2.png`
  - 第 3 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-03-clean-v2.png`
  - 第 4 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-04-clean-v2.png`
  - 第 5 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-05-clean-v2.png`
  - 第 6 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-06-clean-v2.png`
  - 第 7 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-07-clean-v2.png`
  - 第 8 页：`outputs/picturebooks/shenghuo-xiguan-yangcheng/xiaodudu-ding-yixia/artwork/clean/page-08-clean-v2.png`
- P0 初检：封面 + 8 页 v2 样张未见私密暴露、尿液、马桶内部内容、强迫动作、围观、奖励羞耻文字或伪中文。
- P1 初检：暂无必须重做项。第 6 页 v2 已修正 v1 中“训练裤完整穿着坐马桶”的误读；第 6/7 页仍建议正式排版前人工终审隐私安全。
- P2 记录：v2 原始输出均已等比规范化为 `1536x2048`；v1 文件和横版误图不进入项目 clean 交付，仅作历史生成记录。

## 当前结论

封面 + 8 页无字样张 v2 已生成并完成初检，可供用户确认全书视觉方向；下一步可制作缩略联系表、排正文文字并导出 PDF/PPT。
