import numpy as np
import pathlib
from itertools import product


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: int(r.split(" ")[-1]), s))


def wins(_, dmg, amr):
    dmg = max(1, dmg - t[2])
    enemy_d = max(1, t[1] - amr)
    turns = (t[0] - 1) // dmg + 1
    enemy_t = (100 - 1) // enemy_d + 1
    return enemy_t >= turns


def easy():
    m = 9e9
    for w, a, r in product(W, A, R):
        if wins(*(w + a + r)):
            m = min(m, (w + a + r)[0])
    print(m)


def hard():
    m = 0
    for w, a, r in product(W, A, R):
        if not wins(*(w + a + r)):
            m = max(m, (w + a + r)[0])
    print(m)


W = np.array([[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]])
A = np.array([[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]])
R = np.array([[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]])
A, R, n = np.vstack([A, [[0, 0, 0]]]), np.vstack([R, [[0, 0, 0]]]), len(R)
for i in range(n):
    for j in range(i + 1, n):
        R = np.vstack([R, R[i] + R[j]])

teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
    hard()
