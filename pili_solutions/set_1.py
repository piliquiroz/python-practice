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

    - Check out the is s.isalpha() and s.islower() methods to see what they
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
    out = []
    for y in range(-1, -(len(xs)+1), -1):
        out.append(xs[y])
    return out


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

if __name__ == '__main__':
    from tests import test_set_1
    import sys
    this = sys.modules[__name__]
    test_set_1.run(this)
