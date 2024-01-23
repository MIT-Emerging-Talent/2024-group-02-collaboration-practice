#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.12
"""
File: randomize_array.py
Author: Vlad421
Date: 1/23/2024

Description: Randomize sequence array fun
"""


import random

def randomize_array(orig:list[any])-> list[any]:
    """Randomize sequence array fun, returns randomized List

    Parameters:
        orig: list[any] - List of items to randomize


    Returns -> list[any] sorted list    

    >>> randomize_array([1,2,3,4,5,6])
    [4, 6, 1, 2, 5, 3]
    """
    sequence = [*range(0, len(orig))] 
    new_list = []
    for e in orig:
        i = random.choice(sequence)
        new_list.append(orig[i])
        sequence.remove(i)

    return new_list




