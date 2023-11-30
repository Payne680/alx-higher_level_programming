#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Start sum at 0
    total = 0

    # Loop through command-line arguments, skipping the script name (argv[0])
    for arg in argv[1:]:
        # Convert each argument to an integer and add to total
        total += int(arg)

    # Print the sum of all arguments
    print(total)
