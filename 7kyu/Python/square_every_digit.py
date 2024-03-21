#!/usr/bin/env python3

def square_digits(num):
    if num == 0:
        return 0
    else:
        digits = []
        z = ''
        while num != 0:
            digits.append((num%10)**2)
            num //= 10
        digits = digits[::-1]
        z = [str(d) for d in digits]
        return int(''.join(z))

print(square_digits(9119))
print(square_digits(0))
print(square_digits(5432568))
