import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify


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
    I -= a
    E = ("%s-%d" % (E, a)).replace("--", "+")


def incr(a):
    global E, I
    I *= a
    E = "(%s)*%d" % (E, a)


def new_stack(_=0):
    global E, I
    I = -I - 1
    E = "-1*(%s)-1" % E


def easy():
    global I
    I = 2019
    allsteps()
    print(I % N)


def allsteps():
    for op, param in t:
        op(param)


def hard():
    global I, E, N
    I = 2020
    N = 119315717514047
    E = "x"
    allsteps()
    E = str(simplify(E))
    b = int(E.split("x")[-1].replace(" ", "")) % N
    a = int(E.split("*")[0].replace(" ", "")) % N
    dic = {I: 1, 2020: 0}
    print(a)
    print(b)
    print(I % N)
    # print((a ** N) % N)
    i = 0
    while True:
        I = (a * I + b) % N
        i += 1
        if dic.get(I, None) is not None:
            print(dic[I])
            break
        dic[I] = i
    print(I)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
E = I = N = 10007

if __name__ == "__main__":
    easy()
    hard()
    # for i in [3, 7, 9]:
    #     A = list(range(N))
    #     incr(i)
    #     print(i, A)
    #     print()
