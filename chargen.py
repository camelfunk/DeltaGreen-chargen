from random import randint

num_sides = 6  # 6-sided die
num_dice = 4  # number of dice to roll
num_smallest = int()  # smallest roll
num_final = int()  # added dice rolls together

stats = ['STR', 'DEX', 'CON', 'INT', 'POW', 'CHA']

for x in stats:
    for i in range(num_dice):

        num_random = (randint(1, num_sides))
        num_final = num_final + num_random

        if num_random < num_smallest:
            num_smallest = num_random

        elif num_smallest == int():
            num_smallest = num_random

    num_final = num_final - num_smallest

    print(x, num_final)
    num_final = int()
