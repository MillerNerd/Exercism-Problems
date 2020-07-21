"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

import re

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    total = 0
    if category == YACHT:
        for i in range(1, 5):
            if dice[0] != dice[i]:
                return 0
        return 50
    if category == ONES:
        return sum(filter(lambda x: x == 1, dice))
    if category == TWOS:
        return sum(filter(lambda x: x == 2, dice))
    if category == THREES:
        return sum(filter(lambda x: x == 3, dice))
    if category == FOURS:
        return sum(filter(lambda x: x == 4, dice))
    if category == FIVES:
        return sum(filter(lambda x: x == 5, dice))
    if category == SIXES:
        return sum(filter(lambda x: x == 6, dice))
    if category == FULL_HOUSE:
        dice.sort()
        if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
            return 0
        if dice[0] == dice[1] == dice[2] and dice[3] == dice[4]:
            return sum(dice)
        if dice[0] == dice[1] and dice[2] == dice[3] == dice[4]:
            return sum(dice)
        return 0
    if category == FOUR_OF_A_KIND:
        for i in range(2, 7):
            if dice.count(i) == 4:
                return sum(filter(lambda x: x == i, dice))
            if dice.count(i) == 5:
                return sum(filter(lambda x: x == i, dice)) - i
        return 0
    if category == LITTLE_STRAIGHT:
        if all(i in dice for i in [1, 2, 3, 4, 5]):
            return 30
        return 0
    if category == BIG_STRAIGHT:
        if all(i in dice for i in [2, 3, 4, 5, 6]):
            return 30
        return 0
    if category == CHOICE:
        return sum(dice)
