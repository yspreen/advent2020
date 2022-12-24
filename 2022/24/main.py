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
        s = (
            (f.read() if teststr == "" else teststr)
            .replace(".", "0")
            .replace("#", "5")
            .replace("^", "1")
            .replace("v", "2")
            .replace("<", "3")
            .replace(">", "4")
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
    (0, 0),  # R
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
]


def BFS(start, start_c, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, start_c)]
    visited = set([(start, start_c)])

    while options:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                cost_ = cost + cost_fn(pos, new_p)
                if goal(new_p):
                    return cost_
                if new_p[0] < 1:  # lower bound check
                    continue
                if new_p[1] < 1:  # lower bound check
                    continue
                if new_p[0] > N:  # lower bound check
                    continue
                if new_p[1] > M:  # lower bound check
                    continue
                try:
                    assert can_walk(*new_p, cost_)
                except Exception:
                    continue  # upper bound check
                # print(*new_p, cost_)
                if (new_p, cost_) in visited:
                    continue
                visited.add((new_p, cost_))
                new_o.append((new_p, cost_))
        options = new_o
    return None


no_bliz_dict = {}


def no_bliz_fast(x, y, t):
    return no_bliz_dict[(x, y, t % (N * M))]


def no_bliz(x, y, t):
    for bp, mb in bliz:
        bx, by = bp
        if bx == x and mb[1] != 0:
            if y == ((by - 1 + mb[1] * t) % M) + 1:
                return False
        if by == y and mb[0] != 0:
            if x == ((bx - 1 + mb[0] * t) % N) + 1:
                return False
    return True


def easy():
    global bliz, N, M
    N, M = t.shape
    N -= 2
    M -= 2
    bliz = []
    for x, y in zip(*np.where(t == 1)):
        bliz.append(((x, y), mv[0]))
    for x, y in zip(*np.where(t == 2)):
        bliz.append(((x, y), mv[1]))
    for x, y in zip(*np.where(t == 3)):
        bliz.append(((x, y), mv[2]))
    for x, y in zip(*np.where(t == 4)):
        bliz.append(((x, y), mv[3]))

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            for k in range(N * M):
                no_bliz_dict[(i, j, k)] = True

    for p, m in bliz:
        x, y = p
        mx, my = m
        x -= 1
        y -= 1

        for k in range(N * M):
            no_bliz_dict[(x + 1, y + 1, k)] = False
            x += mx
            x %= N
            y += my
            y %= M

    C = []

    res = None
    c = 0
    while res is None:
        res = BFS((0, 1), c, no_bliz_fast, lambda p: p == (N + 1, M))
        c += 1

    print(res)

    C += [res]

    res = None
    c = C[-1]
    while res is None:
        res = BFS((N + 1, M), c, no_bliz_fast, lambda p: p == (0, 1))
        c += 1

    C += [res]
    res = None
    c = C[-1]
    while res is None:
        res = BFS((0, 1), c, no_bliz_fast, lambda p: p == (N + 1, M))
        c += 1

    C += [res]
    print(C[2])


def hard():
    return


teststr = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
