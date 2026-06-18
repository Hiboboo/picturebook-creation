---
name: picturebook-check-local-record
description: Use when a user provides or asks to create a picturebook series, theme, title/name, or story concept and Codex must check local records before creating a new preschool picturebook, avoid duplicate stories, inspect or update a local JSON registry, or reserve a new story identity.
---

# 绘本记录查重

## 核心原则

先查重，再创作。只要用户输入了绘本系列、主题、名字、标题或故事概念，就必须在构思故事之前检查本地记录。

默认记录文件：`~/.codex/picturebook-records/picturebook-records.json`。如需使用项目内记录，设置环境变量 `PICTUREBOOK_RECORDS_PATH` 指向 JSON 文件。

## 工作流程

1. 收集最小查重键：`series`、`theme`、`title`。用户说“名字”时按 `title` 处理。
2. 运行脚本检查：

```powershell
python "$env:USERPROFILE\.codex\skills\picturebook-check-local-record\scripts\picturebook_records.py" check --series "系列" --theme "主题" --title "书名"
```

3. 如果返回 `duplicate: true`，停止新故事创作，告诉用户已存在的记录摘要、创建时间和输出路径。只有用户明确要求“做一个变体/新版/重写”时，才继续，并要求使用新的标题或明确的版本标识。
4. 如果返回 `duplicate: false`，在创作前登记草稿占位：

```powershell
python "$env:USERPROFILE\.codex\skills\picturebook-check-local-record\scripts\picturebook_records.py" add --series "系列" --theme "主题" --title "书名" --status "draft"
```

5. PDF/PPT 完成后，更新记录为 `completed`，并写入输出路径、人物、风格、摘要。

```powershell
python "$env:USERPROFILE\.codex\skills\picturebook-check-local-record\scripts\picturebook_records.py" add --series "系列" --theme "主题" --title "书名" --status "completed" --summary "一句话摘要" --output-dir "输出目录"
```

## 判定规则

- 标题完全相同且系列相同：重复。
- 标题接近、主题相同、系列相同：疑似重复，必须向用户说明并请求确认是否继续。
- 系列为空时，以标题和主题作为查重键，但要提示记录不完整。
- 不要用“这次只是草稿”“稍后再登记”跳过记录。草稿也要登记。

## 输出要求

查重后用简短中文说明：

- `未发现重复，已登记草稿。`
- 或 `发现重复/疑似重复：...`
- 给出记录文件路径，方便用户追踪。

