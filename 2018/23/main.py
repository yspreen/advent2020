import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols, solve


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    t = list(
        map(
            lambda l: (
                tuple(map(int, l.split("<")[1].split(">")[0].split(","))),
                int(l.split("=")[-1]),
            ),
            t,
        )
    )
    return t


def dist(a, b):
    return sum([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])])


def count(m):
    c = 0
    for l in t:
        if dist(m[0], l[0]) <= m[1]:
            c += 1
    return c


def easy():
    t.sort(key=lambda i: i[1])
    m = t[-1]

    print(count(m))


def neighbors(rule):
    p = rule[0]
    d = rule[1]

    n = []
    for v in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        n.append((p[0] + v[0] * d, p[1] + v[1] * d, p[2] + v[2] * d))
    return n


def hard():
    import math

    ps = []
    for r in t:
        ps.extend(neighbors(r))

    c = {}
    for p in ps:
        c[p] = 0
        for r in t:
            if dist(p, r[0]) <= r[1]:
                c[p] += 1
    c = [sum(k) for k, v in c.items() if v == max([i for i in c.values()])]
    print(min(c))


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()