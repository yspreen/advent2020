import numpy as np
import pathlib
from itertools import product

DIR = pathlib.Path(__file__).parent.absolute()

N = 20


def read():
    with open(DIR / "input") as f:
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


def do_stuff(dim):
    A = np.zeros((N,) * dim, dtype=np.int32)
    index = [N // 2] * dim
    for i in [0, 1]:
        index[i] = slice(N // 2 - 4, N // 2 + 4, None)
    A[tuple(index)] = t

    for _ in range(6):
        A = step(A)
    print(A.sum())


def easy():
    do_stuff(3)


def hard():
    do_stuff(4)


if __name__ == "__main__":
    easy()
    hard()
