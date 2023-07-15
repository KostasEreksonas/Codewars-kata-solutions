#!/usr/bin/env python3

def count_positives_sum_negatives(arr):
    count_pos, count_neg = [0 for i in range(2)]
    if len(arr) == 0:
        return []
    else:
        for x in arr:
            if x < 0:
                count_neg += x
            elif x:
                count_pos += 1
    result = [count_pos, count_neg]
    return result

arr1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
arr2=[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
arr3=[-1]
arr4=[1]

print(f"{arr1} returns {count_positives_sum_negatives(arr1)}")
print(f"{arr2} returns {count_positives_sum_negatives(arr2)}")
print(f"{arr3} returns {count_positives_sum_negatives(arr3)}")
print(f"{arr4} returns {count_positives_sum_negatives(arr4)}")
