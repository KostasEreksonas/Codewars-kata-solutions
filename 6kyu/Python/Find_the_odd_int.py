#!/usr/bin/env python3

def find_it(seq):
    unique = []
    for s in seq:
        if s not in unique:
            unique.append(s)
    for u in unique:
        c = 0
        n = ""
        for s in seq:
            if s == u:
                c += 1
        n = "Even" if c % 2 == 0 else "Odd"
        if n == "Odd":
            result = u
            break
    return result

arr1 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
arr2 = [1,1,2,-2,5,2,4,4,-1,-2,5]

print(f"Odd int: {find_it(arr1)}")
print(f"Odd int: {find_it(arr2)}")
