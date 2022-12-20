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
from itertools import combinations


def TSP(G):
    n = len(G)
    C = [[inf for _ in range(n)] for __ in range(1 << n)]
    C[1][0] = 0  # {0} <-> 1
    for size in range(1, n):
        for S in combinations(range(1, n), size):
            S = (0,) + S
            k = sum([1 << i for i in S])
            for i in S:
                if i == 0:
                    continue
                for j in S:
                    if j == i:
                        continue
                    cur_index = k ^ (1 << i)
                    C[k][i] = min(C[k][i], C[cur_index][j] + G[j][i])
                    # C[S−{i}][j]
    all_index = (1 << n) - 1
    return min([(C[all_index][i] + G[0][i], i) for i in range(n)])


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    s = s.replace("Valve ", "")
    s = re.sub(r"[a-z\=\;\,]", "", s)
    s = re.sub(r" +", " ", s)
    s = s.splitlines()
    return lmap(
        lambda line: [line[0], line[1], line[2:]],
        lmap(lambda r: lmap(maybeint, r.split(" ")), s),
    )


def maybeint(line):
    try:
        return int(line)
    except:
        return line


paths = {}
flows = {}
idx = {}
valves = []
G = np.array([[0]])


def easy():
    global G
    for pos, flow, dest in t:
        paths[pos] = dest
        flows[pos] = flow
        idx[pos] = len(valves)
        valves.append(pos)
    print((flows))
    G = np.zeros((len(paths), len(paths)))

    start = ["AA"]
    prev = []
    while len(prev) < len(valves):
        new_starts = []
        for b in start:
            for n in paths[b]:
                if n not in prev and n not in new_starts:
                    new_starts.append(n)
                G[idx[b], idx[n]] = 1
                G[idx[n], idx[b]] = 1
                for a in prev:
                    G[idx[a], idx[n]] = G[idx[a], idx[b]] + 1
                    G[idx[n], idx[a]] = G[idx[a], idx[b]] + 1
        prev += start
        start = new_starts
    print(G)


def hard():
    return


teststr = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
