#!/usr/bin/env python3

def count_sheeps(sheep):
  # TODO May the force be with you
    count = 0
    for x in sheep:
        if x == True:
            count += 1
    return count

print(f"Sheep count: {count_sheeps([True,  True,  True,  False, True,  True,  True,  True, True,  False, True,  False, True,  False, False, True, True,  True,  True,  True, False, False, True,  True])}")
