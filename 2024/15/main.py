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
        top, bottom = (f.read() if teststr == "" else teststr).split("\n\n")

    return lmap(lambda r: lmap(str, r), top.splitlines()), [
        mv_c.index(c) for c in bottom.replace("\n", "")
    ]


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (0, 1),  # R
    (1, 0),  # D
    (0, -1),  # L
]

mv_c = ["^", ">", "v", "<"]

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


def can_move(mv_idx, pos, A):
    new_pos = (pos[0] + mv[mv_idx][0], pos[1] + mv[mv_idx][1])
    if new_pos[0] < 0 or new_pos[1] < 0:
        return False
    if new_pos[0] >= len(A) or new_pos[1] >= len(A[0]):
        return False
    if A[new_pos[0]][new_pos[1]] == "#":
        return False

    if A[new_pos[0]][new_pos[1]] == ".":
        return True

    if not can_move(mv_idx, new_pos, A):
        return False

    # move circle
    newer_pos = (new_pos[0] + mv[mv_idx][0], new_pos[1] + mv[mv_idx][1])
    A[new_pos[0]][new_pos[1]] = "."
    A[newer_pos[0]][newer_pos[1]] = "O"

    return True


def can_move_two(mv_idx, pos, A, do_move=True):
    new_pos = (pos[0] + mv[mv_idx][0], pos[1] + mv[mv_idx][1])
    if new_pos[0] < 0 or new_pos[1] < 0:
        return False
    if new_pos[0] >= len(A) or new_pos[1] >= len(A[0]):
        return False
    if A[new_pos[0]][new_pos[1]] == "#":
        return False

    if A[new_pos[0]][new_pos[1]] == ".":
        return True

    if mv_idx in [1, 3]:
        if not can_move_two(mv_idx, new_pos, A):
            return False

        # move circle
        if do_move:
            newer_pos = (new_pos[0] + mv[mv_idx][0], new_pos[1] + mv[mv_idx][1])
            A[newer_pos[0]][newer_pos[1]] = A[new_pos[0]][new_pos[1]]
            A[new_pos[0]][new_pos[1]] = "."

        return True

    other = (new_pos[0], new_pos[1] - 1)
    if A[new_pos[0]][new_pos[1]] == "[":
        other = (new_pos[0], new_pos[1] + 1)

    if not can_move_two(mv_idx, new_pos, A, do_move=False):
        return False
    if not can_move_two(mv_idx, other, A, do_move=False):
        return False

    if not do_move:
        return True

    can_move_two(mv_idx, new_pos, A, do_move=True)
    can_move_two(mv_idx, other, A, do_move=True)

    # move circle
    newer_pos = (new_pos[0] + mv[mv_idx][0], new_pos[1] + mv[mv_idx][1])
    A[newer_pos[0]][newer_pos[1]] = A[new_pos[0]][new_pos[1]]
    A[new_pos[0]][new_pos[1]] = "."
    newer_pos = (other[0] + mv[mv_idx][0], other[1] + mv[mv_idx][1])
    A[newer_pos[0]][newer_pos[1]] = A[other[0]][other[1]]
    A[other[0]][other[1]] = "."

    return True


def easy():
    A = deepcopy(t[0])
    for x, row in enumerate(A):
        for y, c in enumerate(row):
            if c == "@":
                start = (x, y)
                A[x][y] = "."
    for m in t[1]:
        v = mv[m]
        if can_move(m, start, A):
            start = (start[0] + v[0], start[1] + v[1])

    print("\n".join(["".join(r) for r in A]))

    s = 0
    for x, row in enumerate(A):
        for y, c in enumerate(row):
            if c != "O":
                continue
            s += x * 100 + y

    print(s)


def hard():
    A = [
        [
            c
            for c in "".join(
                [
                    {
                        "#": "##",
                        "O": "[]",
                        ".": "..",
                        "@": "@.",
                    }[c]
                    for c in r
                ]
            )
        ]
        for r in t[0]
    ]
    print(A[4])
    for x, row in enumerate(A):
        for y, c in enumerate(row):
            if c == "@":
                start = (x, y)
                A[x][y] = "."
    for m in t[1]:
        v = mv[m]
        if can_move_two(m, start, A):
            start = (start[0] + v[0], start[1] + v[1])

    print("\n".join(["".join(r) for r in A]))

    s = 0
    for x, row in enumerate(A):
        for y, c in enumerate(row):
            if c != "[":
                continue
            s += x * 100 + y

    print(s)


teststr = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
