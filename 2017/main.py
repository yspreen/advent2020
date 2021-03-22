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
    return lmap(lambda r: lmap(int, r.split("\t")), s)


def easy():
    return


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()