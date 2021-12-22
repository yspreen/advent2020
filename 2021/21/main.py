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
    return lmap(lambda r: int(r.split(": ")[1]), s)


def dice():
    while True:
        for i in range(1000):
            yield i + 1


class Player:
    dice_rolls = 0

    def __init__(self, p, d) -> None:
        self.score = 0
        self.pos = p
        self.dice = d

    def next(self) -> bool:
        for _ in range(3):
            self.pos += next(self.dice)
            self.__class__.dice_rolls += 1
        self.pos %= 10
        self.score += self.pos + 1
        return self.score >= 1000


def easy():
    d = dice()
    players = [Player(i - 1, d) for i in t]

    while True:
        for p in players:
            if p.next():
                return print([o for o in players if o != p][0].score * p.dice_rolls)


def calc(score_1, score_2, pos_1, pos_2, turn):
    win_1 = win_2 = 0
    for r1, r2, r3 in product([1, 2, 3], repeat=3):
        if turn:
            p = (pos_2 + r1 + r2 + r3) % 10
            s = score_2 + p + 1
            if s >= 21:
                win_2 += 1
                continue
            prev = S[(score_1, s, pos_1, p, 1 - turn)]
        else:
            p = (pos_1 + r1 + r2 + r3) % 10
            s = score_1 + p + 1
            if s >= 21:
                win_1 += 1
                continue
            prev = S[(s, score_2, p, pos_2, 1 - turn)]
        win_1 += prev[0]
        win_2 += prev[1]
    S[score_1, score_2, pos_1, pos_2, turn] = (win_1, win_2)


def hard():
    for score_1, score_2 in product(range(21)[::-1], repeat=2):
        for pos_1, pos_2 in product(range(10), repeat=2):
            calc(score_1, score_2, pos_1, pos_2, 0)
            calc(score_1, score_2, pos_1, pos_2, 1)
    print(max(S[(0, 0, t[0] - 1, t[1] - 1, 0)]))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t, S = read(), dict()
if __name__ == "__main__":
    easy()
    hard()
