#!/usr/bin/python3
"""for the checker"""
def save_to_json_file(my_obj, filename):
    """for the checker"""
    import json
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(json.dumps(my_obj))