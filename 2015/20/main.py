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
        return (f.read() if teststr == "" else teststr).splitlines()[0]


import itertools


def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


def presents(x):
    sq = int(sqrt(x)) + 1
    values = [1, x]
    for prime in erat2():
        if prime > sq:
            break
        val = prime
        while True:
            if val >= x or x % val > 0:
                break
            values.append(val)
            val += prime
    return sum(values) * 10


def easy():
    for i in range(int(9e9)):
        if presents(i) >= t:
            return print(i)


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = int(read())
if __name__ == "__main__":
    easy()
    hard()
