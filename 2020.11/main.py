import numpy as np
import re
import pathlib
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")

lookup = {
    ".": 0,
    "L": 1,
    "#": 2,
}
reverse_lookup = {}
for k, v in lookup.items():
    reverse_lookup[v] = k


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().replace("\r", "")
    #     t = """L.LL.LL.LL
    # LLLLLLL.LL
    # L.L.L..L..
    # LLLL.LL.LL
    # L.LL.LL.LL
    # L.LLLLL.LL
    # ..L.L.....
    # LLLLLLLLLL
    # L.LLLLLL.L
    # L.LLLLL.LL"""
    t = t.split("\n")
    if t[-1] == "":
        t.pop()
    t = [[lookup[e] for e in l] for l in t]

    t = [[0] + l + [0] for l in t]
    pad = [0 for _ in t[0]]
    t = [pad] + t + [pad]

    t = np.array(t, dtype=np.uint32)

    return t


A_ = A = read()
change = True


def change_field(A, A_, i, j):
    global change

    if A[i, j] == 0:  # .
        return
    masked = A_[i - 1 : i + 2, j - 1 : j + 2]
    adj = len(np.where(masked == 2)[0])
    if A[i, j] == 1:  # L
        flip = adj == 0
    elif A[i, j] == 2:  # #
        flip = adj >= 4 + 1  # center is part of mask
    if flip:
        change = True
        A[i, j] = 3 - A[i, j]


def change_field_masked(A, A_, Mask, i, j):
    global change

    if A[i, j] == 0:  # .
        return
    masked = A_[Mask[i][j]]
    adj = len(np.where(masked == 2)[0])
    if A[i, j] == 1:  # L
        flip = adj == 0
    elif A[i, j] == 2:  # #
        flip = adj >= 5  # center is not part of mask
    if flip:
        change = True
        A[i, j] = 3 - A[i, j]


def fancyprint(end="\n"):
    for row in A[1:-1]:
        for e in row[1:-1]:
            print(reverse_lookup[e], end="")
        print()
    print(end=end)


def find_lookup_mask(A):
    Mask = [[list() for i in row] for row in A]

    directions = list(product([0, 1, -1], repeat=2))[1:]

    N, M = A.shape
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            for d in directions:
                i_ = i + d[0]
                j_ = j + d[1]
                while (
                    i_ > 0 and i_ < N - 1 and j_ > 0 and j_ < M - 1 and A[i_, j_] == 0
                ):
                    i_ += d[0]
                    j_ += d[1]
                if i_ > 0 and i_ < N - 1 and j_ > 0 and j_ < M - 1:
                    Mask[i][j].append((i_, j_))
    Mask = [[tuple(zip(*tuple(e))) for e in row] for row in Mask]
    return Mask


def easy():
    global change, A, A_

    N, M = A.shape

    while change:
        # fancyprint()
        change = False

        A_ = A.copy()
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                change_field(A, A_, i, j)
    print(len(np.where(A == 2)[0]))


def check_mask(A, Mask, x, y):
    for i, row in enumerate(A[1:-1]):
        for j, e in enumerate(row[1:-1]):
            if (i + 1, j + 1) in list(zip(*Mask[x + 1][y + 1])):
                print("x", end="")
            elif i == x and j == y:
                print("@", end="")
            else:
                print(reverse_lookup[e], end="")
        print()
    print()


def hard():
    global change, A, A_

    A = read()
    Mask = find_lookup_mask(A)
    # print(Mask[3][5])
    # check_mask(A, Mask, 3, 5)

    N, M = A.shape

    change = True
    while change:
        # fancyprint()
        change = False

        A_ = A.copy()
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                change_field_masked(A, A_, Mask, i, j)
    print(len(np.where(A == 2)[0]))


if __name__ == "__main__":
    easy()
    hard()
