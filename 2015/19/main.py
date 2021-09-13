import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import cos, prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    c = ord("a")
    for element in sorted(
        list(set(map(lambda i: i.split(" ")[0], s.splitlines()[:-2])))
    ):
        if element == "e":
            continue
        while chr(c) in s:
            c += 1
        s = s.replace(element, chr(c))
        c += 1

    repl = {}
    for k, v in map(lambda r: tuple(r.split(" => ")), s.splitlines()[:-2]):
        repl[k] = repl.get(k, []) + [v]
    return repl, s.splitlines()[-1]


def easy():
    found = set()
    for i, c in enumerate(t):
        for r in repl.get(c, []):
            found.add(t[:i] + r + t[i + 1 :])
    print(len(found))


def neighbors(chain):
    n = []
    for s in [s for s in search if s in chain]:
        n.append(chain.replace(s, rev[s], 1))
    return n


def step(cost, pos, visited):
    for m in [m for m in neighbors(pos) if m not in visited]:
        visited.add(m)
        if m == "e":
            return print(cost + 1)
        if not step(cost + 1, m, visited):
            return 0
    return 1


def DFS(start_pos):
    step(0, start_pos, set())


def hard():
    DFS(t)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
repl, t = read()
rev = {}
for k, v in repl.items():
    for r in v:
        rev[r] = k
search = list(sorted(rev.keys(), key=lambda i: -len(i)))
if __name__ == "__main__":
    easy()
    hard()
