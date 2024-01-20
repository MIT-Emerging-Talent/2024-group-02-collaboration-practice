import unittest
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(file_dir)))
src_path = os.path.join(project_root, "src")
sys.path.append(src_path)


from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_empty_array(self):
        array = list()
        result = list()
        self.assertEqual(quick_sort(array), result)

    def test_single_element(self):
        array = [1]
        result = [1]
        self.assertEqual(quick_sort(array), result)

    def test_increasing_order(self):
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(array), result)

    def test_decreasing_order(self):
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(array), result)

    def test_random_order(self):
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(array), result)

if __name__ == "__main__":
    unittest.main()