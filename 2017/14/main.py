import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product


def lmap(*a):
    return list(map(*a))


def hash(s, N=256):
    T = list(range(N))
    t = lmap(ord, s)
    t.extend([17, 31, 73, 47, 23])
    i = s = 0
    for _ in range(64):
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
    r = map(lambda i: reduce(lambda a, b: a ^ b, T[i * 16 : i * 16 + 16], 0), range(16))
    return ("%02x" * 16) % tuple(r)


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return s


def count_binary(n):
    if n == 0:
        return 0
    return (n & 1) + count_binary(n // 2)


def easy():
    global A
    for i in range(128):
        A += [[]]
        h = hash("%s-%d" % (t, i))
        for j in h:
            A[-1] += vect_binary(int(j, 16))
    A = np.array(A, np.int)
    print(A.sum())


def vect_binary(n):
    return lmap(int, "{0:04b}".format(n))


class Group:
    items = {}
    keys = set()

    def __init__(self, tupl):
        self.tupl = tupl
        self.members = set([tupl])

    @classmethod
    def merge(cls, a, b):
        g = cls.items[a]
        g.members |= cls.items[b].members
        for i in cls.items[b].members:
            cls.items[i] = g


def hard():
    Group.items = {t: Group(t) for t in zip(*np.where(A))}
    Group.keys = set(Group.items.keys())

    for i in Group.keys:
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            j = (i[0] + x, i[1] + y)
            if j in Group.keys:
                Group.merge(i, j)
    print(len(set(Group.items.values())))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
A = []
if __name__ == "__main__":
    easy()
    hard()