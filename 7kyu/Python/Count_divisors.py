#!/usr/bin/env python3

def divisors(n):
    c = 0
    for x in range(1,n+1):
        if n % x == 0:
            c += 1
    return c

print(divisors(1))
print(divisors(4))
print(divisors(5))
print(divisors(12))
print(divisors(30))
print(divisors(4096))
