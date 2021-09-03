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
        s = (f.read() if teststr == "" else teststr).replace(".", "").splitlines()
    return lmap(lambda r: lmap(int, map(lambda i: r.split(" ")[i], [3, 11])), s)


def easy():
    for i in range(len(t)):
        t[i][1] += i + 1
        t[i][1] %= t[i][0]

    N = 0
    for i in range(len(t)):
        X = t[i][0] - t[i][1]
        for j in range(len(t)):
            if i == j:
                continue
            X *= t[j][0]
        N += X
    N %= prod([i[0] for i in t])
    print(N)


def hard():
    return


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
