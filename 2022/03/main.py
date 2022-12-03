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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(str, r), s)


def prio(c):
    return chars.find(c) + 1


def easy():
    s = 0
    for line in t:
        first = set(line[: len(line) // 2])
        second = set(line[len(line) // 2 :])
        overlap = list(first & second)[0]
        s += prio(overlap)
    print(s)


def hard():
    s = 0
    for i in range(len(t))[::3]:
        o = reduce(lambda x, y: x & y, map(set, t[i : i + 3]), set(chars))
        o = list(o)[0]
        s += prio(o)
    print(s)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
smap = lambda *a: set(map(*a))
inf = float("inf")
chars = ascii_lowercase + ascii_lowercase.upper()
t = read()
if __name__ == "__main__":
    easy()
    hard()
