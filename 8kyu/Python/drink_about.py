#!/usr/bin/env python3

def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age >= 14 and age < 18:
        return 'drink coke'
    elif age >= 18 and age < 21:
        return 'drink beer'
    elif age >= 21:
        return 'drink whisky'

age1 = 13
age2 = 16
age3 = 19
age4 = 22
print(f"Age: {age1}, drink: {people_with_age_drink(age1)}")
print(f"Age: {age2}, drink: {people_with_age_drink(age2)}")
print(f"Age: {age3}, drink: {people_with_age_drink(age3)}")
print(f"Age: {age4}, drink: {people_with_age_drink(age4)}")
