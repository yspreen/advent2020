import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product, combinations
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
import cvxpy as cp


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(int, s)


def subsetSum(li, comb, sums):
    for i in range(len(li) + 1):
        for subset in combinations(li, i):
            comb.append(list(subset))
            sums.append(sum(subset))


def calcSubsets(n, arr, x):
    arr1, arr2 = arr[: n // 2], arr[n // 2 :]
    comb1, sums1 = [], []
    subsetSum(arr1, comb1, sums1)
    comb2, sums2 = [], []
    subsetSum(arr2, comb2, sums2)
    for i in range(len(sums1)):
        for j in range(len(sums2)):
            if sums1[i] + sums2[j] == x:
                yield comb1[i] + comb2[j]


def balance(k):
    sets = calcSubsets(len(t), t, sum(t) // k)
    m, shortest = 9e9, []
    for s in sets:
        l = len(s)
        if l == m:
            shortest.append(s)
        if l < m:
            shortest, m = [s], l
    print(min([prod(s) for s in shortest]))


def easy():
    balance(3)


def hard():
    balance(4)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
