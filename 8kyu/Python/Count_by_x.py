#!/usr/bin/env python3

def count_by(x, n):
    tmp = x
    result = []
    for i in range(n):
        result.append(x)
        x += tmp
    return result

print(count_by(1, 5))
print(count_by(2, 5))
print(count_by(3, 5))
print(count_by(50, 5))
print(count_by(100, 5))
