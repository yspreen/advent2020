import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().splitlines()
    return [(op(i), int(i.replace("stack", "0").split(" ")[-1])) for i in t]


def op(s):
    for i, c in enumerate(["new", "incr", "cut"]):
        if c in s:
            return [new_stack, incr, cut][i]


def cut(a):
    global E, I
    I += a % N
    E = "%s+%d" % (E, (a % N))


def incr(a):
    global E, I
    if a == 0:
        return
    n = 0
    while (I / a) % 1 > 0:
        I += N
        n += N
    I //= a
    E = "(%s+%d)*%d" % (E, n, a)


def new_stack(_=0):
    global E, I
    I = -I - 1
    E = "-1*(%s)-1" % E


def easy():
    return


def allsteps(reverse=False):
    for op, param in reversed(t) if reverse else t:
        op(param)


def double(e):
    e = str(simplify(e))
    b = int(e.split("x")[-1].replace(" ", "")) % N
    a = int(e.split("*")[0].replace(" ", "")) % N
    return a * (a * symbols("x") + b) + b


def hard():
    global I, E, N
    I = 2020
    N = 119315717514047
    E = "x"
    allsteps(True)

    simple = simplify(E)
    M = 101741582076661
    I = 2020
    i = 0
    while M > 0:
        times = 1
        e = simple
        while times * 2 <= M:
            times *= 2
            e = double(e)
        M -= times
        I = e.subs(symbols("x"), I) % N
    print(I)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
E = I = N = 10007

if __name__ == "__main__":
    # easy()
    # hard()
    for i in [3, 7, 9]:
        N = 10
        A_ = list(range(N))
        B_ = list(range(N))
        for k in range(N):
            I = k
            E = "x"

            A = list(range(N))
            for j in range(N):
                A[j * i % N] = j
            A_[k] = A[I]

            incr(i)
            B_[k] = I
        print(i, A_)
        print(i, B_)
        print()
