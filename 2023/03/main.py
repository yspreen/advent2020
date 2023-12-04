import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256

SYM = -1
GEAR = -3
DOT = -2


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(getnum, list(r)), s))


def getnum(sym):
    if sym in "@#-=/+%$&":
        return SYM
    if sym == ".":
        return DOT
    if sym == "*":
        return GEAR
    return int(sym)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
    (-1, 1),  # UR
    (1, 1),  # DR
    (-1, -1),  # UL
    (1, -1),  # DL
]


def easy():
    result = 0
    seen = set()

    def add_num(x, y):
        y_min = y_max = y
        if (x, y) in seen:
            return 0
        seen.add((x, y))
        while y_min > 0 and t[x, y_min - 1] > SYM:
            y_min -= 1
            seen.add((x, y_min))
        while y_max < t.shape[1] - 1 and t[x, y_max + 1] > SYM:
            y_max += 1
            seen.add((x, y_max))
        return int("".join(map(lambda i: str(int(i)), t[x, y_min : y_max + 1])))

    for x, y in list(zip(*np.where(t == SYM))) + list(zip(*np.where(t == GEAR))):
        for mv_x, mv_y in mv:
            x_, y_ = x + mv_x, y + mv_y
            if 0 <= x_ < t.shape[0] and 0 <= y_ < t.shape[1] and t[x_, y_] > SYM:
                result += add_num(x_, y_)
    print(result)


def hard():
    result = 0

    def add_num(x, y, seen):
        y_min = y_max = y
        seen.add((x, y))
        while y_min > 0 and t[x, y_min - 1] > SYM:
            y_min -= 1
            seen.add((x, y_min))
        while y_max < t.shape[1] - 1 and t[x, y_max + 1] > SYM:
            y_max += 1
            seen.add((x, y_max))
        return int("".join(map(lambda i: str(int(i)), t[x, y_min : y_max + 1])))

    for x, y in zip(*np.where(t == GEAR)):
        seen = set()
        numbers = []
        for mv_x, mv_y in mv:
            x_, y_ = x + mv_x, y + mv_y
            if 0 <= x_ < t.shape[0] and 0 <= y_ < t.shape[1] and t[x_, y_] > SYM:
                if (x_, y_) in seen:
                    continue
                numbers.append(add_num(x_, y_, seen))
        if len(numbers) != 2:
            continue
        result += numbers[0] * numbers[1]
    print(result)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
    hard()
