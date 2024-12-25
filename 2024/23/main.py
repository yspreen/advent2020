import numpy as np
import re
import pathlib
import json
from functools import reduce, cmp_to_key
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(str, r.split("-")), s)


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
    connections = {}
    for lhs, rhs in t:
        connections[lhs] = connections.get(lhs, set()) | set([rhs])
        connections[rhs] = connections.get(rhs, set()) | set([lhs])

    threes = set()

    for a in connections:
        others = list(connections[a])
        for i, b in enumerate(others):
            for c_ in range(i + 1, len(others)):
                c = others[c_]
                if c in connections[b]:
                    threes.add(tuple(sorted([a, b, c])))

    s = 0
    for a, b, c in threes:
        if a.startswith("t") or b.startswith("t") or c.startswith("t"):
            s += 1
    print(s)


def all_connected(s, connections):
    l = list(s)
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] not in connections[l[i]]:
                return False
    return True


def hard():
    connections = {}
    for lhs, rhs in t:
        connections[lhs] = connections.get(lhs, set()) | set([rhs])
        connections[rhs] = connections.get(rhs, set()) | set([lhs])

    max_connected = 0, None

    for start_node in connections:
        n = len(connections[start_node])
        l = list(connections[start_node])
        for i in range(1, 2**n):
            s = set()
            for j in range(n):
                if i & (1 << j):
                    s.add(l[j])
            if len(s) <= max_connected[0]:
                continue
            if all_connected(s | set([start_node]), connections):
                max_connected = len(s), s | set([start_node])
    print(",".join(sorted(list(max_connected[1]))))


teststr = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
