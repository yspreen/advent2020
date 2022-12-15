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
    return lmap(lambda r: lmap(lambda q: lmap(int, q.split(",")), r.split(" -> ")), s)


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


def draw(A, x1, x2, y1, y2):
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    A[x1 : x2 + 1, y1 : y2 + 1] = 1


def prep():
    global A, ymax

    max_x = 0
    max_y = 0
    for row in t:
        for x, y in row:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    A = np.zeros((max_x + 200, max_y + 200), dtype=int)
    ymax = max_y + 2

    for r in t:
        for i in range(1, len(r)):
            draw(A, r[i - 1][0], r[i][0], r[i - 1][1], r[i][1])


def can_place(A, pos):
    if pos[0] >= A.shape[0] - 1:
        return "bounds"
    if pos[1] >= A.shape[1] - 1:
        return "bounds"
    if A[pos[0], pos[1]] != 0:
        return "impossible"

    if A[pos[0], pos[1] + 1] == 0:
        return can_place(A, (pos[0], pos[1] + 1))
    if A[pos[0] - 1, pos[1] + 1] == 0:
        return can_place(A, (pos[0] - 1, pos[1] + 1))
    if A[pos[0] + 1, pos[1] + 1] == 0:
        return can_place(A, (pos[0] + 1, pos[1] + 1))

    A[pos] = 2


i = 0
ymax = 0


def easy():
    global i
    while True:
        if can_place(A, sand) != "bounds":
            i += 1
            continue
        return print(i)


def hard():
    global i
    y = ymax
    draw(A, 0, A.shape[0] - 2, y, y)
    while True:
        res = can_place(A, sand)
        assert res != "bounds"
        if res != "impossible":
            i += 1
            continue
        return print(i)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
A = []
sand = (500, 0)
if __name__ == "__main__":
    prep()
    easy()
    hard()
