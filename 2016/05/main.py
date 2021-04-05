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
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def hash(num):
    from hashlib import md5

    return str(md5((t + str(num)).encode()).hexdigest())


def easy():
    s, i = "", 0
    for _ in range(8):
        while True:
            i += 1
            h = hash(i)
            if h[:5] == "0" * 5:
                s += h[5]
                break
    print(s)


def hard():
    s, i, solved = ["_"] * 8, 0, set()
    while len(solved) != 8:
        while True:
            i += 1
            h = hash(i)
            if h[:5] == "0" * 5 and h[5] in map(str, range(8)) and h[5] not in solved:
                s[int(h[5])] = h[6]
                # print("".join(s))
                solved.add(h[5])
                break
    print("".join(s))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()