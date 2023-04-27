#!/usr/share/bin python3

import re

def valid_phone_number(phone_number):
    pattern = '^\(\d{3}\)\s\d{3}\-\d{4}$'
    x = re.search(pattern, phone_number)
    if (x == None):
        return False
    else:
        return True

number1 = "(123) 456-7890"
number2 = "(1111)555 2345"
number3 = "(098) 123 4567"

print(f"Validity of number {number1} is {valid_phone_number(number1)}")
print(f"Validity of number {number2} is {valid_phone_number(number2)}")
print(f"Validity of number {number3} is {valid_phone_number(number3)}")
