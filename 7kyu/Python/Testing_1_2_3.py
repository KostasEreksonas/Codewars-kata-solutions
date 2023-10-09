#!/usr/bin/env python3

def number(lines):
    result = []
    for x in range(1,len(lines)+1):
        r = str(x) + ': ' + lines[x-1]
        result.append(r)
    return result

print(number([]))
print(number(["a", "b", "c"]))
