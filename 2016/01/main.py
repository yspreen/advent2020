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
        s = (f.read() if teststr == "" else teststr).split(", ")
    return lmap(lambda r: (r[0], int(r[1:])), s)


def left(p):
    return (-p[1], p[0])


def right(p):
    return (p[1], -p[0])


def easy():
    p, d = (0, 0), (-1, 0)
    for turn, move in t:
        d = {"L": left, "R": right}[turn](d)
        p = (p[0] + move * d[0], p[1] + move * d[1])
    print(sum(map(abs, p)))


def hard():
    p, d, seen = (0, 0), (-1, 0), {(0, 0)}
    for turn, move in t:
        d = {"L": left, "R": right}[turn](d)
        for _ in range(move):
            p = (p[0] + d[0], p[1] + d[1])
            if p in seen:
                return print(sum(map(abs, p)))
            seen.add(p)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()