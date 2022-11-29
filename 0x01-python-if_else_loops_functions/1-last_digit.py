#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    rm = (-1) * (number % 10)
    number = number * -1
else:
    rm = number % 10

if rm > 5:
    print(f"Last digit of {number:d} is {rm:d} and is greater than 5")
elif rm == 0:
    print(f"Last digit of {number:d} is {rm:d} and is 0")
else:
    print(f"Last digit of {number:d} is {rm:d} and is less than 6 and not 0")
