#!/usr/share/bin python3

from itertools import combinations

def choose_best_sum(t, k, ls):
    #print(f"Maximum sum of distances: {t}, number of towns to visit: {k}, list of distances: {ls}")
    sum = 0
    combination = combinations(ls, k)
    for values in combination:
        temp = 0
        for value in values:
            temp += value
        if (temp <= t and temp > sum):
            sum = temp
    if (sum != 0):
        return sum
    else:
        return None

"""List of distances"""
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

"""Maximum sum of distance"""
t1 = 230
t2 = 430
t3 = 430

"""Number of towns to visit"""
k1 = 4
k2 = 5
k3 = 8

print(f"Max distance: {t1}, number of towns: {k1}, maximum sum: {choose_best_sum(t1, k1, xs)}")
print(f"Max distance: {t2}, number of towns: {k2}, maximum sum: {choose_best_sum(t2, k2, xs)}")
print(f"Max distance: {t3}, number of towns: {k3}, maximum sum: {choose_best_sum(t3, k3, xs)}")
