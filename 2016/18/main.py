import numpy as np
import pathlib
from itertools import product


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return np.array([1 if i == "^" else 0 for i in s], dtype=np.uint8)


allowed = {}
for t in product(*([[0, 1]] * 3)):
    allowed[t] = t in [(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)]


def next(row):
    new = np.zeros_like(row)
    row = np.hstack(([0], row, [0]))
    for i in range(1, row.size - 1):
        elem = row[i - 1 : i + 2]
        if allowed[tuple(elem)]:
            new[i - 1] = 1
    return new


def run(steps):
    a = t
    N = int(a.size)
    s = N - int(a.sum())
    seen = {tuple(a): 0}
    scores = [s]
    i = 1
    while i < steps:
        a = next(a)
        tup = tuple(a)
        s += N - int(a.sum())
        scores.append(s)
        if tup in seen:
            prev_index = seen[tup]
            diff = i - prev_index
            score_diff = s - scores[prev_index]
            j = (steps - 1 - i) // diff
            s += score_diff * j
            i += diff * j
            seen = {}
        else:
            seen[tup] = i
        i += 1
    print(s)


def easy():
    run(40)


def hard():
    run(400000)


teststr = ""  # """.^^.^.^^^^"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
