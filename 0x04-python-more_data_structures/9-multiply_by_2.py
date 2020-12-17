#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for itr in copy:
        copy[itr] *= 2
    return copy
