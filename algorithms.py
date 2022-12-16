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
    """
    Merge sort
    >>> merge_sort([11, 2, 2, 5, 8, 5, 13, 9, 3, 3, 1, 1, 12, 4, 4, 6, 10])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 8, 9, 10, 11, 12, 13]
    >>> merge_sort([1,1,1,1,3])
    >>> merge_sort('3')
    """
    if not isinstance(lst, list):
        return None

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    lst1 = lst[:mid]
    lst2 = lst[mid:]
    merge_sort(lst1)
    merge_sort(lst2)
    first = 0
    second = 0
    index = 0

    while first < len(lst1) and second < len(lst2):
        if lst1[first] < lst2[second]:
            lst[index] = lst1[first]
            first += 1
        else:
            lst[index] = lst2[second]
            second += 1
        index += 1
    
    while first < len(lst1):
        lst[index] = lst1[first]
        first += 1
        index += 1

    while second < len(lst2):
        lst[index] = lst2[second]
        second += 1
        index += 1
    return lst

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
