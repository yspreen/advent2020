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
        s = (
            (f.read() if teststr == "" else teststr)
            .replace("#", "1")
            .replace(".", "0")
            .split("\n\n")
        )
    return [np.array(lmap(lambda r: lmap(int, r), block.splitlines())) for block in s]


def mirrors(A, col):
    A_rev = A[:, ::-1]
    A = A[:, : col + 1]
    A_rev = A_rev[:, : -col - 1]
    min_dim = min(A.shape[1], A_rev.shape[1])
    A = A[:, -min_dim:]
    A_rev = A_rev[:, -min_dim:]

    return np.all(A == A_rev)


def easy():
    horizontals = []
    verticals = []
    for A in t:
        found = False
        for i in range(A.shape[1] - 1):
            if mirrors(A, i):
                horizontals.append(i + 1)
                found = True
                break
        if found:
            continue
        A = A.T
        for i in range(A.shape[1] - 1):
            if mirrors(A, i):
                verticals.append(i + 1)
                break
    print(sum(horizontals) + 100 * sum(verticals))


def hard():
    return


teststr = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
if environ["AOC_SOLVE"] == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
