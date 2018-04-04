"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""
import unittest


class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")


    def test_assertEqual(self):


if __name__ == '__main__':
    unittest.main(verbosity=2)
