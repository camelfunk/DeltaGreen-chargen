from random import randint
import random
from random import gauss
from data import *


print(random.choice(sex))

age = int(gauss(40, 6))
print("АGE", age)

for x in stats:
    for i in range(num_dice):

        num_random = (randint(1, num_sides))
        num_final = num_final + num_random

        if num_random < num_smallest:
            num_smallest = num_random

        elif num_smallest == int():
            num_smallest = num_random

    num_final = num_final - num_smallest

    stats[x] = num_final
    factor.append(num_final * 5)

    num_final = int()

print(stats)
print("x5", factor)

health = (stats['STR'] + stats['CON']) // 2 + ((stats['STR'] + stats['CON']) % 2 > 0)
print("HP", health)

willpower = stats['POW']
print("WP", willpower)

sanity = stats['POW'] * 5
print("SAN", sanity)

breakingPoint = sanity - stats['POW']
print("BP", breakingPoint)


