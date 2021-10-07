import numpy as np
import pathlib
from itertools import product


W = np.array([[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]])
A = np.array([[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]])
R = np.array([[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]])
A, R, n = np.vstack([A, [[0, 0, 0]]]), np.vstack([R, [[0, 0, 0]]]), len(R)
for i, j in product(range(n), repeat=2):
    R = R if j <= i else np.vstack([R, R[i] + R[j]])
with open(pathlib.Path(__file__).parent.absolute() / "input") as f:
    t = np.array(list(map(lambda r: int(r.split(" ")[-1]), f.read().splitlines())))
f = lambda a: 99 // max(1, t[1] - a[2]) + 1 >= (t[0] - 1) // max(1, a[1] - t[2]) + 1
win = [(f(w + a + r), (w + a + r)[0]) for w, a, r in product(W, A, R)]
print(min([cost for wins, cost in win if wins]))
print(max([cost for wins, cost in win if not wins]))
