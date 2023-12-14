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
    return np.array(lmap(lambda r: lmap(".#".find, r), s))


def count(t):
    galaxies = list(zip(*np.where(t == 1)))

    result = 0
    for i in range(len(galaxies)):
        min_d = inf
        for j in range(i + 1, len(galaxies)):
            result += abs(galaxies[i][0] - galaxies[j][0]) + abs(
                galaxies[i][1] - galaxies[j][1]
            )
    return result


def run():
    t_ = t

    i = 0
    while i < t_.shape[0]:
        if t_[i, :].sum() == 0:
            t_ = np.insert(t_, i, 0, axis=0)
            i += 1
        i += 1
    j = 0
    while j < t_.shape[1]:
        if t_[:, j].sum() == 0:
            t_ = np.insert(t_, j, 0, axis=1)
            j += 1
        j += 1

    padded = count(t_)
    raw = count(t)
    print(padded)
    print((padded - raw) * 999999 + raw)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    run()
