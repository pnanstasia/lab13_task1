"""
Work with algorithms in functions
"""

def linear_search(list_of_values, value):
    """
    Linear search of a value in a list. Return an index
    if the value. If the value not in list, return 1.
    >>> linear_search([1, 2, 3, 4, 5, 6], 3)
    2
    >>> linear_search(["flower", "sky", "grass"], "flower")
    0
    >>> linear_search([56, 89, 100, 101], 102)
    1
    >>> linear_search("123", 3)
    """
    if not isinstance(list_of_values, list):
        return None
    elif value not in list_of_values:
        return 1
    for index, element in enumerate(list_of_values):
        if element == value:
            return index

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
