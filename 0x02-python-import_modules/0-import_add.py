#!/usr/bin/python3
from importlib import import_module

module = import_module("0-add")
add = module.add

a = 1
b = 2

result = add(a, b)
print("{} + {} = {}".format(a, b, result))
