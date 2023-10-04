#!/usr/bin/env python3

def find_uniq(arr):
    # your code here
    arr.sort()
    if arr[0] == arr[1] and arr[0] != arr[-1]:
        return arr[-1]
    elif arr[-1] == arr[-2] and arr[-1] != arr[0]:
        return arr[0]

arr1 = [ 1, 1, 1, 2, 1, 1 ]
arr2 = [ 0, 0, 0.55, 0, 0 ]
arr3 = [ 3, 10, 3, 3, 3 ]

print(f"Highest number in {arr1} is {find_uniq(arr1)}")
print(f"Highest number in {arr2} is {find_uniq(arr2)}")
print(f"Highest number in {arr3} is {find_uniq(arr3)}")
