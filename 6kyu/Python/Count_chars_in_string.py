#!/usr/bin/env python3

def count(s):
    if not s:
        return {}
    else:
        result = {}
        for x in s:
            if x in result:
                result[x] += 1
            else:
                result[x] = 1
    return result

str1='aba'
str2='aabb'
str3='aaabbc'

print(f"{str1}, {count(str1)}")
print(f"{str2}, {count(str2)}")
print(f"{str3}, {count(str3)}")
