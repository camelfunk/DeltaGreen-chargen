from random import randint
import random
from random import gauss
from data import *
from collections import OrderedDict

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


# Skill generation based on profession


if statGenerate == "STR":
    ProfessionGenerate = random.choice(strProfession)
    print(ProfessionGenerate)

    if ProfessionGenerate == profession[7]:
        specopskillreplacement()

    elif ProfessionGenerate == profession[8]:
        criminalskillreplacement()

    elif ProfessionGenerate == profession[9]:
        firefighterskillreplacement()

    elif ProfessionGenerate == profession[20]:
        policeskillreplacement()

    elif ProfessionGenerate == profession[22]:
        soldierskillreplacement()

    else:
        marineskillreplacement()


elif statGenerate == "DEX":
    ProfessionGenerate = random.choice(dexProfession)
    print(ProfessionGenerate)

    if ProfessionGenerate == profession[5]:
        physicianskillreplacement()

    elif ProfessionGenerate == profession[8]:
        criminalskillreplacement()

    elif ProfessionGenerate == profession[9]:
        firefighterskillreplacement()

    else:
        pilotskillreplacement()

elif statGenerate == "CON":
    ProfessionGenerate = random.choice(conProfession)
    print(ProfessionGenerate)

    if ProfessionGenerate == profession[4]:
        fagentskillreplacement()

    elif ProfessionGenerate == profession[7]:
        specopskillreplacement()

    elif ProfessionGenerate == profession[9]:
        firefighterskillreplacement()

    elif ProfessionGenerate == profession[20]:
        policeskillreplacement()

    elif ProfessionGenerate == profession[22]:
        soldierskillreplacement()

    else:
        marineskillreplacement()


elif statGenerate == "INT":
    ProfessionGenerate = random.choice(intProfession)
    print(ProfessionGenerate)

    if ProfessionGenerate == profession[0]:
        anthroskillreplacement()

    elif ProfessionGenerate == profession[1]:
        historianskillreplacement()

    elif ProfessionGenerate == profession[2] or ProfessionGenerate == profession[3]:
        compsciskillreplacement()

    elif ProfessionGenerate == profession[5]:
        physicianskillreplacement()

    elif ProfessionGenerate == profession[6]:
        scientistskillreplacement()

    elif ProfessionGenerate == profession[10]:
        fsoskillreplacement()

    elif ProfessionGenerate == profession[11]:
        ianalystskillreplacement()

    elif ProfessionGenerate == profession[12]:
        icoskillreplacement()

    elif ProfessionGenerate == profession[13] or ProfessionGenerate == profession[14]:
        lawyerskillreplacement()

    elif ProfessionGenerate == profession[15]:
        mediaspecialistskillreplacement()

    elif ProfessionGenerate == profession[16] or ProfessionGenerate == profession[17]:
        nurseskillreplacement()

    elif ProfessionGenerate == profession[18] or ProfessionGenerate == profession[19]:
        pilotskillreplacement()

    else:
        progmgrskillreplacement()


elif statGenerate == "POW":
    ProfessionGenerate = random.choice(powProfession)
    print(ProfessionGenerate)

    if ProfessionGenerate == profession[4]:
        fagentskillreplacement()

    elif ProfessionGenerate == profession[5]:
        physicianskillreplacement()

    elif ProfessionGenerate == profession[7]:
        specopskillreplacement()

    elif ProfessionGenerate == profession[12]:
        icoskillreplacement()

    elif ProfessionGenerate == profession[16] or ProfessionGenerate == profession[17]:
        nurseskillreplacement()

    else:
        policeskillreplacement()


else:
    ProfessionGenerate = random.choice(chaProfession)
    print(ProfessionGenerate)

    if ProfessionGenerate == profession[4]:
        fagentskillreplacement()

    elif ProfessionGenerate == profession[10]:
        fsoskillreplacement()

    elif ProfessionGenerate == profession[12]:
        icoskillreplacement()

    elif ProfessionGenerate == profession[13] or ProfessionGenerate == profession[14]:
        lawyerskillreplacement()

    elif ProfessionGenerate == profession[15]:
        mediaspecialistskillreplacement()

    elif ProfessionGenerate == profession[16] or ProfessionGenerate == profession[17]:
        nurseskillreplacement()

    else:
        progmgrskillreplacement()

print(skills)
