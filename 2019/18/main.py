import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")

replacements = {".": 0, "#": -1, "@": -2}
for i, a in enumerate(ascii_lowercase):
    replacements[a] = i + 1
    replacements[a.upper()] = i + 101
rev_replacements = {v: k for k, v in replacements.items()}


def read(n=1):
    with open(DIR / "input.txt") as f:
        t = [[replacements[i] for i in sub] for sub in f.read().split("\n")][:-1]
    return np.array(t, np.int32)


t = read()

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def neighbors(pos):
    n = []
    for d in directions:
        n.append((pos[0] + d[0], pos[1] + d[1]))
    return n


def bfs(c=-2, initial=True):
    pos = c_pos(c)
    t[np.where(t == -2)] = 0

    cost = {pos: 0}
    chain = {pos: []}
    visited = set(pos)
    goal = [pos]
    chain_starts = set()

    while goal:
        pos = goal.pop(0)
        for n in neighbors(pos):
            if n in visited or t[n] == -1:
                continue
            cost[n] = cost[pos] + 1
            if initial:
                chain[n] = list(chain[pos])
                if t[n] > 0:
                    if not chain[n]:
                        chain_starts.add(t[n])
                    chain[n].append(t[n])
            elif t[n] > 0:
                continue
            goal.append(n)
            visited.add(n)
    if not initial:
        return cost
    return cost, chain, chain_starts


def c_pos(c):
    return tuple(map(lambda i: i[0], np.where(t == c)))


def easy():
    cost, chain, chain_starts = bfs()
    distances = {}
    for c in list(chain_starts):
        distances[(0, c)] = distances[(c, 0)] = cost[c_pos(c)]
        ds = bfs(c, False)
        for o in [i for i in chain_starts if i != c]:
            op = c_pos(o)
            distances[(c, o)] = distances[(o, c)] = ds[op]

    # print(chain)
    # print(rev_replacements[12])
    # print(rev_replacements[101])

    # print(list(map(lambda i: rev_replacements[i], chain_starts)))

    chains = map(lambda i: c_pos(i + 1), list(range(26)) + list(range(100, 126)))
    # print((43, 27) in list(chains))
    chains = [chain[k] for k in chains]
    chains = {k: sorted([i for i in chains if k in i]) for k in chain_starts}
    for k, v in chains.items():
        for c in v:
            c = c[-1]


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
