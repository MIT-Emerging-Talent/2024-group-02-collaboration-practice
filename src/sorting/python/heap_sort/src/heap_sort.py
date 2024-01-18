#!/usr/bin/env python

"""
Heap sorting algorythm implementation  
Created on 1/17/2024
"""
__author__ = "Vlad421"


def heap_sort(array_to_sort: list[any], is_ascending: bool = True) -> list[any]:
    """Sorts a list using heap_sort algorithm, mutate given list

    Parameters:
        array_to_sort: list[any] - List of items to sort
        ascending:bool=True - If True (by default) list will be sorted in ascending order, 
            otherwise descending

    Returns -> list[any] sorted list    

    >>> heap_sort([])
    []
    >>> heap_sort([3,15,5,8,19])
    [3, 5, 8, 15, 19]
    >>> merge_sort([1,12,9,20,6], False)
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

    def swap(i: int, j: int):
        """swap 2 elements in list"""
        array[i], array[j] = array[j], array[i]

    def heapify(root: int, size: int):
        """ Builds maxheap or minheap tree 

        Parameters:
            root:int - index of root element
            size:int - size or upper bound of number elements """

        # find child indexes
        swap_index: int = root
        child_left: int = root*2+1
        child_right: int = root*2+2

        # check if left child exist and compare
        if is_ascending:
            if child_left < size and array[swap_index] < array[child_left]:
                swap_index = child_left
        else:
            if child_left < size and array[swap_index] > array[child_left]:
                swap_index = child_left

        # check if right child exist and compare
        if is_ascending:
            if child_right < size and array[swap_index] < array[child_right]:
                swap_index = child_right
        else:
            if child_right < size and array[swap_index] > array[child_right]:
                swap_index = child_right

        # check if root is the largest, if not swap values in array and make recursive call
        if swap_index != root:
            swap(root, swap_index)
            heapify(swap_index, size)

    array_size: int = len(array)

    # initial heapifying
    for i in range(array_size//2, -1, -1):
        heapify(i, array_size)

    # sorting
    for i in range(array_size-1, 0, -1):

        # swap root and last element, then min or max
        swap(0, i)
        heapify(0, i)

    return array
