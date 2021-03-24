import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product, count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


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
        if r[0] == "sub":
            self.R[a] -= b
        if r[0] == "mul":
            self.mul_count += 1
            self.R[a] *= b
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


def print_op(o, i):
    code, A, B = o
    sa = ("$%s" % A.upper()) if isinstance(A, str) else str(A)
    sb = ("$%s" % B.upper()) if isinstance(B, str) else str(B)

    jumps = []
    if code == "sub":
        s = "%s -= %s" % (sa, sb)
    if code == "mul":
        s = "%s *= %s" % (sa, sb)
    if code == "set":
        s = "%s = %s" % (sa, sb)
    if code == "jnz":
        s = "GOTO %s" % (B + i)
        if B + i >= N:
            s = "End."
        else:
            jumps = [(B + i, i)]
        if sa != "1":
            s += " IF %s != 0" % sa
    s = s.replace("-= -", "+= ")
    return jumps, "%3d:  %s" % (i, s)


def reverse_code():
    S, J = [], []
    for i, o in enumerate(t):
        # S.append(print_op(o, i))
        j, s = print_op(o, i)
        J.extend(j)
        S.append(["   ", s])
    for j, o in J:
        S[j][0] = "%2d>" % o
    for pre, s in S:
        print(pre, s)


def hard():
    # reverse_code()
    c = 0
    for i in range(108400, 125400 + 1)[::17]:
        if not is_prime(i):
            c += 1
    print(c)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
N = len(t)
if __name__ == "__main__":
    # easy()
    hard()