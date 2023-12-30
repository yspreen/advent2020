import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt, lcm
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return s[0], lmap(
        lambda r: re.sub(r" +", " ", re.sub(r"[\(\)\,=]+", "", r)).split(" "),
        s[2:],
    )


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
    (-1, 1),  # UR
    (1, 1),  # DR
    (-1, -1),  # UL
    (1, -1),  # DL
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


def easy():
    current = "AAA"
    idx = 0
    while current != "ZZZ":
        move = instr[idx % N]
        current = nodes[current][0] if move == "L" else nodes[current][1]
        idx += 1
    print(idx)


def all_z(current):
    for node in current:
        if node[-1] != "Z":
            return False
    return True


def do_move(c, idx):
    move = 0 if instr[idx % N] == "L" else 1
    return nodes[c][move], idx + 1


def hard():
    current = list([k for k in nodes.keys() if k.endswith("A")])
    factors = []

    for c in current:
        idx = 0
        while not c.endswith("Z"):
            c, idx = do_move(c, idx)
        factors.append(idx)
    print(lcm(*factors))


teststr = """"""
if environ["AOC_SOLVE"] == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
instr, t = read()
N = len(instr)
nodes = {}
for key, l, r in t:
    nodes[key] = (l, r)
if __name__ == "__main__":
    easy()
    hard()
