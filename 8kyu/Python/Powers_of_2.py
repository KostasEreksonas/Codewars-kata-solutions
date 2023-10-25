#!/usr/bin/env python3

def powers_of_two(n):
    result = []
    for x in range(n+1):
        result.append(pow(2,x))
    return result

print(powers_of_two(0))
print(powers_of_two(1))
print(powers_of_two(2))
print(powers_of_two(3))
print(powers_of_two(4))
print(powers_of_two(5))
