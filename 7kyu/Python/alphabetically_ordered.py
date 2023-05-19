#!/usr/bin/env python3

def alphabetic(s):
    for i in range(len(s)):
        if i == 0:
            prev = s[i]
        else:
            if ord(prev) > ord(s[i]):
                return False
            else:
                prev = s[i]
    return True

string1 = "asd"
string2 = "codewars"
string3 = "door"
string4 = "cell"
string5 = "s"

print(f"String: {string1}, result: {alphabetic(string1)}")
print(f"String: {string2}, result: {alphabetic(string2)}")
print(f"String: {string3}, result: {alphabetic(string3)}")
print(f"String: {string4}, result: {alphabetic(string4)}")
print(f"String: {string5}, result: {alphabetic(string5)}")
