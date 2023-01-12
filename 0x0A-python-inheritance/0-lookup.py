#!/usr/bin/python3
"""creat an object attribute lookup function."""

def lookup(obj):
    """Function that returns a list of obj's attributes"""
    return (dir(obj))
