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


def easy():
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


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def runloop(t_, i1, i2, i3, i4):
    t1 = t_[i1]
    t2 = t_[i2]
    t3 = t_[i3]
    t4 = t_[i4]

    A, B, C, D = sorted([t1, t2, t3, t4], key=lambda t: t[1])
    A, B = sorted([A, B], key=lambda t: t[0])
    C, D = sorted([C, D], key=lambda t: t[0])

    x = (A[0] + A[1] + A[2] - B[0] + B[1] - B[2]) / 2
    y = -x + A[0] + A[1] + (A[2] + 1)

    if abs(dist((C[0], C[1]), (x, y)) - (C[2] + 1)) >= 5:
        return
    if abs(dist((D[0], D[1]), (x, y)) - (D[2] + 1)) >= 5:
        return

    print(int(x) * 4000000 + int(y))


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
