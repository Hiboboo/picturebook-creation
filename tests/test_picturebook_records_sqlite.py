import json
import shutil
import sqlite3
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCRIPT = REPO_ROOT / "skills" / "picturebook-check-local-record" / "scripts" / "picturebook_records.py"


class PicturebookRecordsSqliteTest(unittest.TestCase):
    def make_temp_skill_repo(self, temp_dir: str) -> Path:
        root = Path(temp_dir)
        script = root / "skills" / "picturebook-check-local-record" / "scripts" / "picturebook_records.py"
        script.parent.mkdir(parents=True)
        shutil.copy2(SOURCE_SCRIPT, script)
        return script

    def run_script(self, script: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *args],
            check=False,
            encoding="utf-8",
            cwd=script.parents[3],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def test_add_and_check_use_project_sqlite_database(self) -> None:
        with TemporaryDirectory() as temp_dir:
            script = self.make_temp_skill_repo(temp_dir)
            root = Path(temp_dir)
            db_path = root / "records" / "picturebook_records.sqlite"

            add = self.run_script(
                script,
                "add",
                "--series",
                "入园准备",
                "--theme",
                "分离焦虑",
                "--title",
                "小云朵去上学",
                "--status",
                "draft",
            )

            self.assertEqual(add.returncode, 0, add.stderr)
            add_result = json.loads(add.stdout)
            self.assertEqual(Path(add_result["database"]), db_path)
            self.assertTrue(db_path.exists())
            self.assertFalse((root / ".codex" / "picturebook-records" / "picturebook-records.json").exists())

            conn = sqlite3.connect(db_path)
            try:
                row = conn.execute(
                    "select series, theme, title, status from picturebook_records"
                ).fetchone()
            finally:
                conn.close()
            self.assertEqual(row, ("入园准备", "分离焦虑", "小云朵去上学", "draft"))

            check = self.run_script(
                script,
                "check",
                "--series",
                "入园准备",
                "--theme",
                "分离焦虑",
                "--title",
                "小云朵去上学",
            )

            self.assertEqual(check.returncode, 0, check.stderr)
            check_result = json.loads(check.stdout)
            self.assertEqual(Path(check_result["database"]), db_path)
            self.assertTrue(check_result["duplicate"])
            self.assertFalse(check_result["suspected_duplicate"])
            self.assertEqual(check_result["matches"][0]["title"], "小云朵去上学")

    def test_export_writes_project_records_json_from_sqlite(self) -> None:
        with TemporaryDirectory() as temp_dir:
            script = self.make_temp_skill_repo(temp_dir)
            root = Path(temp_dir)
            records_json = root / "records" / "records.json"

            self.run_script(
                script,
                "add",
                "--series",
                "自然科普",
                "--theme",
                "雨后观察",
                "--title",
                "雨滴排队",
                "--status",
                "completed",
                "--summary",
                "孩子观察雨后世界的小故事",
                "--output-dir",
                "output/picturebooks/nature/rain-line",
            )
            export = self.run_script(script, "export")

            self.assertEqual(export.returncode, 0, export.stderr)
            self.assertTrue(records_json.exists())
            data = json.loads(records_json.read_text(encoding="utf-8"))
            self.assertEqual(data["version"], 1)
            self.assertEqual(data["records"][0]["title"], "雨滴排队")
            self.assertEqual(data["records"][0]["status"], "completed")
            self.assertEqual(data["records"][0]["summary"], "孩子观察雨后世界的小故事")

    def test_json_registry_argument_is_not_supported(self) -> None:
        with TemporaryDirectory() as temp_dir:
            script = self.make_temp_skill_repo(temp_dir)
            old_json = Path(temp_dir) / "old.json"

            result = self.run_script(
                script,
                "--registry",
                str(old_json),
                "list",
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(old_json.exists())


if __name__ == "__main__":
    unittest.main()
