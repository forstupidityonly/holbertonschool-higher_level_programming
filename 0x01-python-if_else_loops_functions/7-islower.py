#!/usr/bin/env python3
def islower(c):
    lett = ord(c)
    if lett >= 97 and lett <= 122:
        return (True)
    elif lett >= 65 and lett <= 90:
        return (False)
