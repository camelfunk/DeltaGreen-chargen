from random import randint
import random
from data import *

print(random.choice(sex))

for x in stats:
    for i in range(num_dice):

        num_random = (randint(1, num_sides))
        num_final = num_final + num_random

        if num_random < num_smallest:
            num_smallest = num_random

        elif num_smallest == int():
            num_smallest = num_random

    num_final = num_final - num_smallest

    stats[x] = num_final;
    factor.append(num_final * 5)

    num_final = int()

print(stats)
print("x5", factor)
