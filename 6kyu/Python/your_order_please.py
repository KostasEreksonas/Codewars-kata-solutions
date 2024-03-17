#!/usr/bin/env python3

def order(sentence):
    res = {}
    keys,results = [[] for x in range(2)]
    values = sentence.split()
    if values == []:
        return ''
    else:
        keys = [int(x) for value in values for x in value if x.isnumeric()]
        for key in keys:
            for value in values:
                res[key] = value
                values.remove(value)
                break
    res = dict(sorted(res.items()))
    for value in res.values():
        results.append(value)
    return " ".join(results)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))
