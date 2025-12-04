import unittest

from scripts import ingest


class TestIngest(unittest.TestCase):
    def test_parse_sample(self):
        """Smoke test: parse the internal sample HTML and check key course IDs."""
        html = ingest._sample_html()
        courses = ingest.parse_html_string(html)
        self.assertIsInstance(courses, list)
        ids = {c.get("id") for c in courses}
        # expected sample ids from ingest._sample_html()
        self.assertIn("CS101", ids)
        self.assertIn("MATH101", ids)
        # check CS201 prerequisites include CS101 (from sample later expansion)
        cs201 = next((c for c in courses if c.get("id") == "CS201"), None)
        # cs201 may not be present in the minimal sample; if present, verify prereqs
        if cs201:
            self.assertIn("CS101", cs201.get("prerequisites", []))


if __name__ == "__main__":
    unittest.main()
