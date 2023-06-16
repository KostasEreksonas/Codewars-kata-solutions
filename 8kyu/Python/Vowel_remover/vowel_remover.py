#!/usr/bin/env python3

def shortcut(s):
    vowels = 'aeiou'
    result = ''
    for x in s:
        if x not in vowels:
            result += x
    return result

str1="hello"
str2="codewars"
str3="goodbye"
str4="HELLO"

print(f"{str1}: {shortcut(str1)}")
print(f"{str2}: {shortcut(str2)}")
print(f"{str3}: {shortcut(str3)}")
print(f"{str4}: {shortcut(str4)}")
