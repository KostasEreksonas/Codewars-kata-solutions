#!/usr/bin/env python3

def tower_builder(n_floors):
    # build here
    c = 1
    results = []
    base = 2*n_floors-1
    for floor in range(n_floors):
        s = (base - c)//2
        stars = "*"*c
        spaces = " "*s
        result = spaces + stars + spaces
        results.append(result)
        c += 2
        print(result)
    return results

print(f"{tower_builder(1)}")
print(f"{tower_builder(2)}")
print(f"{tower_builder(3)}")
print(f"{tower_builder(4)}")
print(f"{tower_builder(5)}")
