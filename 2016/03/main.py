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


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, [r[:5], r[5:10], r[10:]]), s)


def easy():
    counter = 0
    for a, b, c in t:
        if a < b + c and b < a + c and c < a + b:
            counter += 1
    print(counter)


def hard():
    counter = 0
    t_ = [i[0] for i in t] + [i[1] for i in t] + [i[2] for i in t]
    for i in range(len(t_))[::3]:
        a, b, c = t_[i], t_[i + 1], t_[i + 2]
        if a < b + c and b < a + c and c < a + b:
            counter += 1
    print(counter)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()