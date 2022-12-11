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
        s = (f.read() if teststr == "" else teststr).split("\n\n")
    return lmap(lambda r: lmap(process_line, r.splitlines()[1:]), s)


def create_lambda(line):
    if "old * old" in line:
        return lambda i: i * i
    if "old + old" in line:
        return lambda i: i + i
    if "old * " in line:
        return lambda i: i * int(line.split("* ")[-1])
    if "old + " in line:
        return lambda i: i + int(line.split("+ ")[-1])


def process_line(line):
    line = line.split(": ", 1)[1]
    if "," in line:
        return lmap(int, line.split(", "))
    if "new" in line:
        return create_lambda(line)
    if "divisible" in line:
        return int(line.split("by ")[1])
    if "throw" in line:
        return int(line.split(" ")[-1])
    return [int(line)]


def easy():
    t_ = deepcopy(t)
    for monkey in t_:
        monkey.append(0)
    for _ in range(20):
        for monkey in t_:
            while True:
                if not monkey[0]:
                    break
                monkey[5] += 1
                item = monkey[0][0]
                monkey[0] = monkey[0][1:]
                item = monkey[1](item)
                item = item // 3
                if item % monkey[2] == 0:
                    t_[monkey[3]][0].append(item)
                else:
                    t_[monkey[4]][0].append(item)
    counters = lmap(lambda m: m[5], t_)
    counters.sort()
    print(counters[-1] * counters[-2])


def hard():
    t_ = deepcopy(t)
    for monkey in t_:
        monkey.append(0)
    produ = prod(lmap(lambda monkey: monkey[2], t_))
    for _ in range(10000):
        for monkey in t_:
            while True:
                if not monkey[0]:
                    break
                monkey[5] += 1
                item = monkey[0][0]
                monkey[0] = monkey[0][1:]
                item = monkey[1](item)
                item %= produ
                if item % monkey[2] == 0:
                    t_[monkey[3]][0].append(item)
                else:
                    t_[monkey[4]][0].append(item)
    counters = lmap(lambda m: m[5], t_)
    counters.sort()
    print(counters[-1] * counters[-2])


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
