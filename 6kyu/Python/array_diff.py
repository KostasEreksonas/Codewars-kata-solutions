#!/usr/bin/env python3

def array_diff(a, b):
    c = [i for i in a if i not in b]
    return c

a1 = [1,2]
a2 = [1]
b1 = [1,2,2,2,3]
b2 = [2]

print(f"Difference between {a1} and {a2} is {array_diff(a1,a2)}")
print(f"Difference between {b1} and {b2} is {array_diff(b1,b2)}")
