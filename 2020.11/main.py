import numpy as np
import re
import pathlib
from functools import reduce
from string import ascii_lowercase
from math import prod

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
        flip = adj >= 4 + 1
    if flip:
        change = True
        A[i, j] = 3 - A[i, j]


def fancyprint(end="\n"):
    for row in A[1:-1]:
        for e in row[1:-1]:
            print(reverse_lookup[e], end="")
        print()
    print(end=end)


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


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
