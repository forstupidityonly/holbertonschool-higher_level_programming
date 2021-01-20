#!/usr/bin/python3
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

try:
    list_obj = load(file_name)
except:
    list_obj = []

for i in range(1, len(sys.argv)):
    list_obj.append(sys.argv[i])

save(list_obj, file_name)