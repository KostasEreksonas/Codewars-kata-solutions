#!/usr/bin/env python3

def title_case(title, minor_words=''):
    title = title.lower()
    minor_words = minor_words.lower()
    title = title.split()
    minor_words = minor_words.split()
    result = []
    for x in range(0,len(title)):
        if x == 0 or title[x] not in minor_words:
            result.append(title[x].capitalize())
        else:
            result.append(title[x])
    return " ".join(result)

print(title_case(''))
print(title_case('a clash of KINGS'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))
