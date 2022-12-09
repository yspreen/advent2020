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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: (r.split(" ")[0], int(r.split(" ")[1])), s)


def easy():
    H = (0, 0)
    T = (0, 0)
    m = {
        "D": [-1, 0],
        "U": [1, 0],
        "L": [0, -1],
        "R": [0, 1],
    }
    seen = set()
    seen.add(T)
    for dir, num in t:
        v = m[dir]
        for _ in range(num):
            old_H = H
            H = (H[0] + v[0], H[1] + v[1])
            if dist(T, H) > 1:
                T = old_H
            seen.add(T)
    print(len(seen))


def dist(H, T):
    return max(abs(H[0] - T[0]), abs(H[1] - T[1]))


def draw(T, seen):
    min_x = min(map(lambda i: i[1], T + list(seen)))
    min_y = min(map(lambda i: i[0], T + list(seen)))
    max_x = max(map(lambda i: i[1], T + list(seen)))
    max_y = max(map(lambda i: i[0], T + list(seen)))

    max_x -= min_x - 1
    max_y -= min_y - 1

    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    num = 9
    for i, j in T:
        grid[i - min_y][j - min_x] = str(num)
        num -= 1
    for i, j in seen:
        grid[i - min_y][j - min_x] = "#"
        num -= 1

    for row in grid:
        print(*row, sep="")


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def move(T, t, h, dir, move_dist, old_H):
    if move_dist < 2:
        d = abs(T[t][0] - old_H[h][0]) + abs(T[t][1] - old_H[h][1])
        T[t] = old_H[h]
        return d
    v = (T[h][0] - T[t][0], T[h][1] - T[t][1])
    d = 0
    if dir in ["U", "D"]:
        d += 1
        T[t] = (T[t][0] + sign(v[0]), T[t][1])
        if dist(T[h], T[t]) > 1:
            d += 1
            T[t] = (T[t][0], T[t][1] + sign(v[1]))
    else:
        d += 1
        T[t] = (T[t][0], T[t][1] + sign(v[1]))
        if dist(T[h], T[t]) > 1:
            d += 1
            T[t] = (T[t][0] + sign(v[0]), T[t][1])

    return d


def hard():
    T = [(0 * i, 0 * i) for i in range(10)]
    old_H = deepcopy(T)
    m = {
        "D": [1, 0],
        "U": [-1, 0],
        "L": [0, -1],
        "R": [0, 1],
    }
    seen = set()
    seen.add(T[9])
    for dir, num in t:
        v = m[dir]
        for _ in range(num):
            old_H = deepcopy(T)
            T[0] = (T[0][0] + v[0], T[0][1] + v[1])
            if dist(T[0], T[1]) > 1:
                move_dist = 0
                for i in range(1, 10):
                    if dist(T[i], T[i - 1]) > 1:
                        move_dist = move(T, i, i - 1, dir, move_dist, old_H)
                    else:
                        break
            seen.add(T[9])
        # draw(T, seen)
    print(len(seen))


teststr = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
