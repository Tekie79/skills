"""Tooling tests use temporary directories and never modify authored skills."""

from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("skills", Path(__file__).resolve().parents[1] / "scripts/skills.py")
skills = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(skills)


class SkillTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "sample-skill"
        self.skill.mkdir()

    def document(self, frontmatter="name: sample-skill\ndescription: Process sample inputs.", body="# Instructions\nProcess the input and verify the result."):
        (self.skill / "SKILL.md").write_text(f"---\n{frontmatter}\n---\n{body}\n", encoding="utf-8")

    def test_valid_minimal_skill(self):
        self.document()
        self.assertEqual(skills.validate(self.skill), [])

    def test_optional_metadata(self):
        self.document('name: sample-skill\ndescription: Process samples.\nlicense: MIT\ncompatibility: Requires Python.\nallowed-tools: Read\nmetadata:\n  version: "1.0"')
        self.assertEqual(skills.validate(self.skill), [])

    def test_name_constraints(self):
        for name in ("", "Upper", "-name", "name-", "two--words", "a" * 65, "../escape", "a/b", "cafe\u00e9"):
            with self.subTest(name=name):
                self.assertFalse(skills.valid_name(name))
        self.assertTrue(skills.valid_name("a" * 64))

    def test_directory_name_mismatch(self):
        self.document("name: other-name\ndescription: Process samples.")
        self.assertIn("must match directory", " ".join(skills.validate(self.skill)))

    def test_invalid_frontmatter(self):
        for frontmatter in ("[]", "name: [", "name: sample-skill\nname: duplicate", "42: value", "name: !!python/object:example {}"):
            with self.subTest(frontmatter=frontmatter):
                self.document(frontmatter)
                self.assertTrue(skills.validate(self.skill))

    def test_missing_delimiters_and_file(self):
        self.assertTrue(skills.validate(self.skill))
        for content in ("# No frontmatter", "---\nname: sample-skill"):
            (self.skill / "SKILL.md").write_text(content, encoding="utf-8")
            self.assertTrue(skills.validate(self.skill))

    def test_field_constraints(self):
        base = "name: sample-skill\ndescription: Process samples."
        for extra in ("unknown: value", "compatibility: ''", "metadata: []", "metadata:\n  version: 1.0", "allowed-tools: []", "license: false"):
            with self.subTest(extra=extra):
                self.document(base + "\n" + extra)
                self.assertTrue(skills.validate(self.skill))
        for description in ("''", "false", "x" * 1025):
            self.document(f"name: sample-skill\ndescription: {description}")
            self.assertTrue(skills.validate(self.skill))

    def test_body_and_draft_constraints(self):
        for body in ("", "TODO: Write instructions", "{{SKILL_NAME}}", "line\n" * 500):
            with self.subTest(body=body[:30]):
                self.document(body=body)
                self.assertTrue(skills.validate(self.skill))

    def test_scaffold_quotes_metadata_and_marks_draft(self):
        target = skills.scaffold("new-skill", 'Use when: input contains "quotes".\nKeep safe.', self.root)
        errors = skills.validate(target)
        self.assertEqual(len(errors), 1)
        self.assertIn("draft TODO", errors[0])

    def test_scaffold_does_not_overwrite(self):
        self.document()
        before = (self.skill / "SKILL.md").read_bytes()
        with self.assertRaises(FileExistsError):
            skills.scaffold("sample-skill", "Process samples.", self.root)
        self.assertEqual((self.skill / "SKILL.md").read_bytes(), before)

    def test_scaffold_rejects_invalid_input_without_creating_files(self):
        for name, description in (("../escape", "Description"), ("valid-name", " "), ("valid-name", "a" * 1025)):
            with self.assertRaises(ValueError):
                skills.scaffold(name, description, self.root)
        self.assertEqual(list(self.root.iterdir()), [self.skill])


    def test_skill_local_markdown_links_pass(self):
        refs = self.skill / "references"
        refs.mkdir()
        assets = self.skill / "assets"
        assets.mkdir()
        (assets / "template.md").write_text("# Template\\n", encoding="utf-8")
        (refs / "details.md").write_text("[template](../assets/template.md)\\n", encoding="utf-8")
        self.document(body="See [details](references/details.md) and [external](https://example.com/a).")
        self.assertEqual(skills.validate(self.skill), [])

    def test_missing_resource_link_in_skill_fails(self):
        self.document(body="See [missing](references/missing.md).")
        self.assertIn("missing linked resource", " ".join(skills.validate(self.skill)))

    def test_missing_resource_link_in_reference_fails(self):
        refs = self.skill / "references"
        refs.mkdir()
        (refs / "details.md").write_text("[gone](other.md)\\n", encoding="utf-8")
        self.document(body="See [details](references/details.md).")
        self.assertIn("missing linked resource", " ".join(skills.validate(self.skill)))

    def test_outside_skill_link_is_rejected(self):
        (self.root / "other.md").write_text("Out of bundle", encoding="utf-8")
        self.document(body="See [outside](../other.md).")
        self.assertIn("resource link escapes", " ".join(skills.validate(self.skill)))

    def test_fenced_examples_and_local_anchors_are_ignored(self):
        self.document(body="# How to\\n\\n```md\\n[example](not-a-file.md)\\n```\\nSee [section](#how-to).")
        self.assertEqual(skills.validate(self.skill), [])

    def test_cli_exit_codes(self):
        self.document()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(skills.main(["validate", "--root", str(self.root)]), 0)
            self.document(body="TODO")
            self.assertEqual(skills.main(["validate", str(self.skill)]), 1)
            self.assertEqual(skills.main(["validate", "--root", str(self.root / "missing")]), 1)
            with tempfile.TemporaryDirectory() as empty:
                self.assertEqual(skills.main(["validate", "--root", empty]), 1)


if __name__ == "__main__":
    unittest.main()
