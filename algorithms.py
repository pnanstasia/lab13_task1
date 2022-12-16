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
    pass

def quick_sort(lst):
    """This is a recursive function that takes an unsorted
    list of numbers as input and returns the sorted list.
    >>> quick_sort([3,6,8,4,5,2])
    [2, 3, 4, 5, 6, 8]
    >>> quick_sort([4,9,0,2,4])
    [0, 2, 4, 4, 9]
    >>> quick_sort(['a', 'd', 'b'])
    ['a', 'b', 'd']
    >>> quick_sort([])
    []"""
    if isinstance(lst, list) is False:
        return "Wrong input"
    if len(lst) <= 1:
        return lst
    main_elem = lst[int(len(lst)/2)]
    lefthand = list(filter(lambda x: x < main_elem, lst))
    righthand = list(filter(lambda x: x> main_elem, lst))
    median= [i for i in lst if i == main_elem]
    return quick_sort(lefthand)+ median + quick_sort(righthand)