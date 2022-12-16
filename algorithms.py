"""
Work with algorithms in functions
"""

def linear_search(list_of_values, value):
    pass

def merge_sort(lst):
    pass

def binary_search(list_of_values, value):
    pass

def selection_sort(lst):
    """
    Function for selection sort
    >>> selection_sort([7, 5, 8, 19, 13, 2, 2, 10])
    [2, 2, 5, 7, 8, 10, 13, 19]
    >>> selection_sort([5, 18, 7, 4, 11, 6])
    [4, 5, 6, 7, 11, 18]
    >>> selection_sort(12)
    """
    if not isinstance(lst, list):
        return None
    start = 0
    while start < len(lst):
        min_el = lst[start]
        for i in lst[start:]:
            if i <= min_el:
                min_el = i
                ind=lst[start:].index(min_el)
                ind+=start
        lst[ind] = lst[start]
        lst[start] = min_el
        start += 1
    return lst

def quick_sort(lst):
    pass
