#!/usr/bin/env python3

def dig_pow(n, p):
    _sum = 0
    tmp = n
    digits = []
    while tmp != 0:
        digits.append(tmp % 10)
        tmp //= 10
    digits.reverse()
    for x in range(len(digits)):
        _sum += pow(digits[x],p+x)
    return -1 if _sum % n != 0 else _sum//n

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
print(dig_pow(41, 5))
print(dig_pow(114, 3))
print(dig_pow(8, 3))
