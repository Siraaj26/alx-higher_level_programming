#!/usr/bin/python3
"""
    Defines a function that calculates addition
    of two integers.
"""


def add_integer(a, b=98):
    """Returns the sum of two integers"""

    if isintstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
