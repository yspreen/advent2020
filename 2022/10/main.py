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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(maybe_int, r.split(" ")), s)


def maybe_int(s):
    try:
        return int(s)
    except:
        return s


def easy():
    x = 1
    cycles = 0
    i = 0
    marker = [20, 60, 100, 140, 180, 220]
    s = 0
    for ins in t:
        old_x = x
        if ins[0] == "noop":
            cycles += 1
        if ins[0] == "addx":
            x += ins[1]
            cycles += 2
        if cycles >= marker[i]:
            s += old_x * marker[i]
            i += 1
            if i == len(marker):
                break
    print(s)


def draw(buffer, pos):
    new_pos = len(buffer) % 40
    if abs(pos - new_pos) < 2:
        buffer.append("##")
    else:
        buffer.append("  ")


def hard():
    buffer = []
    pos = 1
    for ins in t:
        if ins[0] == "noop":
            draw(buffer, pos)
        if ins[0] == "addx":
            draw(buffer, pos)
            draw(buffer, pos)
            pos += ins[1]
    for _ in range(7):
        print("".join(buffer[:40]))
        buffer = buffer[40:]


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
