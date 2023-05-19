#!/usr/share/bin python3

def shorten_to_date(long_date):
    result = long_date.split(",")[0]
    return result

string1 = "Friday May 2, 7pm"
string2 = "Monday April 8, 9pm"

print(f"String1: {string1}, shortened: {shorten_to_date(string1)}")
print(f"String2: {string2}, shortened: {shorten_to_date(string2)}")
