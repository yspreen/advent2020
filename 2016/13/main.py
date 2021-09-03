import numpy as np
import pathlib
from itertools import product


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return int(s[0])


def is_wall(x, y):
    v = x * x + 3 * x + 2 * x * y + y + y * y
    v += t
    v = bin(v)
    v = v.count("1")
    v %= 2
    return v == 1


def moves(x, y):
    moves = []
    for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if p[0] >= 0 and p[1] >= 0 and A[p] == 0:
            moves.append(p)
    return moves


def step(forward_positions, costs_forward, costs_back):
    new_positions = []
    for cost, pos in forward_positions:
        cost += 1
        new_moves = moves(*pos)
        for m in new_moves:
            if m in costs_forward:
                continue
            if m in costs_back:
                return (True, costs_back[m] + cost)
            costs_forward[m] = cost
            new_positions.append((cost, m))
    return (False, new_positions)


def BFS(x, y, max_d=9999999, two_ways=True):
    goal = (x, y)
    start = (1, 1)

    positions_f = [(0, start)]
    positions_b = [(0, goal)]
    reached_f = {start: 0}
    reached_b = {goal: 0}

    for _ in range(max_d):
        found, positions_f = step(positions_f, reached_f, reached_b)
        if found:
            return positions_f
        if not two_ways:
            continue
        found, positions_b = step(positions_b, reached_b, reached_f)
        if found:
            return positions_b
    return reached_f


def easy():
    global A
    A = np.zeros((265, 265), dtype=np.uint)
    for x, y in product(range(265), range(265)):
        A[x, y] = is_wall(x, y)

    print(BFS(31, 39))


def hard():
    print(len(BFS(inf, inf, 50, False)))


teststr = ""  # "10"
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
A = t = read()
if __name__ == "__main__":
    easy()
    hard()
