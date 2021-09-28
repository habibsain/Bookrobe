import random


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        result = (x, y)
        return result


dice = Dice()
print(dice.roll())