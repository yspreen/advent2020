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
        s = (
            (f.read() if teststr == "" else teststr)
            .replace("#", "1")
            .replace(".", "0")
            .replace("S", "2")
            .replace("E", "3")
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
    (0, 1),  # R
    (1, 0),  # D
    (0, -1),  # L
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

    options = [([start], 0, 1)]
    visited = {start: 0}

    min_solution = 9e9

    while options:
        new_o = []
        for hist, cost, prev_mv_index in options:
            pos = hist[-1]
            for mv_idx, d in enumerate(mv):
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:  # lower bound check
                    continue
                if new_p[1] < 0:  # lower bound check
                    continue
                try:
                    assert can_walk(pos, new_p)
                except:
                    continue  # upper bound check
                cost_ = cost + cost_fn(prev_mv_index, mv_idx)
                if new_p in visited and visited[new_p] < cost_:
                    continue
                visited[new_p] = cost_
                new_o.append((hist + [new_p], cost_, mv_idx))
                if goal(new_p) and cost_ <= min_solution:
                    min_solution = cost_
        options = new_o
    return min_solution


def easy():
    start = list(zip(*np.where(t == 2)))[0]

    print(
        BFS(
            start,
            lambda lhs, rhs: t[rhs] != 1,
            lambda p: t[p] == 3,
            lambda lhs, rhs: 1 if lhs == rhs else 1001,
        )
    )


def hard():
    end = (
        int(list(zip(*np.where(t == 3)))[0][0]),
        int(list(zip(*np.where(t == 3)))[0][1]),
    )
    start = (
        int(list(zip(*np.where(t == 2)))[0][0]),
        int(list(zip(*np.where(t == 2)))[0][1]),
    )
    min_dist = {
        (end, 0): 0,
        (end, 1): 0,
        (end, 2): 0,
        (end, 3): 0,
    }

    turns_allowed = 0

    next_options = [
        ((end, 0), 0, 0),
        ((end, 1), 0, 0),
        ((end, 2), 0, 0),
        ((end, 3), 0, 0),
    ]
    while next_options:
        added_new = False
        options = next_options
        next_options = []

        while options:
            new_o = []
            for pos_t, cost, turns in options:
                pos, turn = pos_t
                for mv_idx, d in enumerate(mv):
                    mv_idx = (mv_idx + 2) % 4  # reverse because we are going backwards
                    new_p = (pos[0] + d[0], pos[1] + d[1])
                    if new_p[0] < 0:  # lower bound check
                        continue
                    if new_p[1] < 0:  # lower bound check
                        continue
                    try:
                        assert t[new_p] != 1
                    except:
                        continue  # upper bound check
                    add_turn = 1 if turn != mv_idx else 0
                    if turns + add_turn > turns_allowed:
                        next_options.append((pos_t, cost, turns))
                        continue
                    cost_ = cost + 1 + (1000 if add_turn else 0)
                    new_p_t = (new_p, mv_idx)
                    if new_p_t in min_dist and min_dist[new_p_t] <= cost_:
                        continue
                    min_dist[new_p_t] = cost_
                    new_o.append((new_p_t, cost_, turns + add_turn))
                    added_new = True
            options = new_o

        turns_allowed += 1

    for k, v in list(min_dist.items()):
        pos, turn = k
        for add_turn in [1, 2, 3]:
            new_turn = (turn + add_turn) % 4
            cost = [0, 1000, 2000, 1000][add_turn]
            if (pos, new_turn) not in min_dist or min_dist[(pos, new_turn)] > v + cost:
                min_dist[(pos, new_turn)] = v + cost

    limit = min_dist[(start, 1)]

    search_heads = [((start, 0), 1000, set([start])), ((start, 1), 0, set([start]))]
    all_visited = set()
    while search_heads:
        new_search = []
        for pos_t, cost, hist in search_heads:
            pos, turn = pos_t
            for new_turn, d in enumerate(mv):
                new_p = (pos[0] + d[0], pos[1] + d[1])

                if not (new_p, new_turn) in min_dist:
                    continue
                if min_dist[(new_p, new_turn)] + cost > limit:
                    continue
                new_search.append(
                    (
                        (new_p, new_turn),
                        cost + 1 + (1000 if new_turn != turn else 0),
                        hist | set([new_p]),
                    )
                )
                if new_p == end:
                    all_visited |= hist | set([new_p])
        search_heads = new_search
    print(len(all_visited))

    # print(len(min_dist))
    # print(min_dist[(start, 1)])


teststr = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
