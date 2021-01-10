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
        t = f.read().replace("\n", "").split(",")
    if t[-1] == "":
        t.pop()
    return [int(i) for i in t]


t = read()


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


inputs = outputs = None


def op(i):
    global t, inputs, outputs

    code = t[i]
    ins = code % 100
    mode_a = digit(code, 2)
    mode_b = digit(code, 3)
    mode_c = digit(code, 4)

    try:
        a = t[i + 1]
        b = t[i + 2]
        c = t[i + 3]
        if mode_a == 0 and ins != 3:
            a = t[a]
        if mode_b == 0:
            b = t[b]
    except:
        # end of t.
        pass

    if ins == 99:
        return 0
    if ins == 1:
        t[c] = a + b
        return 4
    if ins == 2:
        t[c] = a * b
        return 4
    if ins == 3:
        t[a] = inputs.pop(0)
        return 2
    if ins == 4:
        outputs.append(a)
        # print(a)
        return 2
    if ins == 5:
        if a != 0:
            return b - i
        return 3
    if ins == 6:
        if a == 0:
            return b - i
        return 3
    if ins == 7:
        t[c] = 1 if a < b else 0
        return 4
    if ins == 8:
        t[c] = 1 if a == b else 0
        return 4


def calc(*inp):
    global t, inputs, outputs
    t = read()

    outputs = []
    inputs = list(inp)

    i = -1
    d = 1
    while d != 0:
        i += d
        d = op(i)
    return outputs


def amp(*param):
    a = 0
    for p in param:
        a = calc(p, a)[0]
    return a


def easy():
    m = (0, 0)
    for p in permutations(range(5)):
        a = amp(*p)
        if a > m[0]:
            m = (a, p)
    print(*m)


def hard():
    from parttwo import hard

    hard()


if __name__ == "__main__":
    easy()
    hard()