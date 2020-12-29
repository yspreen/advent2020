import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().replace("\r", "").split("\n")
    return " " + "\n ".join(t), [
        [l.split(" (")[0].split(" "), l.split(" (")[1][9:-1].split(", ")]
        for l in t[:-1]
    ]


s, t = read()

allergens = set()
foods = set()


def easy():
    global allergens, foods
    for food, a in t:
        allergens |= set(a)
        foods |= set(food)
    could_contain = {a: set(foods) for a in allergens}
    for food, a in t:
        for allergen in a:
            could_contain[allergen] &= set(food)
    changed = True
    filtered = set()
    while changed:
        changed = False
        for k, v in could_contain.items():
            if k in filtered or len(v) != 1:
                continue
            changed = True
            filtered.add(k)
            for l in set(could_contain.keys()) - set([k]):
                could_contain[l] -= v
            break
    contains_none = reduce(lambda a, b: a - b[1], could_contain.items(), set(foods))
    counter = reduce(lambda a, b: a + s.count(" " + b + " "), contains_none, 0)


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
