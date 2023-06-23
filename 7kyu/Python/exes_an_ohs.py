#!/usr/bin/env python3

def xo(s):
    s = s.lower()
    c_x, c_o = [0 for x in range(2)]
    for x in s:
        if x == 'x':
            c_x += 1
        elif x == 'o':
            c_o += 1
    if c_x == c_o:
        return True
    else:
        return False

str1="ooxx"
str2="xooxx"
str3="ooxXm"
str4="zpzpzpp"
str5="zzoo"

print(f"{str1} returns {xo(str1)}")
print(f"{str2} returns {xo(str2)}")
print(f"{str3} returns {xo(str3)}")
print(f"{str4} returns {xo(str4)}")
print(f"{str5} returns {xo(str5)}")
