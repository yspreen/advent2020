import numpy as np
import re
import pathlib
import json
from functools import reduce, cache
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
    return lmap(lambda r: lmap(str, r), s)


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


@cache
def neighbors(x, y, step):
    if step == 1:
        if t[x][y] == "v":
            return [(x + 1, y)]
        if t[x][y] == "^":
            return [(x - 1, y)]
        if t[x][y] == ">":
            return [(x, y + 1)]
        if t[x][y] == "<":
            return [(x, y - 1)]
    n = []
    for d_x, d_y in mv:
        x_ = x + d_x
        y_ = y + d_y
        if x_ < 0 or y_ < 0:
            continue
        if x_ >= N or y_ >= M:
            continue
        if t[x_][y_] == "#":
            continue
        n.append((x_, y_))
    return n


def DFS(start, goal, step):
    longest = 0
    stack = llist([(start, 1)])
    visited = set()

    while stack:
        current, path_len = stack.pop()

        if current not in visited:
            stack.append((current, path_len))
            visited.add(current)

            if current == goal and path_len > longest:
                longest = path_len

            for neighbor in neighbors(*current, step):
                if neighbor not in visited:
                    stack.append((neighbor, path_len + 1))
        else:
            visited.remove(current)

    return longest


def main():
    for part in [1, 2]:
        print(DFS((0, 1), (N - 1, M - 2), part) - 1)


teststr = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
N = len(t)
M = len(t[0])
if __name__ == "__main__":
    main()
