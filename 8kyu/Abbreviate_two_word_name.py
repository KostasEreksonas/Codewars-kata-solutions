#!/usr/bin/env python3

def abbrev_name(name):
    name = name.split()
    return name[0][0].upper() + "." + name[1][0].upper()

name1 = "Sam Harris"
name2 = "patrick feenan"
name3 = "Evan C"

print(f"Abbrevation of {name1} is {abbrev_name(name1)}")
print(f"Abbrevation of {name2} is {abbrev_name(name2)}")
print(f"Abbrevation of {name3} is {abbrev_name(name3)}")
