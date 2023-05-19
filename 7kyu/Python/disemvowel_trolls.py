#!/usr/bin/env python3

def disemvowel(string_):
    vowels = ['A','a','E','e','I','i','O','o','U','u']
    result = ''
    for x in string_:
        if x not in vowels:
            result += x
    return result

string1="This website is for losers LOL!"
string2="No offense but,\nYour writing is among the worst I've ever read"
string3="First fixed test"

print(f"Full string: {string1}\nDisemvoweled string: {disemvowel(string1)}\n\n")
print(f"Full string: {string2}\nDisemvoweled string: {disemvowel(string2)}\n\n")
print(f"Full string: {string3}\nDisemvoweled string: {disemvowel(string3)}\n\n")
