#!/usr/bin/env python3

def two_sort(array):
    # your code here
    array.sort()
    result = ''
    for x in range(len(array[0])-1):
        result += array[0][x] + '***'
    result += array[0][len(array[0])-1]
    return result

arr1 = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
arr2 = ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]
arr3 = ["lets", "talk", "about", "javascript", "the", "best", "language"]
arr4 = ["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]
arr5 = ["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]

print(two_sort(arr1))
print(two_sort(arr2))
print(two_sort(arr3))
print(two_sort(arr4))
print(two_sort(arr5))
