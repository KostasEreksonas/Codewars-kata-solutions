#!/usr/bin/env python3

def is_palindrome(s):
    s = s.lower()
    reverse = []
    string = s.split()
    for letter in string:
        reverse += letter
    print(f"Reverse: {reverse}, String: {s}")
    if ("".join(reverse[::-1]) == s):
        return True
    else:
        return False

print(is_palindrome('a'))
print(is_palindrome('abc'))
print(is_palindrome('abcba'))
