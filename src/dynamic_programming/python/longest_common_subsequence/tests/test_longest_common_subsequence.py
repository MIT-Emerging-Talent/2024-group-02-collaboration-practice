
import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")
from longest_common_subsequence import lcs_basic, lcs_memo, lcs_tab

class TestLCSBasic(unittest.TestCase):
    def test_1(self):
        a = "ABCBDAB"
        b = "BDABCA"
        result = (4, "BDAB")
        self.assertEqual(lcs_basic(a, b), result)

    def test_2(self):
        a = "TUPAKSHAKUR"
        b = "SHAKURTUPAK"
        result = (6, "SHAKUR")
        self.assertEqual(lcs_basic(a, b), result)

    def test_3(self):
        a = "FOOBAR"
        b = "BARFOO"
        result = (3, "FOO")
        self.assertEqual(lcs_basic(a, b), result)

    def test_4(self):
        a = "FOOBAR"
        b = "BARFOOFOO"
        result = (3, "FOO")
        self.assertEqual(lcs_basic(a, b), result)

    def test_5(self):
        a = "FOOBAR"
        b = "FOOBAR"
        result = (6, "FOOBAR")
        self.assertEqual(lcs_basic(a, b), result)

    def test_assertion1(self):
        a = 4
        b = 'aa'
        with self.assertRaises(AssertionError):
            lcs_basic(a, b)


    def test_assertion2(self):
        a = 'dsg'
        b = True
        with self.assertRaises(AssertionError):
            lcs_basic(a, b)

class TestLCSMemo(unittest.TestCase):
    def test_1(self):
        a = "ABCBDAB"
        b = "BDABCA"
        result = (4, "BDAB")
        self.assertEqual(lcs_memo(a, b), result)

    def test_2(self):
        a = "TUPAKSHAKUR"
        b = "SHAKURTUPAK"
        result = (6, "SHAKUR")
        self.assertEqual(lcs_memo(a, b), result)

    def test_3(self):
        a = "FOOBAR"
        b = "BARFOO"
        result1 = (3, "FOO")
        result2 = (3, "BAR")
        self.assertTrue(
            (lcs_memo(a, b)==result1)or
            (lcs_memo(a, b)==result2))

    def test_4(self):
        a = "FOOBAR"
        b = "BARFOOFOO"
        result1 = (3, "FOO")
        result2 = (3, "BAR")
        self.assertTrue(
            (lcs_memo(a, b)==result1)or
            (lcs_memo(a, b)==result2))

    def test_5(self):
        a = "FOOBAR"
        b = "FOOBAR"
        result = (6, "FOOBAR")
        self.assertEqual(lcs_memo(a, b), result)

    def test_assertion1(self):
        a = 4
        b = 'aa'
        with self.assertRaises(AssertionError):
            lcs_basic(a, b)


    def test_assertion2(self):
        a = 'dsg'
        b = True
        with self.assertRaises(AssertionError):
            lcs_basic(a, b)



'''
class TestLCSTab(unittest.TestCase):
    def test_1(self):
        a = "ABCBDAB"
        b = "BDCABA"
        result = 4
        self.assertEqual(lcs_tab(a, b), result)

    def test_2(self):
        a = "TUPAKSHAKUR"
        b = "SHAKURTUPAK"
        result = 6
        self.assertEqual(lcs_tab(a, b), result)

    def test_3(self):
        a = "FOOBAR"
        b = "BARFOO"
        result = 3
        self.assertEqual(lcs_tab(a, b), result)

    def test_4(self):
        a = "FOOBAR"
        b = "BARFOOFOO"
        result = 3
        self.assertEqual(lcs_tab(a, b), result)

    def test_5(self):
        a = "FOOBAR"
        b = "FOOBAR"
        result = 6
        self.assertEqual(lcs_tab(a, b), result)

'''
if __name__ == "__main__":
    unittest.main()
