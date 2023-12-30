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
        s = re.sub(r" +", " ", (f.read() if teststr == "" else teststr)).split("\n\n")
    s = lmap(lambda i: i.splitlines(), s)
    maps = lmap(lambda i: lmap(lambda j: lmap(int, j.split(" ")), i[1:]), s[1:])
    return (lmap(int, s[0][0].split(": ")[1].split(" ")), maps)


def get_row(x, data):
    low, high = 0, len(data) - 1
    result = None

    while low <= high:
        mid = (low + high) // 2
        if data[mid][1] <= x:
            result = data[mid]
            low = mid + 1
        else:
            high = mid - 1

    return result


def merge(seeds):
    idx = 0
    seeds.sort(key=lambda i: i[0])
    while idx < len(seeds) - 1:
        if seeds[idx][0] + seeds[idx][1] + 1 < seeds[idx + 1][0]:
            idx += 1
            continue
        seeds[idx] = (seeds[idx][0], seeds[idx][1] + seeds[idx + 1][1])
        del seeds[idx + 1]


def prepare_map(m, min_seed=0, max_seed=999999):
    m.sort(key=lambda i: i[1])
    if m[0][1] > min_seed:
        m.insert(0, (min_seed, min_seed, m[0][1] - min_seed))
    idx = -1
    while idx < len(m) - 2:
        idx += 1
        if m[idx][1] + m[idx][2] == m[idx + 1][1]:
            continue
        m.insert(
            idx + 1,
            (
                m[idx][1] + m[idx][2],
                m[idx][1] + m[idx][2],
                m[idx + 1][1] - m[idx][1] + m[idx][2],
            ),
        )
        idx += 1
    if m[-1][1] + m[-1][2] - 1 < max_seed:
        m.append(
            (
                m[-1][1] + m[-1][2],
                m[-1][1] + m[-1][2],
                max_seed - m[-1][1] - m[-1][2] + 1,
            )
        )


def easy():
    vals = [i for i in seeds]

    for s_map in t:
        prepare_map(s_map, min(vals), max(vals))
        for i in range(len(vals)):
            row = get_row(vals[i], s_map)
            vals[i] += row[0] - row[1]
    print(min(vals))


def hard():
    vals = list(zip([i for i in seeds[::2]], [i for i in seeds[1::2]]))

    for s_map in t:
        prepare_map(
            s_map,
            min(map(lambda i: i[0], vals)),
            max(map(lambda i: i[0] + i[1] - 1, vals)),
        )
        vals_, vals = vals, []
        for lower, count in vals_:
            upper = lower + count - 1
            while True:
                row = get_row(lower, s_map)
                row_upper = row[1] + row[2] - 1
                delta = row[0] - row[1]
                if row_upper >= upper:
                    vals.append((lower + delta, upper - lower + 1))
                    break
                vals.append((lower + delta, row_upper - lower + 1))
                lower = row_upper + 1
        merge(vals)
    print(min(map(lambda i: i[0], vals)))


teststr = """"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
seeds, t = read()
if __name__ == "__main__":
    easy()
    hard()
