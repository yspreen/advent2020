import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().splitlines()
    return [(op(i), int(i.replace("stack", "0").split(" ")[-1])) for i in t]


def op(s):
    for i, c in enumerate(["new", "incr", "cut"]):
        if c in s:
            return [new_stack, incr, cut][i]


def cut(a):
    global A
    A = A[a % N :] + A[: a % N]


def incr(a):
    global A

    A_ = [0 for _ in A]
    for i in range(N):
        A_[i * a % N] = A[i]
    A = A_


def new_stack(_=0):
    A.reverse()


def easy():
    for op, param in t:
        op(param)
    print(A.index(2019))


def hard():
    return


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
N = 10007
A = list(range(N))

if __name__ == "__main__":
    easy()
    hard()
    # for i in [3, 7, 9]:
    #     A = list(range(N))
    #     incr(i)
    #     print(i, A)
    #     print()
