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
    return lmap(lambda r: (r.split(" ")[0], int(r.split(" ")[1])), s)


def dist(H, T):
    return max(abs(H[0] - T[0]), abs(H[1] - T[1]))


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def move(T, h, t):
    pos_h, pos_t = T[h], list(T[t])
    if dist(pos_h, pos_t) < 2:
        return
    pos_t[0] += sign(pos_h[0] - pos_t[0])
    pos_t[1] += sign(pos_h[1] - pos_t[1])
    T[t] = tuple(pos_t)


def run(length):
    T = [(0 * i, 0 * i) for i in range(length)]
    m = {
        "D": [1, 0],
        "U": [-1, 0],
        "L": [0, -1],
        "R": [0, 1],
    }
    seen = set([T[length - 1]])
    for dir, num in t:
        v = m[dir]
        for _ in range(num):
            T[0] = (T[0][0] + v[0], T[0][1] + v[1])
            for i in range(1, length):
                move(T, i - 1, i)
            seen.add(T[length - 1])
    print(len(seen))


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    run(2)
    run(10)
