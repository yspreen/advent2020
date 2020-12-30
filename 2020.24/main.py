import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product
import llist

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().replace("\r", "").split("\n")

    for a, b in [
        ("se", "1"),
        ("sw", "2"),
        ("nw", "4"),
        ("ne", "5"),
        ("e", "0"),
        ("w", "3"),
    ]:
        t = [l.replace(a, b) for l in t]
    return [[int(i) for i in l] for l in t[:-1]]


changes = [
    [0, 1],  # e 0
    [1, 0],  # se* 1
    [1, -1],  # sw* 2
    [0, -1],  # w 3
    [-1, -1],  # nw* 4
    [-1, 0],  # ne* 5
]

t = read()
N = max([len(l) for l in t]) * 2 + 100
A = np.zeros((N, N), dtype=np.int32)


def change(coord, change):
    if change not in [0, 3]:
        coord[1] += coord[0] % 2
    change = changes[change]
    coord[0] += change[0]
    coord[1] += change[1]


def easy():
    for row in t:
        coord = [N // 2, N // 2]
        for c in row:
            change(coord, c)
        A[tuple(coord)] = 1 - A[tuple(coord)]
    print(A.sum())


def hard():
    global A
    for _ in range(100):
        A_ = A.copy()
        for i, j in product(*[range(1, N - 1) for _ in range(2)]):
            neighbors = 0
            for ci, c in enumerate(changes):
                j_ = j
                if ci not in [0, 3]:
                    j_ += i % 2
                i_ = i + c[0]
                j_ = j_ + c[1]
                neighbors += A[i_, j_]
            if A[i, j] and neighbors not in [1, 2]:
                A_[i, j] = 0
            if not A[i, j] and neighbors == 2:
                A_[i, j] = 1
        A = A_
    print(A.sum())


if __name__ == "__main__":
    easy()
    hard()
