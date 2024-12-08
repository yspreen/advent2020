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
        s = f.read()
        a, b = (
            (s if teststr == "" else teststr).split("\n\n")[0].splitlines(),
            (s if teststr == "" else teststr).split("\n\n")[1].splitlines(),
        )
    return (
        lmap(lambda r: lmap(int, r.split("|")), a),
        lmap(lambda r: lmap(int, r.split(",")), b),
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
    c = 0
    for row in t[1]:
        idx = {}
        for i in range(len(row)):
            idx[row[i]] = i

        valid = True
        for lhs, rhs in t[0]:
            if lhs not in idx:
                continue
            if rhs not in idx:
                continue
            if idx[lhs] > idx[rhs]:
                valid = False
                break
        if valid:
            c += row[len(row) // 2]
    print(c)


def hard():
    rules = set([(a, b) for (a, b) in t[0]])

    c = 0
    for row in t[1]:
        idx = {}
        for i in range(len(row)):
            idx[row[i]] = i

        valid = True
        for lhs, rhs in t[0]:
            if lhs not in idx:
                continue
            if rhs not in idx:
                continue
            if idx[lhs] > idx[rhs]:
                valid = False
                break
        if valid:
            continue
        row.sort(
            key=cmp_to_key(
                lambda lhs, rhs: (
                    -1 if (lhs, rhs) in rules else (1 if (rhs, lhs) in rules else 0)
                )
            )
        )
        c += row[len(row) // 2]

    print(c)


teststr = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
