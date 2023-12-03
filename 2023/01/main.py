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

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def replace_one(r):
    return re.sub("[^0-9]", "", r)


def replace_two(r):
    for number in numbers:
        r = r.replace(number, number[0] + str(numbers.index(number) + 1) + number[-1])
    return re.sub("[^0-9]", "", r)


def read(replace):
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, replace(r)), s)


def run():
    s = 0
    for line in t:
        s += int(str(line[0]) + str(line[-1]))
    print(s)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
if __name__ == "__main__":
    t = read(replace_one)
    run()
    t = read(replace_two)
    run()
