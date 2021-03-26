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
    r = []
    for l in s:
        c = l.split("-")[-1]
        l = l[: -len(c) - 1]
        r.append((l, int(c.split("[")[0]), c.split("[")[1][:-1]))
    return r


def decrypt(line, off):
    s = ""
    for c in line:
        if c == "-":
            s += " "
            continue
        c = ord(c)
        c -= 97
        c += off
        c %= 26
        c += 97
        s += chr(c)
    return s


def easy():
    count = pole = 0
    for line, number, check in t:
        chars = {}
        for c in line.replace("-", ""):
            chars[c] = chars.get(c, 0) + 1
        chars = list(chars.items())
        chars.sort(key=lambda i: i[0])
        chars.sort(key=lambda i: -i[1])
        chars = "".join([i[0] for i in chars[:5]])
        if chars == check:
            count += number
            if decrypt(line, number) == "northpole object storage":
                pole = number
    print(count, pole, sep="\n")


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()