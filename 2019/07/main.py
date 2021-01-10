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


STOP = -1.337


class VM:
    def read(self):
        with open(DIR / "input.txt") as f:
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
            return STOP
        if ins == 1:
            self.t[c] = a + b
            return 4
        if ins == 2:
            self.t[c] = a * b
            return 4
        if ins == 3:
            if self.loop_mode and not self.inputs:
                return STOP
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
        while self.d != STOP:
            self.i += self.d
            self.d = self.op(self.i)
        return self.outputs

    def __init__(self, *inp):
        self.read()
        self.outputs = []
        self.inputs = list(inp)

        self.i = self.d = 0
        self.loop_mode = False
        self.done = False


class LoopVM(VM):
    def __init__(self, *inp):
        super().__init__(*inp)
        self.loop_mode = True


def hard_amp(*param):
    vms = [LoopVM(p) for p in param]
    vms[0].inputs.append(0)
    n = len(param)
    i = 0
    E = []
    while True:
        a = vms[i].calc()
        if i + 1 == n:
            E.extend(a)
            if vms[i].done:
                return E[-1]
        i += 1
        i %= n
        vms[i].inputs.extend(a)


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