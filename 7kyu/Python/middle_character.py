#!/usr/bin/env python3

def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2-1]+s[length//2]
    else:
        return s[length//2]

str1='test'
str2='testing'
str3='middle'
str4='A'
str5='of'

print(f"The middle of {str1} is {get_middle(str1)}")
print(f"The middle of {str2} is {get_middle(str2)}")
print(f"The middle of {str3} is {get_middle(str3)}")
print(f"The middle of {str4} is {get_middle(str4)}")
print(f"The middle of {str5} is {get_middle(str5)}")
