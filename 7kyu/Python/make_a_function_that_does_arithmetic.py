#!/usr/bin/env python3

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b

print(arithmetic(1, 2, "add"))
print(arithmetic(8, 2, "subtract"))
print(arithmetic(5, 2, "multiply"))
print(arithmetic(8, 2, "divide"))
