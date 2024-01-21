#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.10
"""
File: longest_common_subsequence.py
Author: tvsirius
Date: 1/21/2024

Description: Longest Common Subsequence implementaion
"""


def lcs_basic(string1: str, string2: str) -> (int, str):
    """LCS basic implmentaion - with simple iterative approach

    Args:
        string1 (str): String 1
        string2 (str): String 2

    Returns:
        (lcs_lenght:int, - lenght of longest common subsequence
        lcs_string): longest common subsequence itself
    """

    assert isinstance(string1, str), "String1 must be string"
    assert isinstance(string2, str), "String2 must be string"

    if len(string1) < 1 or len(string2) < 0:
        return (0, '')

    lcs_string: str = ''
    lcs_lenght: int = 0

    string1_len = len(string1)

    # iterating by string1, i from 0 to end

    for i in range(string1_len):

        # i will take string1[i:j] and search this substring in string2

        # j will iterate from i to end of string1
        # i will add lcs_lenght - if I already have LCS of lcs_len i don not need to take shorter stings into considerations

        for j in range(i+1+lcs_lenght, string1_len+1):
            if string1[i:j] in string2:
                if len(string1[i:j]) > lcs_lenght:
                    lcs_string = string1[i:j]
                    lcs_lenght = len(lcs_string)

    return (lcs_lenght, lcs_string)


def lcs_memo(string1: str, string2: str) -> (int, str):
    """LCS implmentaion with memoization 

    Args:
        string1 (str): String 1
        string2 (str): String 2

    Returns:
        (lcs_lenght:int, - lenght of longest common subsequence
        lcs_string): longest common subsequence itself
    """

    string1_len = len(string1)
    string2_len = len(string2)

    def max_result_tuple(t1, t2: (int, str)) -> (int, str):
        """ Helper for recursion func    
            t1,t2: tuples in form of our memo uses
            Returns: tuple with max of [0] element
        """
        if t1[0] >= t2[0]:
            return t1
        return t2

    def lcs_memo_recursion_helper(string1: str, string2: str, i: int, j: int, memo: [[int]]) -> (int, str):
        """Helper recursion funtion

        Args:
            string1 (str): string 1
            string2 (str): string 2
            i (int): string 1 index
            j (int): string 2 index
            memo (int]]):  memoization array

        Returns:
            (int,: lenght of longest common subsequence from i,j
            str): string of longest common subsequence from i,j
        """
        # Zero case - if we reach to the end
        if i > string1_len-1 or j > string2_len-1:
            return (0, '')

        # if we already heave the result for this i and j
        if memo[i][j][0] != -1:
            return memo[i][j]

        if string1[i] == string2[j]:
            # include this element and recurce to i+1 and j+1
            # We also keeping the string of longest sequence in the memoization,
            # so recursion call return the string and add to upper level call
            next_memo = lcs_memo_recursion_helper(
                string1, string2, i+1, j+1, memo)
            memo[i][j] = (next_memo[0]+1, string1[i]+next_memo[1])
        else:
            # if we do not match, we try 2 directions: i,j+1 and i+1,j and choose the maximum of them
            memo[i][j] = max_result_tuple(lcs_memo_recursion_helper(string1, string2, i+1, j, memo),
                                          lcs_memo_recursion_helper(string1, string2, i, j+1, memo))

        return memo[i][j]

    assert isinstance(string1, str), "String1 must be string"
    assert isinstance(string2, str), "String2 must be string"

    if len(string1) < 1 or len(string2) < 0:
        return (0, '')

    # array for memoization of (len,str) tuples

    memo = [[(-1, '')]*(string2_len+1) for _ in range(string1_len+1)]

    return lcs_memo_recursion_helper(string1, string2, 0, 0, memo)


def lcs_tab():
    pass
