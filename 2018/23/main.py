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
import z3


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


def hard():
    o = z3.Optimize()
    x, y, z = z3.Ints("x y z")

    for p, d in t:
        o.add_soft(
            z3.If(x > p[0], x - p[0], p[0] - x)
            + z3.If(y > p[1], y - p[1], p[1] - y)
            + z3.If(z > p[2], z - p[2], p[2] - z)
            <= d
        )
    o.check()
    m = o.model()
    print(m.eval(x + y + z))


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()