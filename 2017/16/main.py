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


def easy():
    global T
    for r in t:
        T = {"s": op_s, "x": op_x, "p": op_p}[r[0]](T, *r[1:])
    print("".join(T))


def hard():
    global T
    a = lmap(lambda i: ascii_lowercase.index(i), T)
    print(a)
    for _ in range(1):
        b = list(range(16))
        for q in range(10):
            b = lmap(lambda i: b[a[i]], range(16))
            if q == 0:
                print("x", b)
        a = b
    print("".join(lmap(lambda i: ascii_lowercase[i], a)))
    T = list(ascii_lowercase[:16])
    for r in t * 10:
        T = {"s": op_s, "x": op_x, "p": op_p}[r[0]](T, *r[1:])
    print("".join(T))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
T = list(ascii_lowercase[:16])
if __name__ == "__main__":
    easy()
    hard()