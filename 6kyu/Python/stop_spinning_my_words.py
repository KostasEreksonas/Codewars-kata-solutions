#!/usr/bin/env python3

def spin_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)

print(spin_words("Welcome"))
print(spin_words("to"))
print(spin_words("codewars"))
print(spin_words("Welcome to Codewars"))
