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
    pass

def quick_sort(lst):
    pass