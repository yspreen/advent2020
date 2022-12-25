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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return s


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
]


def BFS(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, 0)]
    visited = set([start])

    while options:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:  # lower bound check
                    continue
                if new_p[1] < 0:  # lower bound check
                    continue
                try:
                    assert can_walk(pos, new_p)
                except:
                    continue  # upper bound check
                if new_p in visited:
                    continue
                visited.add(new_p)
                cost_ = cost + cost_fn(pos, new_p)
                new_o.append((new_p, cost_))
                if goal(new_p):
                    return cost_
        options = new_o
    return None


idx = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}
r_idx = {
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2",
}


def s_to_d(n):
    r = reversed(lmap(str, n))
    prev_num = 0
    x = 1
    for c in r:
        prev_num += x * idx[c]
        x *= 5
    return prev_num


def d_to_s(s):
    res = ""
    x = 1
    added = {}
    while s > x * 2:
        x *= 5
    while x >= 1:
        N = s // x + added.get(x, 0)
        if N > 2:
            x *= 5
            last_v = res[-1]
            res = res[:-1]
            added[x] = added.get(x, 0) + 1
            s += x * idx[last_v]
            continue
        s -= N * x
        res += r_idx[N]
        # print(res, x)
        x //= 5
    return res


def easy():
    s = 0
    for n in t:
        s += s_to_d(n)
    print(s)
    print(s_to_d(d_to_s(s)))
    print(d_to_s(s))


def hard():
    return


teststr = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
