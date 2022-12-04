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
    return lmap(lambda r: lmap(lambda x: lmap(int, x.split("-")), r.split(",")), s)


def easy():
    s = 0
    for left, right in t:
        if left[0] >= right[0] and left[1] <= right[1]:
            s += 1
        elif right[0] >= left[0] and right[1] <= left[1]:
            s += 1
    print(s)


def hard():
    s = 0
    for left, right in t:
        if left[0] <= right[0] <= left[1]:
            s += 1
        elif right[0] <= left[0] <= right[1]:
            s += 1
    print(s)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
