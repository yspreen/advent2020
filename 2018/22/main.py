import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols, solve


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    t = map(lambda l: l.split(": ")[1], t)
    t = list(map(lambda l: list(map(int, l.split(","))), t))
    return t[0][0], t[1][0], t[1][1]


def easy():
    global TX, TY, A
    TX *= 2
    TY *= 2
    A = np.zeros((TX + 1, TY + 1), np.int)
    for x in range(TX + 1):
        A[x, 0] = (X * x + D) % M
    for y in range(1, TY + 1):
        A[0, y] = (Y * y + D) % M
    for x, y in product(range(1, TX + 1), range(1, TY + 1)):
        A[x, y] = (A[x - 1, y] * A[x, y - 1] + D) % M
    TX //= 2
    TY //= 2
    A[TX, TY] = (0 + D) % M
    A %= 3
    # for r in A.T:
    #     for e in r:
    #         print([".", "=", "|"][e], end="")
    #     print()
    print(A[: TX + 1, : TY + 1].sum())


def h(x):
    return x[0] + x[1]


def min_fscore(s, f):
    m = (inf, 0)
    for e in s:
        x = f.get(e, inf)
        if x < m[0]:
            m = (x, e)
    return m[1]


allowed = {0: [1, 2], 1: [0, 2], 2: [0, 1]}


def neighbors(p):
    n = []
    ## Alternative approach: Putting a tool away takes 7min, grabbing the next one another 7min
    # possible_tools = []
    # for i in range(3):
    #     i = 2 ** i
    #     if p[2] & i:
    #         possible_tools.append(p[2] - i)
    #     else:
    #         possible_tools.append(p[2] + i)
    possible_tools = {0, 1, 2} - {p[2]}
    for t in possible_tools:
        if t in allowed[A[p[0], p[1]]]:
            n.append(((p[0], p[1], t), 7))
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = p[0] + dx, p[1] + dy
        if 0 <= x < TX * 2 and 0 <= y < TY * 2 and A[x, y] in allowed[p[2]]:
            n.append(((x, y, p[2]), 1))
    return n


# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def A_Star(start, goal):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = {start}

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {start: 0}  # default value of Infinity

    # For node n, fScore[n] = gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    fScore = {start: h(start)}  # default value of Infinity

    while True:
        # This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current = min_fscore(
            openSet, fScore
        )  # the node in openSet having the lowest fScore[] value
        if current == goal:
            return gScore[goal]

        openSet -= {current}
        for (neighbor, cost) in neighbors(current):
            # cost is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore.get(current, inf) + cost
            if tentative_gScore < gScore.get(neighbor, inf):
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore.get(neighbor, inf) + h(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)


def hard():
    print(A_Star((0, 0, 1), (TX, TY, 1)))


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
D, TX, TY = 510, 10, 10
D, TX, TY = read()
dirs = {}
X = 16807
Y = 48271
M = 20183
A = 0

if __name__ == "__main__":
    easy()
    hard()