#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Version: 3.12
"""
File: linked_list.py
Author: Vlad421
Date: 1/19/2024

Description: Linked list collection implementation
"""


class LinkedList:

    """Linked list data structure representation
    """

    class Node:
        def __init__(self, value: [any]) -> None:
            self.value = value
            self.next = None

    def __init__(self) -> None:
        """Creates empty linked list"""
        self.__data: list[self.Node] = list()
        self.__number_of_elements: int = 0

    def empty(self) -> bool:
        """Returns True if empty, False if not empty"""
        return self.__number_of_elements == 0

    def size(self) -> int:
        """Returns True if empty, False if not empty"""
        return self.__number_of_elements

    def push_back(self, value: any) -> None:
        """Add element to end of list"""
        element = self.Node(value)
        if not self.empty():
            self.__data[-1].next = element

        self.__data.append(element)
        self.__number_of_elements += 1

    def front(self) -> any:
        """Returns first element"""
        element: any = 0
        if not self.empty():
            element = self.__data[0].value
        else:
            element = None
        return element

    def back(self) -> any:
        """Returns last element"""
        element: any = 0
        if not self.empty():
            element = self.__data[-1].value
        else:
            element = None
        return element

    def pop_front(self):
        """Remove first element from list"""
        if not self.empty():
            self.__data.pop(0)
            self.__number_of_elements -= 1

    def pop_back(self):
        """Remove last element from list"""
        if not self.empty():

            if self.__number_of_elements > 1:
                #clearing reference to next element
                self.__data[-2].next = None
            self.__data.pop()
            self.__number_of_elements -= 1

    def clear(self):
        """Remove all elements from list"""
        self.__data: list[self.Node] = list()
        self.__number_of_elements: int = 0

    def remove(self, element: any):
        """Remove all elements from with given value"""

        if not self.empty():

            counter: int = 0
            pointer: self.Node = self.__data[counter]
            
            # Iterating thru nodes
            while pointer.next != None:
                # comparing values of nodes 
                if pointer.value == element:

                    if counter-1 > -1:
                        #Change referense to next element
                        self.__data[counter-1].next = pointer

                    self.__data.pop(counter)
                    self.__number_of_elements -= 1
                    pointer = pointer.next
                else:
                    counter += 1
                    pointer = pointer.next

            counter += 1



