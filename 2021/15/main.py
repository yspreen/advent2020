import numpy as np
import pathlib
from queue import PriorityQueue


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
    frontier = PriorityQueue(N * N)
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while True:
        if frontier.empty():
            break
        current = frontier.get()[1]
        if current == goal:
            break
        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put((new_cost, next))
                came_from[next] = current
    return came_from, cost_so_far


def easy():
    print(dijkstra_search((0, 0), (N - 1, N - 1))[1][(N - 1, N - 1)])


def hard():
    global t, N
    o = t[:N, :N]
    t = np.zeros((N * 5, N * 5), dtype=np.int8)
    for i in range(5):
        for j in range(5):
            t[i * N : (i + 1) * N, j * N : (j + 1) * N] = o + i + j
    while t.max() > 9:
        t[t > 9] -= 9
    N *= 5
    print(dijkstra_search((0, 0), (N - 1, N - 1))[1][(N - 1, N - 1)])


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t, N = read(), (100 if teststr == "" else len(teststr.splitlines()[0]))
if __name__ == "__main__":
    easy()
    hard()
