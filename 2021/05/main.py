import numpy as np
import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(" -> ", ",").splitlines()
    return lmap(lambda r: lmap(int, r.split(",")), s)


def hard():
    A = np.zeros((999, 999))
    B = np.zeros((999, 999))
    for a, b, c, d in t:
        if a != c and b != d:
            dx = 1 if c > a else -1
            dy = 1 if d > b else -1
            while a != c:
                B[a, b] += 1
                a += dx
                b += dy
            B[a, b] += 1
            continue

        a, c = min([a, c]), max([a, c])
        b, d = min([b, d]), max([b, d])
        A[a : c + 1, b : d + 1] += 1
        B[a : c + 1, b : d + 1] += 1

    print(len(np.where(A >= 2)[0]))
    print(len(np.where(B >= 2)[0]))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    hard()
