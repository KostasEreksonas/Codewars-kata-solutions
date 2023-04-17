#!/usr/share/bin python3

def find_hack(arr):
    """Append names of students that hacked the point system"""
    hacked = []
    for student in arr:
        """Add 20 points if all grades are A or B (>=5 grades)"""
        add_points = 1
        score = 0
        name = student[0]
        total = student[1]
        grades = student[2]
        for grade in grades:
            if (grade == "A"):
                score += 30
            elif (grade == "B"):
                score += 20
            elif (grade == "C"):
                score += 10
                add_points = 0
            elif (grade == "D"):
                score += 5
                add_points = 0
            else:
                add_points = 0
        if (len(grades) >= 5 and add_points == 1):
            score += 20
        """Cap total score at 200"""
        if (score > 200):
            score = 200
        if (total != score or total > 200):
            hacked.append(name)
    return hacked

"""Sample array"""
array = [
    ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
    ["name2", 140, ["B", "A", "A", "A"]],
    ["name3", 200, ["B", "A", "A", "C"]]
]

print(find_hack(array))
