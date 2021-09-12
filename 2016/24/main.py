import numpy as np
import pathlib
from python_tsp.exact import solve_tsp_dynamic_programming


def lmap(*a):
    return list(map(*a))


rpl = {
    v: k for k, v in enumerate([".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "#"])
}


def read():
    with open(DIR / "input") as f:
        s = f.read().splitlines()
    return np.array(lmap(lambda r: lmap(lambda i: rpl[i], r), s), dtype=np.uint32)


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


DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    cost = np.zeros((t[t < 10].max(), t[t < 10].max()), dtype=np.uint32)
    for i in range(t[t < 10].max()):
        for j, c in BFS(i + 1).items():
            cost[i, j - 1] = c
    roundtrip = solve_tsp_dynamic_programming(cost)[1]
    cost[:, 0] = 0
    print(solve_tsp_dynamic_programming(cost)[1])
    print(roundtrip)
