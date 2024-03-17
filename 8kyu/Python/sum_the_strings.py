#!/usr/bin/env python3

def sum_str(a, b):
    if not a:
        if not b:
            return '0'
        return b
    elif not b:
        return a
    else:
        return str(int(a) + int(b))

print(sum_str("4","5"))
print(sum_str("34","5"))
