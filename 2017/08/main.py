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


def trn(r):
    if r not in R:
        R.append(r)
        T.append(0)
    return R.index(r)


def lt(a, b):
    return a < b


def le(a, b):
    return a <= b


def gt(a, b):
    return a > b


def ge(a, b):
    return a >= b


def eq(a, b):
    return a == b


def nq(a, b):
    return a != b


def ins(s):
    c = s.split(" if ")[1]
    a = trn(s.split(" ")[0])
    b = trn(c.split(" ")[0])
    m = {">": gt, "<": lt, ">=": ge, "<=": le, "==": eq, "!=": nq}[c.split(" ")[1]]
    k = int(c.split(" ")[2])
    v = int(s.split(" ")[2])
    v = -v if s.split(" ")[1] == "dec" else v

    return (a, v, b, m, k)


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(ins, s.splitlines())


def op(var_a, const_a, var_b, method, const_b):
    if not method(T[var_b], const_b):
        return
    T[var_a] += const_a


def easy():
    for o in t:
        op(*o)
    print(max(T))


def hard():
    m = -inf
    for i in range(len(T)):
        T[i] = 0
    for o in t:
        op(*o)
        m = max(T + [m])
    print(m)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
R = []
T = []
t = read()
if __name__ == "__main__":
    easy()
    hard()