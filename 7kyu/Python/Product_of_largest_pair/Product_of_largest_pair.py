#!/usr/bin/env python3

def max_product(a):
    x = max(a)
    a.remove(x)
    y = max(a)
    return x * y

arr1=[2, 1, 5, 0, 4, 3]
arr2=[7, 8, 9]
arr3=[33, 231, 454, 11, 9, 99, 57]

print(f"Max product of {arr1} is {max_product(arr1)}")
print(f"Max product of {arr2} is {max_product(arr2)}")
print(f"Max product of {arr3} is {max_product(arr3)}")
