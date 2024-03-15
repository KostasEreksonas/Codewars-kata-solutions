#!/usr/bin/env python3

def odd_or_even(arr):
    if len(arr) == 0 or sum(arr) %2 == 0:
        return 'even'
    else:
        return 'odd'

print(odd_or_even([0, 1, 2]))
print(odd_or_even([0, 1, 3]))
print(odd_or_even([1023, 1, 2]))
