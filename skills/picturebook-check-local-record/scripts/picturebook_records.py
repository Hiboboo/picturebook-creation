#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path


def default_registry_path() -> Path:
    override = os.environ.get("PICTUREBOOK_RECORDS_PATH")
    if override:
        return Path(override).expanduser()
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "picturebook-records" / "picturebook-records.json"
    return Path.home() / ".codex" / "picturebook-records" / "picturebook-records.json"


def normalize(value: str) -> str:
    value = (value or "").strip().casefold()
    value = re.sub(r"[\s\-_·:：,，.。!！?？'\"“”‘’《》<>]+", "", value)
    return value


def fingerprint(series: str, theme: str, title: str) -> str:
    raw = "|".join([normalize(series), normalize(theme), normalize(title)])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_records(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "records": []}
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("version", 1)
    data.setdefault("records", [])
    return data


def save_records(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    tmp.replace(path)


def find_matches(records: list, series: str, theme: str, title: str) -> tuple[list, list]:
    exact_key = fingerprint(series, theme, title)
    title_key = normalize(title)
    theme_key = normalize(theme)
    series_key = normalize(series)
    exact = []
    suspected = []
    for record in records:
        if record.get("id") == exact_key:
            exact.append(record)
            continue
        same_series = normalize(record.get("series", "")) == series_key if series_key else True
        same_theme = normalize(record.get("theme", "")) == theme_key if theme_key else False
        same_title = normalize(record.get("title", "")) == title_key if title_key else False
        if same_title and (same_series or same_theme):
            suspected.append(record)
    return exact, suspected


def make_record(args: argparse.Namespace) -> dict:
    return {
        "id": fingerprint(args.series, args.theme, args.title),
        "series": args.series,
        "theme": args.theme,
        "title": args.title,
        "status": args.status,
        "summary": args.summary or "",
        "characters": args.characters or "",
        "style": args.style or "",
        "output_dir": args.output_dir or "",
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }


def cmd_check(args: argparse.Namespace) -> int:
    path = Path(args.registry).expanduser() if args.registry else default_registry_path()
    data = load_records(path)
    exact, suspected = find_matches(data["records"], args.series, args.theme, args.title)
    result = {
        "registry": str(path),
        "duplicate": bool(exact),
        "suspected_duplicate": bool(suspected) and not exact,
        "matches": exact or suspected,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    path = Path(args.registry).expanduser() if args.registry else default_registry_path()
    data = load_records(path)
    record = make_record(args)
    replaced = False
    for index, existing in enumerate(data["records"]):
        if existing.get("id") == record["id"]:
            record["created_at"] = existing.get("created_at", record["created_at"])
            data["records"][index] = {**existing, **record, "updated_at": now_iso()}
            replaced = True
            break
    if not replaced:
        data["records"].append(record)
    save_records(path, data)
    print(json.dumps({"registry": str(path), "added": not replaced, "record": record}, ensure_ascii=False, indent=2))
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    path = Path(args.registry).expanduser() if args.registry else default_registry_path()
    data = load_records(path)
    print(json.dumps({"registry": str(path), "records": data["records"]}, ensure_ascii=False, indent=2))
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Manage local preschool picturebook story records.")
    p.add_argument("--registry", help="Optional registry JSON path. Defaults to ~/.codex/picturebook-records/picturebook-records.json.")
    sub = p.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check")
    check.add_argument("--series", required=True)
    check.add_argument("--theme", required=True)
    check.add_argument("--title", required=True)
    check.set_defaults(func=cmd_check)

    add = sub.add_parser("add")
    add.add_argument("--series", required=True)
    add.add_argument("--theme", required=True)
    add.add_argument("--title", required=True)
    add.add_argument("--status", default="draft", choices=["draft", "completed", "archived"])
    add.add_argument("--summary")
    add.add_argument("--characters")
    add.add_argument("--style")
    add.add_argument("--output-dir")
    add.set_defaults(func=cmd_add)

    list_cmd = sub.add_parser("list")
    list_cmd.set_defaults(func=cmd_list)
    return p


def main() -> int:
    args = parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

