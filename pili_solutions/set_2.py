#!/usr/bin/env python
"""set_2.py

More exercises for Pili. These are probably a lot easier than set_1.

"""

# These variables are used in some of the exercises
DOGS = [('Fido', 'nice'), ('Bruno', 'brown'), ('Beertje', 'dead')]


def capitalize(s):
    """Return s with all capitals

    For example:
    capitalize("david") -> "DAVID"
    capitalize("PiLi") -> "PILI"

    """
    return s.upper()


def is_odd(s):
    """Return True if a number is odd, otherwise False

    Please consider 0 to be an even number.

    """
    return s % 2 == 1



def filter_even(xs):
    """Return a list of numbers by removing all the odd numbers.

    Leave the original list unchanged.

    For example:
    filter_even([1, 2, 3, 4, 5]) -> [2, 4]
    filter_even([0, 2, 4, 1, 3, 5]) -> [0, 2, 4]

    """
    out = []
    for x in xs:
        if x % 2 == 0:
            out.append(x)
    return out


def my_all(xs):
    """Return True if all of the booleans in xs are True.

    Do not use the inbuild 'all' function

    For example:
    my_all([]) -> True
    my_all([True, False]) -> False
    my_all([True, True, True]) -> True

    """
    for x in xs:
        if x == False:
            return False
    return True


def my_any(xs):
    """Return True if any of the booleans in xs is True.

    Do not use the inbuilt 'any' function

    For example:
    my_any([]) -> False
    my_any([True, False]) -> True
    my_any([False, False, False]) -> False

    """
    for x in xs:
        if x == True:
            return True
    return False


def cap_letter(c):
    return chr(ord(c)-32)




def my_capitalize(s):
    """Return a string converted to all-caps.

    Do not use the inbuilt .capitalize or .upper methods.

    This one is harder.

    Hints:
      - you can convert characters to the number that encodes them using ord
      - you can convert numbers to the characters they encode by using chr
      - the relationship between the 'a..z' and 'A..Z' letters is straightforward

    Play around with ord('d') and chr(100) and ord('D').

    """
    out = ''
    for c in s:
        c_ord = ord(c)
        if c_ord in range(97, 123):
            out = out + chr(c_ord-32)
        else:
            out = out + c
    return out


def make_dict(name, age, hobby):
    """Return a dictionary containing a name, age, and hobby.

    For example:
    make_dict('David', 32, 'Haskell') -> {'name': 'David', 'age': 32, 'hobby': 'Haskell'}

    """
    return {'name': name, 'age': age, 'hobby': hobby}


def filter_strings(xs):
    """Return a list of all the strings in xs.

    For example:
    filter_strings(["david", 3, True, "pili"]) -> ["david", "pili"]

    """
    out = []
    for x in xs:
        if isinstance(x, str):
            out.append(x)
    return out


def describe_dog(name):
    """Return the trait associated with the name of the dog.

    Look up the dog's trait in the DOGS variable defined at the top of this
    module. If the dog's name doesn't exist in the list, just return the string
    'no such dog'. Make the dog's name *not* be case-sensitive (disregard any
    capitalization, so 'BeErTje' and 'beertje' and 'BEERTJE' should all be
    equivalent)

    For example:
    describe_dog('beertje') -> 'dead'
    describe_dog('BrunO') -> 'brown'
    describe_dog('Pluto') -> 'no such dog'

    """
    dogs = {'beertje': 'dead',
            'bruno': 'brown',
            'fido': 'nice'}
    return dogs.get(name.lower(), 'no such dog')

    # for k, v in dogs.items():
    #     return v


#------ Ignore code after this point ------#

if __name__ == '__main__':
    from tests import test_set_2
    import sys
    this = sys.modules[__name__]
    test_set_2.run(this)
