import numpy as np
import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, r), s)


def easy():
    counts = [[0, 0] for _ in t[0]]
    for line in t:
        for i, c in enumerate(line):
            counts[i][c] += 1
    a = ""
    for i, c in enumerate(counts):
        m = max(c)
        a += "1" if m == c[1] else "0"
    b = [("1" if c == "0" else "0") for c in a]
    a = int(a, base=2)
    b = int("".join(b), base=2)
    print(a * b)


def val(default):
    A = np.array(t)

    i = 0
    while True:
        n = len(A)
        if n == 1:
            return A[0]
        bits = A[:, i]
        s = bits.sum()
        a = 1 - default
        if s >= n / 2:
            a = default
        A = A[A[:, i] == a, :]
        i += 1


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
    print(
        int("".join(map(str, val(1))), base=2) * int("".join(map(str, val(0))), base=2)
    )
