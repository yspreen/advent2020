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

mapping = {
    "A": "m",
    "K": "l",
    "Q": "k",
    "J": "j",
    "T": "i",
    "9": "h",
    "8": "g",
    "7": "f",
    "6": "e",
    "5": "d",
    "4": "c",
    "3": "b",
    "2": "a",
}


def repl_card(hand):
    result = ""
    for c in hand:
        result += mapping[c]
    return result


from os import environ


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: (repl_card(r.split(" ")[0]), int(r.split(" ")[1])), s)


def one_score(hand):
    counts = sorted([hand.count(c) for c in set(hand + ".")])
    second_count, max_count = counts[-2:]
    rank = 1
    if max_count == 5:
        rank = 7
    if max_count == 4:
        rank = 6
    if max_count == 3 and second_count == 2:
        rank = 5
    elif max_count == 3:
        rank = 4
    if max_count == 2 and second_count == 2:
        rank = 3
    elif max_count == 2:
        rank = 2
    score = rank * (10**10)
    for idx, c in enumerate(hand):
        score += 10 ** (8 - 2 * idx) * (ascii_lowercase.index(c) + 1)
    return score


def two_score(hand):
    counts = sorted([hand.count(c) for c in set(hand.replace("j", "") + ".,")])
    jokers = hand.count("j")
    second_count, max_count = counts[-2:]
    rank = 1
    if max_count + jokers >= 5:
        rank = 7
    if max_count + jokers == 4:
        rank = 6
    if max_count + jokers == 3 and second_count == 2:
        rank = 5
    elif max_count + jokers == 3:
        rank = 4
    if max_count + jokers == 2 and second_count == 2:
        rank = 3
    elif max_count + jokers == 2:
        rank = 2
    score = rank * (10**10)
    for idx, c in enumerate(hand):
        score += 10 ** (8 - 2 * idx) * (("j" + ascii_lowercase).index(c) + 1)
    return score


def run(hand_score):
    t.sort(key=lambda i: hand_score(i[0]))

    score = 0
    for idx, hand_bid in enumerate(t, 1):
        score += idx * hand_bid[1]
    print(score)


teststr = ""
if environ["AOC_SOLVE"] == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    run(one_score)
    run(two_score)
