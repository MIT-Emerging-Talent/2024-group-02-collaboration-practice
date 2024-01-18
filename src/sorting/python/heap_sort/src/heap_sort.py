"""
Heap sorting algorythm implementation  
Created on 1/17/2024
@author: Vlad421
"""


def heap_sort(array: list[any], is_ascending:bool = True):

    """Sorts a list using heap_sort algorithm, mutate given list
   
    Parameters:
        array: list[any] - List of items to sort
        ascending:bool=True - If True (by default) list will be sorted in ascending order, 
            otherwise descending
    
    >>> heap_sort([])
    []
    >>> heap_sort([3,15,5,8,19])
    [3, 5, 8, 15, 19]
    >>> merge_sort([1,12,9,20,6], False)
    [20, 12, 9, 6, 1] """



    def swap(i: int, j: int):
        """swap 2 elements in list"""
        array[i], array[j] = array[j], array[i]

    def heapify(root:int, size:int):
        """ builds maxheap or minheap tree 
        
        Parameters:
            root:int - index of root element
            size:int - size or upper bound of number elements """




        # assume root is largest, adn find child indexes
        heapified_index:int = root
        child_left:int = root*2+1
        child_right:int = root*2+2


        #check if left child exist and compare
        if is_ascending:
            if child_left<size and array[heapified_index]<array[child_left]:
                heapified_index = child_left
        else:
            if child_left<size and array[heapified_index]>array[child_left]:
                heapified_index = child_left
            
        #check if right child exist and compare
        if is_ascending:
            if child_right<size and array[heapified_index]<array[child_right]:
                heapified_index = child_right
        else:
            if child_right<size and array[heapified_index]>array[child_right]:
                heapified_index = child_right


        #check if root is the largest, if not swap values in array and make recurcive call
        if heapified_index != root:
            swap(root, heapified_index)
            heapify(heapified_index, size)

    array_size:int = len(array)

    # initial heapifying
    for i in range(array_size//2, -1, -1):
        heapify(i, array_size)

    # sorting 
    for i in range(array_size-1, 0,-1):

        #swap root and last element, then min o max
        swap(0, i)
        heapify(0,i)
        





data = []
heap_sort(data)
print(data)