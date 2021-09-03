import pathlib
from functools import reduce


def lmap(*a):
    return list(map(*a))


def read(hard=0):
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    if hard:
        return lmap(ord, s.splitlines()[0])
    return lmap(int, s.splitlines()[0].split(","))


def easy():
    hash()
    print(T[0] * T[1])


def hash(i=0, s=0):
    global T
    for l in t:
        i %= N
        T = T + T
        j = i + l
        r = T[i:j]
        r.reverse()
        T = T[:i] + r + T[j:]
        T = T[N : N + i] + T[i:N]
        i += l + s
        s += 1
    return i, s


def hard():
    global T
    T = list(range(N))
    t.extend([17, 31, 73, 47, 23])
    i = s = 0
    for _ in range(64):
        i, s = hash(i, s)
    r = map(lambda i: reduce(lambda a, b: a ^ b, T[i * 16 : i * 16 + 16], 0), range(16))
    print(("%02x" * 16) % tuple(r))


teststr = ""  # "AoC 2017"  # """3,4,1,5"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
N = 256  # 5
T = list(range(N))
if __name__ == "__main__":
    easy()
    t = read(1)
    hard()