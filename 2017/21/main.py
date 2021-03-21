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


def rule(left, right):
    left, right = parse(left), parse(right)
    for i in range(8):
        if i % 2:
            left = np.rot90(left)
        left = np.flip(left, 1)
        t[tuple(left.flatten())] = right


def parse(a):
    a = np.array(
        lmap(lambda i: lmap(ord, i), a.replace("/", "\n").splitlines()), np.int
    )
    a[a == ord(".")] = 0
    a[a == ord("#")] = 1
    return a


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    lmap(lambda r: rule(*r.split(" => ")), s.splitlines())


def iterations(n):
    A = parse(".#./..#/###")
    for _ in range(n):
        S = 2 + (A.shape[0] % 2)
        rows = []
        for x in range(A.shape[0])[::S]:
            row = []
            for y in range(A.shape[0])[::S]:
                row.append(t[tuple(A[x : x + S, y : y + S].flatten())])
            row = np.hstack(row)
            rows.append(row)
        A = np.vstack(rows)
    print(A.sum())


def easy():
    iterations(5)


def hard():
    iterations(18)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = {}
read()
if __name__ == "__main__":
    easy()
    hard()