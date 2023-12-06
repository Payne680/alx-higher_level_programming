#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dictionary = {k: v for k, v in a_dictionary.items() if k != key}
    return new_dictionary
