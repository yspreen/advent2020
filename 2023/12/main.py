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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: (r.split(" ")[0], lmap(int, r.split(" ")[1].split(","))), s)


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
    (-1, 1),  # UR
    (1, 1),  # DR
    (-1, -1),  # UL
    (1, -1),  # DL
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
]


def BFS(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, 0)]
    visited = set([start])

    while options:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:  # lower bound check
                    continue
                if new_p[1] < 0:  # lower bound check
                    continue
                try:
                    assert can_walk(pos, new_p)
                except:
                    continue  # upper bound check
                if new_p in visited:
                    continue
                visited.add(new_p)
                cost_ = cost + cost_fn(pos, new_p)
                new_o.append((new_p, cost_))
                if goal(new_p):
                    return cost_
        options = new_o
    return None


def is_possible(line, nums):
    if line.count("#") > sum(nums):
        return False
    if line.count("#") + line.count("?") < sum(nums):
        return False
    is_set = list(filter(None, line.split("?")[0].split(".")))
    if not is_set:
        return True
    if len(is_set) > len(nums):
        return False
    for group, count in list(zip(is_set, nums))[:-1]:
        if len(group) != count:
            return False
    group, count = list(zip(is_set, nums))[-1]
    if len(group) == count:
        return True
    if len(group) > count:
        return False
    if len(group) < count:
        return "?" in line and line.split("?")[0].endswith("#")
    return True


def possibilities(line, nums, idx=0):
    # print(line)
    if idx == len(line):
        return 1 if is_possible(line, nums) else 0
    if line[idx] != "?":
        return possibilities(line, nums, idx + 1)
    if not is_possible(line, nums):
        return 0
    return possibilities(
        line[:idx] + "." + line[idx + 1 :], nums, idx + 1
    ) + possibilities(line[:idx] + "#" + line[idx + 1 :], nums, idx + 1)


def easy():
    arrange = 0
    for line, nums in t:
        arrange += possibilities(line, nums)
    print(arrange)


def hard():
    arrange = 0
    for line, nums in t:
        line = f"{line}?{line}?{line}?{line}?{line}"
        nums = nums + nums + nums + nums + nums
        arrange += possibilities(line, nums)
    print(arrange)


teststr = """?.??.??###??.#.?? 1,1,4,1,1"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
