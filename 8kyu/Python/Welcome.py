#!/usr/bin/env python3

def greet(language):
    word = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    }
    if language in word:
        return word[language]
    else:
        return 'Welcome'

print(greet('english'))
print(greet('dutch'))
print(greet('IP_ADDRESS_INVALID'))
print(greet(''))
print(greet('2'))
