from random import randint

num_sides = 6       # 6-sided die
num_dice = 3        # number of dice to roll
num_final = 0       # added dice rolls together

for i in range(num_dice):
    num_final = num_final + (randint(1, num_sides))

print(num_final)
