"""
Docstring
"""
import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")


from add_string_numbers import add_string_numbers


class TestAddStringNumbers(unittest.TestCase):
    """obvious docstring :)
    """
    def test_add_two_single_digit_numbers(self):
        """
        1+2=3 in str
        """
        self.assertEqual(add_string_numbers("1", "2"), "3")

    def test_add_two_double_digit_numbers(self):
        """another
        """
        self.assertEqual(add_string_numbers("11", "22"), "33")

    def test_add_two_numbers_with_different_number_of_digits(self):
        """
        I don't see the need to do docstrings here
        """
        self.assertEqual(add_string_numbers("1", "22"), "23")

    def test_add_two_big_numbers(self):
        """
        but maybe it will help me to do a habit
        """
        self.assertEqual(add_string_numbers("123456789", "987654321"), "1111111110")

    def test_add_two_float_numbers(self):
        """
        moreover i will generate test unit cases with LLM in the future
        """
        self.assertEqual(add_string_numbers("1.1", "2.2"), "3.3")

    def test_add_two_numbers_with_different_number_of_digits_and_floats(self):
        """
        just here methods names are self descriptive"""
        self.assertEqual(add_string_numbers("1.1344", "22.99999999"), "24.13439999")

    def test_assertion_types(self):
        """check if i pass not strings
        """
        with self.assertRaises(AssertionError):
            add_string_numbers("325",42)

    def test_assertion_no_number_strings(self):
        """check if i pass not strings
        """
        with self.assertRaises(AssertionError):
            add_string_numbers("3a25","346.3")


if __name__ == "__main__":
    unittest.main()
