#!/usr/bin/env python3

def mouth_size(animal):
    animal = animal.lower()
    return 'small' if animal == 'alligator' else 'wide'

print(mouth_size("toucan"))
print(mouth_size("ant bear"))
print(mouth_size("alligator"))
print(mouth_size("aLLiGatOr"))
