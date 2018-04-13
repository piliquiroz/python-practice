#!/usr/bin/env python
"""set_3.py

More exercises for the Pili, this contains:
- More complex exercises
- Basic use of modules
- Basic file IO
"""


import os.path

FOO_FILE = os.path.abspath('../files/foo.txt')


def write_number(n):
    """Return the string representation of any number between 1 and an octillion.

    - Do not use any capitals.
    - Hyphenate all compound numbers from twenty-one through ninety-nine

    Example:
    write_number(13132) -> "thirteen thousand one hundred thirty-two"
    write_number(19) -> "nineteen"
    write_number(21234567890987) ->
       "twenty-one trillion two hundred thirty-four billion five hundred
        sixety-seven million eight hundred ninety thousand nine hundred eighty-seven
    write_number(1000001) -> "one million one"

    Tips:
    - http://bmanolov.free.fr/numbers_names.php
    - First write a function that turns numbers under a thousand into text,
      then use that to write 'write_number'.
    - Before that, maybe write a function that turns numbers under one
      hundred into text.
    - Before that, maybe write a function that turns numbers between 0 and 9
      into text.

    """
    pass


def overlapping_keys(d1, d2):
    """Return the set of keys that occur in both dictionaries

    Example:
    overlapping_keys({'a': 1, 'b': 2}, {'a': 'apples', 'c': True}) -> {'a'}
    overlapping_keys({'b': 2}, {'a': 'apples', 'c': True}) -> {}

    Tips:
    - You can use the & operator to intersect 2 sets
    - You can use the viewkeys method on a dictionary to get a set of its keys

    """
    pass


def raise_value_error():
    """Raise a ValueError

    Tips:
    - https://docs.python.org/3/tutorial/errors.html#raising-exceptions

    """
    pass


def join_dicts(*args):
    """Join any number of dictionaries into 1 large dictionary.

    If any overlap exists between any of the dictionaries passed in, raise a ValueError.

    Example:
    join_dicts() -> {}
    join_dicts({'a': 1}) -> {'a': 1}
    join_dicts({'a': 1, 'b': 2}, {'c': 3}) -> {'a': 1, 'b':2, 'c':3}
    join_dicts({'a': 1, {'b': 2}, {'c': 3}) -> {'a': 1, 'b':2, 'c':3}
    join_dicts({'a': 1, {'a': 2}) -> ValueError

    Tips:
    - Use the update method on a dictionary to update its contents with another
        dictionary
    - You can see if two dictionaries overlapping by checking that their
        overlapping keys are empty
    """
    pass


def unique_letters(s):
    """Return True if s contains at most 1 of each character, False otherwise.

    Example:
    unique_letters("abcdefg") -> True
    unique_letters("aa") -> False
    unique_letters("12345 !@#$%^") -> True
    unique_letters("this no wrk") -> False

    Tips:
    - This is very easy when you convert a string to a set

    """
    pass


def import_dame_cinco():
    """Return 5

    Write a new module in this directory called 'dame_cinco.py'. In it, write a
    function called 'dame_ahora'. This function should accept no arguments, and
    simply return the number 5. Then import dame_ahora from dame_cinco in this
    function and return it. (Note, this means: return the actual function, not
    the result of calling the function. If this is unclear, just ask me.)

    """
    pass


def read_foo():
    """Return the contents of foo.txt

    The path to the file is stored in the FOO_FILE variable defined at the top
    of this module.

    """
    pass



#------ Ignore code after this point ------#

if __name__ == '__main__':
    from tests import test_set_3
    import sys
    this = sys.modules[__name__]
    test_set_3.run(this)
