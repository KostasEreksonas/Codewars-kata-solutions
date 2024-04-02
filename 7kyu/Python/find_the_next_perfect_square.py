#!/usr/bin/env python3

import math
def find_next_square(sq):
    root = math.sqrt(sq)
    return (root+1)**2 if root % 1 == 0 else -1

print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(319225))
print(find_next_square(15241383936))
