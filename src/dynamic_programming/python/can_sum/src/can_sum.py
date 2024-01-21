#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.12
"""
File: can_sum.py
Author: Vlad421
Date: 1/20/2024
Description: Checks if array could produce given sum
"""


def can_sum_basic(number: int, arr: list[int]) -> bool:
    """Basic brute force algorythm

    Parameters:
        arr: list[int] - List of items to sum
        number:int - Target sum

    Returns -> bool    

    >>> can_sum_basic([2,1],1)
    True """
    if number < 0:
        return False
    elif number == 0:
        return True

    for i in arr:
        reminder = number-i

        return can_sum_basic(reminder, arr[1:]) or can_sum_basic(number, arr[1:])
    return False


def can_sum_memo(number: int, arr: list[int], __memo: int = 0) -> bool:
    """Algorythm with memorization

    Parameters:
        arr: list[int] - List of items to sum
        number:int - Target sum
        memo:int - memorization for recurcive call only

    Returns -> bool    

    >>> can_sum_memo([3,1,1],2)
    True """

    if __memo > number:
        return False
    elif number == __memo:
        return True
    for element in arr:
        __memo += element
        return can_sum_memo(number, arr[1:],  __memo) or can_sum_memo(number, arr[1:])

    return False


def can_sum_table(number: int, arr: list[int]) -> bool:
    """Algorythm using tabulation method

    Parameters:
        arr: list[int] - List of items to sum
        number:int - Target sum

    Returns -> bool    

    >>> can_sum_table([2,1,1,5],10)
    False """

    table:list[int] = [False] * (number + 1)

    table[0] = True

    for num in arr:
        for i in range(number, num - 1, -1):

            if table[i - num]:
                table[i] = True

    return table[number]
