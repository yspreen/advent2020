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
    return np.array([[[".", "#"].index(e) for e in i] for i in t], np.int32), len(t)


def easy():
    global masks, A
    for i, j in product(range(N), repeat=2):
        masks[(i, j)] = []
        for mx, my in dirs:
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


def get_mask(x_, y_, z):
    mask = []
    for mx, my in dirs:
        x, y = x_ + mx, y_ + my
        if x < 0:
            mask.append((1, 2, z - 1))
        elif y < 0:
            mask.append((2, 1, z - 1))
        elif x == N:
            mask.append((3, 2, z - 1))
        elif y == N:
            mask.append((2, 3, z - 1))
        elif (x, y) == (N // 2, N // 2):
            if x_ == 1:
                mask.extend([(0, j, z + 1) for j in range(N)])
            if x_ == 3:
                mask.extend([(N - 1, j, z + 1) for j in range(N)])
            if y_ == 1:
                mask.extend([(j, 0, z + 1) for j in range(N)])
            if y_ == 3:
                mask.extend([(j, N - 1, z + 1) for j in range(N)])
        else:
            mask.append((x, y, z))
    return tuple(zip(*mask))


def hard():
    global A

    A, _ = read()
    A = A[:, :, np.newaxis]

    for _ in range(200):
        if A[:, :, 0].sum() or A[:, :, -1].sum():
            pad()

        A_ = np.zeros_like(A)
        for x, y, z in product(range(N), range(N), range(M)):
            if (x, y) == (N // 2, N // 2):
                continue
            if z == 0 and (x, y) in outer:
                continue
            if z == M - 1 and (x, y) in inner:
                continue
            a = A[get_mask(x, y, z)].sum()
            A_[x, y, z] = 1 if a == 1 or a == 2 else 0
            if A[x, y, z] and a == 2:
                A_[x, y, z] = 0
        A = A_
    print(A.sum())


def pad():
    global A, z_off, M

    A = np.pad(
        A,
        (
            (0, 0),
            (0, 0),
            (1, 1),
        ),
    )
    z_off += 1
    M += 2


def get_A(A, p):
    return A[p[0], p[1], p[2] + z_off]


def set_A(A, p, v):
    A[p[0], p[1], p[2] + z_off] = v


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
A, N = read()
scores = np.power(2, np.arange(N * N)).reshape((N, N))
masks = {}
z_off = 0
M = 1
dirs = list(
    zip(
        (-1, 1, 0, 0),
        (0, 0, -1, 1),
    )
)
outer = [
    (i, j) for i, j in product(range(N), repeat=2) if i in [0, N - 1] or j in [0, N - 1]
]
inner = set([(i, j) for i, j in product(range(N), repeat=2)]) - set(
    outer + [(N // 2, N // 2)]
)

if __name__ == "__main__":
    easy()
    hard()