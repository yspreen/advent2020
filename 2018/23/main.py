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


def dist(a, b, k=1):
    return sum([abs(a[0] - b[0] // k), abs(a[1] - b[1] // k), abs(a[2] - b[2] // k)])


def count(m):
    c = 0
    for l in t:
        if dist(m[0], l[0]) <= m[1]:
            c += 1
    return c


def count_p(p, t, n):
    c = 0
    for l in t:
        if dist(p, l[0]) <= l[1] + (1 if n > 1 else 0):
            c += 1
    return c


def easy():
    t.sort(key=lambda i: i[1])
    m = t[-1]

    print(count(m))


def seed(rule):
    s = []
    for i_, j_, k_ in product(range(rule[1] * 2 + 1), repeat=3):
        i, j, k = (
            i_ - rule[1] + rule[0][0],
            j_ - rule[1] + rule[0][1],
            k_ - rule[1] + rule[0][2],
        )
        if dist((i, j, k), rule[0]) == rule[1]:
            s.append((i, j, k))
    return s


def mask(t, i):
    m = []
    i = 10 ** i
    return [((l[0][0] // i, l[0][1] // i, l[0][2] // i), l[1] // i) for l in t]


def solve(points, n):
    if n == 0:
        print(sum(points[0]))
        return True
    t_ = mask(t, n)
    points = list(map(lambda i: tuple(map(lambda j: j * 10, i)), points))
    m = (0, [])
    for p_ in points:
        for off in product(range(10), repeat=3):
            p = (p_[0] + off[0], p_[1] + off[1], p_[2] + off[2])
            c = count_p(p, t_, n)
            if c == m[0]:
                m[1].append(p)
            if c > m[0]:
                m = (c, [p])
    for p in m[1]:
        if solve([p], n - 1):
            return True


def hard():
    import math

    N = len(str(t[-1][1])) + 1

    points = [(0, 0, 0)]
    i = N - 1
    solve(points, i)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()