#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

last_digit_str = f"{number} is {'-' if number < 0 else ''}{last_digit}"
additional_info = {
    0: "and is 0",
    5: "and is less than 6 and not 0"
}

if last_digit > 5:
    additional_info[last_digit] = "and is greater than 5"
else:
    default_info = additional_info[5]
    additional_info[last_digit] = additional_info.get(last_digit, default_info)

final_info = additional_info[last_digit]
print(f"Last digit of {last_digit_str} {final_info}")
