#!/usr/bin/env python3

def narcissistic( value ):
    tmp = value
    count, _sum = [0 for x in range(2)]
    digits = []
    while tmp != 0:
        digits.append(tmp % 10)
        tmp //= 10
        count += 1
    for x in range(count):
        _sum += digits[x] ** count
    if _sum == value:
        return True
    else:
        return False

print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))
