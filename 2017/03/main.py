import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        t = int(f.read().splitlines()[0])
    return t


def pos(n):
    c = int(sqrt(n - 1))
    c -= (c + 1) % 2
    n -= c ** 2
    ps = []

    p = (c // 2 + 1, c // 2 + 1)

    for m in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        for _ in range(c + 1):
            if n <= 0:
                break
            n -= 1
            p = (p[0] + m[0], p[1] + m[1])
            ps.append(p)

    return ps


def easy():
    print(sum(map(abs, pos(t)[-1])))


def adj(p, v):
    s = 0
    for m in [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]:
        s += v.get((p[0] + m[0], p[1] + m[1]), 0)
    return s


def hard():
    v = {(0, 0): 1}
    for n in range(1, t):
        for p in pos((n * 2 + 1) ** 2):
            n = adj(p, v)
            if n > t:
                print(n)
                return
            v[p] = n


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()