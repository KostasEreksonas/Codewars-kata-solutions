#!/usr/bin/env python3

def printer_error(s):
    # your code
    valid = 'abcdefghijklm'
    bad = 0
    for x in s:
        if x not in valid:
            bad += 1
    return f"{bad}/{len(s)}"

s1="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
s2="kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
s3="kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"

print(printer_error(s1))
print(printer_error(s2))
print(printer_error(s3))
