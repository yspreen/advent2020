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
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return np.array([s.count(str(i)) for i in range(9)], dtype=np.uint64)


def run(days):
    a = np.array(list(t), dtype=np.uint64)
    for _ in range(days):
        a = np.roll(a, -1)
        a[6] += a[8]
    return a.sum()


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    print(run(80))
    print(run(256))
