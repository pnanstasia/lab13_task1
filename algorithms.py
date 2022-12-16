"""
Work with algorithms in functions
"""

def linear_search(list_of_values, value):
    pass

def merge_sort(lst):
     """Merge sort
    >>> merge_sort([11, 2, 2, 5, 8, 5, 13, 9, 3, 3, 1, 1, 12, 4, 4, 6, 10])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 8, 9, 10, 11, 12, 13]
    >>> merge_sort([1,1,1,1,3])
    >>> merge_sort('3')"""
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
    pass

def quick_sort(lst):
    pass