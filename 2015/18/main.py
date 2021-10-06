import numpy as np
import pathlib
from itertools import product


def read():
    with open(pathlib.Path(__file__).parent.absolute() / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(lambda i: ".#".index(i), r), s), dtype=np.uint8)


def step(q):
    global t, t_
    for i, j in product(range(N), repeat=2):
        n = t[i : i + 3, j : j + 3]
        m, s = n[1, 1], n.sum()
        t_[i + 1, j + 1] = 1 if (m == 1 and 3 <= s <= 4) or (m == 0 and s == 3) else 0
    t, t_ = t_, t
    t[corners] = 1 if q else t[corners]


teststr = """"""
lmap, corners = lambda *a: list(map(*a)), ([1, 100, 1, 100], [1, 1, 100, 100])
t, t_, N = np.pad(read(), 1), np.zeros((102, 102), dtype=np.uint8), 100
if __name__ == "__main__":
    [step(0) for _ in range(100)]
    print(t.sum())
    t = np.pad(read(), 1)
    [step(1) for _ in range(100)]
    print(t.sum())
