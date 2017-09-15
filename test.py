import unittest

import awesome


class TestMethods2(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")
        self.assertEqual(awesome.smile(), ":)")
        self.assertEqual(awesome.frown(), ":(")

    def test_sub(self):
        self.assertEqual(awesome.smile(), ":)")

if __name__ == '__main__':
    unittest.main()
