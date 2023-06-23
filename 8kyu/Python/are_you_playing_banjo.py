#!/usr/bin/env python3

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

name1='martin'
name2='Rikke'
name3='bravo'

print(f"{are_you_playing_banjo(name1)}")
print(f"{are_you_playing_banjo(name2)}")
print(f"{are_you_playing_banjo(name3)}")
