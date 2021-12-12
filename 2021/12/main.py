from curses.ascii import isupper
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
        s, d = (f.read() if teststr == "" else teststr).splitlines(), {}
    for a, b in lmap(lambda r: r.split("-"), s):
        d[a] = d.get(a, []) + [b]
        d[b] = d.get(b, []) + [a]
    return d


def easy():
    states, R = [("start", ["start"])], 0
    while states:
        states_, states = states, []
        for pos, hist in states_:
            for path in t[pos]:
                if path == "end":
                    R += 1
                    continue
                if path in hist and not isupper(path[0]):
                    continue
                states.append((path, hist + [path]))
    print(R)


def hard():
    states, R = [("start", ["start"], 0)], 0
    while states:
        states_, states = states, []
        for pos, h, F in states_:
            for p in t[pos]:
                if p == "end":
                    R += 1
                    continue
                if p in h and not isupper(p[0]):
                    if not F and p != "start" and p != "end" and h.count(p) == 1:
                        states.append((p, h + [p], 1))
                    continue
                states.append((p, h + [p], F))
    print(R)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
