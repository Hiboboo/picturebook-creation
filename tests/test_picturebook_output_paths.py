import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_OUTPUT_DIR = "outputs/picturebooks/<series-slug>/<title-slug>/"
OLD_OUTPUT_DIR = "output/picturebooks/<series-slug>/<title-slug>/"


class PicturebookOutputPathsTest(unittest.TestCase):
    def test_story_and_delivery_docs_use_project_outputs_directory(self) -> None:
        paths = [
            REPO_ROOT / "README.md",
            REPO_ROOT / "skills" / "picturebook-story-design" / "SKILL.md",
            REPO_ROOT / "skills" / "picturebook-story-design" / "references" / "story-output-contract.md",
            REPO_ROOT / "skills" / "picturebook-export-pdf-ppt" / "SKILL.md",
        ]

        for path in paths:
            with self.subTest(path=path):
                content = path.read_text(encoding="utf-8")
                self.assertIn(EXPECTED_OUTPUT_DIR, content)
                self.assertNotIn(OLD_OUTPUT_DIR, content)

    def test_story_design_explicitly_rejects_codex_directory_for_outputs(self) -> None:
        paths = [
            REPO_ROOT / "skills" / "picturebook-story-design" / "SKILL.md",
            REPO_ROOT / "skills" / "picturebook-story-design" / "references" / "story-output-contract.md",
        ]

        for path in paths:
            with self.subTest(path=path):
                content = path.read_text(encoding="utf-8").lower()
                self.assertIn("不要", content)
                self.assertIn(".codex", content)


if __name__ == "__main__":
    unittest.main()
