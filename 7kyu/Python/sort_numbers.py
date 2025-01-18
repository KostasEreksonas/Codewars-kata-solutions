#!/usr/bin/env python3

def solution(nums):
    if nums == None:
        return []
    else:
        nums.sort()
        return nums

arr1 = [1,2,3,10,5]
arr2 = None
arr3 = []
arr4 = [20, 2, 10]
arr5 = [2, 20, 10]

print(f"{arr1}")
print(f"{arr2}")
print(f"{arr3}")
print(f"{arr4}")
print(f"{arr5}")
