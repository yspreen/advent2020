import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read(n=1):
    global t, N, OFF
    with open(DIR / "input.txt") as f:
        t_ = f.read().split("\n")[0]
        # t_ = "03036732577212944063491565474664"
    t = np.array([int(i) for i in t_], np.int16)
    N = len(t) * n
    OFF = 0 if n == 1 else int(t_[:7])


t = N = OFF = 0
read()


def easy():
    return


def get_t(i):
    return t[i % len(t)]


def phase(p, p_, n):
    i = N
    s = 0
    while i > OFF:
        i -= 1
        s += p[i - OFF] if n > 0 else get_t(i)
        s %= 10
        p_[i - OFF] = s
    return p_, p


def hard():
    read(10000)
    p = np.zeros((N - OFF,), np.int32)
    p_ = np.zeros_like(p)
    for i in range(100):
        p, p_ = phase(p, p_, i)
    print("".join(map(str, p[:8])))


if __name__ == "__main__":
    easy()
    hard()
