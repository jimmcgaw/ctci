import unittest

from unique import unique_character_string


class Tester(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(unique_character_string('abc'))

    def test_not_unique(self):
        self.assertFalse(unique_character_string('abcdefga'))