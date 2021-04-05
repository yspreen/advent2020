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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(list, s)


def easy():
    s = ""
    for letter in list(zip(*t)):
        m = (0, 0)
        for c in ascii_lowercase:
            count = letter.count(c)
            if count > m[0]:
                m = (count, c)
        s += m[1]
    print(s)


def hard():
    s = ""
    for letter in list(zip(*t)):
        m = (inf, 0)
        for c in ascii_lowercase:
            count = letter.count(c)
            if count < m[0]:
                m = (count, c)
        s += m[1]
    print(s)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()