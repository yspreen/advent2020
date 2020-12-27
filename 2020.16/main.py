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
        t = f.read().replace("\r", "").split("\n\n")
    if t[-1] == "":
        t.pop()
    t = [l.split("\n") for l in t]
    if t[-1][-1] == "":
        t[-1].pop()

    rules = []
    for l in t[0]:
        rules.append(tuple(map(int, l.split(" ")[-3].split("-"))))
        rules.append(tuple(map(int, l.split(" ")[-1].split("-"))))
    t[0] = [l.split(":")[0] for l in t[0]]
    t[1] = list(map(int, t[1][1].split(",")))
    t[2] = [list(map(int, l.split(","))) for l in t[2][1:]]
    return t + [rules]


t = read()


def find_loop(pub, subject=7):
    k = i = 1
    while k != pub:
        k = encrypt(k, subject, 1)
        i += 1
    return i - 1


def encrypt(value, subject, loop):
    for _ in range(loop):
        value = (value * subject) % 20201227
    return value


def easy():
    invalids = 0
    for i, row in enumerate(t[2]):
        for num in row:
            valid = False
            for rule in t[3]:
                if rule[0] <= num <= rule[1]:
                    valid = True
                    break
            if not valid:
                invalids += num
                t[2][i] = None
                break
    t[2] = list(filter(None, t[2]))
    print(invalids)


def hard():
    possible = {name: set([i for i in range(len(t[1]))]) for name in t[0]}
    for row in t[2]:
        for i, num in enumerate(row):
            last = False
            for j, rule in enumerate(t[3]):
                curr = rule[0] <= num <= rule[1]
                if j % 2 == 1 and not (curr or last):
                    possible[t[0][j // 2]].discard(i)
                    assert 0 <= i < 20
                last = curr
    final = {}
    for _ in range(20):
        for k, v in possible.items():
            if len(v) == 1:
                final[k] = list(v)[0]
                for other in possible.values():
                    other.discard(final[k])
    print(prod([t[1][v] for k, v in final.items() if "departure " in k]))


if __name__ == "__main__":
    easy()
    hard()
