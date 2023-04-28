#!/usr/share/bin python3

def nth_even(n):
    return 2*n-2

numbers = [1, 2, 3, 100, 1298734]

for number in numbers:
    print(f"{number} even number is: {nth_even(number)}")
