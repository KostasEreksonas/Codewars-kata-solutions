#!/usr/share/bin python3

def digital_root(n):
    """Sum every digit of a given number, if it's > 9, restart with the sum"""
    sum = 0
    while (n > 0):
        sum += n % 10
        n = n // 10
        if (n == 0 and sum > 9):
            n = sum
            sum = 0
    return sum

print(f"Digital root of 16 is: {digital_root(16)}")
print(f"Digital root of 942 is: {digital_root(942)}")
print(f"Digital root of 132189 is: {digital_root(132189)}")
print(f"Digital root of 493193 is: {digital_root(493193)}")
