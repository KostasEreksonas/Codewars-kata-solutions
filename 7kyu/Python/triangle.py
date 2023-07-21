#!/usr/bin/env python3

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a1 = 1
b1 = 2
c1 = 2

a2 = 7
b2 = 2
c2 = 2

a3 = 1
b3 = 2
c3 = 3

print(f"{a1}, {b1}, {c1} returns {is_triangle(a1,b1,c1)}")
print(f"{a2}, {b2}, {c2} returns {is_triangle(a2,b2,c2)}")
print(f"{a3}, {b3}, {c3} returns {is_triangle(a3,b3,c3)}")
