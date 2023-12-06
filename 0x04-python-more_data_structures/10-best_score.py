#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = max(a_dictionary.values())
    keys_with_max_value = [key for key, value in a_dictionary.items() if value == max_value]

    return keys_with_max_value[0] if len(keys_with_max_value) == 1 else keys_with_max_value
