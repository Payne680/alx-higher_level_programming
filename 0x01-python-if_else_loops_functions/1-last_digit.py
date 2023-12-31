#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

last_digit_str = f"{number} is {'-' if number < 0 else ''}{last_digit}"
additional_info = {
    0: "and is 0",
    5: "and is less than 6 and not 0"
}

if number < 0:
    final_info = "and is less than 6 and not 0"
else:
    final_info = additional_info.get(last_digit, f"and is greater than 5")

print(f"Last digit of {last_digit_str} {final_info}")
