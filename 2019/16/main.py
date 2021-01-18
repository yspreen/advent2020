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
    with open(DIR / "input.txt") as f:
        t = f.read().split("\n")[0] * n
    return np.array([int(i) for i in t], np.int64)


t = read()
N = len(t)
t_ = np.zeros_like(t, np.int64)
pattern = [0, 1, 0, -1]
patterns = {}
raw_patterns = {}


def get_pattern(n):
    print("> ", n)
    if patterns.get(n, None) is None:
        patterns[n] = get_pattern_(n)
    return patterns[n]


def get_pattern_raw(n):
    if raw_patterns.get(n, None) is None:
        if raw_patterns.get(n - 1, None) is None:
            raw_patterns[n] = get_pattern_raw_(n)
        else:
            raw_patterns[n] = iterate(raw_patterns[n - 1])
    return raw_patterns[n]


def iterate(pattern):
    # print("i", N)
    last = 0
    i = -1
    while True:
        print(">> ", i)
        i += 1
        if i >= N + 1:
            break
        p = pattern[i]
        if last != p:
            pattern = np.insert(pattern, i, last)[: N + 1]
            i += 1
        last = p
    return pattern


def get_pattern_raw_(n):
    p = [[i] * (n + 1) for i in pattern]
    a = np.array(
        [i for sublist in p * (len(t) // len(p) + 1) for i in sublist],
        np.int32,
    )
    return a[: len(t) + 1]


def get_pattern_(n):
    a = get_pattern_raw(n)[1:]
    plus = np.where(a == 1)
    minus = np.where(a == -1)
    return plus, minus


def trim(i):
    return (i % 10) - (0 if i > 0 else 10)


def step():
    global t, t_
    t_ *= 0
    for i in range(N):
        x = [-1, 1, 1, -1][i % 4]
        for j in range(1, N + 1):
            y = j // (i + 1)
            if y >= N:
                continue
            t_[y] = t_[y] + t[j - 1] * x
    for i in range(N):
        if i < N - 1:
            t_[i + 1] += t_[i]
        t_[i] = abs(t_[i]) % 10
    t, t_ = t_, t


def easy():
    for _ in range(100):
        step()
    print("".join(map(str, t[:8])))


def hard():
    global t, t_, patterns, raw_patterns, N
    patterns = {}
    raw_patterns = {}
    t = read(10000)
    t_ = np.zeros_like(t, np.int64)
    N = len(t)
    for i in range(100):
        # print(i)
        step()
    print("".join(map(str, t[:8])))


if __name__ == "__main__":
    easy()
    hard()
