#!/usr/bin/env python3

def multiplication_table(size):
    table = []
    for x in range(1,size+1):
        row = []
        for y in range(1,size+1):
            row.append(y*x)
        table.append(row)
    return table

print(multiplication_table(1))
print(multiplication_table(2))
print(multiplication_table(3))
print(multiplication_table(4))
print(multiplication_table(5))
