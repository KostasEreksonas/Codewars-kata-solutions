#!/usr/bin/env python3

def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr) or len(strarr) == 0:
        return ''
    else:
        res = ["".join(strarr[idx: idx + k]) for idx in range(len(strarr) - k + 1)]
        length = 0
        longest = ''
        for x in res:
            if len(x) > length:
                length = len(x)
                longest = x
        return longest

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(longest_consec([], 3))
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))
