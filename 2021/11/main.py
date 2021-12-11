import numpy as np
import pathlib


def read() -> any:
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array((lmap(lambda r: lmap(int, r), s)))


def step():
    global t, F
    t += 1
    while True:
        p = list(zip(*np.where(t >= 10)))
        if not p:
            t[t < 0] = 0
            return
        for x, y in p:
            F += 1
            xm = x - 1 if x > 0 else x
            ym = y - 1 if y > 0 else y
            t[xm : x + 2, ym : y + 2] += 1
            t[x, y] = -int(9e9)


def easy(steps):
    for _ in range(steps):
        step()
    print(F)


def hard(previous_steps):
    for i in range(int(9e9)):
        step()
        if t.max() == 0:
            return print(previous_steps + i + 1)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t, F = read(), 0
if __name__ == "__main__":
    easy(100)
    hard(100)
