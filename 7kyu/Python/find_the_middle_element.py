#!/usr/bin/env python3

def gimme(input_array):
    tmp = []
    for x in input_array:
        tmp.append(x)
    tmp.sort()
    for x in range(len(tmp)):
        if input_array[x] == tmp[1]:
            return x

print(gimme([2,3,1]))
print(gimme([5,10,14]))
