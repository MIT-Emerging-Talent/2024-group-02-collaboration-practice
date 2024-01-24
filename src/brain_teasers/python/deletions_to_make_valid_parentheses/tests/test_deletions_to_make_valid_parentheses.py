import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from deletions_to_make_valid_parentheses import (
    deletions_to_make_valid_parentheses,
)

class TestDeletionsToMakeValidParentheses(unittest.TestCase):
    def test_1(self):
        input_string = "(()))"
        expected = 1
        actual = deletions_to_make_valid_parentheses(input_string)
        self.assertEqual(actual, expected)

    def test_2(self):
        input_string = "()())())"
        expected = 2
        actual = deletions_to_make_valid_parentheses(input_string)
        self.assertEqual(actual, expected)

    def test_3(self):
        input_string = "()(())))(("
        expected = 4
        actual = deletions_to_make_valid_parentheses(input_string)
        self.assertEqual(actual, expected)

    def test_4(self):
        input_string = "()(())"
        expected = 0
        actual = deletions_to_make_valid_parentheses(input_string)
        self.assertEqual(actual, expected)

    def test_5(self):
        input_string = ")((())"
        expected = 2
        actual = deletions_to_make_valid_parentheses(input_string)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
