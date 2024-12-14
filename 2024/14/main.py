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
            .replace(" v=", ",")
            .replace("p=", "")
            .splitlines()
        )
    return lmap(lambda r: lmap(int, r.split(",")), s)


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
    return None


X = 101
Y = 103


def easy():
    p = [(x, y) for x, y, _, _ in t]
    v = [(x, y) for _, _, x, y in t]
    for _ in range(100):
        for i in range(len(p)):
            x, y = p[i]
            vx, vy = v[i]
            x += vx
            y += vy
            p[i] = (x % X, y % Y)
    q = [0, 0, 0, 0]
    for x, y in p:
        if x > X // 2:
            if y > Y // 2:
                q[3] += 1
            elif y < Y // 2:
                q[2] += 1
        elif x < X // 2:
            if y > Y // 2:
                q[1] += 1
            elif y < Y // 2:
                q[0] += 1

    # A = [[0 for _ in range(X)] for _ in range(Y)]
    # for x, y in p:
    #     A[y][x] += 1
    # print("\n".join(["".join([(" " if i == 0 else str(i)) for i in r]) for r in A]))

    # print(q)
    print(q[0] * q[1] * q[2] * q[3])


class JoinedSides:
    def __init__(self):
        self.d = [False, False, False, False]
        self.p = 4


def area(A):
    max_area = 0
    joined = {}
    blob_for_pos = {}
    cells_for_blob = {}

    for x in range(len(A)):
        for y in range(len(A[0])):
            blob_idx = len(blob_for_pos)
            joined[(x, y)] = JoinedSides()
            blob_for_pos[(x, y)] = blob_idx
            cells_for_blob[blob_idx] = set([(x, y)])

    for x in range(len(A)):
        for y in range(len(A[0])):
            if A[x][y] == 0:
                continue
            blob_idx = blob_for_pos[(x, y)]
            for dir in range(4):
                dx, dy = mv[dir]
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= len(A) or new_y >= len(A[0]):
                    continue
                if A[x][y] != A[new_x][new_y]:
                    continue
                if joined[(x, y)].d[dir]:
                    continue
                new_blob_idx = blob_for_pos[(new_x, new_y)]

                if new_blob_idx != blob_idx:
                    cells_for_blob[blob_idx] |= cells_for_blob[new_blob_idx]
                    for pos in cells_for_blob[new_blob_idx]:
                        blob_for_pos[pos] = blob_idx
                    del cells_for_blob[new_blob_idx]
                    if A[x][y] != 0 and len(cells_for_blob[blob_idx]) > max_area:
                        max_area = len(cells_for_blob[blob_idx])

                joined[(x, y)].d[dir] = True
                joined[(x, y)].p -= 1

                joined[(new_x, new_y)].d[(dir + 2) % 4] = True
                joined[(new_x, new_y)].p -= 1

    return max_area


def hard():
    max_area = 0
    p = [(x, y) for x, y, _, _ in t]
    v = [(x, y) for _, _, x, y in t]
    for move in range(6644):
        for i in range(len(p)):
            x, y = p[i]
            vx, vy = v[i]
            x += vx
            y += vy
            p[i] = (x % X, y % Y)
        A = [[0 for _ in range(X)] for _ in range(Y)]
        for x, y in p:
            A[y][x] += 1

        if area(A) > 200:
            print(move + 1)
            return


teststr = ""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
