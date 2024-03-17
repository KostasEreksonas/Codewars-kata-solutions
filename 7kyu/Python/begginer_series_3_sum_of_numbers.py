#!/usr/bin/env python3

def get_sum(a,b):
    _sum = 0
    if a == b:
        return a
    elif b < a:
        _min = b
        _max = a
    else:
        _min = a
        _max = b
    for x in range(_min, _max+1):
        _sum += x
    return _sum

print(get_sum(0, 1))
print(get_sum(0, -1))
print(get_sum(1, 5))
print(get_sum(-1, 5))
