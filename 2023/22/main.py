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
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace("~", ",").splitlines()
    s = np.array(lmap(lambda r: lmap(int, r.split(",")), s))
    x = max(np.max(s[:, 0]), np.max(s[:, 3])) + 1
    y = max(np.max(s[:, 1]), np.max(s[:, 4])) + 1
    z = max(np.max(s[:, 2]), np.max(s[:, 5])) + 1
    t = np.zeros((x, y, z), np.int32)
    for i, piece in enumerate(s, 1):
        x, y, z, x_, y_, z_ = piece
        t[
            min(x, x_) : max(x, x_) + 1,
            min(y, y_) : max(y, y_) + 1,
            min(z, z_) : max(z, z_) + 1,
        ] = i
    return t


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


def settle_at(t, num, down, positions):
    for x, y, z in positions:
        z -= down
        t[x, y, z] = num


def move_down(t, num):
    positions = list(zip(*np.where(t == num)))
    t[t == num] = 0
    for down in range(1, t.shape[2] + 1):
        for x, y, z in positions:
            z -= down
            if z <= 0 or t[x, y, z] not in [0, num]:
                settle_at(t, num, down - 1, positions)
                return


def move_all_down(t):
    done = set()
    for z in range(t.shape[2]):
        for num in set(t[:, :, z].flatten()) - done:
            if num == 0:
                continue
            done.add(num)
            move_down(t, num)


class Dep:
    def __init__(self, idx):
        self.idx = idx
        self.lower = set()
        self.upper = set()
        self.unstable = False

    def __repr__(self):
        return str({"i": self.idx, "l": self.lower, "u": self.upper})

    def simulate_falls(self, dep, fallen=None):
        if fallen and (self.lower - fallen):
            return False, fallen
        fallen = set() if fallen is None else fallen
        fallen.add(self.idx)

        while True:
            count = len(fallen)
            for other in self.upper:
                dep[other].simulate_falls(dep, fallen)
            if count == len(fallen):
                break

        return True, fallen


def get_dep(t):
    dep = {(i + 1): Dep(i + 1) for i in range(np.max(t))}
    for i in dep:
        for x, y, z in list(zip(*np.where(t == i))):
            if z == 1:
                break
            lower = t[x, y, z - 1]
            if lower in [0, i]:
                continue
            dep[i].lower.add(lower)
            dep[lower].upper.add(i)
    for d in dep.values():
        d.unstable = len(d.lower) == 1
    return dep


def main():
    move_all_down(t)
    dep = get_dep(t)
    stable = 0
    falls = 0
    for d in dep.values():
        falls += len(d.simulate_falls(dep)[1]) - 1
        stable += 1
        for upper in d.upper:
            if dep[upper].unstable:
                stable -= 1
                break
    print(stable)
    print(falls)


teststr = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    main()
