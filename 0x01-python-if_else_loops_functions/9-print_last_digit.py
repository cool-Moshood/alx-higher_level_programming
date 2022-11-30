#!/usr/bin/env python3
def print_last_digit(number):
    last_digit = number % 10

    if number < 0:
        new_number = (-1) * (number)
        last_digit = (new_number % 10)
    print(f"{last_digit:d}", end='')
    return last_digit
