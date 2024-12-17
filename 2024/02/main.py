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
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, r.split(" ")), s)


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


def is_safe(line):
    first_diff = line[1] - line[0]
    if first_diff == 0 or abs(first_diff) > 3:
        return False
    ascending = first_diff > 0
    for i in range(2, len(line)):
        diff = line[i] - line[i - 1]
        if (diff > 0) != ascending:
            return False
        if diff == 0 or abs(diff) > 3:
            return False
    return True


def easy():
    sum = 0
    for line in t:
        if is_safe(line):
            sum += 1
    print(sum)


def is_safe_kinda(line):
    if is_safe(line):
        return True

    first_diff = line[1] - line[0]
    if is_safe(line[1:]) or is_safe(line[:1] + line[2:]):
        return True
    ascending = first_diff > 0
    for i in range(3, len(line)):
        diff = line[i] - line[i - 1]
        if (diff > 0) != ascending or diff == 0 or abs(diff) > 3:
            return is_safe(line[: i - 1] + line[i:]) or is_safe(
                line[:i] + line[i + 1 :]
            )


def hard():
    sum = 0
    for line in t:
        if is_safe_kinda(line):
            sum += 1
    print(sum)


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
