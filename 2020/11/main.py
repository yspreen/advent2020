import numpy as np
import pathlib
from itertools import product

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
    with open(DIR / "input") as f:
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


def change_field(A, A_, i, j, Mask=None):
    global change

    if A[i, j] == 0:  # .
        return
    if Mask is None:
        masked = A_[i - 1 : i + 2, j - 1 : j + 2]
    else:
        masked = A_[Mask[i][j]]
    adj = len(np.where(masked == 2)[0])
    if A[i, j] == 1:  # L
        flip = adj == 0
    elif A[i, j] == 2:  # #
        flip = adj >= 5
    if flip:
        change = True
        A[i, j] = 3 - A[i, j]


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
        change = False

        A_ = A.copy()
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                change_field(A, A_, i, j)
    print(len(np.where(A == 2)[0]))


def hard():
    global change, A, A_

    A = read()
    Mask = find_lookup_mask(A)

    N, M = A.shape

    change = True
    while change:
        change = False

        A_ = A.copy()
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                change_field(A, A_, i, j, Mask)
    print(len(np.where(A == 2)[0]))


if __name__ == "__main__":
    easy()
    hard()
