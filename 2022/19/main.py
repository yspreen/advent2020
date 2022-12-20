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
    s = lmap(lambda l: l.split(":")[1], s)
    s = lmap(lambda l: list(filter(None, lmap(maybeint, l.split(" ")))), s)
    return s


def maybeint(s):
    try:
        return int(s)
    except:
        return ""


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


def easy():
    for or_or, cl_or, ob_or, ob_cl, ge_or, ge_ob in t:
        or_m = 0
        or_r = 1
        cl_m = 0
        cl_r = 0
        ob_m = 0
        ob_r = 0
        ge_m = 0
        ge_r = 0

        r = (ob_cl) / (ob_or + ge_or)

        for i in range(24):
            print(or_m, cl_m, ob_m, ge_m)
            or_m += or_r
            cl_m += cl_r
            ob_m += ob_r
            ge_m += ge_r

            if ge_or <= or_m and ge_ob <= ob_m:
                or_m -= ge_or
                ob_m -= ge_ob
                ge_r += 1
            if ob_cl <= cl_m and ob_or <= or_m:
                cl_m -= ob_cl
                or_m -= ob_or
                ob_r += 1
            if cl_or <= or_m and ob_r * r > cl_r:
                or_m -= cl_or
                cl_r += 1
            if or_or <= or_m:
                or_m -= or_or
                or_r += 1
        print(ge_m)


def hard():
    return


teststr = """    Blueprint 1:
      Each ore robot costs 4 ore.
      Each clay robot costs 2 ore.
      Each obsidian robot costs 3 ore and 14 clay.
      Each geode robot costs 2 ore and 7 obsidian.""".replace(
    "\n", ""
)
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
