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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, r.split("/")), s)


def resolve(a, seen, value=0, l=0):
    s = []
    for b in T.get(a, []):
        if (a, b) in seen:
            continue
        s.extend(resolve(b, seen | {(a, b), (b, a)}, value + a + b, l + 1))
    if not s and value > 0:
        s = [(value, l)]
    return s


def easy():
    for a, b in t:
        T[a] = T.get(a, []) + [b]
        T[b] = T.get(b, []) + [a]

    s = resolve(0, set())
    print(max([a for a, b in s]))
    s.sort(key=lambda i: i[1] * 10000 + i[0])
    print(s[-1][0])


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
T = {}
if __name__ == "__main__":
    easy()