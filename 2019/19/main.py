import numpy as np
import re
import pathlib
import json
import random
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product
from time import sleep


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


class VM:
    def read(self):
        with open(DIR / "input") as f:
            t = f.read().replace("\n", "").split(",")
        if t[-1] == "":
            t.pop()
        t = [int(i) for i in t]
        self.t = {i: v for i, v in enumerate(t)}
        self.t_ = dict(self.t)

    def op(self, i):
        code = self.t[i]
        ins = code % 100
        mode_a = digit(code, 2)
        mode_b = digit(code, 3)
        mode_c = digit(code, 4)

        a = self.t.get(i + 1, 0)
        if mode_a == 2:
            a += self.r
            mode_a = 0
        if mode_a == 0 and ins != 3:
            a = self.t.get(a, 0)
        b = self.t.get(i + 2, 0)
        if mode_b == 0:
            b = self.t.get(b, 0)
        if mode_b == 2:
            b = self.t.get(self.r + b, 0)
        c = self.t.get(i + 3, 0)
        if mode_c == 2:
            c += self.r

        if ins == 99:
            self.done = True
            return
        if ins == 1:
            self.t[c] = a + b
            return 4
        if ins == 2:
            self.t[c] = a * b
            return 4
        if ins == 3:
            if not len(self.inputs):
                return
            self.t[a] = self.inputs.pop(0)
            return 2
        if ins == 4:
            self.outputs.append(a)
            return 2
        if ins == 5:
            if a != 0:
                return b - i
            return 3
        if ins == 6:
            if a == 0:
                return b - i
            return 3
        if ins == 7:
            self.t[c] = 1 if a < b else 0
            return 4
        if ins == 8:
            self.t[c] = 1 if a == b else 0
            return 4
        if ins == 9:
            self.r += a
            return 2

    def draw(self):
        if len(self.outputs) != 1:
            return
        self.A[self.pos[1], self.pos[0]] = self.outputs.pop() + 1

    def check(self, pos):
        try:
            a = self.A[pos[1], pos[0]]
            assert a > 0
            return a
        except:
            pass
        self.pos = pos
        self.h = self.l = self.i = self.d = self.r = 0
        self.done = False
        self.t = dict(self.t_)
        while not (self.pos[0] < self.A.shape[0] and self.pos[1] < self.A.shape[1]):
            self.pad()
        self.calc(*pos)
        return self.A[pos[1], pos[0]]

    def calc(self, *inp):
        if self.done:
            return
        self.inputs.extend(inp)
        self.d = 0
        self.outputs = []
        while self.d is not None:
            self.i += self.d
            self.d = self.op(self.i)
            self.draw()
        return self.outputs

    def pad(self):
        n = self.A.shape[0]
        self.A = np.pad(self.A, ((0, n), (0, n)))

    def __init__(self):
        self.read()
        self.outputs = []
        self.inputs = []

        self.h = self.l = self.i = self.d = self.r = 0
        self.A = np.zeros((2, 2), np.int32)
        self.pos = [0, 0]
        self.done = False

    @property
    def direction(self):
        return directions[self.h % 4]


def find_match(A, B):
    matches = []
    n = A.shape[0] - B.shape[0]
    m = A.shape[1] - B.shape[1]
    for i, j in product(range(n + 1), range(m + 1)):
        B_ = np.pad(B, ((i, n - i), (j, m - j)))
        if (A - B_).min() == 0:
            matches.append((i, j))
    if matches:
        return matches


def pprint(t):
    t[t == ord(".")] = 0
    p = np.where(t != 0)
    t = t[min(p[0]) : max(p[0]) + 1, min(p[1]) : max(p[1]) + 1]

    for r in t:
        for e in r:
            print(chr(e) if e else " ", end="")
        print()


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
directions = [
    (-1, 0),  # u
    (0, 1),  # r
    (1, 0),  # d
    (0, -1),  # l
]
v = VM()


def top_right(A, n=-1):
    try:
        a = A[:, n]
        return (np.where(a == 2)[0][0], A.shape[1] + n)
    except:
        return top_right(A, n - 1)


def bottom_left(A, n=-1):
    try:
        a = A[n, :]
        return (A.shape[0] + n, np.where(a == 2)[0][0])
    except:
        return bottom_left(A, n - 1)


def easy():
    for i, j in product(*[range(50) for _ in range(2)]):
        v.check([i, j])
    v.A = v.A[:50, :50]
    print((v.A - 1).sum())


def hard():
    y_a, x_a = top_right(v.A)
    y_b, x_b = bottom_left(v.A)
    da = y_a / x_a
    db = y_b / x_b

    x_b_g = (-100 / da - 100) / (1 - db / da)
    y_b_g = x_b_g * db
    x_a_g = x_b_g + 100
    y_a_g = y_b_g - 100
    delta = x_a_g / 50 + 1
    x = int(x_b_g + 1)
    y = int(y_a_g + 1)

    while True:
        for mx, my in zip(
            (1, 0, 1, 2, 1),
            (0, 1, 1, 1, 2),
        ):
            x_, y_ = x - mx, y - my
            if v.check([x_ + 99, y_]) == v.check([x_, y_ + 99]) == 2:
                x, y = x_, y_
                break
            if (mx, my) == (1, 2):
                return print(x * 10000 + y)


if __name__ == "__main__":
    easy()
    hard()
