#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.12
"""
File: can_sum.py
Author: Vlad421
Date: 1/19/2024
Description: Checks if array can produce given sum
"""


def can_sum_basic(arr: list[int], number: int) -> bool:

    if number < 0:
            return False
    elif number == 0:
        return True

    for i in arr:
        reminder = number-i
        
        return can_sum_basic(arr[1:], reminder) or can_sum_basic(arr[1:], number)



def can_sum_memo(arr: list[int], n: int, memo: int = 0) -> bool:

    if memo > n:
        return False
    elif len(arr) > 0:
        memo += arr[0]
        return can_sum_memo(arr[1:], n, memo) or can_sum_memo(arr[1:], n)

    elif n == memo:
        return True
    else:
        return False


def can_sum_table(arr: list[int], n: int) -> bool:
    return False


l = [2, 1]

print(can_sum_memo(l, 1))
