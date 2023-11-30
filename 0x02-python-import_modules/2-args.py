#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args_count = len(argv) - 1

    if args_count == 0:
        print("0 arguments.")
    else:
        print(f"{args_count} {'argument' if args_count == 1 else 'arguments'}:")
        for index, arg in enumerate(argv[1:], start=1):
            print(f"{index}: {arg}")
