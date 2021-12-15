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


def dijkstra_search(start, goal):
    frontier = [[start]]
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while True:
        try:
            i = 0
            while True:
                if not frontier[i]:
                    i += 1
                else:
                    current = frontier[i].pop(0)
                    break
        except:
            break
        if current == goal:
            break
        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                while len(frontier) < new_cost + 1:
                    frontier += [[]]
                frontier[new_cost] += [next]
                came_from[next] = current
    return came_from, cost_so_far


def easy():
    print(dijkstra_search((0, 0), (N - 1, N - 1))[1][(N - 1, N - 1)])


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t, N = read(), (100 if teststr == "" else len(teststr.splitlines()[0]))
if __name__ == "__main__":
    easy()
    hard()
