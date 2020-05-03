"""
摇色子游戏
"""
from random import randint

def roll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

print(roll_dice())
print(roll_dice(3))
pr