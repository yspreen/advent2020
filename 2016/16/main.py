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
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return np.array(lmap(int, s), dtype=np.uint8)


def iterate(data):
    a = data
    b = np.flip(data)
    b = 1 - b
    return np.hstack((a, [0], b))


def fill(length, data):
    if data.size < length:
        return fill(length, iterate(data))
    return data[:length]


def hash(data):
    h = np.zeros(data.size // 2, dtype=np.uint8)
    for i in range(data.size)[::2]:
        a, b = data[i : i + 2]
        if a == b:
            h[i // 2] = 1
    if h.size % 2:
        return h
    return hash(h)


def hash_print(h):
    print("".join(map(str, h)))


def easy():
    hash_print(hash(fill(272, t)))


def hard():
    hash_print(hash(fill(35651584, t)))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
