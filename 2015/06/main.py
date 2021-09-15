import numpy as np
import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = map(
            lambda r: r.split(","),
            (f.read() if teststr == "" else teststr)
            .replace("turn ", "")
            .replace(" ", ",")
            .splitlines(),
        )
    return lmap(lambda r: (r[0], int(r[1]), int(r[2]), int(r[4]), int(r[5])), s)


def easy():
    A = np.zeros((1000, 1000), dtype=np.uint8)
    for instr, x1, y1, x2, y2 in t:
        if instr == "on":
            A[x1 : x2 + 1, y1 : y2 + 1] = 1
        elif instr == "off":
            A[x1 : x2 + 1, y1 : y2 + 1] = 0
        else:
            A[x1 : x2 + 1, y1 : y2 + 1] = 1 - A[x1 : x2 + 1, y1 : y2 + 1]
    print(A.sum())


def hard():
    A = np.zeros((1000, 1000), dtype=np.uint8)
    for instr, x1, y1, x2, y2 in t:
        if instr == "on":
            A[x1 : x2 + 1, y1 : y2 + 1] += 1
        elif instr == "off":
            A[x1 : x2 + 1, y1 : y2 + 1] -= np.array(
                1 * (A[x1 : x2 + 1, y1 : y2 + 1] > 0), dtype=A.dtype
            )
        else:
            A[x1 : x2 + 1, y1 : y2 + 1] += 2
    print(A.sum())


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
