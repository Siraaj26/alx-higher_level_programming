#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num_end = (number % 10)
else:
    num_end = ((number * -1) % 10) * -1

if number_end > 5:
    print(f"Last digit of {number} is {num_end} and is greater than 5")
elif number_end == 0:
    print(f"Last digit of {number} is {num_end} and is 0")
elif number_end != 0 and number_end < 6:
    print(f"Last digit of {number} is {num_end} and is less than 6 and not 0")
