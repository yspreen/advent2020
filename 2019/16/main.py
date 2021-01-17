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


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().split("\n")[0]
    return [int(i) for i in t]


t = read()
pattern = [0, 1, 0, -1]

patterns = {}


def get_pattern(n):
    if patterns.get(n, None) is None:
        patterns[n] = get_pattern_(n)
    return patterns[n]


def get_pattern_(n):
    p = [[i] * (n + 1) for i in pattern]
    return [i for sublist in p * (len(t) // 3) for i in sublist][1 : len(t) + 1]


def step():
    global t
    t_ = []
    for i in range(len(t)):
        p = get_pattern(i)
        s = sum(map(prod, zip(t, p)))
        t_.append(abs(s) % 10)
    t = t_


def easy():
    for _ in range(100):
        step()
    print("".join(map(str, t[:8])))


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
