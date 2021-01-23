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


def neighbors(pos):
    n = []
    for d in directions:
        n.append((pos[0] + d[0], pos[1] + d[1]))
    try:
        n.append(portal_dest[pos])
    except:
        pass
    return n


def bfs(pos):
    cost = {pos: 0}
    visited = set([pos])
    goal = [pos]

    while goal:
        pos = goal.pop(0)
        for n in neighbors(pos):
            if n in visited or t[n] != 0:
                continue
            cost[n] = cost[pos] + 1
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
    for a, b in [(32, 2), (35, 1), (46, 0)]:
        t[t == a] = b
    # B = np.zeros_like(t, np.int32)
    # for x, y in zip(*np.where(t > 64)):
    #     B[tuple(label_pos(x, y))] = 1
    #     B[(x, y)] = label_ord(x, y)
    # for r in B:
    #     for e in r:
    #         print(" " if e == 0 else e, end="")
    #     print()
    points = {}
    portals = {}
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
    portal_dest[-2] = list(portals[25 * 27])[0]
    cost = bfs(portal_dest[-1])
    print(cost[portal_dest[-2]])


def hard():
    return


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
X, Y = [i[0] for i in np.where(t[2:-2, 2:-2] == 32)]
NX, NY = t.shape[0] - 4, t.shape[1] - 4
portal_dest = {}
directions = (
    (-1, 0),  # u / N
    (0, 1),  # r / E
    (1, 0),  # d / S
    (0, -1),  # l / W
)

if __name__ == "__main__":
    easy()
    hard()
