#!/usr/bin/python3
letters = ''.join(
    f"{chr(char)}" for char in range(ord('a'), ord('z') + 1)
)
print(letters, end='')
