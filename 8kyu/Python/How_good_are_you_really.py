#!/usr/bin/python3

def better_than_average(class_points, your_points):
    if your_points > sum(class_points) / len(class_points):
        return True
    else:
        return False

print(better_than_average([2, 3], 5))
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
