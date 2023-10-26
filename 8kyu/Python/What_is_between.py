#!/usr/bin/env python3

def between(a,b):
    result = []
    for x in range(a,b+1):
        result.append(x)
    return result

print(between(1, 4))
print(between(-2, 2))
