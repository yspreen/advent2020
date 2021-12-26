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
    x, y = pos
    char = positions[y][x]
    if char == 0:
        return []
    f = costs_per_char[char]

    if y > 1 and positions[y - 1][x] != 0:
        return []

    if y == 0:
        for i in range(1, N):
            v = positions[i][char - 1]
            if v != char and v != 0:
                return []
            if v == 0:
                depth = i
        diff = 1 if x <= char else -1
        limit = char + 1 if diff > 0 else char
        x_ = x + diff
        while x_ != limit:
            if positions[0][x_] != 0:
                return []
            x_ += diff
        c = cost(x, char)
        return [(char - 1, depth, (c + depth) * f)]

    # if x == char - 1 and y == N - 1:
    #     return []

    if x == char - 1 and y > 0:
        some_wrong = False
        for y_ in range(y + 1, N):
            some_wrong = positions[y_][x] != char
            if some_wrong:
                break
        if not some_wrong:
            return []

    opt = []
    x_ = x + 2
    while x_ <= 6:
        if positions[0][x_] != 0:
            break
        opt.append((x_, 0, (cost(x_, x + 1) + y) * f))
        x_ += 1
    x_ = x + 1
    while x_ >= 0:
        if positions[0][x_] != 0:
            break
        opt.append((x_, 0, (cost(x_, x + 1) + y) * f))
        x_ -= 1
    return sorted(opt, key=lambda i: i[2])


def init_positions():
    if len(t[0]) > 8:
        for d in [8, 6, 4, 2]:
            del t[0][d]
    return tuple(tuple(i for i in row) for row in t)


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
    return positions == (
        (0, 0, 0, 0, 0, 0, 0),
        (1, 2, 3, 4),
        (1, 2, 3, 4),
    ) or positions == (
        (0, 0, 0, 0, 0, 0, 0),
        (1, 2, 3, 4),
        (1, 2, 3, 4),
        (1, 2, 3, 4),
        (1, 2, 3, 4),
    )


def pprint(positions):
    print("#" * 13 + "\n#", end="")
    for x in range(7):
        print(".ABCD"[positions[0][x]], end=("." if x in [1, 2, 3, 4] else ""))
    print("#")
    for y in range(N - 1):
        print(["###", "  #", "  #", "  #"][y], end="")
        for x in range(4):
            print(".ABCD"[positions[y + 1][x]], end="#")
        print(["##", "", "", ""][y])
    print(" ", "#" * 9)


def move(positions, old_x, old_y, new_x, new_y):
    return tuple(
        tuple(
            (i if x != new_x or y != new_y else positions[old_y][old_x])
            if x != old_x or y != old_y
            else 0
            for (x, i) in enumerate(row)
        )
        for (y, row) in enumerate(positions)
    )


def next_moves(positions, previous_cost):
    # pprint(positions)
    if previous_cost >= costs.get(positions, 9e9):
        # print("x")
        return []
    costs[positions] = previous_cost
    res = []
    # pprint(positions)
    # print(previous_cost)
    for pos in indices(positions):
        for x_, y_, cost in options(positions, pos):
            cost += previous_cost
            new_pos = move(positions, *pos, x_, y_)

            if is_done(new_pos):
                res.append(cost)
                # pprint(positions)
                # print(cost)
            else:
                res.extend(next_moves(new_pos, cost))

    return res


def easy():
    pprint(init_positions())
    print(min(next_moves(init_positions(), 0)))
    # print(options(init_positions(), (0, 1)))


def hard():
    global t, N, costs
    N += 2
    t = t[:2] + [[4, 3, 2, 1], [4, 2, 1, 3]] + t[2:]
    costs = {}
    pprint(init_positions())
    print(min(next_moves(init_positions(), 0)))


def indices(pos):
    for y, row in enumerate(pos):
        for x, _ in enumerate(row):
            yield (x, y)


teststr = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t, costs, N = read(), {}, 3
if __name__ == "__main__":
    # easy()
    hard()
