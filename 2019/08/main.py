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


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().split("\n")
    if t[-1] == "":
        t.pop()
    return np.array([int(i) for i in t[0]], dtype=np.int32).reshape(-1, 6, 25)


t = read()


def easy():
    m = (inf, 0)
    for i in range(100):
        c = len(np.where(t[i, :, :] == 0)[0])
        if c < m[0]:
            m = (c, i)
    print(prod([len(np.where(t[m[1], :, :] == k)[0]) for k in range(1, 3)]))


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()