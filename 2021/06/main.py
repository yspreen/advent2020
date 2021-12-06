import numpy as np
import pathlib


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return [s.count(str(i)) for i in range(9)]


def run(days):
    a = np.array(t, dtype=np.uint64)
    for _ in range(days):
        a = np.roll(a, -1)
        a[6] += a[8]
    return a.sum()


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    print(run(80))
    print(run(256))
