#!/usr/share/bin python3

def hero(bullets, dragons):
    if (bullets/2 >= dragons):
        return True
    else:
        return False
bullets1 = 6
dragons1 = 3
bullets2 = 3
dragons2 = 2
bullets3 = 8
dragons3 = 5

print(f"Bullets: {bullets1}, dragons: {dragons1}, survival: {hero(bullets1, dragons1)}")
print(f"Bullets: {bullets2}, dragons: {dragons2}, survival: {hero(bullets2, dragons2)}")
print(f"Bullets: {bullets3}, dragons: {dragons3}, survival: {hero(bullets3, dragons3)}")
