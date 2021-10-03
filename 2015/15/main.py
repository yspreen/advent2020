import numpy as np
import pathlib
from itertools import product


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(",", "").splitlines()
    return lmap(
        lambda r: lmap(lambda i: int(r.split(" ")[i]), [2, 4, 6, 8, 10]),
        s,
    )


def easy():
    weights = np.array(t)[:, :-1]
    s = 0

    for l in product(*([range(100)] * (len(weights) - 1))):
        if sum(l) > 100:
            continue
        l = list(l) + [100 - sum(l)]
        r = weights.T @ np.array(l)
        if (r <= 0).any():
            continue
        s = max(s, np.prod(r))
    print(s)


def hard():
    weights = np.array(t)
    s = 0

    for l in product(*([range(100)] * (len(weights) - 1))):
        if sum(l) > 100:
            continue
        l = list(l) + [100 - sum(l)]
        r = weights.T @ np.array(l)
        if r[-1] != 500:
            continue
        if (r[:-1] <= 0).any():
            continue
        s = max(s, np.prod(r[:-1]))
    print(s)


teststr = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
    hard()
