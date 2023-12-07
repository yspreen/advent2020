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


def read():
    with open(DIR / "input") as f:
        s = re.sub(r" +", " ", (f.read() if teststr == "" else teststr)).splitlines()
    return list(zip(*lmap(lambda row: lmap(int, row.split(" ")[1:]), s)))


def maybeint(line):
    try:
        return int(line)
    except:
        return line


def easy():
    result = 1
    for time, distance in t:
        wins = 0
        for press_t in range(1, time):
            if (time - press_t) * press_t > distance:
                wins += 1
        result *= wins
    print(result)


def hard():
    time = int("".join(map(str, [i[0] for i in t])))
    distance = int("".join(map(str, [i[1] for i in t])))

    wins = 0
    for press_t in range(1, time):
        if (time - press_t) * press_t > distance:
            wins += 1
    print(wins)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
