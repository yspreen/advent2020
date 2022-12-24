import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase, ascii_uppercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def read():
    global u
    with open(DIR / "input") as f:
        s, u = (f.read() if teststr == "" else teststr).split("\n\n")
        s = s.replace(".", "0").replace("#", "1").replace(" ", "2").splitlines()
    m = 0
    for line in s:
        m = max(m, len(line))
    for i in range(len(s)):
        while len(s[i]) < m:
            s[i] += "2"
    return np.array(lmap(lambda r: lmap(int, r), s), dtype=int)


mv = [
    (0, 1),  # R
    (1, 0),  # D
    (0, -1),  # L
    (-1, 0),  # U
]

mv_t = {
    ((-1, 0), "L"): (0, -1),
    ((-1, 0), "R"): (0, 1),
    ((-1, 0), "F"): (1, 0),
    ((1, 0), "L"): (0, 1),
    ((1, 0), "R"): (0, -1),
    ((1, 0), "F"): (-1, 0),
    ((0, -1), "L"): (1, 0),
    ((0, -1), "R"): (-1, 0),
    ((0, -1), "F"): (0, 1),
    ((0, 1), "L"): (-1, 0),
    ((0, 1), "R"): (1, 0),
    ((0, 1), "F"): (0, -1),
}


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


def next_step():
    n = ""
    while True:
        if not u:
            if n:
                return int(n), None
            return None, None
        c = u.pop()
        if c in ascii_uppercase:
            return int(n), c
        else:
            n += c


def move(pos, mv):
    new_p = (pos[0] + mv[0], pos[1] + mv[1])
    if t[new_p] == 1:  # wall
        return pos
    if t[new_p] == 2:  # wrap
        opp = (-mv[0], -mv[1])
        opp_t = pos
        while t[opp_t] != 2:
            opp_t = (opp_t[0] + opp[0], opp_t[1] + opp[1])
        opp_t = (opp_t[0] - opp[0], opp_t[1] - opp[1])
        if t[opp_t] == 1:  # wall
            return pos
        return opp_t
    return new_p


def cube_walk(tup, v):
    y, x = tup

    if y == 1 and x < 102:  # 1 c
        # print(1)
        v = mv_t[(v, "R")]
        y = x + 50
        x = 2
    elif y == 1:  # 2 c
        # print(2)
        # v = mv_t[(v, "-")]
        y = 201
        x = x - 100
    elif x == 152:  # 3 c
        # print(3)
        v = mv_t[(v, "F")]
        x = 101
        y = 153 - y
    elif y == 52 and x >= 102:  # 4 c
        # print(4)
        v = mv_t[(v, "R")]
        y = x - 50
        x = 101
    elif x == 102 and y < 102:  # 5 c
        # print(5)
        v = mv_t[(v, "L")]
        y = 51
        x = y + 50
    elif x == 102:  # 6 c
        # print(6)
        v = mv_t[(v, "F")]
        x = 151
        y = 153 - y
    elif y == 152 and x >= 52:  # 7 c
        # print(7)
        v = mv_t[(v, "R")]
        y = x + 100
        x = 51
    elif x == 52 and y >= 152:  # 8 c
        # print(8)
        v = mv_t[(v, "L")]
        x = y - 100
        y = 151
    elif y == 202:  # 9 c
        # print(9)
        # v = mv_t[(v, "-")]
        y = 2
        x = x + 100
    elif x == 1 and y >= 152:  # 10 c
        # print(10)
        v = mv_t[(v, "L")]
        x = y - 50
        y = 2
    elif x == 1:  # 11 c
        # print(11)
        v = mv_t[(v, "F")]
        y = 153 - y
        x = 52
    elif x < 52 and y == 101:  # 12 c
        # print(12)
        v = mv_t[(v, "R")]
        y = x + 50
        x = 52
    elif x == 51 and y < 52:  # 14 c
        # print(14)
        v = mv_t[(v, "F")]
        x = 2
        y = 153 - y
    elif x == 51 and y < 102:  # 13 c
        v = mv_t[(v, "L")]
        # print(13)
        x = y - 50
        y = 102
    else:
        print(x, y)
        assert False, "this isn't supposed to happen"

    return (y, x), v


def move_h(pos, mv):
    og_mv = mv
    after_move = new_p = (pos[0] + mv[0], pos[1] + mv[1])
    if t[new_p] == 1:  # wall
        return pos, og_mv
    if t[new_p] == 2:  # wrap
        new_p, mv = cube_walk(new_p, mv)
        if new_p[0] < 0 or new_p[1] < 0:
            print(after_move[1], after_move[0])
            print(new_p[1], new_p[0])
            assert False, "neg"
        if after_move == new_p:
            print(after_move[1], after_move[0])
            print(new_p[1], new_p[0])
            assert False, "this isn't supposed to happen at all"
        if t[new_p] == 2:
            print(after_move[1], after_move[0])
            print(new_p[1], new_p[0])
            assert False, "this isn't supposed to happen either"
        if t[new_p] == 1:  # wall
            return pos, og_mv
    return new_p, mv


def easy():
    global t
    t = np.pad(t, ((2, 2), (2, 2)), constant_values=2)

    pos = 2, (list(zip(*np.where(t[2] == 0)))[0][0])
    v = (0, 1)  # R

    # print(pos, v)
    while True:
        dist, dir = next_step()
        if dist is None:
            break

        for _ in range(dist):
            pos = move(pos, v)
        if dir is None:
            break
        v = mv_t[(v, dir)]
        # print(pos, v)

    result = 1000 * (pos[0] - 1) + 4 * (pos[1] - 1) + mv.index(v)
    # print(pos)
    print(result)


def hard():
    pos = 2, (list(zip(*np.where(t[2] == 0)))[0][0])
    v = (0, 1)  # R

    # print(pos, v)
    while True:
        dist, dir = next_step()
        if dist is None:
            break

        for _ in range(dist):
            pos, v = move_h(pos, v)
        if dir is None:
            break
        v = mv_t[(v, dir)]
        # print(pos, v)

    result = 1000 * (pos[0] - 1) + 4 * (pos[1] - 1) + mv.index(v)
    # print(pos)
    print(result)


teststr = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
teststr = """......#

1L1L5"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
u_ = u
u = list(u)
u.reverse()
if __name__ == "__main__":
    easy()
    u = u_
    u = list(u)
    u.reverse()
    hard()
