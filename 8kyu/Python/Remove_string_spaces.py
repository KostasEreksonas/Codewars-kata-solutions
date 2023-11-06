#!/usr/bin/env python3

def no_space(x):
    result = ''
    for char in x:
        if char != ' ':
            result += char
    return result

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'))
print(no_space('8aaaaa dddd r     '))
