#!/usr/share/bin python3

def generate_hashtag(s):
    #your code here
    words = s.split() # Split words by whitespace
    string = "#"
    for word in words:
        word = word.lower().capitalize()
        string += word
    if (len(string) > 140 or string == "#"):
        return False
    else:
        return string

string1 = " Hello there thanks for trying my Kata"
string2 = "    Hello     World   "
string3 = ""

print(f"String \"{string1}\" is: {generate_hashtag(string1)}")
print(f"String \"{string2}\" is: {generate_hashtag(string2)}")
print(f"String \"{string3}\" is: {generate_hashtag(string3)}")
