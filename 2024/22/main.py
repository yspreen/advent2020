import numpy as np
import re
import pathlib
import json
from functools import reduce, cmp_to_key, cache
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
    return lmap(int, s)


def iterate(n, k=1):
    for _ in range(k):
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216
    return n


def easy():
    s = 0
    for n in t:
        s += iterate(n, 2000)
    print(s)


def hard():
    diffs_d = []

    for n in t:
        diffs = []
        for _ in range(2000):
            n_new = iterate(n)
            diffs.append(((n_new % 10) - (n % 10), n_new % 10))
            n = n_new

        diff_d = {}
        diffs_d.append(diff_d)
        for i in range(len(diffs) - 3):
            seq = tuple([d for d, n in diffs[i : i + 4]])

            diff_d[seq] = diff_d.get(seq, diffs[i + 3][1])

    diff_keys = set()
    for d in diffs_d:
        for k in d.keys():
            diff_keys.add(k)

    max_v = 0, None
    for diff in diff_keys:
        value = sum([d.get(diff, 0) for d in diffs_d])
        if value > max_v[0]:
            max_v = value, diff
    print(max_v[0])


teststr = """1
2
3
2024"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
