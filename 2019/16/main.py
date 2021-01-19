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
    t = np.array([int(i) for i in t_], np.int16)
    N = len(t)
    OFF = 0 if n == 1 else int(t_[:7])
    base = [0, 1, 0, -1]
    pattern = {}
    phases = [{} for _ in range(100 + 1)]


t = N = OFF = base = pattern = phases = 0
read()


def encode(arr):
    r = []
    last = 0
    curr = None
    for i in range(len(arr)):
        a = arr[i]
        if a != last:
            if a != 0:
                curr = (a, i)
            else:
                r.append((curr[0], curr[1], i))
                curr = None
        last = a
    if curr is not None:
        r.append((curr[0], curr[1], len(arr)))
    return r


def pattern_row(n):
    try:
        return pattern[n]
    except:
        pass

    i = n
    r = []
    while i < N + 1:
        r.append(i - 1)
        i += n
    r.append(N)
    x = 1
    for i in range(len(r) - 1):
        r[i] = (x, r[i], r[i + 1])
        x = -x
    r.pop()

    return r


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
    print(pattern_row(4))  # print("".join(map(str, calc())))


def hard():
    read(10000)
    # print("".join(map(str, calc())))
    print(OFF, pattern_row(OFF))

    lower = OFF
    upper = OFF + 8
    for _ in range(100):
        lower = pattern_row(lower)[0][1]
        upper = pattern_row(upper)[-1][2] - 1
    print(pattern_row(lower))
    print(pattern_row(upper))


if __name__ == "__main__":
    easy()
    hard()
