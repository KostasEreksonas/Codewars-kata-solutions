#!/usr/bin/env python3

def rot13(message):
    uppercase = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }
    lowercase = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    result = ''
    for char in message:
        if char in '?!.,<>/\[]{}();:+@~\'\"-_#$^=&*%0123456789 ':
            result += char
        elif char in uppercase:
            encoded_val = uppercase[char]+13
            if encoded_val > uppercase['Z']:
                encoded_val = encoded_val - uppercase['Z']
            result += list(uppercase.keys())[list(uppercase.values()).index(encoded_val)]
        elif char in lowercase:
            encoded_val = lowercase[char]+13
            if encoded_val > lowercase['z']:
                encoded_val = encoded_val - lowercase['z']
            result += list(lowercase.keys())[list(lowercase.values()).index(encoded_val)]
    return result

print(rot13('test'))
print(rot13('Test'))
print(rot13('aA bB zZ 1234 *!?%'))
