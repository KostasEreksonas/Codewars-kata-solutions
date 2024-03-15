#!/usr/bin/env python3

def friend(x):
    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result

print(friend(["Ryan", "Kieran", "Mark"]))
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))
