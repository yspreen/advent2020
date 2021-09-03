import numpy as np
import pathlib
from itertools import product


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    t = map(lambda l: l.split(": ")[1], t)
    t = list(map(lambda l: list(map(int, l.split(","))), t))
    return t[0][0], t[1][0], t[1][1]


def min_f_score(s, f):
    m = (inf, 0)
    for e in s:
        x = f.get(e, inf)
        if x < m[0]:
            m = (x, e)
    return m[1]


def neighbors(p):
    n = []
    possible_tools = {0, 1, 2} - {p[2]}
    for t in possible_tools & set(allowed[A[p[0], p[1]]]):
        n.append(((p[0], p[1], t), 7))
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = p[0] + dx, p[1] + dy
        if 0 <= x < TX * K and 0 <= y < TY * K and A[x, y] in allowed[p[2]]:
            n.append(((x, y, p[2]), 1))
    return n


def a_star(start, goal):
    open_set = {start}
    cameFrom = {}
    g_score = {start: 0}
    f_score = {start: 0}
    while True:
        current = min_f_score(open_set, f_score)
        if current == goal:
            return g_score[goal]
        open_set -= {current}
        for (neighbor, cost) in neighbors(current):
            tentative_gScore = g_score.get(current, inf) + cost
            if tentative_gScore < g_score.get(neighbor, inf):
                cameFrom[neighbor] = current
                g_score[neighbor] = tentative_gScore
                f_score[neighbor] = g_score.get(neighbor, inf) + sum(neighbor[:2])
                if neighbor not in open_set:
                    open_set.add(neighbor)


def easy():
    global TX, TY, A
    TX *= K
    TY *= K
    A = np.zeros((TX + 1, TY + 1), np.int)
    for x in range(TX + 1):
        A[x, 0] = (X * x + D) % M
    for y in range(1, TY + 1):
        A[0, y] = (Y * y + D) % M
    for x, y in product(range(1, TX + 1), range(1, TY + 1)):
        A[x, y] = (A[x - 1, y] * A[x, y - 1] + D) % M
    TX //= K
    TY //= K
    A[TX, TY] = (0 + D) % M
    A %= 3
    print(A[: TX + 1, : TY + 1].sum())


def hard():
    print(a_star((0, 0, 1), (TX, TY, 1)))


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
D, TX, TY = 510, 10, 10
D, TX, TY = read()
dirs = {}
X = 16807
Y = 48271
M = 20183
A = 0
allowed = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
K = 8
if __name__ == "__main__":
    easy()
    hard()