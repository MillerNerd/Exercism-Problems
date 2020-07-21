from math import hypot


def score(x, y):
    dist = hypot(x, y)
    if dist > 10:
        return 0
    if dist > 5:
        return 1
    if dist > 1:
        return 5
    return 10
