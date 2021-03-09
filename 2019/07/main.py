import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


class VM:
    def read(self):
        with open(DIR / "input") as f:
            t = f.read().replace("\n", "").split(",")
        if t[-1] == "":
            t.pop()
        self.t = [int(i) for i in t]

    def op(self, i):
        code = self.t[i]
        ins = code % 100
        mode_a = digit(code, 2)
        mode_b = digit(code, 3)
        mode_c = digit(code, 4)

        try:
            a = self.t[i + 1]
            if mode_a == 0 and ins != 3:
                a = self.t[a]
            b = self.t[i + 2]
            if mode_b == 0:
                b = self.t[b]
            c = self.t[i + 3]
        except:
            # end of t.
            pass

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
            if not self.inputs:
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

    def calc(self):
        if self.done:
            return []
        self.d = 0
        self.outputs = []
        while self.d is not None:
            self.i += self.d
            self.d = self.op(self.i)
        return self.outputs

    def __init__(self, *inp):
        self.read()
        self.outputs = []
        self.inputs = list(inp)

        self.i = self.d = 0
        self.done = False


def hard_amp(*param):
    vms = [VM(p) for p in param]
    n = len(param)
    i = 0
    a = [0]
    while True:
        vms[i].inputs.extend(a)
        a = vms[i].calc()
        if i + 1 == n and vms[i].done:
            return a[-1]
        i = (i + 1) % n


def solve(func, offset=0):
    m = (0, 0)
    for p in permutations(range(offset, offset + 5)):
        a = func(*p)
        if a > m[0]:
            m = (a, p)
    print(*m)


def easy_amp(*param):
    a = 0
    for p in param:
        a = VM(p, a).calc()[0]
    return a


if __name__ == "__main__":
    solve(easy_amp)
    solve(hard_amp, 5)