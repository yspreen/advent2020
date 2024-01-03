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
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return s.split(",")


def maybeint(line):
    try:
        return int(line)
    except:
        return line


def hash(string):
    h = 0
    for c in string:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def easy():
    print(sum(hash(s) for s in t))


def hard():
    boxes = [[] for _ in range(256)]
    for line in t:
        has_dash = line.endswith("-")
        if has_dash:
            label = line[:-1]
        else:
            label = line.split("=")[0]
            amount = int(line.split("=")[1])
        box = hash(label)
        if has_dash:
            boxes[box] = list(filter(lambda i: i[0] != label, boxes[box]))
        else:
            if label in map(lambda i: i[0], boxes[box]):
                idx = list(map(lambda i: i[0], boxes[box])).index(label)
                boxes[box][idx] = (label, amount)
            else:
                boxes[box].append((label, amount))
    v = 0
    for box_no, box in enumerate(boxes, 1):
        for lens_no, lens in enumerate(box, 1):
            v += box_no * lens_no * lens[1]
    print(v)


teststr = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
