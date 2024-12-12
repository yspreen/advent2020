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
    return lmap(lambda r: lmap(str, r), s)


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (0, 1),  # R
    (1, 0),  # D
    (0, -1),  # L
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


class JoinedSides:
    def __init__(self):
        self.d = [False, False, False, False]
        self.p = 4


def easy():
    joined = {}
    blob_for_pos = {}
    cells_for_blob = {}

    for x in range(len(t)):
        for y in range(len(t[0])):
            blob_idx = len(blob_for_pos)
            joined[(x, y)] = JoinedSides()
            blob_for_pos[(x, y)] = blob_idx
            cells_for_blob[blob_idx] = set([(x, y)])

    did_join = True
    while did_join:
        did_join = False
        for x in range(len(t)):
            for y in range(len(t[0])):
                blob_idx = blob_for_pos[(x, y)]
                for dir in range(4):
                    dx, dy = mv[dir]
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_y < 0 or new_x >= len(t) or new_y >= len(t[0]):
                        continue
                    if t[x][y] != t[new_x][new_y]:
                        continue
                    if joined[(x, y)].d[dir]:
                        continue
                    new_blob_idx = blob_for_pos[(new_x, new_y)]
                    did_join = True
                    if new_blob_idx != blob_idx:
                        cells_for_blob[blob_idx] |= cells_for_blob[new_blob_idx]
                        for pos in cells_for_blob[new_blob_idx]:
                            blob_for_pos[pos] = blob_idx
                        del cells_for_blob[new_blob_idx]

                    joined[(x, y)].d[dir] = True
                    joined[(x, y)].p -= 1

                    joined[(new_x, new_y)].d[(dir + 2) % 4] = True
                    joined[(new_x, new_y)].p -= 1

    # calculate sum of p for all cells per blob:
    p_sum = {}
    for blob_idx, cells in cells_for_blob.items():
        p_sum[blob_idx] = sum([joined[pos].p for pos in cells])

    # calculate sum cells per blob:
    a_sum = {}
    for blob_idx, cells in cells_for_blob.items():
        a_sum[blob_idx] = len(cells)

    # find sum of area * perimeter for all blobs:
    res = 0
    for blob_idx in cells_for_blob:
        res += a_sum[blob_idx] * p_sum[blob_idx]

    print(res)

    for x in range(len(t)):
        for y in range(len(t[0])):
            for m in range(4):
                if joined[(x, y)].d[m]:
                    continue
                rotated = (m + 1) % 4
                if not joined[(x, y)].d[rotated]:
                    continue
                dx, dy = mv[rotated]
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= len(t) or new_y >= len(t[0]):
                    continue
                new_joined = joined[(new_x, new_y)]
                if new_joined.d[m]:
                    continue
                joined[(x, y)].p -= 1

    # calculate sum of p for all cells per blob:
    p_sum = {}
    for blob_idx, cells in cells_for_blob.items():
        p_sum[blob_idx] = sum([joined[pos].p for pos in cells])

    # calculate sum cells per blob:
    a_sum = {}
    for blob_idx, cells in cells_for_blob.items():
        a_sum[blob_idx] = len(cells)

    # find sum of area * perimeter for all blobs:
    res = 0
    for blob_idx in cells_for_blob:
        res += a_sum[blob_idx] * p_sum[blob_idx]

    print(res)


def hard():
    return


teststr = """"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
