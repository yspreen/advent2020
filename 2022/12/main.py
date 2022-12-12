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
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]


def BFS(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, 0)]
    visited = set([start])

    while options:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:  # lower bound check
                    continue
                if new_p[1] < 0:  # lower bound check
                    continue
                try:
                    assert can_walk(pos, new_p)
                except:
                    continue  # upper bound check
                if new_p in visited:
                    continue
                visited.add(new_p)
                cost_ = cost + cost_fn(pos, new_p)
                new_o.append((new_p, cost_))
                if goal(new_p):
                    return cost_
        options = new_o
    return None


def easy():
    print(BFS(start, lambda a, b: t[b] <= t[a] + 1, lambda p: p == end))


def hard():
    print(BFS(end, lambda a, b: t[b] >= t[a] - 1, lambda p: t[p] == 0))


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
