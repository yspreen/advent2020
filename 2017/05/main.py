import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product


def lmap(*a):
    return list(map(*a))


teststr = """"""


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(int, filter(None, s.splitlines()))


def easy():
    n = p = 0
    try:
        while True:
            t[p] += 1
            p += t[p] - 1
            n += 1
    except:
        pass
    print(n)


def hard():
    n = p = 0
    try:
        while True:
            x = -1 if t[p] >= 3 else 1
            t[p] += x
            p += t[p] - x
            n += 1
    except:
        pass
    print(n)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    t = read()
    hard()