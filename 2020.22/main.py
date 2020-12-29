import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().replace("\r", "").split("\n\n")
    t = [l.split("\n")[1:] for l in t]
    t[1].pop()
    return [[int(i) for i in l] for l in t]


t = read()


def round():
    p1 = t[0].pop(0)
    p2 = t[1].pop(0)
    if p1 > p2:
        t[0].extend([p1, p2])
    else:
        t[1].extend([p2, p1])


def recround(a, b, return_list=False):
    seen = set()
    while True:
        if not (a and b):
            if return_list:
                return a if a else b
            return 0 if a else 1
        h = hash(tuple(a + [-1] + b))
        if h in seen:
            return a if return_list else 0
        seen.add(h)

        p1 = a.pop(0)
        p2 = b.pop(0)
        if p1 <= len(a) and p2 <= len(b):
            win = recround(list(a[:p1]), list(b[:p2]))
        else:
            win = 0 if p1 > p2 else 1
        if win == 0:
            a.extend([p1, p2])
        else:
            b.extend([p2, p1])


def score(A):
    return reduce(lambda a, b: (a[1] * b + a[0], a[1] + 1), reversed(A), (0, 1))[0]


def easy():
    round()
    print(score(t[0] + t[1]))


def hard():
    print(score(recround(*read(), return_list=True)))


if __name__ == "__main__":
    easy()
    hard()
