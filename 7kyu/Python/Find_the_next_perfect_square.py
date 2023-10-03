#!/usr/bin/env python3

import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    square = math.sqrt(sq)
    if square % 1 > 0:
        return -1
    else:
        return (square+1)**2

print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(319225))
print(find_next_square(15241383936))
