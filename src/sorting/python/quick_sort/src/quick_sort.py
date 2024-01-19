def quick_sort(iterable):
    """Sorts an iterable (list, tuple, set, or any object that behaves like iterable).
    
    If the input is not a list, it is converted to a list and assigned to the 'sequence' variable.
    
    Parameters:
        iterable: Iterable object to be sorted.
        
    Returns:
        list: Sorted list.
        quick_sort([3,2,5,7])
        return=[2,3,5,7]
        quick_sort(("back"))
        return 'a','b', 'c', 'k' """

    try:
        if isinstance(iterable, str):
            sequence = list(iterable)
        else:
            sequence= list(iterable)
    except TypeError:
        raise TypeError("Input must be convertible to a list")
    seq_len= len(sequence)
    #if the list has 1 element or is empty it will be already sorted
    if seq_len <=1:  
        return sequence  
    else: #Partition the array into three parts: elements less than, equal to, and greater than the pivot.
    
        pivot= sequence[-1] # Pivot is like the base number that will be used to for comparison
        upper_items=[]
        lower_items=[]
        equal_items=[]
    # Then we compare each element in the sequence with the pivot    
    for i in sequence:

       # if the lement is less than the pivot it is added to left side of the pivot at because it is lower than the pivot, otherwise on the right which is upper_items. 
        if i < pivot:
            lower_items.append(i)
        elif i== pivot:
            equal_items.append(i)
        else:
            upper_items.append(i)
            
    #Recursively apply quicksort to the left and right sub-arrays then concatenate the results.
    return quick_sort(lower_items) + equal_items + quick_sort(upper_items)