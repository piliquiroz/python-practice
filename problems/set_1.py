#!/usr/bin/env python
"""The first set of exercises for Pili.

Here are 4 functions that have a description of their function written in their
docstring. Look through the docstring and try to make the function work. You
can test whether the functions work by running this python file: 'python
set_1.py'. The bottom of this file defines tests that your code has to satisfy,
and running this file will show how well you are doing. Feel free to approach
me with questions if anything is unclear.

"""

def is_name(s):
    """Return True when 's' is a name, False otherwise.

    Something is considered a name when it consists of 2 sets of letters
    seperated by a space, with the beginning letter of each set capitalized.

    Names:
    Pili Quiroz
    Apple Briefcase
    AAAA BBBB

    Not names:
    Pili Quiroz3
    apple briefCAse
    thisisnotaname
    this is also not a name

    Hints:

    - Check out the s.isalpha() and s.islower() methods to see what they
    do.

    - This is a complex problem with many steps, break it down into little
    steps first, then solve each little step.

    """
    pass


def reverse_list(xs):
    """Return a list consisting of xs, but in reverse order.

    For example:
    reverse_list([1, 2, 3]) --> [3, 2, 1]
    reverse_list('banana') --> 'ananab'

    Notes:
    - Lists have a l.reverse() method, don't use this.

    """
    pass


def is_palindrome(name):
    """Return True if name is a palindrome, False otherwise.

    A palindrome is a string that is spelled the same forwards and backwards.
    Disregard capitalization for checking for equality.

    Palindromes:
    Bob
    ABBA
    reachcaer
    CaRRAc

    Not palindromes:
    palindrome
    apple
    tree

    Tip:
    - Use your reverse_list function from earlier.
    """
    pass


def count_palindromes(xs):
    """Return the number of palindromes that occur in list 'xs'

    For example:
    count_palindromes(['abba', 'babe', 'Bob']) --> 2
    count_palindromes([]) --> 0
    count_palindromes(['three', 'apples', 'Abba']) --> 1

    """
    pass

#------ Ignore code after this point ------#

# Ignore this for now, this is how we import libraries
import unittest

class TestProblemSolutions(unittest.TestCase):

    def test_is_name(self):
        self.assertTrue(is_name('Pili Quiroz'))
        self.assertTrue(is_name('David Janssen'))
        self.assertTrue(is_name('Cheesecake Factory'))
        self.assertFalse(is_name('Pili1 Quiroz'))
        self.assertFalse(is_name('Pili quiroz'))
        self.assertFalse(is_name('Piliquiroz'))
        self.assertFalse(is_name('Pili Andrea Quiroz'))

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list('banana'), list('ananab'))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('Bob'))
        self.assertFalse(is_palindrome('palindrome'))

    def test_count_palindromes(self):
        self.assertEqual(count_palindromes([]), 0)
        self.assertEqual(count_palindromes(['Abba', 'bob', 'tree']), 2)


if __name__ == '__main__':
    unittest.main()
