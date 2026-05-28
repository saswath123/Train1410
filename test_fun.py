"""Tests for the `fun` file introduced in this PR."""

import os
import unittest


class TestFunFile(unittest.TestCase):
    FILE_PATH = os.path.join(os.path.dirname(__file__), "fun")

    def test_file_exists(self):
        """The `fun` file must exist in the repository root."""
        self.assertTrue(os.path.isfile(self.FILE_PATH), "File 'fun' does not exist")

    def test_file_content_equals_jolly_trip(self):
        """The `fun` file must contain exactly 'jolly trip' (ignoring trailing newline)."""
        with open(self.FILE_PATH) as f:
            content = f.read().strip()
        self.assertEqual(content, "jolly trip")

    def test_file_content_starts_with_jolly(self):
        """The content must start with 'jolly'."""
        with open(self.FILE_PATH) as f:
            content = f.read().strip()
        self.assertTrue(content.startswith("jolly"), f"Expected content to start with 'jolly', got: {content!r}")

    def test_file_content_ends_with_trip(self):
        """The content must end with 'trip'."""
        with open(self.FILE_PATH) as f:
            content = f.read().strip()
        self.assertTrue(content.endswith("trip"), f"Expected content to end with 'trip', got: {content!r}")

    def test_file_is_not_empty(self):
        """The `fun` file must not be empty."""
        self.assertGreater(os.path.getsize(self.FILE_PATH), 0, "File 'fun' is empty")

    def test_file_contains_exactly_two_words(self):
        """The content must consist of exactly two whitespace-separated words."""
        with open(self.FILE_PATH) as f:
            content = f.read().strip()
        words = content.split()
        self.assertEqual(len(words), 2, f"Expected 2 words, got {len(words)}: {words}")

    def test_file_content_is_lowercase(self):
        """The content must be entirely lowercase (no uppercase letters)."""
        with open(self.FILE_PATH) as f:
            content = f.read().strip()
        self.assertEqual(content, content.lower(), f"Expected lowercase content, got: {content!r}")

    def test_file_not_binary(self):
        """The `fun` file must be a readable text file (not binary)."""
        with open(self.FILE_PATH, "rb") as f:
            raw = f.read()
        # Check no null bytes (common indicator of binary content)
        self.assertNotIn(b"\x00", raw, "File 'fun' appears to be binary")


if __name__ == "__main__":
    unittest.main()
