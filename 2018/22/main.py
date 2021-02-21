import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols, solve


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    t = map(lambda l: l.split(": ")[1], t)
    t = list(map(lambda l: list(map(int, l.split(","))), t))
    return t[0][0], t[1][0], t[1][1]


def easy():
    A = np.zeros((TX + 1, TY + 1), np.int)
    for x in range(TX + 1):
        A[x, 0] = (X * x + D) % M
    for y in range(1, TY + 1):
        A[0, y] = (Y * y + D) % M
    for x, y in product(range(1, TX + 1), range(1, TY + 1)):
        A[x, y] = (A[x - 1, y] * A[x, y - 1] + D) % M
    A[TX, TY] = (0 + D) % M
    A %= 3
    # for r in A.T:
    #     for e in r:
    #         print([".", "=", "|"][e], end="")
    #     print()
    print(A.sum())


def hard():
    return


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
D, TX, TY = read()
dirs = {}
X = 16807
Y = 48271
M = 20183

if __name__ == "__main__":
    easy()
    hard()