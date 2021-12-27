import numpy as np
import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return np.array(lmap(lambda r: lmap(".>v".index, r), s))


def step():
    moved = 0
    moves = []
    for y, x in zip(*np.where(t == 1)):
        if t[y, (x + 1) % t.shape[1]] == 0:
            moves.append((y, x))
    for y, x in moves:
        t[y, (x + 1) % t.shape[1]], t[y, x], moved = 1, 0, 1
    moves = []
    for y, x in zip(*np.where(t == 2)):
        if t[(y + 1) % t.shape[0], x] == 0:
            moves.append((y, x))
    for y, x in moves:
        t[(y + 1) % t.shape[0], x], t[y, x], moved = 2, 0, 1

    return moved


def easy():
    i = 0
    while step():
        i += 1
    print(i + 1)


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
