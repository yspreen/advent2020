import numpy as np
import pathlib
from math import prod


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(int, r), s))


def easy():
    s = 0
    for i in range(N):
        for j in range(M):
            n = t[i, j]
            if i - 1 >= 0 and t[i - 1, j] <= n:
                continue
            if j - 1 >= 0 and t[i, j - 1] <= n:
                continue
            if i + 1 < N and t[i + 1, j] <= n:
                continue
            if j + 1 < M and t[i, j + 1] <= n:
                continue
            s += n + 1
            B.append((i, j))
    print(s)


def hard():
    lens = []
    for p in B:
        queue, found = [p], set([p])
        while queue:
            old, queue = queue, []
            for i, j in old:
                if i - 1 >= 0 and t[i - 1, j] < 9 and (i - 1, j) not in found:
                    p = (i - 1, j)
                    found.add(p)
                    queue.append(p)
                if j - 1 >= 0 and t[i, j - 1] < 9 and (i, j - 1) not in found:
                    p = (i, j - 1)
                    found.add(p)
                    queue.append(p)
                if i + 1 < N and t[i + 1, j] < 9 and (i + 1, j) not in found:
                    p = (i + 1, j)
                    found.add(p)
                    queue.append(p)
                if j + 1 < M and t[i, j + 1] < 9 and (i, j + 1) not in found:
                    p = (i, j + 1)
                    found.add(p)
                    queue.append(p)
        lens.append(len(found))
    print(prod(sorted(lens)[-3:]))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
B, N, M = [], len(t), len(t[0])
if __name__ == "__main__":
    easy()
    hard()
