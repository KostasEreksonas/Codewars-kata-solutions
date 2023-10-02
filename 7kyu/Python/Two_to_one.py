#!/usr/bin/env python3

def longest(a1, a2):
    uniq = []
    for x in a1:
        if x not in uniq:
            uniq.append(x)
    for x in a2:
        if x not in uniq:
            uniq.append(x)
    uniq.sort()
    return "".join(uniq)

print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
print(longest("inmanylanguages", "theresapairoffunctions"))
