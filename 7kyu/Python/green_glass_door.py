#!/usr/share/bin python3

def step_through_with(s):
    # You can't bring your code, but you can bring this comment
    for i in range(len(s)):
        if (i> 0 and s[i-1] == s[i]):
            return True
    return False

string1 = "moon"
string2 = "sun"
string3 = "letter"
string4 = "card"
string5 = "character"

print(f"String {string1} returns: {step_through_with(string1)}")
print(f"String {string2} returns: {step_through_with(string2)}")
print(f"String {string3} returns: {step_through_with(string3)}")
print(f"String {string4} returns: {step_through_with(string4)}")
print(f"String {string5} returns: {step_through_with(string5)}")
