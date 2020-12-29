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


def easy():
    while len(t[0]) and len(t[1]):
        round()
    print(
        reduce(lambda a, b: (a[1] * b + a[0], a[1] + 1), reversed(t[0] + t[1]), (0, 1))[
            0
        ]
    )


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
