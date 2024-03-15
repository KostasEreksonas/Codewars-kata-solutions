#!/usr/bin/env python3

def is_isogram(string):
    string = string.lower()
    result = {}
    for x in string:
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1
    for x in result:
        if result[x] != 1:
            return False
    return True

str1 = "Dermatoglyphics"
str2 = "isogram"
str3 = "aba"

print(f"Is {str1} an isogram: {is_isogram(str1)}")
print(f"Is {str2} an isogram: {is_isogram(str2)}")
print(f"Is {str3} an isogram: {is_isogram(str3)}")
