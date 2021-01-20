#!/usr/bin/python3
"""cant use isinstance bc that checks for inheritence and this bull
asked for exact type match"""


def is_same_class(obj, a_class):
    """stuff for checker"""
    return type(obj) is a_class