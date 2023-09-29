#!/usr/bin/env python3

def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False

print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a123"))
