#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.12
"""
File: vector.py
Author: Vlad421
Date: 1/23/2024

Description: Vector collection implementation
"""


class Vector:
    """Linked list data structure representation
    """

    def __init__(self) -> None:
        """Creates empty vector"""
        self.__data: list[any] = []
        self.__number_of_elements: int = 0

    def empty(self) -> bool:
        """Returns True if empty, False if not empty"""
        return self.__number_of_elements == 0

    def size(self) -> int:
        """Returns True if empty, False if not empty"""
        return self.__number_of_elements

    def push_back(self, value: any) -> None:
        """Add element to end of list"""

        self.__data.append(value)
        self.__number_of_elements += 1

    def front(self) -> any:
        """Returns first element"""

        if not self.empty():
            return self.__data[0]

        raise IndexError()

    def back(self) -> any:
        """Returns last element"""

        if not self.empty():
            return self.__data[-1]

        raise IndexError()

    def pop_back(self):
        """Remove last element from vector"""
        if not self.empty():
            self.__number_of_elements -= 1
            return self.__data.pop()

        raise IndexError()

    def clear(self):
        """Remove all elements from vector"""
        self.__data: list[self.Node] = list()
        self.__number_of_elements: int = 0

    def resize(self, new_size: any):
        """Resize vector to given value"""

        if new_size > self.__number_of_elements:

            self.__data += [None]*(new_size-self.__number_of_elements)
            self.__number_of_elements = new_size
        elif new_size < self.__number_of_elements:

            self.__data = self.__data[:new_size:]
            self.__number_of_elements = new_size

    def __getitem__(self, key):
        if key > len(self.__data)-1:
            raise IndexError
        return self.__data[key]
