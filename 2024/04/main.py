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


def diag_match(t, i, j, s):
    for k in range(len(s)):
        if i + k >= len(t) or j + k >= len(t[0]):
            return False
        if t[i + k][j + k] != s[k]:
            return False
    return True


def rev_diag_match(t, i, j, s):
    for k in range(len(s)):
        if i + k >= len(t) or j - k < 0:
            return False
        if t[i + k][j - k] != s[k]:
            return False
    return True


def easy():
    c = 0
    for line in t:
        c += "".join(line).count("XMAS")
        c += "".join(line).count("SAMX")
    for line in list(zip(*t)):
        c += "".join(line).count("XMAS")
        c += "".join(line).count("SAMX")

    for i in range(len(t)):
        for j in range(len(t[0])):
            if diag_match(t, i, j, "XMAS"):
                c += 1
            if diag_match(t, i, j, "SAMX"):
                c += 1
            if rev_diag_match(t, i, j, "XMAS"):
                c += 1
            if rev_diag_match(t, i, j, "SAMX"):
                c += 1
    print(c)


def hard():
    c = 0
    for i in range(len(t) - 2):
        for j in range(len(t[0]) - 2):
            if t[i + 1][j + 1] != "A":
                continue
            if t[i + 0][j + 0] != "S" and t[i + 0][j + 0] != "M":
                continue
            if t[i + 0][j + 2] != "S" and t[i + 0][j + 2] != "M":
                continue
            if t[i + 2][j + 0] != "S" and t[i + 2][j + 0] != "M":
                continue
            if t[i + 2][j + 2] != "S" and t[i + 2][j + 2] != "M":
                continue
            if t[i + 0][j + 0] == t[i + 2][j + 2]:
                continue
            if t[i + 0][j + 2] == t[i + 2][j + 0]:
                continue
            c += 1
    print(c)


teststr = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
