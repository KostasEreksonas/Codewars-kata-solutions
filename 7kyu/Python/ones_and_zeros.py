#!/usr/bin/env python3

def binary_array_to_number(arr):
    _sum = 0
    for a in range(len(arr)):
        _sum += 2**(len(arr)-1-a) if arr[a] == 1 else 0
    return _sum

print(binary_array_to_number([0,0,0,1]))
print(binary_array_to_number([0,0,1,0]))
print(binary_array_to_number([1,1,1,1]))
print(binary_array_to_number([0,1,1,0]))
