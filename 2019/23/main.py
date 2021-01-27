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
    items = {}

    def read(self):
        with open(DIR / "input.txt") as f:
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
                self.inputs = [-1]
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
        a, x, y = self.outputs
        self.outputs = []
        if a == 255:
            return y
        self.items[a].inputs.extend([x, y])

    def step(self, *inp):
        if self.done:
            return
        self.inputs.extend(inp)
        self.d = self.op(self.i)
        self.i += 0 if self.d is None else self.d
        return self.draw()

    def __init__(self, addr=0):
        self.read()
        self.outputs = []
        self.inputs = [addr]

        self.addr = addr
        self.items[addr] = self
        self.i = self.d = self.r = 0
        self.done = False


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
vs = [VM(i) for i in range(50)]


def easy():
    while True:
        for v in vs:
            i = v.step()
            if i is not None:
                return print(i)


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
