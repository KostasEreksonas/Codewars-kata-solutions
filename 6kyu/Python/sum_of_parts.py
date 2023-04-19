#!/usr/share/bin python3

def parts_sums(ls):
    # your code
    count = len(ls)
    results = []
    while (count > 0):
        sum = 0
        for element in ls:
            sum += element
        results.append(sum)
        ls.pop(0)
        count = len(ls)
    if (count == 0):
        results.append(0)
    return results

print(parts_sums([0,1,3,6,10]))
