from random import Random, random
from random import randint, choice, shuffle, choices

val = random()
print(val)

for i in range(10):
    val = randint(1, 10)
    print(val, end='')

num = []
for i in range(10):
    num.append(randint(1, 1000))
print("\n",num)

animal = ['frog','tiger','dog','cow']

sel_ani=choice(animal)
print(f'selected 3 animal: {" ".join(sel_ani)}')

sel_3_anim= choices(animal,)

