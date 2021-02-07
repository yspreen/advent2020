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


def op(o, i):
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
    s = re.sub(r"\[%d\]" % ip, "$P", s)
    s = re.sub(r"\[0\]", "$0", s)
    s = re.sub(r"\[1\]", "$a", s)
    s = re.sub(r"\[2\]", "$b", s)
    s = re.sub(r"\[3\]", "$c", s)
    s = re.sub(r"\[4\]", "$d", s)
    s = re.sub(r"\[5\]", "$e", s)
    s = re.sub(r"\$P = \$P \+ \$(.)", r"SKIP if $\1", s)
    s = re.sub(r"\$P = \$(.) \+ \$P", r"SKIP if $\1", s)
    if "=" in s:
        s = s.split("=")
        s[1] = s[1].replace("$P", str(i))
        if re.match(r"^(\s|\+|\d)+$", s[1]):
            s[1] = " " + str(
                sum(map(int, filter(None, s[1].replace("+", "0").split(" "))))
            )
        if re.match(r"^(\s|\*|\d)+$", s[1]):
            s[1] = " " + str(
                prod(map(int, filter(None, s[1].replace("*", "1").split(" "))))
            )
        s = "=".join(s)
    s = re.sub(r"(.+) = (.+) \+ \1", r"\1 += \2", s)
    s = re.sub(r"(.+) = \1 \+ (.+)", r"\1 += \2", s)
    s = re.sub(r"(.+) = (.+) \* \1", r"\1 *= \2", s)
    s = re.sub(r"(.+) = \1 \* (.+)", r"\1 *= \2", s)
    s = re.sub(r"\$P = (\d+)", r"GOTO \1", s)
    if "GOTO" in s:
        s = "GOTO " + str(int(s[5:]) + 1)
    print("%3d: %s" % (i, s))


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
    # print("#ip %d" % ip)
    for i, o in enumerate(t):
        op(o, i)
