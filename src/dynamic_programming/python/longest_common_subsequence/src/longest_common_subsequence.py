#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.10
"""
File: longest_common_subsequence.py
Author: tvsirius
Date: 1/21/2024

Description: Longest Common Subsequence implementaion
"""


def max_result_tuple(t1, t2: (int, str)) -> (int, str):
    """ Helper for recursion function    
        t1,t2: tuples in form of our lcs functions uses
        Returns: tuple with max of [0](where lenght is stored) element
    """
    if t1[0] >= t2[0]:
        return t1
    return t2


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

    string1_len = len(string1)
    string2_len = len(string2)

    def lcs_recursion_helper(string1: str, string2: str, i: int, j: int) -> (int, str):
        """Helper recursion function

        Args:
            string1 (str): string 1
            string2 (str): string 2
            i (int): string 1 index
            j (int): string 2 index

        Returns:
            (int,: lenght of longest common subsequence from i,j
            str): string of longest common subsequence from i,j
        """
        # Zero case - if we reach to the end
        if i < 0 or j < 0:
            return (0, '')

        if string1[i] == string2[j]:
            # include this element and recurce to i+1 and j+1
            # We also keeping the string of longest sequence in the memoization,
            # so recursion call return the string and add to upper level call
            next_memo = lcs_recursion_helper(
                string1, string2, i-1, j-1)
            return (next_memo[0]+1, next_memo[1]+string1[i])
        else:
            # if we do not match, we try 2 directions:
            # i,j+1 and i+1,j and choose the maximum of them
            return max_result_tuple(lcs_recursion_helper(string1, string2, i, j-1),
                                    lcs_recursion_helper(string1, string2, i-1, j))

    if len(string1) < 1 or len(string2) < 0:
        return (0, '')

    return lcs_recursion_helper(string1, string2, string1_len-1, string2_len-1)


def lcs_memo(string1: str, string2: str) -> (int, str):
    """LCS implmentaion with memoization 

    Args:
        string1 (str): String 1
        string2 (str): String 2

    Returns:
        (lcs_lenght:int, - lenght of longest common subsequence
        lcs_string): longest common subsequence itself
    """

    assert isinstance(string1, str), "String1 must be string"
    assert isinstance(string2, str), "String2 must be string"

    string1_len = len(string1)
    string2_len = len(string2)

    def lcs_memo_recursion_helper(string1: str, string2:
                                  str, i: int, j: int, memo: [[int]]) -> (int, str):
        """Helper recursion function

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
        if i < 0 or j < 0:
            return (0, '')

        # if we already heave the result for this i and j
        if memo[i][j][0] != -1:
            return memo[i][j]

        if string1[i] == string2[j]:
            # include this element and recurce to i+1 and j+1
            # We also keeping the string of longest sequence in the memoization,
            # so recursion call return the string and add to upper level call
            next_memo = lcs_memo_recursion_helper(
                string1, string2, i-1, j-1, memo)
            memo[i][j] = (next_memo[0]+1, next_memo[1]+string1[i])
        else:
            # if we do not match, we try 2 directions:
            # i,j+1 and i+1,j and choose the maximum of them
            memo[i][j] = max_result_tuple(lcs_memo_recursion_helper(string1, string2, i, j-1, memo),
                                          lcs_memo_recursion_helper(string1, string2, i-1, j, memo))

        return memo[i][j]

    if len(string1) < 1 or len(string2) < 0:
        return (0, '')

    # array for memoization of (len,str) tuples
    memo = [[(-1, '')]*(string2_len+1) for _ in range(string1_len+1)]

    return lcs_memo_recursion_helper(string1, string2, string1_len-1, string2_len-1, memo)


def lcs_tab(string1: str, string2: str) -> (int, str):
    """LCS implmentaion with memoization table
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

    string1_len = len(string1)
    string2_len = len(string2)

    # similar to memoization, but we build a table instead

    memo_table = [[0]*(string2_len+1) for _ in range(string1_len+1)]

    # using iteration we aggregate sum over diagonal (in case chars are equal),
    # otherwise we get the max of the previous (minus one) column or row

    for i in range(0, string1_len):
        for j in range(0, string2_len):
            if string1[i] == string2[j]:
                # on the previous we keep the previos max lenght of common
                # subsequence on this area (defined by current i and j)
                memo_table[i][j] = memo_table[i-1][j-1]+1
            else:
                # no equal - copy the max lenght we have here, like reference
                memo_table[i][j] = max(memo_table[i-1][j], memo_table[i][j-1])



    # to recreate the string we go backwards:

    lcs_string = ''

    l = string1_len-1
    m = string2_len-1

    while l >= 0 and m >= 0:
        if string1[l] == string2[m]:
            # equal char - append to our string
            lcs_string = string1[l]+lcs_string
            l -= 1
            m -= 1
        # not equal - go on behalf of max
        elif memo_table[l-1][m] > memo_table[l][m-1]:
            l -= 1
        else:
            m -= 1

    return (memo_table[i][j], lcs_string)
