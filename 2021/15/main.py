from turtle import st
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


def heuristic(a, b) -> float:
    x1, y1 = a
    x2, y2 = b
    return (abs(x1 - x2) + abs(y1 - y2)) * 9


def neighbors(p):
    x, y = p
    n = []
    if x > 0:
        n.append((x - 1, y))
    if y > 0:
        n.append((x, y - 1))
    if x < N - 1:
        n.append((x + 1, y))
    if y < N - 1:
        n.append((x, y + 1))
    return n


def cost(_, next):
    return t[next]


def a_star_search(start, goal):
    frontier = []
    frontier += [start]
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = frontier.pop(0)

        if current == goal:
            break

        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.insert(priority - 1, next)
                came_from[next] = current

    return came_from, cost_so_far


def easy():
    origin, cost_d = a_star_search((0, 0), (N - 1, N - 1))
    print(origin, cost_d[(N - 1, N - 1)])
    p = (N - 1, N - 1)
    print(p)
    while p != (0, 0):
        p = origin[p]
        print(p)
    print(t)


def hard():
    return


teststr = """19999
19111
19191
19191
11191"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t, N = read(), (100 if teststr == "" else len(teststr.splitlines()[0]))
if __name__ == "__main__":
    easy()
    hard()
