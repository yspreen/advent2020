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


def sint(v):
    try:
        return int(v)
    except:
        return v


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(lambda r: lmap(sint, r.split(" ")), s.splitlines())


def easy():
    R = {k: 0 for k in ascii_lowercase[:16]}
    sound = i = 0
    while True:
        r = t[i]
        o = 1
        a = r[1]
        if isinstance(a, str) and r[0] == "jgz":
            a = R[a]
        if len(r) > 2:
            b = r[2]
            if isinstance(b, str):
                b = R[b]
        if r[0] == "snd":
            sound = R[a]
        if r[0] == "set":
            R[a] = b
        if r[0] == "add":
            R[a] += b
        if r[0] == "mul":
            R[a] *= b
        if r[0] == "mod":
            R[a] %= b
        if r[0] == "rcv" and a != 0:
            return print(sound)
        if r[0] == "jgz" and a > 0:
            o = b
        i += o


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()