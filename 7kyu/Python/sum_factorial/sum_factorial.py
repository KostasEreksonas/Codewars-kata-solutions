#!/usr/share/bin python3

def sum_factorial(lst):
    result = 0
    for i in range(len(lst)):
        factorial = 1
        while (lst[i] > 0):
            factorial *= lst[i]
            lst[i] -= 1
        result += factorial
    return result

print(f"Sum of 4 and 6 factorials are: {sum_factorial([4,6])}")
print(f"Sum of 5, 4 and 1 factorials are: {sum_factorial([5,4,1])}")
