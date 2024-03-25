#!/usr/bin/env python3

def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi > 18.5 and bmi <= 25:
        return "Normal"
    elif bmi > 25 and bmi <= 30:
        return "Overweight"
    elif bmi > 30:
        return "Obese"

print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(110, 1.80))
print(bmi(50, 1.50))
