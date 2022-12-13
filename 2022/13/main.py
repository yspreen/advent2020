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
from functools import cmp_to_key


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).split("\n\n")
    return lmap(lambda s: lmap(parseline, s.splitlines()), s)


def parseline(line):
    return eval(line)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
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


def is_right_order(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        if l > r:
            return False
        else:
            return None
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]

    for i in range(len(l)):
        if i >= len(r):
            return False
        val = is_right_order(l[i], r[i])
        if val == True:
            return True
        if val == False:
            return False

    if len(l) < len(r):
        return True

    return None


def easy():
    s = 0
    for i in range(len(t)):
        if is_right_order(t[i][0], t[i][1]):
            s += i + 1
    print(s)


def hard():
    t_ = []
    for a, b in t:
        t_.append(a)
        t_.append(b)
    t_.append([[2]])
    t_.append([[6]])

    t_.sort(key=cmp_to_key(lambda a, b: -1 if is_right_order(a, b) else 1))
    a = b = 0
    for i in range(len(t_)):
        if str(t_[i]) == "[[2]]":
            a = i + 1
        if str(t_[i]) == "[[6]]":
            b = i + 1
    print(a * b)


teststr = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
