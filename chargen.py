from random import randint
import random
from random import gauss
from data import *

print(random.choice(sex))

age = int(gauss(40, 6))
print("АGE", age)

# Rolls 4d6, sums them together, subtracts the smallest roll, gives the rolled sum a stat

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

    num_smallest = int()
    num_final = int()

# Prints rolled stats and their factor of 5

print(stats)
print("x5", factor)

# Derives attributes from stats

health = (stats['STR'] + stats['CON']) // 2 + ((stats['STR'] + stats['CON']) % 2 > 0)
print("HP", health)

willpower = stats['POW']
print("WP", willpower)

sanity = stats['POW'] * 5
print("SAN", sanity)

breakingPoint = sanity - stats['POW']
print("BP", breakingPoint)

# Picks max value and picks a profession based on it

maxValue = max(stats.values())
statGenerate = random.choice([k for k, v in stats.items() if v == maxValue])

if statGenerate == "STR":
    print(random.choice(strProfession))
elif statGenerate == "DEX":
    print(random.choice(dexProfession))
elif statGenerate == "CON":
    print(random.choice(conProfession))
elif statGenerate == "INT":
    print(random.choice(intProfession))
elif statGenerate == "POW":
    print(random.choice(powProfession))
else:
    print(random.choice(chaProfession))

