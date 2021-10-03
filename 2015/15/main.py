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
    res = minimize(
        score,
        [10e-6] * len(t),
        bounds=[(0, 100e-6)] * len(t),
        options={"disp": False},
        tol=1e-7,
        constraints={"type": "eq", "fun": lambda x: sum(x) - 100e-6},
    )
    x = lmap(lambda i: i * 1e6, res.x)
    print(x)
    x = lmap(round, x)
    print(x)
    print(score(x))
    print(-round(score(x)))


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
