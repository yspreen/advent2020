import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr

    brd, ins = s.split("\n\n")
    brd = brd.splitlines()[:-1]
    ins = re.sub(r"[a-z]+ ", "", ins).splitlines()
    brd = lmap(lambda l: l[1::4], brd)
    brd = lmap(list, zip(*brd))
    for line in brd:
        line.reverse()
        while line[-1] == " ":
            line.pop()
    ins = lmap(lambda l: lmap(int, l.split(" ")), ins)
    return brd, ins


def easy():
    brd, ins = deepcopy(t[0]), deepcopy(t[1])

    for amount, before, after in ins:
        for _ in range(amount):
            item = brd[before - 1].pop()
            brd[after - 1].append(item)

    print("".join(lmap(lambda i: i[-1], brd)))


def hard():
    brd, ins = deepcopy(t[0]), deepcopy(t[1])

    for amount, before, after in ins:
        buffer = []
        for _ in range(amount):
            item = brd[before - 1].pop()
            buffer.insert(0, item)
        brd[after - 1] += buffer

    print("".join(lmap(lambda i: i[-1], brd)))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
