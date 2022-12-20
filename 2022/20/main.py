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
    return lmap(int, s)


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
    for i in range(len(t)):
        t[i] = t[i] % len(t)

    i = -1
    for _ in range(len(t)):
        i += 1
        i %= len(t)
        n = t[i]
        if n > 0:
            for j in range(i):
                end = t.pop()
                t.insert(0, end)
                i += 1
        if n < 0:
            for j in range(i):
                start = t[0]
                del t[0]
                t.append(start)
                i -= 1
            i += len(t)
    print(t[1000 % len(t)] + t[2000 % len(t)] + t[3000 % len(t)])


def hard():
    return


teststr = """1
2
-3
3
-2
0
4"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
