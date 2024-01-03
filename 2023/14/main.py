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
        s = (
            (f.read() if teststr == "" else teststr)
            .replace(".", "0")
            .replace("#", "1")
            .replace("O", "2")
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


def move(A, dir):
    for x, y in list(zip(*np.where(A == 2)))[:: -1 if dir in ["D", "R"] else 1]:
        old_x = x
        old_y = y
        if dir == "U":
            while x > 0 and A[x - 1, y] == 0:
                x -= 1
        if dir == "D":
            while x < A.shape[0] - 1 and A[x + 1, y] == 0:
                x += 1
        if dir == "L":
            while y > 0 and A[x, y - 1] == 0:
                y -= 1
        if dir == "R":
            while y < A.shape[1] - 1 and A[x, y + 1] == 0:
                y += 1
        A[old_x, old_y] = 0
        A[x, y] = 2
    return A


def spin(A):
    move(A, "U")
    move(A, "L")
    move(A, "D")
    move(A, "R")


def count(A):
    answer = 0
    for x, y in zip(*np.where(A[::-1] == 2)):
        answer += x + 1

    return answer


def easy():
    print(count(move(np.array(t), "U")))


def hash(A):
    a = A.flatten()
    a[a != 2] = 0
    a[a == 2] = 1
    v = 0
    for i in a:
        v *= 2
        v += int(i)
    return v


def hard():
    A = t
    a = b = i = 0
    scores = {i: count(A)}
    seen = {hash(A): i}
    while True:
        spin(A)
        i += 1
        score = count(A)
        scores[i] = score
        h = hash(A)
        if h in seen:
            b = seen[h]
            a = i - seen[h]
            break
        seen[h] = i

    print(scores[(1000000000 - b) % a + b])


teststr = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
