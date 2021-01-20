#!/usr/bin.python3
"""stuff for checker"""


def inherits_from(obj, a_class):
    """stuff for checker"""
    if(isinstance(type(obj), a_class)):
        return(True)
    elif(not isinstance(obj, a_class)):
        return(True)
    return(False)
