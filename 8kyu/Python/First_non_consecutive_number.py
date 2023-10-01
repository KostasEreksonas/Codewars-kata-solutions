#!/usr/bin/env python3

def first_non_consecutive(arr):
    for x in range(len(arr)-1):
        if arr[x+1]-arr[x] > 1:
            return arr[x+1]

print(first_non_consecutive([1,2,3,4,6,7,8]))
print(first_non_consecutive([1,2,4,5,6,7,8]))
print(first_non_consecutive([1,3,4,5,6,7,8]))
