import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input.txt") as f:
        t = f.read()
    n = len(t.split("\n")[0])
    t = t.replace("\n", "").replace("#", "1").replace(".", "0")
    return np.array([int(i) for i in t], dtype=np.int32).reshape(-1, n)


t = read()
coord = list(zip(*np.where(t == 1)))


def get_vector(a, b):
    v = (b[0] - a[0], b[1] - a[1])
    return (v[0] / gcd(*v), v[1] / gcd(*v))


def easy():
    vectors = {}
    for i, asteroid in enumerate(coord):
        vectors[i] = set()
        for j, other in enumerate(coord):
            if other == asteroid:
                continue
            vector = get_vector(asteroid, other)
            vectors[i].add(vector)
    print(max(map(len, vectors.values())))


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
