#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.12
"""
File: selection_sort.py
Author: Vlad421
Date: 1/21/2024

Description: Heap sorting algorythm implementation
"""


def selection_sort(array_to_sort: list[any], ascending: bool = True) -> list[any]:
    """Sorts a list using heap_sort algorithm, returns sorted List

    Parameters:
        array_to_sort: list[any] - List of items to sort
        ascending:bool=True - If True (by default) list will be sorted in ascending order, 
            otherwise descending

    Returns -> list[any] sorted list    

    >>> selection_sort([])
    []
    >>> selection_sort([3,15,5,8,19])
    [3, 5, 8, 15, 19]
    >>> selection_sort([1,12,9,20,6], False)
    [20, 12, 9, 6, 1] """

    assert isinstance(array_to_sort, (list, tuple)
                      ), "array_to_sort must be list or tuple"

    if len(array_to_sort) > 0:

        previous_element = array_to_sort[0]
        for e in range(len(array_to_sort)):
            if type(previous_element) != type(array_to_sort[e]):
                raise TypeError("Array data types mismatch")
            previous_element = array_to_sort[e]

    array: list = list(array_to_sort)
    array_size: int = len(array)

    def swap(i: int, j: int):
        """swap 2 elements in list"""
        array[i], array[j] = array[j], array[i]

    # sorting array
    for i in range(array_size):
        to_swap = i
        # compare to destination pointer
        for j in range(i+1, array_size):
            if ascending:
                if array[j] < array[to_swap]:
                    to_swap = j
            else:
                if array[j] > array[to_swap]:
                    to_swap = j

        # swap values
        swap(i, to_swap)

    # return sorted array
    return array
