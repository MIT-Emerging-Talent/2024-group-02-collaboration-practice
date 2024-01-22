

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
        result1 = (3, "FOO")
        result2 = (3, "BAR")
        self.assertTrue(
            (lcs_basic(a, b) == result1) or
            (lcs_basic(a, b) == result2))

    def test_4(self):
        a = "FOOBAR"
        b = "BARFOOFOO"
        result1 = (3, "FOO")
        result2 = (3, "BAR")
        self.assertTrue(
            (lcs_basic(a, b) == result1) or
            (lcs_basic(a, b) == result2))

    def test_5(self):
        a = "FOOBAR"
        b = "FOOBAR"
        result = (6, "FOOBAR")
        self.assertEqual(lcs_basic(a, b), result)

    # This tests takes too much time to compute
    # def test_6(self):
    #     """ Special case"""
    #     a='ABCDEFGEOIUXYZO'
    #     b='MZBCDEFGLMKMLXYZL'
    #     result=(9, 'BCDEFGXYZ')
    #     self.assertEqual(lcs_basic(a, b), result)

    # def test_8(self):
    #     """ Special case 2"""
    #     a='AXYZABCDEFGEOIUO'
    #     b='MXYZZBCDEFGLMKMLL'
    #     result=(9, 'XYZBCDEFG')
    #     self.assertEqual(lcs_basic(a, b), result)

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
            (lcs_memo(a, b) == result1) or
            (lcs_memo(a, b) == result2))

    def test_4(self):
        a = "FOOBAR"
        b = "BARFOOFOO"
        result1 = (3, "FOO")
        result2 = (3, "BAR")
        self.assertTrue(
            (lcs_memo(a, b) == result1) or
            (lcs_memo(a, b) == result2))

    def test_5(self):
        a = "FOOBAR"
        b = "FOOBAR"
        result = (6, "FOOBAR")
        self.assertEqual(lcs_memo(a, b), result)

    def test_6(self):
        """ Special case
        Notes - first I thought it was error, 
        and result must be (6,"BCDEFG")
        but we are searching for the longest subsequence,
        that can be get from strings removing any chars. 
        Anywhere in the internet it says so, and so the problem is solved

        """
        a = 'ABCDEFGEOIUXYZO'
        b = 'MZBCDEFGLMKMLXYZL'
        result = (9, 'BCDEFGXYZ')
        self.assertEqual(lcs_memo(a, b), result)

    def test_7(self):
        """ Special case 2"""
        a = 'AXYZABCDEFGEOIUO'
        b = 'MXYZZBCDEFGLMKMLL'
        result = (9, 'XYZBCDEFG')
        self.assertEqual(lcs_memo(a, b), result)

    def test_assertion1(self):
        a = 4
        b = 'aa'
        with self.assertRaises(AssertionError):
            lcs_memo(a, b)

    def test_assertion2(self):
        a = 'dsg'
        b = True
        with self.assertRaises(AssertionError):
            lcs_memo(a, b)


class TestLCSTab(unittest.TestCase):
    def test_1(self):
        a = "ABCBDAB"
        b = "BDABCA"
        result = (4, "BDAB")
        self.assertEqual(lcs_tab(a, b), result)

    def test_2(self):
        a = "TUPAKSHAKUR"
        b = "SHAKURTUPAK"
        result = (6, "SHAKUR")
        self.assertEqual(lcs_tab(a, b), result)

    def test_3(self):
        a = "FOOBAR"
        b = "BARFOO"
        result1 = (3, "FOO")
        result2 = (3, "BAR")
        self.assertTrue(
            (lcs_tab(a, b) == result1) or
            (lcs_tab(a, b) == result2))

    def test_4(self):
        a = "FOOBAR"
        b = "BARFOOFOO"
        result1 = (3, "FOO")
        result2 = (3, "BAR")
        self.assertTrue(
            (lcs_tab(a, b) == result1) or
            (lcs_tab(a, b) == result2))

    def test_5(self):
        a = "FOOBAR"
        b = "FOOBAR"
        result = (6, "FOOBAR")
        self.assertEqual(lcs_tab(a, b), result)

    def test_6(self):
        """ Special case"""
        a = 'ABCDEFGEOIUXYZO'
        b = 'MZBCDEFGLMKMLXYZL'
        result = (9, 'BCDEFGXYZ')
        self.assertEqual(lcs_tab(a, b), result)

    def test_7(self):
        """ Special case 2"""
        a = 'AXYZABCDEFGEOIUO'
        b = 'MXYZZBCDEFGLMKMLL'
        result = (9, 'XYZBCDEFG')
        self.assertEqual(lcs_tab(a, b), result)

    def test_assertion1(self):
        a = 4
        b = 'aa'
        with self.assertRaises(AssertionError):
            lcs_tab(a, b)

    def test_assertion2(self):
        a = 'dsg'
        b = True
        with self.assertRaises(AssertionError):
            lcs_tab(a, b)


if __name__ == "__main__":
    unittest.main()
