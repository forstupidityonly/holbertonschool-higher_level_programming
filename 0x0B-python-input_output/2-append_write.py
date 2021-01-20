#!/usr/bin/python3
"""for the checker"""
def append_write(filename="", text=""):
    """for the checker"""
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)