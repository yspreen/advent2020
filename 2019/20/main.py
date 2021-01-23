import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool


def read():
    with open(DIR / "input.txt") as f:
        t = [[ord(i) for i in sub] for sub in f.read().split("\n")][:-1]
    return np.array(t, np.int32)


class Move:
    def __init__(self, newpos, level=0):
        self.x = x
        self.y = y
        self.level = level


def neigh_3d(pos):
    n = []
    pos, lvl = (pos[0], pos[1]), pos[2]
    if lvl > 32:
        return n
    for p, c, dl in neigh[pos]:
        if p == -2:
            if lvl != 0:
                continue
            p, dl = (-1, -1), 0
        if lvl + dl < 0 or p == -1:
            continue
        n.append(((p[0], p[1], lvl + dl), c))
    return n


def neighbors(pos, portals):
    if len(pos) == 3:
        return neigh_3d(pos)
    n = []
    for d in directions:
        n.append(((pos[0] + d[0], pos[1] + d[1]), 1))
    try:
        assert portals
        n.append((portal_dest[pos], 1))
    except:
        pass
    return n


steps = 0


def bfs(pos, portals=True):
    global steps
    steps = {pos: [pos]}
    cost = {pos: 0}
    visited = set([pos])
    goal = [pos]

    while goal:
        pos = goal.pop(0)
        for n, c in neighbors(pos, portals=portals):
            if n in visited or (len(n) == 2 and t[n] != 0):
                continue
            cost[n] = cost[pos] + c
            steps[n] = steps[pos] + [n]
            if n == (-1, -1, 0):
                goal = []
                break
            goal.append(n)
            visited.add(n)
    return cost


def label_pos(x, y):
    for i in range(1, 3):
        for d in directions:
            x_, y_ = x + i * d[0], y + i * d[1]
            if t[x_ % (NX + 4), y_ % (NY + 4)] == 0:
                return x_ % (NX + 4), y_ % (NY + 4)


def label_ord(x, y):
    if x in [0, NX + 2] or y in [0, NY + 2]:
        return 26
    if x in [1, NX + 3] or y in [1, NY + 3]:
        return 1
    if x in [X + 2, NX - X] or y in [Y + 2, NY - Y]:
        return 26
    return 1


def easy():
    global points, portals, cost, portal_dest
    for a, b in [(32, 2), (35, 1), (46, 0)]:
        t[t == a] = b
    points = {}
    portals = {}
    portal_dest = {}
    for x, y in zip(*np.where(t > 64)):
        point = label_pos(x, y)
        c = (t[x, y] - 65) * label_ord(x, y)
        points[point] = points.get(point, 0) + c
    for k, v in points.items():
        portals[v] = portals.get(v, set()) | set([k])
    for k, v in points.items():
        o = portals[v] - set([k])
        if o:
            portal_dest[k] = list(o)[0]
    portal_dest[-1] = list(portals[0])[0]
    portal_dest[-2] = list(portals[26 * 26 - 1])[0]
    cost = bfs(portal_dest[-1])
    print(cost[portal_dest[-2]])
    portal_dest[list(portals[0])[0]] = -1
    portal_dest[list(portals[26 * 26 - 1])[0]] = -2


def inner_donut(x, y):
    return X / 2 + 2 < x < NX - X / 2 + 2 and Y / 2 + 2 < y < NY - Y / 2 + 2


def hard():
    for p in points.keys():
        cost = bfs(p, portals=False)
        neigh[p] = []
        for b in [i for i in points.keys() if i != p]:
            c = cost.get(b, None)
            if not c:
                continue
            b_ = portal_dest[b]
            neigh[p].append((b_, c + 1, 1 if inner_donut(*b) else -1))
    # print(neigh)
    cost = bfs((*portal_dest[-1], 0))
    print(cost[(-1, -1, 0)])
    print(
        *list(
            zip(
                [(name(a, b), c) for a, b, c in steps[(-1, -1, 0)]],
                [cost[p] for p in steps[(-1, -1, 0)]],
            )
        ),
        sep="\n"
    )


def name(x, y):
    if (x, y) == (-1, -1):
        return "zz"
    p = points[(x, y)]
    return ascii_lowercase[p // 26] + ascii_lowercase[p % 26]


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
X, Y = [i[0] for i in np.where(t[2:-2, 2:-2] == 32)]
NX, NY = t.shape[0] - 4, t.shape[1] - 4
directions = (
    (-1, 0),  # u / N
    (0, 1),  # r / E
    (1, 0),  # d / S
    (0, -1),  # l / W
)
points = portals = cost = portal_dest = neigh = {}

if __name__ == "__main__":
    easy()
    hard()
