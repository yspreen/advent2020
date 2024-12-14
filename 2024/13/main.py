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
        blocks = (f.read() if teststr == "" else teststr).split("\n\n")
    blocks = [
        b.replace(",", "+").replace("\n", "+").replace("=", "+").split("+")
        for b in blocks
    ]
    return [lmap(int, [b[1], b[3], b[5], b[7], b[9], b[11]]) for b in blocks]


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


def easy():
    c = 0
    for x1, y1, x2, y2, xs, ys in t:
        min = float("inf"), None
        for n1 in range(101):
            x = x1 * n1
            n2 = (xs - x) / x2
            if not n2.is_integer():
                continue
            y = y1 * n1 + y2 * n2
            if y != ys:
                continue
            if min[0] > n1 * 3 + n2:
                min = n1 * 3 + n2, (n1, n2)
        if min[1] is None:
            continue
        c += min[0]
    print(int(c))


from sympy import Matrix


def hard():
    s = 0
    for a, b, c, d, s1, s2 in t:
        # Adjust s1 and s2 as per your requirement
        s1 = s1 + 10_000_000_000_000
        s2 = s2 + 10_000_000_000_000

        # Define the matrices
        A = Matrix([[a, b], [c, d]]).T
        S = Matrix([s1, s2])

        # Check if determinant of A is zero
        if A.det() == 0:
            A_S = Matrix([[a, b, s1], [c, d, s2]])  # Augmented matrix

            # Check ranks for consistency
            if A.rank() < A_S.rank():
                # print("No solution")
                continue
            else:
                # print("Infinite solutions")
                continue

        # Solve the system of equations
        X = A.inv() * S  # Matrix multiplication to find solution

        # Check if solutions are integers
        if not X[0].is_integer or not X[1].is_integer:
            # print("No solution", X[0], X[1])
            continue

        s += X[0] * 3 + X[1]
    print(s)


teststr = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
