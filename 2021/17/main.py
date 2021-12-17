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


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return lmap(int, s.split("x=")[1].replace(", y=", "..").split(".."))


def step(x, y, vx, vy):
    x += vx
    y += vy
    vx -= 1 if vx > 0 else 0
    vy -= 1
    return x, y, vx, vy


def run(vx, vy):
    x = y = 0
    while x <= t[1] and y >= t[2] and (x < t[0] or y > t[3]):
        x, y, vx, vy = step(x, y, vx, vy)
    return x <= t[1] and y >= t[2]


def easy():
    for i in range(-t[2]):
        j = i = -t[2] - i
        x = 0
        while x > t[3]:
            x -= i
            i += 1
        if x < t[2]:
            continue
        return print(sumto(j - 1))


def sumto(x):
    return (x + 1) * x // 2


def hard():
    pairs = []
    for vx in range(t[1] + 1):
        for vy in range(t[2], -t[2]):
            if run(vx, vy):
                pairs.append((vx, vy))
    print(len(pairs))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
