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


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr

    s = re.sub(r"[ a-zS,:]+", "", s)
    s = s.splitlines()
    return lmap(lambda r: lmap(int, r.split("=")[1:]), s)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]

t_ = []


def easy():
    global t_
    t_ = []
    min_x = inf
    max_x = 0
    y = 10
    y = 2000000
    r = 0
    seen_bx = set([])
    for sx, sy, bx, by in t:
        d = dist((sx, sy), (bx, by))
        t_.append((sx, sy, d))
        min_x = min(min_x, sx)
        min_x = min(min_x, bx)
        max_x = max(max_x, sx)
        max_x = max(max_x, bx)
        if by == y and bx not in seen_bx:
            r -= 1
            seen_bx.add(bx)

    # for x in range(int(min_x) - 1000000, max_x + 1000000):
    #     feasible = True
    #     for sx, sy, d in t_:
    #         d_ = abs(sx - x) + abs(sy - y)
    #         if d_ <= d:
    #             feasible = False
    #             break
    #     if not feasible:
    #         r += 1
    # print(r)


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def resolution(t_, divisor, potentials):
    t__ = []
    for x, y, d in t_:
        x //= divisor
        y //= divisor
        d //= divisor
        t__.append((x, y, d))

    potentials_ = []
    for x__, y__ in potentials:
        possible = True
        x__ *= 10
        y__ *= 10
        for x_ in range(10):
            for y_ in range(10):
                x = x__ + x_
                y = y__ + y_
                if x < 0:
                    continue
                if y < 0:
                    continue
                for xs, ys, d in t__:
                    if dist((x, y), (xs, ys)) <= (d - 11 if divisor > 1 else d):
                        possible = False
                        break
                if possible:
                    potentials_.append((x, y))
    return list(set(potentials_))


def hard():
    divisor = 10000
    limit = 4000000 // divisor // 10

    p = []
    for x in range(limit + 1):
        for y in range(limit + 1):
            p.append((x, y))

    while divisor > 1:
        p = resolution(t_, divisor, p)
        print(p)
        divisor //= 10

    print(resolution(t_, divisor, p))


teststr = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
