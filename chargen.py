from random import randint
import random
from data import *


# Anthropologist, recommended INT, Anthropology 50, Bureaucracy 40, Foreign language (1) 50, Foreign language (2) 40, History 60, Occult 40, Persuade 40
# Choose two of these you don't already have: Archeology 40, HUMINT 50, Navigate 50, Ride 50, Search 60, Survival 50


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

    print(x, num_final, " x5", num_final * 5)
    num_final = int()
