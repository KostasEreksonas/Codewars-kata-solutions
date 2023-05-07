#!/usr/bin/env python3

def find_caterer(budget, people):
    cost_1, cost_2, cost_3 = [0 for i in range(3)]
    cost_1 = 15*people
    cost_2 = 20*people
    cost_3 = 30*people
    if people > 60:
        cost_3 *= 0.8
    if people == 0 or budget < cost_1:
        return -1
    elif budget >= cost_1 and budget < cost_2 and budget < cost_3:
        return 1
    elif budget >= cost_2 and budget < cost_3:
        return 2
    elif budget >= cost_3:
        return 3

budget1 = 150
budget2 = 1500
budget3 = 200

people1 = 10
people2 = 60
people3 = 5

print(f"Budget: {budget1}, people: {people1}, caterer: {find_caterer(budget1, people1)}")
print(f"Budget: {budget2}, people: {people2}, caterer: {find_caterer(budget2, people2)}")
print(f"Budget: {budget3}, people: {people3}, caterer: {find_caterer(budget3, people3)}")
