#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]


my_list = [10, 20, 30, 40, 50]
result = element_at(my_list, 2)
print(result)  # Output will be 30
