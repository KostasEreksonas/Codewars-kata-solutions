#!/usr/bin/env python3

import re

def is_uppercase(inp):
    return True if re.search('[a-zA-Z]', inp) == None else inp.isupper()

print(is_uppercase("c"))
print(is_uppercase("C"))
print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))
print(is_uppercase("$%&"))
