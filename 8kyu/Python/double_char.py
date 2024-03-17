#!/usr/bin/env python3

def double_char(s):
    result = ''
    for x in s:
        result += 2*x
    return result

print(double_char("Hello, World!"))
print(double_char("Test String"))
print(double_char("123"))
