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

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
VID = "n"


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


directions = [
    (-1, 0),  # u
    (0, 1),  # r
    (1, 0),  # d
    (0, -1),  # l
]
vac = [94, 62, 118, 60]


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
        if len(self.outputs) != 1 or self.outputs[0] > 1000:
            return
        char = self.outputs.pop()
        if self.move_vacs and VID == "y":
            if self.l == 10 and char == 10:
                self.pos[0] = -1
                pprint(self.A)
            self.l = char
        if char == 10:
            self.pos[0] += 1
            self.pos[1] = 0
        else:
            self.A[tuple(self.pos)] = 0 if char == 46 else 1
            if self.move_vacs:
                self.A[tuple(self.pos)] = char
            if char in vac:
                self.v = [i for i in self.pos]
                self.h = vac.index(char)
            self.pos[1] += 1
        if not (self.pos[0] < self.A.shape[0] and self.pos[1] < self.A.shape[1]):
            self.pad()

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

    def __init__(self, move_vacs=False):
        self.read()
        self.outputs = []
        self.inputs = []

        self.h = self.l = self.i = self.d = self.r = 0
        self.A = np.zeros((2, 2), np.int32)
        self.pos = [0, 0]
        self.v = [0, 0]
        self.done = False
        self.move_vacs = move_vacs
        self.t[0] = 2 if move_vacs else 1

    @property
    def direction(self):
        return directions[self.h % 4]


v = VM()


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


def easy():
    v.calc()
    B = np.zeros((3, 3), np.int32)
    for i, j in product(range(3), range(3)):
        B[i, j] = 1 if i == 1 or j == 1 else 0
    print(sum(map(lambda a: (a[0] + 1) * (a[1] + 1), find_match(v.A, B))))


def nextpos(A, p, h):
    h = directions[h]
    return A[p[0] + h[0], p[1] + h[1]]


def move(p, h):
    p[0] += directions[h][0]
    p[1] += directions[h][1]


def count(a, b):
    r = 0
    for i in range(len(a) - len(b) + 1):
        r += 1 if b == a[i : i + len(b)] else 0
    return r


def hard():
    l = 0
    program = []
    ended = False
    while not ended:
        if nextpos(v.A, v.v, v.h) == 1:
            move(v.v, v.h)
            l += 1
            continue
        if l or program:
            program.append(str(l))
        l = 0
        if nextpos(v.A, v.v, (v.h + 1) % 4) == 1:
            program.append("R")
            v.h = (v.h + 1) % 4
        elif nextpos(v.A, v.v, (v.h - 1) % 4) == 1:
            program.append("L")
            v.h = (v.h - 1) % 4
        else:
            ended = True

    program_ = [i for i in program]
    subs = []
    for A in ["A", "B", "C"]:
        candidates = []
        for i in range(len(program) - 1):
            for j in range(i + 2, len(program) + 1):
                sub = program[i:j]
                c = count(program, sub)
                if len(",".join(sub)) > 20 or "A" in sub or "B" in sub:
                    break
                candidates.append(((c ** 0.5) * (j - i), program[i:j]))
                if c < 2:
                    break
        candidates.sort(key=lambda i: i[0])
        sub = ",".join(candidates[-1][-1])
        subs.append(sub)
        program = ",".join(program).replace(sub, A).split(",")

    program = ",".join(program)
    program = [ord(i) for i in ("\n".join([program] + subs) + "\n%s\n" % VID)]
    print(VM(True).calc(*program)[-1])


if __name__ == "__main__":
    easy()
    hard()
