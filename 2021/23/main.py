import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy, copy
from hashlib import md5, sha256


def read():
    with open(DIR / "input") as f:
        s = (
            (f.read() if teststr == "" else teststr)
            .replace(" ", "")
            .replace("#", "")
            .splitlines()[1:4]
        )
    return lmap(lambda r: lmap(lambda i: ".ABCD".index(i), r), s)


def options(positions, pos):
    char = positions.get(pos, 0)
    if char == 0:
        return []
    x, y = pos

    if y == 2 and positions.get((x, 1), 0) != 0:
        return []

    if y == 0:
        l1 = positions.get((char - 1, 1), 0)
        if l1 != 0:
            return []
        l2 = positions.get((char - 1, 2), 0)
        if l2 != 0 and l2 != char:
            return []
        diff = 1 if x <= char else -1
        limit = char + 1 if diff > 0 else char
        x_ = x + diff
        while x_ != limit:
            if positions.get((x_, 0), 0) != 0:
                return []
            x_ += diff
        c = cost(x, char)
        return [(char - 1, 2, c + 2)] if l2 == 0 else [(char - 1, 1, c + 1)]

    if x == char - 1 and (y == 2 or (y == 1 and positions.get((x, 2), 0) == char)):
        return []

    opt = []
    x_ = x + 2
    while x_ <= 6:
        if positions.get((x_, 0), 0) != 0:
            break
        opt.append((x_, 0, cost(x_, x + 1) + y))
        x_ += 1
    x_ = x + 1
    while x_ >= 0:
        if positions.get((x_, 0), 0) != 0:
            break
        opt.append((x_, 0, cost(x_, x + 1) + y))
        x_ -= 1
    return opt


def init_positions():
    positions = {}
    for d in [8, 6, 4, 2]:
        del t[0][d]
    for k in range(3):
        for i, c in enumerate(t[k]):
            positions[(i, k)] = c
    return positions


def cost(x, char):
    for num in [1, 3, 5, 7]:
        if x > num:
            x += 1
        else:
            break
    char = 2 * char
    return abs(x - char)


costs_per_char = [0, 1, 10, 100, 1000]


def is_done(positions):
    for y in [1, 2]:
        for x in range(4):
            if positions.get((x, y), 0) != x + 1:
                return False
    return True


def pprint(positions):
    print("#" * 13 + "\n#", end="")
    for x in range(7):
        print(".ABCD"[positions.get((x, 0), 0)], end=("." if x in [1, 2, 3, 4] else ""))
    print("#")
    for y in range(2):
        print(["###", "  #"][y], end="")
        for x in range(4):
            print(".ABCD"[positions.get((x, y + 1), 0)], end="#")
        print(["##", ""][y])
    print(" ", "#" * 9)


def next_moves(positions, previous_cost):
    res = []
    for pos, char in positions.items():
        for x, y, cost in options(positions, pos):
            cost *= costs_per_char[char]
            cost += previous_cost
            new_pos = copy(positions)
            del new_pos[pos]
            new_pos[(x, y)] = char

            res.append((new_pos, cost))

    return res


def easy():
    M, next_up = inf, [(init_positions(), 0)]

    while next_up:
        current, next_up = next_up, []
        current.sort(key=lambda i: i[1])
        for pos, cost in current:
            if is_done(pos):
                M = min(cost, M)
                print(M)
            if cost < M:
                next_up += next_moves(pos, cost)
    print(M)


def hard():
    return


teststr = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
