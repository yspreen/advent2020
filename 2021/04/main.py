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

from numpy.core.numeric import zeros_like


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace("\n ", "\n").split("\n\n")
    numbers = lmap(int, s[0].split(","))
    boards = lmap(
        lambda i: np.array(
            lmap(lambda j: lmap(int, j.split(" ")), i.replace("  ", " ").splitlines())
        ),
        s[1:],
    )
    return numbers, boards


def detect(board, hit, number):
    if number not in board:
        return 0
    pos = list(zip(*np.where(board == number)))[0]
    hit[pos] = 1
    if hit[pos[0], :].sum() < 5 and hit[:, pos[1]].sum() < 5:
        return 0
    return 1


def easy():
    numbers, boards = read()
    hits = lmap(lambda i: zeros_like(i), boards)
    for number in numbers:
        for (i, board) in enumerate(boards):
            if detect(board, hits[i], number) != 0:
                return print(score(board, hits[i], number))


def hard():
    numbers, boards = read()
    hits = lmap(lambda i: zeros_like(i), boards)
    done = set()
    for number in numbers:
        for (i, board) in enumerate(boards):
            if i in done:
                continue
            if detect(board, hits[i], number) != 0:
                done |= {i}
                if len(done) == len(boards):
                    return print(score(board, hits[i], number))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
score = lambda board, hit, number: ((1 - hit) * board).sum() * number
if __name__ == "__main__":
    easy()
    hard()
