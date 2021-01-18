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
    global t, N, OFF, base, pattern, phases
    with open(DIR / "input.txt") as f:
        t_ = f.read().split("\n")[0] * n
    t = np.array([int(i) for i in t_], np.int64)
    N = len(t)
    OFF = 0 if n == 1 else int(t_[:7])
    base = [0, 1, 0, -1]
    pattern = {}
    phases = [{} for _ in range(100 + 1)]


t = N = OFF = base = pattern = phases = 0
read()


def pattern_row(n):
    try:
        return pattern[n]
    except:
        pass

    p = [[i] * (n + 1) for i in base][: N + 1]
    a = np.array(
        [i for sublist in p * (N // len(p) + 1) for i in sublist],
        np.int32,
    )[1 : N + 1]

    plus = np.where(a == 1)
    minus = np.where(a == -1)
    a = (plus, minus)

    pattern[n] = a
    return a


def phase(i, n):
    try:
        return phases[n][i]
    except:
        pass
    if n == 0:
        p = t[i]
    else:
        plus, minus = pattern_row(i)
        p = 0
        for j in plus[0]:
            p += phase(j, n - 1)
        for j in minus[0]:
            p -= phase(j, n - 1)
    p = abs(p) % 10
    phases[n][i] = p
    return p


def calc():
    r = []
    for i in range(OFF, OFF + 8):
        r.append(phase(i, 100))
    return r


def easy():
    print("".join(map(str, calc())))


def hard():
    read(10000)
    print("".join(map(str, calc())))


if __name__ == "__main__":
    easy()
    hard()
