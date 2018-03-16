#!/usr/bin/env python
"""The prequel to the first set of exercises, this time a lot easier.

Just like in set_1, go through the function definitions, and complete the
functions to perform the tasks they are described to have in the docstring. The
bottom of this module contains a set of unittests that will check your
exercises for you.

"""


def id(x):
    """Return x unchanged"""
    pass


def add1(i):
    """Take a number i, and return that number plus 1"""
    pass


def add3(i):
    """Take a number i, and return that number plus 3

    Note: you are only allowed to use the add1 function, do not use + or -.

    """
    pass


def concat_strings(a, b):
    """Take two strings and glue them together.

    For example:
    concat_strings("hello", "world") -> "helloworld"

    """
    pass


def is_negative(i):
    """Return True if i is smaller than 0, otherwise False"""
    pass


def count_positive(xs):
    """Return a count of how many numbers in a list are above 0

    For example:
    count_positive([1, -3, 3, 8, -7]) -> 3
    """
    pass


def reverse_tuple(a):
    """Return 2-tuple a reversed.

    For example:
    reverse_tuple((1, 3)) -> (3, 1)
    reverse_tuple((2, 4)) -> (2, 4)

    """
    pass


def is_between(i, lower, upper):
    """Return whether number i is greater than lower, but smaller than upper.

    For example:
    is_between(3, 2, 4) -> True
    is_between(3, 3, 4) -> False
    is_between(3, 2, 3) -> False
    is_between(3, 4, 2) -> False

    """
    pass


def is_ordered(xs):
    """Return whether a list is in ascending order.

    For example:
    is_ordered([1, 2, 3]) -> True
    is_ordered([1, 10, 13]) -> True
    is_ordered([2, 1, 3]) -> False

    """
    pass


#------ Ignore code after this point ------#

if __name__ == '__main__':
    from tests import test_set_0
    import sys
    this = sys.modules[__name__]
    test_set_0.run(this)
