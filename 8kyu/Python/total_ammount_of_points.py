#!/usr/bin/env python3

def points(games):
    total = 0
    for game in games:
        if game[0] > game[2]:
            total += 3
        elif game[0] == game[2]:
            total += 1
    return total

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))
