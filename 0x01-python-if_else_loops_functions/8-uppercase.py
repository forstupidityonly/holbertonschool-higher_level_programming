#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            newstring += chr(ord(element) - 32)
        else:
            newstring += element
    print("{}".format(newstring))
