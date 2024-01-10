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
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(str, r), s)


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]


def can_walk(x, y):
    if x < 0 or y < 0:
        return False
    return t[x][y] != "#"


def can_walk_hard(x, y):
    return t[x % N][y % M] != "#"


def BFS(start, can_walk, steps):
    options = {start}
    seen = {start}
    counts = [0, 0]

    for i in range(steps):
        counts[i % 2] += len(options)
        new_o = set()
        for pos in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p in seen:
                    continue
                seen.add(new_p)
                try:
                    assert can_walk(*new_p)
                except:
                    continue
                new_o.add(new_p)
        seen = options
        options = new_o
    return len(options) + counts[steps % 2]


def easy():
    start = None
    for x, row in enumerate(t):
        try:
            y = row.index("S")
            start = (x, y)
            break
        except Exception:
            continue
    print((BFS(start, can_walk, 64)))


def hard():
    start = None
    for x, row in enumerate(t):
        try:
            y = row.index("S")
            start = (x, y)
            break
        except Exception:
            continue
    print(len(BFS(start, can_walk_hard, 26501365)))


teststr = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
N = len(t)
M = len(t[0])
if __name__ == "__main__":
    easy()
    hard()
