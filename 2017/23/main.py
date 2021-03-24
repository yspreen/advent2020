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


def sint(v):
    try:
        return int(v)
    except:
        return v


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(lambda r: lmap(sint, r.split(" ")), s.splitlines())


class VM:
    def __init__(self, id=0):
        self.R = {k: 0 for k in ascii_lowercase[:16]}
        self.i = 0
        # self.sound = 0
        # self.R["p"] = id
        # self.buf = []
        # self.locked = False
        self.mul_count = 0

    def step(self, rcv=None, part_one=False):
        self.locked = False
        # if rcv is not None:
        #     self.buf.append(rcv)
        r = t[self.i]
        o = 1
        a = r[1]
        # v = None
        if isinstance(a, str) and r[0] == "jnz":
            a = self.R[a]
        if len(r) > 2:
            b = r[2]
            if isinstance(b, str):
                b = self.R[b]
        # if r[0] == "snd":
        #     if part_one:
        #         self.sound = self.R[a]
        #     else:
        #         self.sound += 1
        #         v = self.R[a]
        if r[0] == "set":
            self.R[a] = b
        if r[0] == "add":
            self.R[a] += b
        if r[0] == "sub":
            self.R[a] -= b
        if r[0] == "mul":
            self.mul_count += 1
            self.R[a] *= b
        if r[0] == "mod":
            self.R[a] %= b
        # if r[0] == "rcv":
        #     if part_one and a != 0:
        #         print(self.sound)
        #         return 1
        #     if not part_one:
        #         if not self.buf:
        #             self.locked = True
        #             return
        #         self.R[a] = self.buf.pop(0)
        if r[0] == "jnz" and a != 0:
            o = b
        self.i += o
        return True if self.i >= N else None
        # return v


def easy():
    v = VM()
    while not v.step():
        continue
    print(v.mul_count)


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
N = len(t)
if __name__ == "__main__":
    easy()
    hard()