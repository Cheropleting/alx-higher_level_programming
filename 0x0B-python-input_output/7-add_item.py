#!/usr/bin/python3
""" Module """
import sys
from os import path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    filename = "add_item.json"

    try:
        arg_list = load_from_json_file(filename)
    except:
        arg_list = []

    for arg in sys.argv[1:]:
        arg_list.append(arg)
    save_to_json_file(arg_list, filename)


new_list = []
if path.isfile("add_item.json"):
    new_list = load_from_json_file("add_item.json")
save_to_json_file(new_list + sys.argv[1:], "add_item.json")

