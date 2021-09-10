import numpy as np
import pathlib
from math import prod

DIR = pathlib.Path(__file__).parent.absolute()


def read(n=1):
    global t, N, OFF
    with open(DIR / "input") as f:
        t_ = f.read().split("\n")[0]
        # t_ = "03036732577212944063491565474664"
    t = np.array([int(i) for i in t_], np.int16)
    N = len(t) * n
    OFF = 0 if n == 1 else int(t_[:7])


t = N = OFF = 0
pattern = [0, 1, 0, -1]
patterns = {}


def get_pattern(n):
    if patterns.get(n, None) is None:
        patterns[n] = get_pattern_(n)
    return patterns[n]


def get_pattern_(n):
    p = [[i] * (n + 1) for i in pattern]
    return [i for sublist in p * (N // 3) for i in sublist][1 : N + 1]


def step():
    global t
    t_ = []
    for i in range(N):
        p = get_pattern(i)
        s = sum(map(prod, zip(t, p)))
        t_.append(abs(s) % 10)
    t = t_


def easy():
    read()
    for _ in range(100):
        step()
    print("".join(map(str, t[:8])))


def get_t(i):
    return t[i % len(t)]


def phase(p, p_, n):
    i = N
    s = 0
    while i > OFF:
        i -= 1
        s += p[i - OFF] if n > 0 else get_t(i)
        s %= 10
        p_[i - OFF] = s
    return p_, p


def hard():
    read(10000)
    p = np.zeros((N - OFF,), np.int32)
    p_ = np.zeros_like(p)
    for i in range(100):
        p, p_ = phase(p, p_, i)
    print("".join(map(str, p[:8])))


if __name__ == "__main__":
    easy()
    hard()
