#!/usr/bin/python3
if __name__ == "__main__":
    from importlib import import_module

    module = import_module("0-add")
    add = module.add

    a = 1
    b = 2

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
