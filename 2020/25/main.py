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
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()
    return [int(i) for i in t]


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
    loop_card = find_loop(t[0])
    print(loop_card)
    loop_door = find_loop(t[1])
    print(encrypt(1, t[0], loop_door))


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
