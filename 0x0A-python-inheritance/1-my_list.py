#!/usr/bin/python3
"""Creates an inherited list class; MyList."""


class MyList(list):
    """print sorted values for the built in class; list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
