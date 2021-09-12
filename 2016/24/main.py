import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from python_tsp.exact import solve_tsp_dynamic_programming


def lmap(*a):
    return list(map(*a))


rpl = {
    ".": 0,
    "0": 1,
    "1": 2,
    "2": 3,
    "3": 4,
    "4": 5,
    "5": 6,
    "6": 7,
    "7": 8,
    "8": 9,
    "#": 10,
}


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(lambda i: rpl[i], r), s), dtype=np.uint32)


def coord(m):
    return (m.count("R") - m.count("L"), m.count("D") - m.count("U"))


def neighbors(x, y):
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if t[p] < 10]


def step(positions, visited, costs):
    new_positions = []
    for cost, pos in positions:
        for m in [m for m in neighbors(*pos) if m not in visited]:
            visited.add(m)
            new_positions.append((cost + 1, m))
            if t[m] > 0:
                costs[t[m]] = cost + 1
    return new_positions


def BFS(start=1):
    start_pos = list(zip(*np.where(t == start)))[0]
    visited, positions, costs = {start_pos}, [(0, start_pos)], {start: 0}
    while positions:
        positions = step(positions, visited, costs)
    return costs


def easy():
    cost = np.zeros((t[t < 10].max(), t[t < 10].max()), dtype=np.uint32)
    for i in range(t[t < 10].max()):
        for j, c in BFS(i + 1).items():
            cost[i, j - 1] = c
    cost[:, 0] = 0
    _, distance = solve_tsp_dynamic_programming(cost)
    print(distance)


def hard():
    return


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
