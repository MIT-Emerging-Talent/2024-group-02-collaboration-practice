#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.12
"""
File: array_product.py
Author: Vlad421
Date: 1/19/2024

Description: Array product except inself function
"""

def array_product(arr:list[int]) -> list[int]:
    """Renurns new list of product of elements except itself

    Parameters:
       arr: list[int] array of int's

    Returns -> list[any] product of input array except itself    

    >>> array_product([1,2,3,4,5])
    [120, 60, 40, 30, 24]
    """
    for each in arr:
        assert  isinstance(each,int), "Input must be list of ontegers"

    new_arr:list[int] = list(arr)
    size:int = len(arr)
    for i in range(size):
        product:int = 1
        for j in range(size):
            if i != j:
                product  *= arr[j]
        new_arr[i] = product

    return new_arr

