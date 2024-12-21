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
        s = (
            (f.read() if teststr == "" else teststr)
            .replace("#", "1")
            .replace(".", "0")
            .replace("S", "2")
            .replace("E", "3")
            .splitlines()
        )
    return np.array(lmap(lambda r: lmap(int, r), s))


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

distances = {}


def BFS(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, 0)]
    visited = set([start])

    while options:
        new_o = []
        for pos, cost in options:
            distances[pos] = cost
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
                    distances[new_p] = cost_
                    return cost_
        options = new_o
    return None


def easy():
    S = tuple(list(zip(*np.where(t == 2)))[0])
    E = tuple(list(zip(*np.where(t == 3)))[0])

    BFS(S, lambda _, p: t[p] != 1, lambda p: p == E)

    cheats = 0

    for x, y in zip(*np.where(t == 1)):
        if x == 0 or y == 0 or x == t.shape[0] - 1 or y == t.shape[1] - 1:
            continue
        if (x - 1, y) in distances and (x + 1, y) in distances:
            cheat = abs(distances[(x - 1, y)] - distances[(x + 1, y)])
            if cheat - 2 >= 100:
                cheats += 1
        if (x, y - 1) in distances and (x, y + 1) in distances:
            cheat = abs(distances[(x, y - 1)] - distances[(x, y + 1)])
            if cheat - 2 >= 100:
                cheats += 1

    print(cheats)


def hard():
    cheats = 0
    for x, y in distances.keys():
        for x_, y_ in distances.keys():
            dist = abs(x - x_) + abs(y - y_)
            if dist <= 20:
                cheat = distances[(x, y)] - distances[(x_, y_)]
                if cheat - dist >= 100:
                    cheats += 1
    print(cheats)


teststr = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
