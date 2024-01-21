"""Test unit for all_permutaions
"""

import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from all_permutations import all_permutations

class TestAllPermutations(unittest.TestCase):
    """Test class"""

    def test_one_elements(self):
        """Fro one elements"""
        input_list = [1]
        excepted = [[1]]
        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_two_elements(self):
        """Fro two elements"""
        input_list = [1, 2]
        excepted = [[1, 2], [2, 1]]
        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_three_elements(self):
        """For three"""
        input_list = [3, 1, 2]
        excepted = [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                    [2, 3, 1], [3, 2, 1], [3, 1, 2]]

        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_three_strings(self):
        """For list of chars"""
        input_list = ["A", "B", "C"]
        excepted = [
            ["A", "B", "C"],
            ["A", "C", "B"],
            ["B", "A", "C"],
            ["B", "C", "A"],
            ["C", "A", "B"],
            ["C", "B", "A"],
        ]

        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_four_elements(self):
        """Four elements tuple"""
        input_list = (3, 1, 2, 4)
        excepted = [
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 1, 4],
            [3, 2, 4, 1],
            [3, 4, 1, 2],
            [3, 4, 2, 1],
            [1, 3, 2, 4],
            [1, 3, 4, 2],
            [1, 2, 3, 4],
            [1, 2, 4, 3],
            [1, 4, 3, 2],
            [1, 4, 2, 3],
            [2, 3, 1, 4],
            [2, 3, 4, 1],
            [2, 1, 3, 4],
            [2, 1, 4, 3],
            [2, 4, 3, 1],
            [2, 4, 1, 3],
            [4, 3, 1, 2],
            [4, 3, 2, 1],
            [4, 1, 3, 2],
            [4, 1, 2, 3],
            [4, 2, 3, 1],
            [4, 2, 1, 3],
        ]

        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_string(self):
        """String"""
        input_string = 'MIT'
        excepted = [['M', 'I', 'T'], ['M', 'T', 'I'], ['I', 'M', 'T'], [
            'I', 'T', 'M'], ['T', 'M', 'I'], ['T', 'I', 'M']]

        actual = all_permutations(input_string)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_empty_list(self):
        """now with emply"""
        input_list = []
        excepted = []

        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def assertion(self):
        """And test input assertion"""
        input_int = 40

        with self.assertRaises(AssertionError):
            all_permutations(input_int)


if __name__ == "__main__":
    unittest.main()
