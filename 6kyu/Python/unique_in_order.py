#!/usr/bin/env python3

def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    else:
        result = [sequence[0]]
        current = result[0]
        for s in sequence:
            if s != current:
                current = s
                result.append(current)
        return result

print(unique_in_order("AABBCC"))
print(unique_in_order("AAAABBCCCDAABBB"))
print(unique_in_order("112233"))
