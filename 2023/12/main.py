import numpy as np
import re
import pathlib
import json
from functools import reduce, cache
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: (r.split(" ")[0], lmap(int, r.split(" ")[1].split(","))), s)


def possible(pattern, string):
    return re.match()


def dict_add(dict, key, val):
    dict[key] = dict.get(key, 0) + val


def calc(pattern, counts):
    teststr = ".".join("".join("#" for _ in range(count)) for count in [0, *counts, 0])
    endpos = len(teststr) - 1
    possibilities = {0: 1}
    new_possibilities = {}
    for c in pattern:
        for pos, count in possibilities.items():
            if c == "." or c == "?":
                if teststr[pos] == ".":
                    dict_add(new_possibilities, pos, count)
                elif pos <= endpos and teststr[pos + 1] == ".":
                    dict_add(new_possibilities, pos + 1, count)
            if c == "#" or c == "?":
                if pos < endpos and teststr[pos + 1] == "#":
                    dict_add(new_possibilities, pos + 1, count)
        possibilities = new_possibilities
        new_possibilities = {}
    return possibilities.get(endpos - 1, 0) + possibilities.get(endpos, 0)


def easy():
    count = 0
    for pattern, counts in t:
        count += calc(pattern, counts)
    print(count)


def hard():
    count = 0
    for line, nums in t:
        line = f"{line}?{line}?{line}?{line}?{line}"
        nums = nums + nums + nums + nums + nums
        count += calc(line, nums)
    print(count)


teststr = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
