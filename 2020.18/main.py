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
    t.pop()
    return [l.split(" ") for l in t]


t = read()


def calc(line):
    sign = "+"
    result = 0
    while line:
        op = line[0]
        if op.startswith("("):
            line[0] = line[0][1:]
            op = str(calc(line))
        else:
            line.pop(0)
        if op in ["*", "+"]:
            sign = op
        else:
            num = op.replace(")", "")
            num = int(num)
            if sign == "+":
                result += num
            else:
                result *= num
        if op.endswith(")"):
            line.insert(0, "0" + ")" * (op.count(")") - 1))
            line.insert(0, "+")
            return result

    return result


def easy():
    print(sum([calc(i) for i in t]))


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
