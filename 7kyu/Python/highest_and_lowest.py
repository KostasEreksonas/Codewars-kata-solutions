#!/usr/bin/env python3

def high_and_low(numbers):
    numbers = numbers.split(" ")
    arr = []
    for x in numbers:
        arr.append(int(x))
    result = str(max(arr)) + ' ' + str(min(arr))
    return result

print(high_and_low("1 -1 2 -2 3 -3 4 7"))
print(high_and_low("1 2 3"))
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
