#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """
        at prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    delims = ['.', ':', '?']
    string = ""
    itr = 0

    for i in text:
        if not (itr == 0 and i == " "):
            string += i
            itr += 1
        if i in delims:
            string += '\n\n'
            itr = 0
        print(string, end="")
