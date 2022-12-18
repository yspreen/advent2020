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
from scipy import ndimage


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(int, r.split(",")), s))


mv = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # L
    (0, 0, 1),  # R
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
    print(get_area(t))


def get_area(t):
    m = t.max()

    A = np.zeros((m + 2, m + 2, m + 2))

    c = 0
    for x, y, z in t:
        c += 6
        for m in mv:
            if A[x + m[0], y + m[1], z + m[2]] > 0:
                c -= 2

        A[x, y, z] = 1
    return c, A


def hard():
    m = t.max()

    c, A = get_area(t)

    a = 1 - A
    a = ndimage.label(a)

    holes = a[1] - 1
    for i in range(2, holes + 2):
        c -= get_area(np.array(list(zip(*np.where(a[0] == i)))))[0]
    print(c)


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
