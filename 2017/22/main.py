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
    return np.array(lmap(lambda r: lmap(ord, r), s), np.int)


def right(p):
    return (p[1], -p[0])


def left(p):
    return (-p[1], p[0])


def straight(p):
    return p


def back(p):
    return (-p[0], -p[1])


def run(iterations, moves, changes):
    t = read()
    t[t == ord(".")] = 0
    t[t == ord("#")] = 1
    d, p, c, n = (-1, 0), (t.shape[0] // 2, t.shape[1] // 2), 0, 1
    for i in range(iterations):
        if not (0 < p[0] < t.shape[0] - 1 and 0 < p[1] < t.shape[1] - 1):
            t = np.pad(t, ((n, n), (n, n)))
            p = (p[0] + n, p[1] + n)
            n *= 2
        d = moves[t[p]](d)
        t[p] = changes[t[p]]
        c += 1 if t[p] == 1 else 0
        p = (p[0] + d[0], p[1] + d[1])
    print(c)


def easy():
    run(10000, {0: left, 1: right}, {0: 1, 1: 0})


def hard():
    run(10 ** 7, [left, right, straight, back], [2, 3, 1, 0])


teststr = ""  # "..#\n#..\n..."
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
if __name__ == "__main__":
    easy()
    hard()