import numpy as np
import pathlib


def lmap(*a):
    return list(map(*a))


def sint(v):
    try:
        return int(v)
    except:
        return v


def read():
    with open(DIR / "input") as f:
        s = (
            (f.read() if teststr == "" else teststr)
            .replace("rotate ", "")
            .replace("x=", "")
            .replace("y=", "")
            .replace(" by", "")
            .replace("x", " ")
            .splitlines()
        )
    return lmap(lambda r: lmap(sint, r.split(" ")), s)


def rect(A, x, y):
    A[:y, :x] |= 1
    return A


def row(A, x, y):
    rows, cols = np.ogrid[: A.shape[0], : A.shape[1]]
    cols = cols - (np.eye(6, dtype=np.int)[x] * y)[:, np.newaxis]
    return A[rows, cols]


def column(A, x, y):
    rows, cols = np.ogrid[: A.shape[0], : A.shape[1]]
    rows = rows - (np.eye(50, dtype=np.int)[x] * y)[np.newaxis, :]
    return A[rows, cols]


def easy():
    global A
    for name, x, y in t:
        A = {"rect": rect, "row": row, "column": column}[name](A, x, y)
    print(A.sum())


def hard():
    a, s = A.T, ""
    for i in range(len(a) // 5):
        l = a[i * 5 : i * 5 + 5].T
        # print(*["".join([[" ", "#"][i] for i in r]) for r in l], sep="\n")
        s += {
            "111111101001101001100001000000": "E",
            "111111101000101000100000000000": "F",
            "110000001000000111001000110000": "Y",
            "111111100100100110011001000000": "R",
            "000000100001111111100001000000": "I",
            "000010000001100001111110000000": "J",
            "111111001000010110100001000000": "K",
        }["".join((map(str, a[i * 5 : i * 5 + 5].flatten())))]
    print(s)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t, A = read(), np.zeros((6, 50), np.int)
if __name__ == "__main__":
    easy()
    hard()