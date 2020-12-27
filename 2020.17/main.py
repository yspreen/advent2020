import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")

N = 20


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().replace("\r", "").split("\n")
    t.pop()
    return np.array([[1 if i == "#" else 0 for i in l] for l in t], dtype=np.int32)


t = read()


def step(A):
    A_ = np.zeros_like(A, dtype=np.int32)
    ranges = [range(1, N - 1) for _ in range(len(A.shape))]
    for coords in product(*ranges):
        middle = A[coords]
        cube = tuple([slice(i - 1, i + 2, None) for i in list(coords)])
        cube = A[cube]
        count = cube.sum()
        if middle == 1:
            state = count == 3 or count == 4
        else:
            state = count == 3
        A_[coords] = 1 if state else 0
    return A_


def easy():
    A = np.zeros((N, N, N), dtype=np.int32)
    A[N // 2 - 4 : N // 2 + 4, N // 2 - 4 : N // 2 + 4, N // 2] = t

    # fancyprint(A)
    for _ in range(6):
        A = step(A)
        # fancyprint(A)
    print(A.sum())


def hard():
    A = np.zeros((N, N, N, N), dtype=np.int32)
    A[N // 2 - 4 : N // 2 + 4, N // 2 - 4 : N // 2 + 4, N // 2, N // 2] = t

    # fancyprint(A)
    for _ in range(6):
        A = step(A)
        # fancyprint(A)
    print(A.sum())


def fancyprint(A):
    for z in range(N):
        if A[:, :, z].sum() == 0:
            continue
        print("z = ", z - N // 2)
        d = np.array(np.where(A[:, :, z] > 0))
        d = abs(d.reshape(d.size) - N // 2).max()
        A_ = A[N // 2 - d : N // 2 + d, N // 2 - d : N // 2 + d, z]
        for row in A_:
            for e in row:
                print("#" if e == 1 else ".", end="")
            print()
        print()
    print("---")


if __name__ == "__main__":
    easy()
    hard()
