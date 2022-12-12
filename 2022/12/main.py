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
from typing import Tuple, Any


idxs = ascii_lowercase + "SE"


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(lambda i: idxs.index(i), r), s), dtype=int)


mv = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]


def easy():
    options = [(start, 0)]
    visited = set([start])

    while True:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:
                    continue
                if new_p[1] < 0:
                    continue
                try:
                    if t[pos] + 1 < t[new_p]:
                        continue
                except:
                    continue
                if new_p in visited:
                    continue
                visited.add(new_p)
                new_o.append((new_p, cost + 1))
                if new_p == end:
                    return print(cost + 1)
        options = new_o


def hard():
    t[t == 26] = 0
    t[t == 27] = 25
    options = [(end, 0)]
    visited = set([end])

    while True:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:
                    continue
                if new_p[1] < 0:
                    continue
                try:
                    if t[pos] - 1 > t[new_p]:
                        continue
                except:
                    continue
                if new_p in visited:
                    continue
                visited.add(new_p)
                new_o.append((new_p, cost + 1))
                if t[new_p] == 0:
                    return print(cost + 1)
        options = new_o


teststr = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()


start_ = list(zip(*np.where(t == 26)))[0]  # type: Any
start = start_  # type: Tuple[int,int]
end_ = list(zip(*np.where(t == 27)))[0]  # type: Any
end = end_  # type: Tuple[int,int]
t[t == 26] = 0
t[t == 27] = 25
if __name__ == "__main__":
    easy()
    hard()
