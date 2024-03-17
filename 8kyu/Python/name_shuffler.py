#!/usr/bin/env python3

def name_shuffler(str_):
    name = str_.split()
    return ' '.join([name[1], name[0]])

print(name_shuffler("john McClane"))
print(name_shuffler("Mary jeggins"))
print(name_shuffler("tom jerry"))
