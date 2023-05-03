#!/usr/share/bin python3

def remove_every_other(my_list):
    result = []
    for i in range(len(my_list)):
        if (i % 2 == 0):
            result.append(my_list[i])
    return result

list1 = ['Hello', 'Goodbye', 'Hello Again']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = [['Goodbye'], {'Great': 'Job'}]

print(f"Full list: {list1}, list with removed elements: {remove_every_other(list1)}")
print(f"Full list: {list2}, list with removed elements: {remove_every_other(list2)}")
print(f"Full list: {list3}, list with removed elements: {remove_every_other(list3)}")
