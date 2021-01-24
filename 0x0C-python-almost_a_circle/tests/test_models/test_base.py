the ''0-add_integer'' module
============================

using ''add_integer''
---------------------

First import ''add_integer'':

    >>> add_integer = __import__('0-add_integer').add_integer

test: regular:

    >>> add_integer(1, 2)
    3
