#!/usr/share/bin python3

def clean_string(s):
    """Append character to resulting string. If # symbol is matched, delete last character"""
    string = ''
    length = len(s)
    for letter in range(length):
        if (s[letter] != "#"):
            string += s[letter]
        elif (len(string) > 0 and s[letter] == "#"):
            string = string[:-1]
    return string

print(clean_string("abc#d##c"))
print(clean_string("abc####d##c#"))
print(clean_string("#######"))
print(clean_string(""))
