import enum
import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt, sin, cos, pi
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).split("\n\n")
    return lmap(
        lambda i: np.array(lmap(lambda j: lmap(int, j.split(",")), i.splitlines()[1:])),
        s,
    )


def rotate_vector(v, axis, rotations=1):
    ax, ay, az = axis
    vx, vy, vz = v

    if rotations == 0:
        return np.array(v)

    if ax:
        v = [vx, -vz, vy]
    if ay:
        v = [vz, vy, -vx]
    if az:
        v = [-vy, vx, vz]

    return rotate_vector(v, axis, rotations - 1)


def rotations(v):
    res = []
    v = np.array(v)

    x = [1, 0, 0]
    y = [0, 1, 0]
    z = [0, 0, 1]

    for _ in range(4):
        for _ in range(4):
            res.append(v)
            v = rotate_vector(v, x)
        v = rotate_vector(v, z)
    for i in range(2):
        v = rotate_vector(v, y, i + 1)
        for _ in range(4):
            v = rotate_vector(v, x)
            res.append(v)

    return res


def easy():
    diffs = [{} for _ in t]
    for vi, vs in enumerate(t):
        ds = []
        for i, j in [(i, j) for i, j in product(range(len(vs)), repeat=2) if i != j]:
            ds.append((i, j, vs[i] - vs[j]))
        double = set()
        for i, j, d in ds:
            for k, o in enumerate(rotations(d)):
                if vi == 0 and k > 0:
                    break
                o = tuple(o)
                if o in diffs[vi]:
                    double.add(o)
                else:
                    diffs[vi][o] = (i, j, k)
        for o in double:
            del diffs[vi][o]

    added = [0]
    points = set([tuple(v) for v in t[0]])
    while len(added) < len(t):
        print(len(added), len(t))
        m = (0, 0)
        for i in [i for i in range(len(t)) if i not in added]:
            match = len(set(diffs[0].keys()) & set(diffs[i].keys()))
            m = (match, i) if match > m[0] else m
        i = m[1]
        assert i > 0
        added += [i]

        e = set(diffs[0].keys()) & set(diffs[i].keys())
        e = e.pop()
        vi, _, _ = diffs[0][e]
        vj, _, r = diffs[i][e]
        d = t[0][vi] - rotations(t[i][vj])[r]

        for v in t[i]:
            v = rotations(v)[r] + d
            if tuple(v) in points:
                continue
            points.add(tuple(v))
            new_j = len(t[0])
            for new_i, old_v in enumerate(t[0]):
                d = tuple(old_v - v)
                if d in diffs[0]:
                    continue
                diffs[0][d] = (new_i, new_j, 0)
                d = tuple(v - old_v)
                diffs[0][d] = (new_j, new_i, 0)

            t[0] = np.vstack([t[0], np.array([v])])
    print(len(points))


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
