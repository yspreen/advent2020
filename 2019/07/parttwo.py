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


STOP = -1


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
            b = self.t[i + 2]
            c = self.t[i + 3]
            if mode_a == 0 and ins != 3:
                a = self.t[a]
            if mode_b == 0:
                b = self.t[b]
        except:
            # end of t.
            pass

        if ins == 99:
            return STOP
        if ins == 1:
            self.t[c] = a + b
            return 4
        if ins == 2:
            self.t[c] = a * b
            return 4
        if ins == 3:
            self.t[a] = self.inputs.pop(0)
            return 2
        if ins == 4:
            self.outputs.append(a)
            if self.loop_mode:
                self.i += 2
                return STOP
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
        self.d = 0
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


class LoopVM:
    def __init__(self, *inp):
        super().__init__(*inp)
        self.loop_mode = True


def amp(*param):
    a = 0
    for p in param:
        a = VM(p, a).calc()[0]
    return a


def hard():
    m = (0, 0)
    for p in permutations(range(5)):
        a = amp(*p)
        if a > m[0]:
            m = (a, p)
    print(*m)
    return


if __name__ == "__main__":
    hard()