#!/usr/bin/env python3

def integrate(coefficient, exponent):
    integral = int(coefficient/(exponent+1))
    return str(integral)+'x^'+str(exponent+1)

print(f"Integral: {integrate(3,2)}")
print(f"Integral: {integrate(12,5)}")
print(f"Integral: {integrate(20,1)}")
