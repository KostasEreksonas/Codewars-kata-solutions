#!/usr/bin/env python3

def alphabet_position(text):
    text = text.lower()
    keys = [chr(x) for x in range(97,123)]
    values = [x for x in range(1,27)]
    alphabet = {}
    result = []
    for i in range(len(keys)):
        alphabet[keys[i]] = values[i]
    for x in text:
        if x in alphabet.keys():
            result.append(str(alphabet[x]))
    return ' '.join(result)

print(alphabet_position("The sunset sets at twelve o' clockThe sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
