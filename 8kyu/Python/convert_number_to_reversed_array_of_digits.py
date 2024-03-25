#!/usr/bin/env python3

def digitize(n):
    d = []
    if n == 0:
        d.append(0)
    else:
        while n != 0:
            d.append(n % 10)
            n //= 10
    return d

print(digitize(35231))
print(digitize(0))
print(digitize(23582357))
print(digitize(984764738))
print(digitize(45762893920))
print(digitize(548702838394))
