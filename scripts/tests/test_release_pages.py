import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class ReleasePageTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp = Path(self.temp_dir.name)
        self.artifacts = self.temp / "artifacts.json"
        self.notes = self.temp / "notes.md"
        self.artifacts.write_text(
            json.dumps(
                {
                    "ipa": {"name": "tvs-selfsign-2.0.0.ipa", "size": 34, "sha256": "a" * 64},
                    "dmg": {"name": "tvs-2.0.0.dmg", "size": 41, "sha256": "b" * 64},
                    "arm64-v8a": {"name": "tvs-2.0.0-arm64-v8a.apk", "size": 32, "sha256": "c" * 64},
                }
            ),
            encoding="utf-8",
        )
        self.notes.write_text("- 最新修复\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_readme_update_replaces_previous_release_rows_and_notes(self):
        readme = self.temp / "README.md"
        readme.write_text(
            """## 下载（最新版 1.9.0）

| 平台 | 下载 | 说明 |
| --- | --- | --- |
| iOS | old | old |

## 最新版本

### iOS（IPA）

| 版本 | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- |
| 1.9.0 (build 1) | old.ipa | 30 MB | `old` | 2026-01-01 |

### Android（APK）

| 版本 | ABI | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- | --- |
| 1.9.0 (build 1) | arm64-v8a | old.apk | 30 MB | `old` | 2026-01-01 |

### macOS（DMG）

| 版本 | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- |
| 1.9.0 (build 1) | old.dmg | 40 MB | `old` | 2026-01-01 |

### 1.9.0 更新内容

- 旧内容
""",
            encoding="utf-8",
        )

        subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/update_readme.py"),
                "--version",
                "2.0.0",
                "--date",
                "2026-02-02",
                "--build",
                "1",
                "--notes-file",
                str(self.notes),
                "--artifacts",
                str(self.artifacts),
                "--readme",
                str(readme),
            ],
            check=True,
        )

        output = readme.read_text(encoding="utf-8")
        self.assertNotIn("1.9.0", output)
        self.assertNotIn("旧内容", output)
        self.assertIn("### 2.0.0 更新内容", output)
        self.assertEqual(output.count("| 2.0.0 (build 1)"), 3)

    def test_site_update_links_to_latest_readme_section(self):
        site = self.temp / "index.html"
        site.write_text(
            """<main>
<!-- BEGIN:downloads -->
old downloads
<!-- END:downloads -->
</main>
""",
            encoding="utf-8",
        )

        subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/update_site.py"),
                "--version",
                "2.0.0",
                "--artifacts",
                str(self.artifacts),
                "--site",
                str(site),
            ],
            check=True,
        )

        output = site.read_text(encoding="utf-8")
        self.assertIn("下载最新版 2.0.0", output)
        self.assertIn("TVBox-tvs#最新版本", output)
        self.assertNotIn("#版本记录", output)


if __name__ == "__main__":
    unittest.main()
