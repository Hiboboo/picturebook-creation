#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path


def find_project_root() -> Path:
    cwd = Path.cwd().resolve()
    for candidate in (cwd, *cwd.parents):
        if (candidate / "records" / "schema.sql").exists():
            return candidate
        if (candidate / "skills" / "picturebook-check-local-record" / "scripts" / "picturebook_records.py").exists():
            return candidate
    return Path(__file__).resolve().parents[3]


PROJECT_ROOT = find_project_root()
RECORDS_DIR = PROJECT_ROOT / "records"
DATABASE_PATH = RECORDS_DIR / "picturebook_records.sqlite"
SCHEMA_PATH = RECORDS_DIR / "schema.sql"
EXPORT_PATH = RECORDS_DIR / "records.json"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

FALLBACK_SCHEMA = """
CREATE TABLE IF NOT EXISTS picturebook_records (
  id TEXT PRIMARY KEY,
  series TEXT NOT NULL DEFAULT '',
  theme TEXT NOT NULL DEFAULT '',
  title TEXT NOT NULL,
  series_key TEXT NOT NULL DEFAULT '',
  theme_key TEXT NOT NULL DEFAULT '',
  title_key TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('draft', 'completed', 'archived')),
  summary TEXT NOT NULL DEFAULT '',
  characters TEXT NOT NULL DEFAULT '',
  style TEXT NOT NULL DEFAULT '',
  output_dir TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_picturebook_records_title_key
  ON picturebook_records(title_key);

CREATE INDEX IF NOT EXISTS idx_picturebook_records_lookup_keys
  ON picturebook_records(series_key, theme_key, title_key);
"""


def normalize(value: str) -> str:
    value = (value or "").strip().casefold()
    value = re.sub(r"[\s\-_·:：,，.。!！?？'\"“”‘’《》<>]+", "", value)
    return value


def fingerprint(series: str, theme: str, title: str) -> str:
    raw = "|".join([normalize(series), normalize(theme), normalize(title)])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def schema_sql() -> str:
    if SCHEMA_PATH.exists():
        return SCHEMA_PATH.read_text(encoding="utf-8")
    return FALLBACK_SCHEMA


def connect() -> sqlite3.Connection:
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(schema_sql())
    conn.commit()
    return conn


def row_to_record(row: sqlite3.Row) -> dict:
    return {
        "id": row["id"],
        "series": row["series"],
        "theme": row["theme"],
        "title": row["title"],
        "status": row["status"],
        "summary": row["summary"],
        "characters": row["characters"],
        "style": row["style"],
        "output_dir": row["output_dir"],
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }


def find_matches(conn: sqlite3.Connection, series: str, theme: str, title: str) -> tuple[list[dict], list[dict]]:
    exact_id = fingerprint(series, theme, title)
    series_key = normalize(series)
    theme_key = normalize(theme)
    title_key = normalize(title)

    exact = [
        row_to_record(row)
        for row in conn.execute(
            """
            SELECT * FROM picturebook_records
            WHERE id = ?
            ORDER BY created_at ASC
            """,
            (exact_id,),
        )
    ]
    if exact:
        return exact, []

    suspected = []
    for row in conn.execute(
        """
        SELECT * FROM picturebook_records
        WHERE title_key = ?
        ORDER BY created_at ASC
        """,
        (title_key,),
    ):
        same_series = row["series_key"] == series_key if series_key else True
        same_theme = row["theme_key"] == theme_key if theme_key else False
        if same_series or same_theme:
            suspected.append(row_to_record(row))
    return [], suspected


def make_record(args: argparse.Namespace) -> dict:
    created_at = now_iso()
    return {
        "id": fingerprint(args.series, args.theme, args.title),
        "series": args.series,
        "theme": args.theme,
        "title": args.title,
        "series_key": normalize(args.series),
        "theme_key": normalize(args.theme),
        "title_key": normalize(args.title),
        "status": args.status,
        "summary": args.summary or "",
        "characters": args.characters or "",
        "style": args.style or "",
        "output_dir": args.output_dir or "",
        "created_at": created_at,
        "updated_at": created_at,
    }


def list_records(conn: sqlite3.Connection) -> list[dict]:
    return [
        row_to_record(row)
        for row in conn.execute(
            """
            SELECT * FROM picturebook_records
            ORDER BY created_at ASC, title ASC
            """
        )
    ]


def cmd_check(args: argparse.Namespace) -> int:
    with connect() as conn:
        exact, suspected = find_matches(conn, args.series, args.theme, args.title)
    result = {
        "database": str(DATABASE_PATH),
        "export": str(EXPORT_PATH),
        "duplicate": bool(exact),
        "suspected_duplicate": bool(suspected) and not exact,
        "matches": exact or suspected,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    record = make_record(args)
    with connect() as conn:
        existing = conn.execute(
            "SELECT created_at FROM picturebook_records WHERE id = ?",
            (record["id"],),
        ).fetchone()
        if existing:
            record["created_at"] = existing["created_at"]
            record["updated_at"] = now_iso()
        conn.execute(
            """
            INSERT INTO picturebook_records (
              id, series, theme, title, series_key, theme_key, title_key,
              status, summary, characters, style, output_dir, created_at, updated_at
            )
            VALUES (
              :id, :series, :theme, :title, :series_key, :theme_key, :title_key,
              :status, :summary, :characters, :style, :output_dir, :created_at, :updated_at
            )
            ON CONFLICT(id) DO UPDATE SET
              series = excluded.series,
              theme = excluded.theme,
              title = excluded.title,
              series_key = excluded.series_key,
              theme_key = excluded.theme_key,
              title_key = excluded.title_key,
              status = excluded.status,
              summary = excluded.summary,
              characters = excluded.characters,
              style = excluded.style,
              output_dir = excluded.output_dir,
              updated_at = excluded.updated_at
            """,
            record,
        )
        conn.commit()
    print(
        json.dumps(
            {
                "database": str(DATABASE_PATH),
                "export": str(EXPORT_PATH),
                "added": not existing,
                "record": row_to_record_like(record),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def row_to_record_like(record: dict) -> dict:
    return {
        "id": record["id"],
        "series": record["series"],
        "theme": record["theme"],
        "title": record["title"],
        "status": record["status"],
        "summary": record["summary"],
        "characters": record["characters"],
        "style": record["style"],
        "output_dir": record["output_dir"],
        "created_at": record["created_at"],
        "updated_at": record["updated_at"],
    }


def cmd_list(args: argparse.Namespace) -> int:
    with connect() as conn:
        records = list_records(conn)
    print(json.dumps({"database": str(DATABASE_PATH), "export": str(EXPORT_PATH), "records": records}, ensure_ascii=False, indent=2))
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    with connect() as conn:
        records = list_records(conn)
    data = {
        "version": 1,
        "database": str(DATABASE_PATH),
        "exported_at": now_iso(),
        "records": records,
    }
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)
    EXPORT_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"database": str(DATABASE_PATH), "export": str(EXPORT_PATH), "records": len(records)}, ensure_ascii=False, indent=2))
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Manage project-local preschool picturebook story records in SQLite.")
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

    export_cmd = sub.add_parser("export")
    export_cmd.set_defaults(func=cmd_export)
    return p


def main() -> int:
    args = parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
