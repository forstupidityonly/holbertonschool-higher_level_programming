#!/usr/bin/python3
"""for the checker"""
def write_file(filename="", text=""):
    """for the checker"""
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)