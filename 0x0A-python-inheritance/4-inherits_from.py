#!/usr/bin/python3
"""Creates an inherited class-checking functions."""


def inherits_from(obj, a_class):
    """Function that checks if an obj is an inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of object to.
    Returns:
        True: if an object is an inherited instance.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
