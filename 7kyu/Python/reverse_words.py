#!/usr/bin/env python3

def reverse_words(text):
    text = text.split(" ")
    words = []
    for word in text:
        words.append(word[::-1])
    return ' '.join(words)

print(reverse_words("The quick brown fox jumps over the lazy dog."))
print(reverse_words("apple"))
print(reverse_words("a b c d"))
print(reverse_words("double  spaced  words"))
