import numpy as np
import re
import pathlib
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")

lookup = {
    ".": 0,
    "L": 1,
    "#": 2,
}
reverse_lookup = {}
for k, v in lookup.items():
    reverse_lookup[v] = k


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "")
    t = t.split("\n")
    N = int(t[0])
    t = t[1].split(",")

    t = ["x" if e == "x" else int(e) for e in t]

    return N, t


N, t = read()


def easy():
    r = []
    for i in t:
        if i == "x":
            continue
        r.append((i, i - (N % i)))
    r.sort(key=lambda e: e[1])
    print(r[0][0] * r[0][1])


def hard():
    constraints = []
    for i, n in enumerate(t):
        if n == "x":
            continue
        constraints.append((n, n - i))

    j = 0
    add = 1
    for div, rst in constraints:
        while j % div != rst % div:
            j += add
        add *= div
    print(j)


if __name__ == "__main__":
    easy()
    hard()
