"""
Work with algorithms in functions
"""

def linear_search(list_of_values, value):
    pass

def merge_sort(lst):
    pass

def binary_search(list_of_values, value):
    """
    Function conducts a binary search.
    >>> binary_search([2, 3, 7, 9, 13], 7)
    2
    >>> binary_search(['Andrew', 'Camila', 'Ethan', 'Katelyn', 'Opera', 'Yasmine'], 'Opera')
    4
    >>> binary_search([8, 12, 18, 23], 42)
    -1
    """
    the_lowest = 0
    the_highest = len(list_of_values) - 1
    while the_lowest <= the_highest:
        midpoint = the_lowest + (the_highest - the_lowest)//2
        if list_of_values[midpoint] == value:
            return midpoint
        elif list_of_values[midpoint] < value:
            the_lowest = midpoint + 1
        else:
            the_highest = midpoint + 1
    return -1
    

def selection_sort(lst):
    pass

def quick_sort(lst):
    pass