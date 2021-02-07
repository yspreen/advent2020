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


def easy():
    while not op():
        continue
    print(reg[0])


def hard():
    global reg

    reg = [0] * 6
    reg[0] = 1
    easy()


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
ip, t = read()
ip = int(ip[4])
reg = [0] * 6


if __name__ == "__main__":
    print("#ip %d" % ip)
    for o in t:
        op(o)
