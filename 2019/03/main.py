import numpy as np
from scipy.sparse import *

N = 100000


def easy():
    import pathlib

    with open(pathlib.Path(__file__).parent.absolute() / "input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    t = [[(e[0], int(e[1:])) for e in l.split(",")] for l in t]

    A = lil_matrix(eye(N) * 0, dtype=np.int64)

    x = 1
    for l in t:
        p = [N // 2, N // 2]
        for e in l:
            d, n = e

            for _ in range(n):
                if d == "U":
                    p[1] -= 1
                if d == "D":
                    p[1] += 1
                if d == "L":
                    p[0] -= 1
                if d == "R":
                    p[0] += 1
                A[p[0], p[1]] = A[p[0], p[1]] | x
        x *= 2

    A = np.argwhere(A == x - 1)
    A = abs(A - N // 2)
    B = A.sum(axis=1)
    B = B.argmin()

    print(A[B].sum())


def hard():
    import pathlib

    with open(pathlib.Path(__file__).parent.absolute() / "input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    t = [[(e[0], int(e[1:])) for e in l.split(",")] for l in t]

    A = lil_matrix(eye(N) * 0, dtype=np.int64)
    D = [
        0,
        lil_matrix(eye(N) * 0, dtype=np.int64),
        lil_matrix(eye(N) * 0, dtype=np.int64),
    ]

    x = 1
    for l in t:
        p = [N // 2, N // 2]
        s = 0
        for e in l:
            d, n = e

            for _ in range(n):
                s += 1
                if d == "U":
                    p[1] -= 1
                if d == "D":
                    p[1] += 1
                if d == "L":
                    p[0] -= 1
                if d == "R":
                    p[0] += 1
                A[p[0], p[1]] = A[p[0], p[1]] | x
                if D[x][p[0], p[1]] == 0:
                    D[x][p[0], p[1]] = s
        x *= 2

    D = D[1] + D[2]
    print(D[A == x - 1].min())


if __name__ == "__main__":
    easy()
    hard()