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

# Ignore this for now, this is how we import libraries
import unittest

class TestProblemSolutions(unittest.TestCase):

    def test_id(self):
        self.assertEqual(id("hello"), "hello")
        self.assertEqual(id(3), 3)

    def test_add1(self):
        self.assertEqual(add1(1), 2)
        self.assertEqual(add1(2), 3)

    def test_add3(self):
        self.assertEqual(add3(0), 3)
        self.assertEqual(add3(1), 4)

    def test_concat_strings(self):
        self.assertEqual(concat_strings("foo", "bar"), "foobar")

    def test_is_negative(self):
        self.assertTrue(is_negative(-3))
        self.assertFalse(is_negative(3))

    def test_count_positive(self):
        self.assertEqual(count_positive([1, -3, 3, 8, -7]), 3)

    def test_reverse_tuple(self):
        self.assertEqual(reverse_tuple((1, 3)), (3, 1))
        self.assertEqual(reverse_tuple((2, 4)), (4, 2))

    def test_is_between(self):
        self.assertTrue(is_between(3, 2, 4))
        self.assertFalse(is_between(3, 3, 4))
        self.assertFalse(is_between(3, 2, 3))
        self.assertFalse(is_between(3, 4, 2))

    def test_is_ordered(self):
        self.assertTrue(is_ordered([1, 2, 3]))
        self.assertTrue(is_ordered([1, 10, 13]))
        self.assertFalse(is_ordered([2, 1, 3]))


if __name__ == '__main__':
    unittest.main()
