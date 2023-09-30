#!/usr/bin/env python3

def solution(s):
    words = []
    word = ''
    for x in s:
        if x.islower() == True:
            word += x
        else:
            words.append(word)
            word = ''
            word += x
    words.append(word)
    return " ".join(words)

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
