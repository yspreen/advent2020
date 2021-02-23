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


def count(m, k=1):
    c = 0
    for l in t:
        if dist(m[0], l[0], k=k) <= m[1] // k:
            c += 1
    return c


def count_p(p, k=1):
    c = 0
    for l in t:
        if dist(p, l[0], k=k) <= l[1] // k:
            c += 1
    return c


def easy():
    t.sort(key=lambda i: -i[1])
    m = t[0]

    print(count(m))


def hard():
    import math

    m = max(map(lambda i: max(i[0]), t))
    m = int(math.log(m) // math.log(10))
    p = (0, 0, 0)
    for i in range(m + 1):
        i = m - i  # m...0
        p = (p[0] * 10, p[1] * 10, p[2] * 10)
        mx = (0, 0)
        for x in product(range(16), repeat=3):
            p_ = (p[0] + x[0] - 5, p[1] + x[1] - 5, p[2] + x[2] - 5)
            # print(p_)
            c = count_p(p_, 10 ** i)
            if c > mx[0]:
                mx = (c, p_)
        p = mx[1]
    print(p, sum(p))


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()