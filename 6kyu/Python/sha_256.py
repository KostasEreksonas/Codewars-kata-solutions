#!/usr/share/bin python3

import hashlib

def to_sha256(s):
    hash = hashlib.sha256(s.encode('utf-8')).hexdigest()
    return hash

string1 = 'Hello'
string2 = 'Testing'
string3 = 'A string for a test'

print(f"Hash of \"{string1}\" is: {to_sha256(string1)}")
print(f"Hash of \"{string2}\" is: {to_sha256(string2)}")
print(f"Hash of \"{string3}\" is: {to_sha256(string3)}")
