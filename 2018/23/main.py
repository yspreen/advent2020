import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols, solve


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    t = list(
        map(
            lambda l: (
                tuple(map(int, l.split("<")[1].split(">")[0].split(","))),
                int(l.split("=")[-1]),
            ),
            t,
        )
    )
    return t


def dist(a, b, k=1):
    return sum([abs(a[0] - b[0] // k), abs(a[1] - b[1] // k), abs(a[2] - b[2] // k)])


def count(m, k=1):
    c = 0
    for l in t:
        if dist(m[0], l[0], k=k) <= m[1] // k:
            c += 1
    return c


def count_p(p, k=1):
    c = 0
    for l in t:
        if dist(p, l[0], k=k) <= l[1] // k:
            c += 1
    return c


def easy():
    t.sort(key=lambda i: i[1])
    m = t[-1]

    print(count(m))


def seed(rule):
    s = []
    for i_, j_, k_ in product(range(rule[1] * 2 + 1), repeat=3):
        i, j, k = (
            i_ - rule[1] + rule[0][0],
            j_ - rule[1] + rule[0][1],
            k_ - rule[1] + rule[0][2],
        )
        if dist((i, j, k), rule[0]) <= rule[1]:
            s.append((i, j, k))
    return s


def hard():
    import math

    for n in range(7):
        print("no")
        n = "0{0:b}".format(n)
        l = [t[i] for i in range(len(t)) if n[-(i + 1) :][:1] != "1"]
        s = seed(l[0])
        broken = False
        for r in l[1:]:
            del_queue = []
            for i, p in enumerate(s):
                if dist(p, r[0]) > r[1]:
                    del_queue.append(i)
            del_queue.reverse()
            for i in del_queue:
                del s[i]
            if not s:
                broken = True
                break
        if not broken:
            print(s)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()