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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(str, r), s)


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


def rotate_90_r(dir):
    return (dir + 1) % 4


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


def does_loop(added_block):
    pos = "".join(["".join(r) for r in t]).find("^")
    pos = (
        pos // len(t[0]),
        pos % len(t[0]),
    )
    dir = 0
    for attempt in range(4):
        next_pos = (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
        if t[next_pos[0]][next_pos[1]] == "#" or next_pos == added_block:
            dir = rotate_90_r(dir)
        else:
            break
    visited = set([(pos, dir)])

    while True:
        pos = (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
        for attempt in range(4):
            next_pos = (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
            if not (0 <= next_pos[0] < len(t) and 0 <= next_pos[1] < len(t[0])):
                return False
            if t[next_pos[0]][next_pos[1]] == "#" or next_pos == added_block:
                dir = rotate_90_r(dir)
            else:
                break

        if (pos, dir) in visited:
            return True
        visited.add((pos, dir))


def easy():
    pos = "".join(["".join(r) for r in t]).find("^")
    pos = (
        pos // len(t[0]),
        pos % len(t[0]),
    )
    visited = set([pos])
    dir = 0

    while True:
        pos = (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
        visited.add(pos)
        next_pos = (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
        if not (0 <= next_pos[0] < len(t) and 0 <= next_pos[1] < len(t[0])):
            break
        if t[next_pos[0]][next_pos[1]] == "#":
            dir = rotate_90_r(dir)
    print(len(visited))


def hard():
    pos = "".join(["".join(r) for r in t]).find("^")
    starting = pos = (
        pos // len(t[0]),
        pos % len(t[0]),
    )
    visited = set([pos])
    dir = 0

    while True:
        pos = (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
        visited.add(pos)
        next_pos = (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
        if not (0 <= next_pos[0] < len(t) and 0 <= next_pos[1] < len(t[0])):
            break
        if t[next_pos[0]][next_pos[1]] == "#":
            dir = rotate_90_r(dir)

    c = 0
    for pos in visited:
        if pos != starting and does_loop(pos):
            c += 1
    print(c)


teststr = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
