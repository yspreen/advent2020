import numpy as np
import re
import pathlib
import json
from functools import reduce, cmp_to_key
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
    (-1, 1),  # UR
    (1, 1),  # DR
    (-1, -1),  # UL
    (1, -1),  # DL
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
]


def BFS(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, 0)]
    visited = set([start])

    while options:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:  # lower bound check
                    continue
                if new_p[1] < 0:  # lower bound check
                    continue
                try:
                    assert can_walk(pos, new_p)
                except:
                    continue  # upper bound check
                if new_p in visited:
                    continue
                visited.add(new_p)
                cost_ = cost + cost_fn(pos, new_p)
                new_o.append((new_p, cost_))
                if goal(new_p):
                    return cost_
        options = new_o
    return None


def easy():
    spots = {}
    seen = set()
    for i in range(len(t)):
        for j in range(len(t[0])):
            c = t[i][j]
            if c == ".":
                continue
            if c not in spots:
                spots[c] = []
            spots[c].append((i, j))
    for c, v in spots.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                a, b = v[i], v[j]
                diff = (a[0] - b[0], a[1] - b[1])
                point_a = a[0] + diff[0], a[1] + diff[1]
                point_b = b[0] - diff[0], b[1] - diff[1]
                if 0 <= point_a[0] < len(t) and 0 <= point_a[1] < len(t[0]):
                    seen.add(point_a)
                if 0 <= point_b[0] < len(t) and 0 <= point_b[1] < len(t[0]):
                    seen.add(point_b)
    print(len(seen))


def hard():
    spots = {}
    seen = set()
    for i in range(len(t)):
        for j in range(len(t[0])):
            c = t[i][j]
            if c == ".":
                continue
            if c not in spots:
                spots[c] = []
            spots[c].append((i, j))
    for c, v in spots.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                a, b = v[i], v[j]
                diff = (a[0] - b[0], a[1] - b[1])
                for multiplier in range(100):
                    point_a = a[0] + multiplier * diff[0], a[1] + multiplier * diff[1]
                    if 0 <= point_a[0] < len(t) and 0 <= point_a[1] < len(t[0]):
                        seen.add(point_a)
                    else:
                        break
                for multiplier in range(100):
                    point_b = b[0] - multiplier * diff[0], b[1] - multiplier * diff[1]
                    if 0 <= point_b[0] < len(t) and 0 <= point_b[1] < len(t[0]):
                        seen.add(point_b)
                    else:
                        break
    print(len(seen))


teststr = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
