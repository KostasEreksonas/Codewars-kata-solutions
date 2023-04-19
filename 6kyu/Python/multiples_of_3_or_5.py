#!/usr/share/bin python3

def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum

print(f"Sum of multiples for number 6 is: {solution(6)}")
print(f"Sum of multiples for number 15 is: {solution(15)}")
print(f"Sum of multiples for number 54 is: {solution(54)}")
