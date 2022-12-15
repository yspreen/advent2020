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
    t_ = []
    min_x = inf
    max_x = 0
    y = 10
    y = 2000000
    r = 0
    seen_bx = set([])
    for sx, sy, bx, by in t:
        d = abs(sx - bx) + abs(sy - by)
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

    for i1 in range(len(t_)):
        for i2 in range(len(t_)):
            for i3 in range(len(t_)):
                for i4 in range(len(t_)):
                    if i1 == i2:
                        continue
                    if i1 == i3:
                        continue
                    if i1 == i4:
                        continue
                    if i2 == i3:
                        continue
                    if i2 == i4:
                        continue
                    if i3 == i4:
                        continue
                    runloop(t_, i1, i2, i3, i4)


def runloop(t_, i1, i2, i3, i4):
    t1 = t_[i1]
    t2 = t_[i2]
    t3 = t_[i3]
    t4 = t_[i4]

    t1, t2, t3, t4 = sorted([t1, t2, t3, t4], key=lambda t: t[1])
    t1, t2 = sorted([t1, t2], key=lambda t: t[0])

    x1, x1, d1 = t1
    x2, x2, d2 = t2
    x3, x3, d3 = t3
    x4, x4, d4 = t4

    abs(mx - x1) + abs(my - y1) == d1 + 1
    abs(mx - x2) + abs(my - y2) == d2 + 1
    abs(mx - x3) + abs(my - y3) == d3 + 1
    abs(mx - x4) + abs(my - y4) == d4 + 1


#   1  2
#  3   4


"""
   
         2



       1
        x

         4
3
"""


def hard():
    return


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
