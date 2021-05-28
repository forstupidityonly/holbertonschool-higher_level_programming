#!/usr/bin/pyhton3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as val:
        sys.stderr.write("Exception: {}\n".format(val))
        return False
