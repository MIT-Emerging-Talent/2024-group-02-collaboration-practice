#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 17 01 24

@author: tvsirius
"""


def merge_sort(list_to_sort: list[any], ascending: bool = True) -> list[any]:
    """Sorts a list using merge algorithm
    Can sort any list of items that can be compared
    (int, bool,char,**). Items compatibility will be checked on the fly,
    for performance reasons

    Parameters:
        list_to_sort: list[any] - List (or tuple) of similar item 
            that allows comparison methods (< > <= >=)
        ascending:bool=True - If True (by default) list will be sorted in ascending order, 
            otherwise descending

    Returns -> list[any] sorted list 

    >>> merge_sort([])
    []

    >>> merge_sort([3,2])
    [2,3]

    >>> merge_sort([1,5,10,2,22],ascending = False)
    [22,10,5,2,1]
    
    
    """

    if len(list_to_sort) == 0:
        return []

    # checks for type
    assert isinstance(list_to_sort, (list, tuple)
                      ), "list_to_sort must be list or tuple"


    def helper_merge(list1, list2) -> list:
        """Helper function for merging two lists, based on ascending parameter
        """
        i = j = 0
        list1_len = len(list1)
        list2_len = len(list2)
        result_list = []
        # while both list are not empty
        while i < list1_len and j < list2_len:
            try:
                if ascending:
                    # ascending and Descending varies only on using <= or >=
                    # now ascending, so smaller first
                    if list1[i] <= list2[j]:
                        result_list.append(list1[i])
                        i += 1
                    else:
                        result_list.append(list2[j])
                        j += 1
                else:
                    # Descending
                    if list1[i] >= list2[j]:
                        result_list.append(list1[i])
                        i += 1
                    else:
                        result_list.append(list2[j])
                        j += 1
            except TypeError as exc:
                # This is how I check if I list can be sorted
                # ISSUE - how whoul it be best - to raise Assertion, or to raise TypeError instead
                # (and then change it in the start assertions)
                raise TypeError(
                    f"Items of list are not compatible for sorting:{exc}") from exc
        # add the one list left
        result_list += list1[i:]+list2[j:]
        return result_list

    def helper_sort_recursion(list_to_sort) -> list:
        """Helper recursion function.
        If len of list_to_sort is 1 return it, otherwise split it, calls itself of both halves 
        merge and return result 
        """
        mid_point = len(list_to_sort)//2
        # Zero case
        if len(list_to_sort) < 2:
            return list_to_sort

        # Recursion
        return helper_merge(helper_sort_recursion(list_to_sort[0:mid_point]),
                            helper_sort_recursion(list_to_sort[mid_point:]))

    return helper_sort_recursion(list_to_sort)
