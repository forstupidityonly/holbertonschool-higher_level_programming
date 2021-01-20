#!/usr/bin/python3
"""for the checker"""
def load_from_json_file(filename):
    """for the checker"""
    import json
    with open(filename, "r", encoding="UTF-8") as file:
        return(json.load(file))