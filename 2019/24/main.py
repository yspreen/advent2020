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
    with open(DIR / "input.txt") as f:
        t = f.read().splitlines()
    return np.array([[[".", "#"].index(e) for e in i] for i in t], np.int32), len(t)


def easy():
    global masks, A
    for i, j in product(range(N), repeat=2):
        masks[(i, j)] = []
        for mx, my in zip(
            (-1, 1, 0, 0),
            (0, 0, -1, 1),
        ):
            if 0 <= i + mx < N and 0 <= j + my < N:
                masks[(i, j)].append((i + mx, j + my))
    seen = set([score(A)])
    masks = {k: tuple(zip(*v)) for k, v in masks.items()}
    while True:
        A_ = np.zeros_like(A)
        for i, j in product(range(N), repeat=2):
            a = A[masks[(i, j)]].sum()
            A_[i, j] = 1 if a == 1 or a == 2 else 0
            if A[i, j] and a == 2:
                A_[i, j] = 0
        A = A_
        s = score(A)
        if s in seen:
            print(s)
            return
        seen.add(s)


def score(A):
    return (A * scores).sum()


def hard():
    return


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
A, N = read()
scores = np.power(2, np.arange(N * N)).reshape((N, N))
masks = {}

if __name__ == "__main__":
    easy()
    hard()