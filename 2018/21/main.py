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


def test():
    s = set()
    a = b = c = d = z = i = 0
    while True:
        b = c | A
        c = C
        while True:
            a = b & 255
            c += a
            c &= D
            c *= B
            c &= D
            if b < 256:
                if i == 0:
                    print(c)
                if c in s:
                    print(d)
                    return
                d = c
                i = 1
                s.add(c)
                break
            else:
                b = b // 256


def easy():
    return


def hard():
    test()


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
_, t = read()
A = t[6][2]
B = t[11][2]
C = t[7][1]
D = t[10][2]
reg = [0] * 6


if __name__ == "__main__":
    easy()
    hard()