#!/usr/bin/python3
def search_replace(input_list, search_item, replace_item):
    new_list = [replace_item if x == search_item else x for x in input_list]
    return new_list
