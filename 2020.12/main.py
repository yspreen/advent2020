import numpy as np
import re
import pathlib
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")

lookup = {
    "N": (-1, 0, 0, 0),
    "E": (0, 1, 0, 0),
    "S": (1, 0, 0, 0),
    "W": (0, -1, 0, 0),
    "L": (0, 0, -1, 0),
    "R": (0, 0, 1, 0),
    "F": (0, 0, 0, 1),
}
angle = {
    0: "N",
    90: "E",
    180: "S",
    270: "W",
}


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().replace("\r", "")
    t = t.split("\n")
    if t[-1] == "":
        t.pop()
    t = [(l[0], int(l[1:])) for l in t]

    return t


t = read()


def move(i, p):
    movement, param = t[i]
    vector = lookup[movement]
    p[2] += param * vector[2]
    p[2] = (p[2] + 360) % 360
    if vector[3]:
        forward = lookup[angle[p[2]]]
        p[0] += param * vector[3] * forward[0]
        p[1] += param * vector[3] * forward[1]
    else:
        p[0] += param * vector[0]
        p[1] += param * vector[1]


def easy():
    global t

    pos = [0, 0, 90]

    for i in range(len(t)):
        move(i, pos)
    print(sum(map(abs, pos[:2])))


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
