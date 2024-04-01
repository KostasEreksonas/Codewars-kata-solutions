#!/usr/bin/env python3

def move_zeros(lst):
    numbers,zeroes = [[] for x in range(2)]
    for l in lst:
        zeroes.append(l) if l == 0 else numbers.append(l)
    return numbers+zeroes

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([0,0]))
print(move_zeros([0]))
print(move_zeros([]))
