def linear_search(list_of_values, value):
    """
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
            