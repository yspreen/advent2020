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
    t = []
    for r in s.splitlines()[0].split(","):
        if r[0] == "s":
            t.append(("s", int(r[1:])))
        if r[0] == "x":
            t.append(("x", *lmap(int, r[1:].split("/"))))
        if r[0] == "p":
            t.append(("p", *lmap(str, r[1:].split("/"))))
    return t


def op_s(T, a, _=None):
    return T[-a:] + T[:-a]


def op_x(T, a, b):
    T[a], T[b] = T[b], T[a]
    return T


def op_p(T, a, b):
    return op_x(T, T.index(a), T.index(b))


def loop(T=None):
    T = list(ascii_lowercase[:16]) if T is None else T
    for r in t:
        T = {"s": op_s, "x": op_x, "p": op_p}[r[0]](T, *r[1:])
    return T


def easy():
    print("".join(loop()))


def hard():
    T, s, n = None, set(["".join(ascii_lowercase[:16])]), 0
    while True:
        n += 1
        T = loop(T)
        c = "".join(T)
        if c in s:
            break
        s.add(c)
    T = None
    for _ in range(1000000000 % n):
        T = loop(T)
    print("".join(T))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()