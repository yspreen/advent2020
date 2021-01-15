import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product


def getkey():
    paddle = tiles.index("=")
    ball = tiles.index("o")

    try:
        paddle = np.where(v.A == paddle)[1][0]
        ball = np.where(v.A == ball)[1][0]

        if paddle < ball:
            return 1
        if paddle > ball:
            return -1
    except:
        pass
    return 0


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")

tiles = [" ", "#", "x", "=", "o"]


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


class VM:
    def read(self):
        with open(DIR / "input.txt") as f:
            t = f.read().replace("\n", "").split(",")
        if t[-1] == "":
            t.pop()
        t = [int(i) for i in t]
        self.t = {i: v for i, v in enumerate(t)}

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
        if len(self.outputs) != 3:
            return
        y, x, color = self.outputs
        x += 2
        self.outputs = []
        while not (x < self.A.shape[0] and y < self.A.shape[1]):
            self.pad()
        if (y, x) == (-1, 2):
            self.score = color
        else:
            self.A[x, y] = color
            if tiles[color] == "x":
                self.blocks += 1

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

    def pad(self):
        n = self.A.shape[0]
        self.A = np.pad(self.A, ((0, n), (0, n)))

    def __init__(self):
        self.read()
        self.t[0] = 2
        self.outputs = []
        self.inputs = []

        self.score = self.blocks = self.i = self.d = self.r = 0
        self.A = np.zeros((2, 2), np.int32)
        self.done = False

    def print(self):
        import os

        os.system("clear")
        for r in self.A:
            for i in r:
                print(tiles[i], end="")
            print()

    def trim(self):
        while self.A[-3:, :].sum() == 0:
            self.A = self.A[:-1, :]
        while self.A[:, -3:].sum() == 0:
            self.A = self.A[:, :-1]


v = VM()


def easy():
    v.calc()
    print(v.blocks)
    input()


def hard():
    from time import sleep

    v.trim()
    while not v.done:
        v.print()
        sleep(0.001)
        v.calc(getkey())
    print(v.score)


if __name__ == "__main__":
    easy()
    hard()
