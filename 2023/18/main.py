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
import math


def read():
    with open(DIR / "input") as f:
        s = (
            (f.read() if teststr == "" else teststr)
            .replace("(", "")
            .replace(")", "")
            .splitlines()
        )
    return lmap(lambda r: lmap(maybeint, r.split(" ")), s)


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def calculate_polygon_area(points):
    n = len(points)
    area = 0.0

    for i in range(n - 1):
        area += points[i][0] * points[i + 1][1]
        area -= points[i + 1][0] * points[i][1]

    area = abs(area) / 2.0
    return area + calculate_perimeter(points) / 2 + 1


def calculate_distance(point1, point2):
    """Calculate the distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def calculate_perimeter(points):
    """Calculate the perimeter of the polygon."""
    perimeter = 0.0
    n = len(points)

    for i in range(n - 1):
        perimeter += calculate_distance(points[i], points[i + 1])

    return perimeter


def easy():
    p = (0, 0)
    ps = [p]

    for d, c, _ in t:
        for _ in range(c):
            p = (p[0] + mv[d][0], p[1] + mv[d][1])
        ps.append(p)
    print(int(calculate_polygon_area(ps)))


def hard():
    p = (0, 0)
    ps = [p]

    for _, _, code in t:
        d = {"0": "R", "1": "D", "2": "L", "3": "U"}[code[-1]]
        c = int(code[1:-1], 16)
        for _ in range(c):
            p = (p[0] + mv[d][0], p[1] + mv[d][1])
        ps.append(p)
    print(int(calculate_polygon_area(ps)))


teststr = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
