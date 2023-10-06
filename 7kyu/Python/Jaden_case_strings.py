#!/usr/bin/env python3

def to_jaden_case(string):
    arr = string.split()
    newarr = []
    for word in arr:
        newarr.append(word.capitalize())
    return " ".join(newarr)

print(to_jaden_case("Sample text"))
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
print(to_jaden_case("Another sample text"))
