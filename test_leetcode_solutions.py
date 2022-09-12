import unittest
import leetcode_solutions


class TestClass(unittest.TestCase):
    def test_isPalindrome(self):
        tests = {121: True, -121: False, 10:False}
        for key, value in tests.items():
            self.assertEqual(leetcode_solutions.isPalindrome(key), value)