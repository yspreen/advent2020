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
    return lmap(lambda r: lmap(int, r), s)


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
    return visited


def count_nine(i, j):
    v = BFS(
        (i, j),
        lambda now, next: (t[now[0]][now[1]] - t[next[0]][next[1]]) == -1,
        lambda p: False,
    )
    c = 0
    for i, j in v:
        if t[i][j] == 9:
            c += 1
    return c


def BFS_(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [((start,), 0)]

    paths = set()

    while options:
        new_o = []
        for chain, cost in options:
            pos = chain[-1]
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

                cost_ = cost + cost_fn(pos, new_p)
                new_chain = tuple([*chain, new_p])
                if new_chain in paths:
                    continue
                new_o.append((new_chain, cost_))
                paths.add(new_chain)
        options = new_o
    return len([p for p in paths if len(p) == 10])


def count_two(i, j):
    return BFS_(
        (i, j),
        lambda now, next: (t[now[0]][now[1]] - t[next[0]][next[1]]) == -1,
        lambda p: t[p[0]][p[1]] == 9,
    )


def easy():
    c = 0
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != 0:
                continue
            c += count_nine(i, j)
    print(c)


def hard():
    c = 0
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != 0:
                continue
            c += count_two(i, j)
    print(c)


teststr = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
