#!/usr/bin/env python3

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

arr1=[5, 8, 12, 18, 22]
arr2=[7, 15, 12, 18, 22]
arr3=[25, 42, 12, 18, 22]

print(f"Array: {arr1}, sum of two smallest integers: {sum_two_smallest_numbers(arr1)}")
print(f"Array: {arr2}, sum of two smallest integers: {sum_two_smallest_numbers(arr2)}")
print(f"Array: {arr3}, sum of two smallest integers: {sum_two_smallest_numbers(arr3)}")
