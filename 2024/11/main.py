import numpy as np
import re
import pathlib
import json
from functools import reduce, cmp_to_key
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, r.split(" ")), s)[0]


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
    (-1, 1),  # UR
    (1, 1),  # DR
    (-1, -1),  # UL
    (1, -1),  # DL
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
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
    T = t
    for step in range(25):
        t_ = []
        for i in T:
            s = str(i)
            if i == 0:
                t_.append(1)
            elif len(s) % 2 == 0:
                t_.append(int(s[: len(s) // 2]))
                t_.append(int(s[len(s) // 2 :]))
            else:
                t_.append(i * 2024)
        T = t_
    print(len(T))


def hard():
    T = [(i, 1) for i in t]
    for step in range(75):
        t_ = []
        for i, c in T:
            s = str(i)
            if i == 0:
                t_.append((1, c))
            elif len(s) % 2 == 0:
                t_.append((int(s[: len(s) // 2]), c))
                t_.append((int(s[len(s) // 2 :]), c))
            else:
                t_.append((i * 2024, c))

        unique = {}
        for i, c in t_:
            if i not in unique:
                unique[i] = 0
            unique[i] += c
        T = [(i, c) for i, c in unique.items()]
    print(sum([c for i, c in T]))


teststr = """"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
