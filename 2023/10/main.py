import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(list, s)


def maybeint(line):
    try:
        return int(line)
    except:
        return line


move = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
dirs = move.keys()

pipes = {
    ("D", "|"): "D",
    ("R", "-"): "R",
    ("D", "L"): "R",
    ("D", "J"): "L",
    ("U", "7"): "L",
    ("U", "F"): "R",
    ("U", "|"): "U",
    ("L", "-"): "L",
    ("L", "L"): "U",
    ("R", "J"): "U",
    ("R", "7"): "D",
    ("L", "F"): "D",
}


def calculate_polygon_area(points):
    n = len(points)  # Number of points
    area = 0

    # Sum over each point
    for i in range(n):
        j = (i + 1) % n  # Next vertex index, wrapping around
        area += points[i][0] * points[j][1]  # x[i] * y[j+1]
        area -= points[j][0] * points[i][1]  # y[i] * x[j+1]

    return abs(area) / 2


def run():
    pos = (0, 0)
    for y, row in enumerate(t):
        for x, c in enumerate(row):
            if c == "S":
                pos = (y, x)

    for dir in dirs:
        pos_ = (pos[0] + move[dir][0], pos[1] + move[dir][1])
        if (dir, t[pos_[0]][pos_[1]]) not in pipes:
            continue
        c = t[pos_[0]][pos_[1]]
        loop = [pos, pos_]
        pos, dir = pos_, pipes[(dir, c)]
        break
    dist = 1
    while True:
        dist += 1
        pos = (pos[0] + move[dir][0], pos[1] + move[dir][1])
        loop.append(pos)
        c = t[pos[0]][pos[1]]
        if c == "S":
            break
        dir = pipes[(dir, c)]
    print(dist // 2)

    print(int(calculate_polygon_area(loop)) - dist // 2 + 1)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    run()
