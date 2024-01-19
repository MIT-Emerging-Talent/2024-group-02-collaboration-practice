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
    if seq_len <=1:
        return sequence
    else:
        pivot= sequence[-1] # Pivot is like the base number that will be used to for comparison
        upper_items=[]
        lower_items=[]
        equal_items=[]
    for i in sequence:
        if i < pivot:
            lower_items.append(i)
        elif i== pivot:
            equal_items.append(i)
        else:
            upper_items.append(i)
    return quick_sort(lower_items) + equal_items + quick_sort(upper_items)