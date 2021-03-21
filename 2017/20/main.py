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
        s = f.read() if teststr == "" else teststr
    return lmap(
        lambda r: lmap(
            lambda i: np.array(lmap(int, i[3:-1].split(",")), np.int), r.split(", ")
        ),
        s.splitlines(),
    )


def easy():
    m = (inf, inf)
    for i, r in enumerate(t):
        s_a = sum(map(abs, r[2] * 10000 + r[1]))
        if s_a < m[0]:
            m = (s_a, i)
    print(m[1])


def hard():
    for _ in range(10 ** 3):
        p = {}
        for i, r in enumerate(t):
            r[1] += r[2]
            r[0] += r[1]
            tp = tuple(r[0])
            p[tp] = p.get(tp, []) + [i]
        removed = []
        for l in p.values():
            if len(l) < 2:
                continue
            removed.extend(l)
        for i in reversed(sorted(removed)):
            del t[i]
    print(len(t))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()