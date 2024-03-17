#!/usr/bin/env python3

def enough(cap, on, wait):
    space = cap - on - wait
    return 0 if space >= 0 else abs(space)

print(enough(10, 5, 5))
print(enough(100, 60, 50))
print(enough(20, 5, 5))
