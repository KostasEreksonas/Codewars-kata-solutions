#!/usr/bin/env python3

def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count

string1 = "aeiou"
string2 = "y"
string3 = "bcdfghjklmnpqrstvwxz y"

print(f"{string1} has {get_count(string1)} vowels")
print(f"{string2} has {get_count(string2)} vowels")
print(f"{string3} has {get_count(string3)} vowels")
