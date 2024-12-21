import numpy as np
import re
import pathlib
import json
from functools import reduce, cmp_to_key
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).split("\n\n")
    return s[0].split(", "), s[1].splitlines()


def has_prefix(string, patterns):
    for p in patterns:
        if p.startswith(string):
            return True
    return False


def easy():
    patterns = t[0]
    designs = t[1]
    possible = 0

    for line in designs:
        cursors = set([""])
        for i, c in enumerate(line):
            new_cursors = set()
            for old_string in cursors:
                string = old_string + c
                if string in patterns:
                    new_cursors.add("")
                if has_prefix(string, patterns):
                    new_cursors.add(string)
            cursors = new_cursors
        possible += 1 if any(string == "" for string in cursors) else 0

    print(possible)


def hard():
    patterns = t[0]
    designs = t[1]
    possible = 0

    for line in designs:
        cursors = {"": 1}
        for i, c in enumerate(line):
            new_cursors = {}
            for old_string, count in cursors.items():
                string = old_string + c
                if string in patterns:
                    new_cursors[""] = new_cursors.get("", 0) + count
                if has_prefix(string, patterns):
                    new_cursors[string] = new_cursors.get(string, 0) + count
            cursors = new_cursors
        possible += cursors.get("", 0)

    print(possible)


teststr = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
