import unittest

from compression import compress_string


class Tester(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string('aaabbccccccc'), 'a3b2c6')

    def test_not_compress_string(self):
        self.assertEqual(compress_string('abcdefga'), 'abcdefga')