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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, r.replace(":", "").split(" ")), s)


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


def count_options(current_result, check, numbers):
    if not numbers:
        return 1 if current_result == check else 0
    if current_result > check:
        return 0
    return count_options(
        current_result + numbers[0], check, numbers[1:]
    ) + count_options(current_result * numbers[0], check, numbers[1:])


def count_more_options(current_result, check, numbers):
    if not numbers:
        return 1 if current_result == check else 0
    if current_result > check:
        return 0
    return (
        count_more_options(current_result + numbers[0], check, numbers[1:])
        + count_more_options(current_result * numbers[0], check, numbers[1:])
        + count_more_options(
            int(str(current_result) + str(numbers[0])), check, numbers[1:]
        )
    )


def easy():
    c = 0
    for line in t:
        check, numbers = line[0], line[1:]
        result, numbers = numbers[0], numbers[1:]
        if count_options(result, check, numbers) > 0:
            c += check
    print(c)


def hard():
    c = 0
    for line in t:
        check, numbers = line[0], line[1:]
        result, numbers = numbers[0], numbers[1:]
        if count_more_options(result, check, numbers) > 0:
            c += check
    print(c)


teststr = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
