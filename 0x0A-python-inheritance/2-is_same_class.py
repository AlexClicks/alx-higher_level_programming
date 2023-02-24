#!/usr/bin/python3
"""function that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Checing if an object is an instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns: True or False
    """
    if type(obj) == a_class:
        return True
    return False
