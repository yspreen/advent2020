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
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return lmap(int, s)


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
    l = [0] * sum(t)
    i = 0
    for idx, num in enumerate(t):
        for j in range(num):
            l[i + j] = -1 if idx % 2 else idx // 2
        i += num

    empty = l.count(-1)

    last_idx = len(l) - 1
    first_idx = l.index(-1)

    while True:
        while l[last_idx] == -1:
            last_idx -= 1
        while l[first_idx] != -1:
            first_idx += 1
        if first_idx >= last_idx:
            break
        l[first_idx] = l[last_idx]
        l[last_idx] = -1

    c = 0
    for i in range(first_idx):
        v = l[i]
        c += v * i
    print(c)


def hard():
    empty = t[1::2] + [0]
    not_empty = t[::2]

    idx = 0
    pos = 0
    not_empty_ = not_empty
    empty_ = empty
    not_empty = [0] * len(not_empty)
    empty = [0] * len(empty)
    for ne, e in zip(not_empty_, empty_):
        not_empty[idx] = (pos, ne, idx)
        empty[idx] = (pos + ne, e)

        pos += ne + e
        idx += 1

    for ne_idx, v in list(enumerate(not_empty))[::-1]:
        pos, count, ne_block = v
        for e_idx, v in enumerate(empty):
            e_pos, e_count = v
            if e_count < count:
                continue
            if e_pos > pos:
                break
            empty[e_idx] = (e_pos + count, e_count - count)
            not_empty[ne_idx] = (e_pos, count, ne_block)
            break

    l = [-1] * sum(t)
    for i, num, block in not_empty:
        for j in range(num):
            l[i + j] = block

    c = 0
    for i in range(sum(t)):
        v = l[i]
        if v == -1:
            continue
        c += v * i
    print(c)


teststr = """2333133121414131402"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
