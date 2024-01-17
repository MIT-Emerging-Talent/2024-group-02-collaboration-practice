"""
Test unitest suite for merge_sort
"""

import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from merge_sort import merge_sort


class TestMergeSortV1(unittest.TestCase):
    """Test case for merge_sort"""
    def test_empty_array(self):
        """Empty list test
        """
        array = list()
        result = list()

        self.assertEqual(merge_sort(array), result)

    def test_single_element(self):
        """Single element test
        """
        array = [1]
        result = [1]

        self.assertEqual(merge_sort(array), result)

    def test_increasing_order(self):
        """Increasing order test with ascending"""
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(merge_sort(array), result)

    def test_increasing_order_desc(self):
        """Increasing order test with descending"""
        array = [1, 2, 3, 4, 5]
        result = [5, 4, 3, 2, 1]

        self.assertEqual(merge_sort(array, ascending=False), result)

    def test_decreasing_order(self):
        """Decreasing order test with ascending"""
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(merge_sort(array), result)

    def test_decreasing_order_desc(self):
        """Decreasing order test with descending"""
        array = [5, 4, 3, 2, 1]
        result = [5, 4, 3, 2, 1]

        self.assertEqual(merge_sort(array, ascending=False), result)

    def test_random_order(self):
        """Random order with ascending"""
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(merge_sort(array), result)

    def test_random_order_desc(self):
        """Random order with descending"""
        array = [2, 5, 1, 4, 3]
        result = [5, 4, 3, 2, 1]

        self.assertEqual(merge_sort(array, ascending=False), result)

    def test_chars(self):
        """Try sorting chars"""
        array = ["a", "d", "b", "e", "c"]
        result = ["a", "b", "c", "d", "e"]

        self.assertEqual(merge_sort(array), result)

    def test_assertion_list(self):
        """Test for passing not list"""
        array = "Hello"
        with self.assertRaises(AssertionError):
            merge_sort(array)

    def test_typeerror_list(self):
        """Test for passing uncompatible list"""
        array = ["a", 3, "b", "e", "c"]
        with self.assertRaises(TypeError):
            merge_sort(array)


if __name__ == "__main__":
    unittest.main()
