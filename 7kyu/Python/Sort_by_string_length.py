#!/usr/bin/env python3

def sort_by_length(arr):
    strings = {}
    result = []
    for x in arr:
        strings[len(x)] = x
    sorted_strings = dict(sorted(strings.items()))
    for x in sorted_strings:
        result.append(sorted_strings[x])
    return result

print(sort_by_length(["beg", "life", "i", "to"]))
print(sort_by_length(["", "moderately", "brains", "pizza"]))
print(sort_by_length(["longer", "longest", "short"]))
