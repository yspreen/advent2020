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
from scipy.optimize import minimize, rosen, rosen_der
import cvxpy as cp


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(",", "").splitlines()
    return lmap(
        lambda r: lmap(lambda i: int(r.split(" ")[i]), [2, 4, 6, 8, 10]),
        s,
    )


def score(x):
    # print(x)
    # if x < 0 or x > 100:
    #     return inf
    s = [0] * N
    for amount, weights in zip(x, t):
        for i, weight in enumerate(weights[:-1]):
            s[i] += (amount * 1e6) * weight
    r, a = 1.0, 0
    for v in s:
        if v < 0:
            a = 1e6
        r *= v
    return -r + a


def easy():
    weights = np.array(t)[:, :-1]

    x = cp.Variable(len(weights), integer=True)

    part_constraint = weights.T @ x >= 0
    sum_constraint = cp.sum(x) == 100

    opt = cp.prod(weights.T @ x)

    ip = cp.Problem(cp.Maximize(opt), [part_constraint, sum_constraint])

    ip.solve()


def hard():
    return


teststr = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
# teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
inf, N = float("inf"), len(t[0]) - 1
if __name__ == "__main__":
    easy()
    hard()
