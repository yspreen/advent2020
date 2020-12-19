import numpy as np
import re
import pathlib
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().replace("\r", "")
    t = t.split("\n")
    if t[-1] == "":
        t.pop()
    t = [i.split(" ") for i in t]
    for i in t:
        if i[0] == "mask":
            i[1] = i[-1]
        else:
            i[0] = int(i[0][4:-1])
            i[1] = int(i[-1])
    t = [tuple(i[:2]) for i in t]

    return t


t = read()


def easy():
    m_or = 0
    m_and = 0
    mem = {}
    for cmd, param in t:
        if cmd == "mask":
            m_and = int(param.replace("X", "1"), 2)
            m_or = int(param.replace("X", "0"), 2)
            continue
        mem[cmd] = (param | m_or) & m_and
    print(sum(mem.values()))


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
