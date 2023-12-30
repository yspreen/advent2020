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
    return np.array(lmap(lambda r: lmap(int, r), s))


def cost(current, next):
    return t[next[0], next[1]]


def same_dir(pos, new_pos, origin, max_length=3):
    p = pos
    c = 0
    v = (new_pos[0] - p[0], new_pos[1] - p[1])
    while p in origin and c < max_length:
        prev = origin[p]
        if (p[0] - prev[0], p[1] - prev[1]) != v:
            return False
        p = prev
        c += 1
    return c == max_length


def neighbors(state):
    (x, y, d, c) = state
    pos = (x, y)
    n = []

    backwards = {
        "U": "D",
        "D": "U",
        "L": "R",
        "R": "L",
    }[d]

    for k, v in mv.items():
        c_ = c + 1 if k == d else 1
        if c_ == 4:
            continue
        if k == backwards:
            continue
        pos_ = (pos[0] + v[0], pos[1] + v[1])
        if pos_[0] < 0:
            continue
        if pos_[1] < 0:
            continue
        try:
            _ = t[pos_]
        except Exception:
            continue
        n.append((*pos_, k, c_))
    return n


def is_goal(pos):
    return pos[:2] == (t.shape[0] - 1, t.shape[1] - 1)


def dijkstra_search(start):
    from queue import PriorityQueue

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    current = cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()[1]
        if is_goal(current):
            break
        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put((new_cost, next))
                came_from[next] = current
    return came_from, cost_so_far, cost_so_far[current], current


mv = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def easy():
    start = (0, 0, "D", 0)
    origin, costs, cost, end = dijkstra_search(start)

    # A = np.zeros_like(t)
    # p = end
    # while p != start:
    #     A[p[:2]] = 1
    #     p = origin[p]
    # A[p[:2]] = 1
    # print(A)
    print(cost)


def hard():
    return


teststr = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))

t = read()
if __name__ == "__main__":
    easy()
    hard()
