#/usr/bin/env python3

def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'

light1 = 'green'
light2 = 'yellow'
light3 = 'red'

print(f"Current: {light1}, next: {update_light(light1)}")
print(f"Current: {light2}, next: {update_light(light2)}")
print(f"Current: {light3}, next: {update_light(light3)}")
