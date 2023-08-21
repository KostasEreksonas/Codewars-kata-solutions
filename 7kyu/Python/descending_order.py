#!/usr/bin/env python3

def descending_order(num):
    # Bust a move right here
    arr = []
    result = 0
    while int(num) != 0:
        arr.append(num%10)
        num = num//10
    arr.sort(reverse=True)
    for x in range(len(arr)):
        result *= 10
        result += arr[x]
    return result

print(f"{descending_order(1)}")
print(f"{descending_order(123)}")
print(f"{descending_order(12345)}")
