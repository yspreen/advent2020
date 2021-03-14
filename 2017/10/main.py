import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(int, s.splitlines()[0].split(","))


def easy():
    global T
    i = 0
    s = 0
    for l in t:
        i %= N
        T = T + T
        j = i + l
        r = T[i:j]
        r.reverse()
        T = T[:i] + r + T[j:]
        T = T[N : N + i] + T[i:N]
        i += l + s
        s += 1
    print(T[0] * T[1])


def hard():
    return


teststr = ""  # """3,4,1,5"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
N = 256  # 5
T = list(range(N))
if __name__ == "__main__":
    easy()
    hard()