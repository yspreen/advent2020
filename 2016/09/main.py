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


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def easy():
    front, back = "", t
    while back:
        if back[0] != "(":
            front, back = front + back[0], back[1:]
        else:
            bracket, back = back[1:].split(")", 1)
            x, y = map(int, bracket.split("x"))
            bracket, back = back[:x], back[x:]
            # back = y * bracket + back
            front += y * bracket
    print(len(front))


def hard():
    is_group = False
    values = []
    i = 0
    for c in t:
        if c == "(":
            is_group = True
        values.append(0 if is_group else 1)
        if c == ")":
            is_group = False
    while i < len(t):
        c = t[i]
        i += 1
        if c != "(":
            continue
        bracket = t[i:].split(")")[0]
        i += len(bracket) + 1
        x, y = map(int, bracket.split("x"))
        for j in range(i, i + x):
            values[j] *= y
    print(sum(values))


teststr = ""  # """(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()