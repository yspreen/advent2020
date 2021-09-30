import pathlib
from itertools import permutations
from copy import deepcopy


def read():
    with open(DIR / "input") as f:
        s = (
            (f.read() if teststr == "" else teststr)
            .replace("lose ", "-")
            .replace("gain ", "")
            .replace(".", "")
            .splitlines()
        )
    return {(r.split(" ")[0], r.split(" ")[-1]): int(r.split(" ")[2]) for r in s}


def score(perm, n):
    s = 0
    for i in range(n):
        s += t.get((perm[i], perm[(i + 1) % n]), 0)
    return s


def find(names):
    i, s, n = 0, {}, len(names)
    for perm in permutations(names):
        s[i] = score(perm, n)
        i += 1
    print(max(s.values()))


def easy():
    t_ = deepcopy(t)
    for index in t.keys():
        l, r = index
        t[(l, r)] += t_[(r, l)]
    find([v[0] for v in list(sorted(t.keys()))[:: int(len(t) ** 0.5)]])


def hard():
    find([v[0] for v in list(sorted(t.keys()))[:: int(len(t) ** 0.5)]] + [""])


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
