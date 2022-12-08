import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def draw():
    scale = "@%" + "#*om:. "
    for row in t:
        for i in row:
            print(scale[i - 1], end="")
            print(scale[i - 1], end="")
        print()


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(int, r), s), dtype=int)


def easy():
    seen = set()
    for i in range(len(t)):
        seen.add((i, 0))
        seen.add((i, len(t[0]) - 1))
    for j in range(len(t[0])):
        seen.add((0, j))
        seen.add((len(t) - 1, j))

    # top down
    for j in range(len(t[0])):
        i = 0
        max = 0
        while i < len(t) and max < 9:
            if t[i, j] > max:
                seen.add((i, j))
                max = t[i, j]
            i += 1

    # left right
    for i in range(len(t)):
        j = 0
        max = 0
        while j < len(t[0]) and max < 9:
            if t[i, j] > max:
                seen.add((i, j))
                max = t[i, j]
            j += 1

    # bottom up
    for j in range(len(t[0])):
        i = len(t) - 1
        max = 0
        while i >= 0 and max < 9:
            if t[i, j] > max:
                seen.add((i, j))
                max = t[i, j]
            i -= 1

    # right left
    for i in range(len(t)):
        j = len(t[0]) - 1
        max = 0
        while j >= 0 and max < 9:
            if t[i, j] > max:
                seen.add((i, j))
                max = t[i, j]
            j -= 1

    print(len(seen))


def hard():
    max_seen = 0
    for i in range(len(t))[1:-1]:
        for j in range(len(t[0]))[1:-1]:
            all_seen = 1

            # down
            seen = 0
            i_ = i + 1
            max = t[i, j]
            while i_ < len(t):
                seen += 1
                if t[i_, j] >= max:
                    break
                i_ += 1
            all_seen *= seen

            # right
            seen = 0
            j_ = j + 1
            while j_ < len(t[0]):
                seen += 1
                if t[i, j_] >= max:
                    break
                j_ += 1
            all_seen *= seen

            # up
            seen = 0
            i_ = i - 1

            while i_ >= 0:
                seen += 1
                if t[i_, j] >= max:
                    break
                i_ -= 1
            all_seen *= seen

            # left
            seen = 0
            j_ = j - 1
            while j_ >= 0:
                if t[i, j_] >= max:
                    break
                seen += 1
                j_ -= 1
            all_seen *= seen
            max_seen = all_seen if all_seen > max_seen else max_seen

    print(max_seen)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    # draw()
    easy()
    hard()
