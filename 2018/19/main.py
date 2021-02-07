import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols, solve


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().splitlines()
    return t[0], [[i[:4], *map(int, i[5:].split(" "))] for i in t[1:]]


def op(o):
    code, A, B, C = o

    if code == "addr":
        s = "[%d] = [%d] + [%d]" % (C, A, B)
    if code == "addi":
        s = "[%d] = [%d] + %d" % (C, A, B)
    if code == "mulr":
        s = "[%d] = [%d] * [%d]" % (C, A, B)
    if code == "muli":
        s = "[%d] = [%d] * %d" % (C, A, B)
    if code == "banr":
        s = "[%d] = [%d] & [%d]" % (C, A, B)
    if code == "bani":
        s = "[%d] = [%d] & %d" % (C, A, B)
    if code == "borr":
        s = "[%d] = [%d] | [%d]" % (C, A, B)
    if code == "bori":
        s = "[%d] = [%d] | %d" % (C, A, B)
    if code == "setr":
        s = "[%d] = [%d]" % (C, A)
    if code == "seti":
        s = "[%d] = %d" % (C, A)
    if code == "gtir":
        s = "[%d] = %d > [%d]" % (C, A, B)
    if code == "gtri":
        s = "[%d] = [%d] > %d" % (C, A, B)
    if code == "gtrr":
        s = "[%d] = [%d] > [%d]" % (C, A, B)
    if code == "eqir":
        s = "[%d] = %d == [%d]" % (C, A, B)
    if code == "eqri":
        s = "[%d] = [%d] == %d" % (C, A, B)
    if code == "eqrr":
        s = "[%d] = [%d] == [%d]" % (C, A, B)
    print(s)


def fact(N):
    n = 0
    for a in range(N):
        if N % (a + 1) == 0:
            n += a + 1
    print(n)


def easy():
    fact(945)


def hard():
    fact(10188465)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
ip, t = read()
ip = int(ip[4])
reg = [0] * 6


if __name__ == "__main__":
    easy()
    hard()
