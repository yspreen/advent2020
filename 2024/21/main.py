import numpy as np
import re
import pathlib
import json
from functools import reduce, cmp_to_key
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
from os import environ

KEYA = "789\n456\n123\n.0A"
KEYB = ".^A\n<v>"


def getidx(keypad, btn):
    x = 0
    y = 0
    for c in keypad:
        if btn == c:
            return (x, y)
        if c == "\n":
            x += 1
            y = 0
        else:
            y += 1


IDX_KEYA = {c: getidx(KEYA, c) for c in KEYA if c != "\n"}
IDX_KEYB = {c: getidx(KEYB, c) for c in KEYB if c != "\n"}
INV_IDX_KEYA = {v: k for k, v in IDX_KEYA.items()}
INV_IDX_KEYB = {v: k for k, v in IDX_KEYB.items()}


def movement(btn, btn_, keypad):
    if btn == btn_:
        return [""]

    idx_map = IDX_KEYA if keypad == "A" else IDX_KEYB
    x, y = idx_map[btn]
    x_, y_ = idx_map[btn_]
    dot_pos = idx_map["."]

    # Collect required moves in each dimension
    moves = []
    if y_ - y > 0:  # right
        moves.append(">" * (y_ - y))
    if y - y_ > 0:  # left
        moves.append("<" * (y - y_))
    if x - x_ > 0:  # up
        moves.append("^" * (x - x_))
    if x_ - x > 0:  # down
        moves.append("v" * (x_ - x))

    # Generate all possible orderings of the move groups
    results = []
    for perm in permutations(moves):
        path = "".join(perm)

        # Validate path doesn't hit '.'
        curr_x, curr_y = x, y
        valid = True

        for move in path:
            if move == ">":
                curr_y += 1
            elif move == "<":
                curr_y -= 1
            elif move == "^":
                curr_x -= 1
            else:
                curr_x += 1

            if (curr_x, curr_y) == dot_pos:
                valid = False
                break

        if valid:
            results.append(path)

    return results


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(str, r), s)


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
]


def BFS(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, 0)]
    visited = set([start])

    while options:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:  # lower bound check
                    continue
                if new_p[1] < 0:  # lower bound check
                    continue
                try:
                    assert can_walk(pos, new_p)
                except:
                    continue  # upper bound check
                if new_p in visited:
                    continue
                visited.add(new_p)
                cost_ = cost + cost_fn(pos, new_p)
                new_o.append((new_p, cost_))
                if goal(new_p):
                    return cost_
        options = new_o
    return None


def get_seq(keypad, lines):
    r = []
    for line in lines:
        seq = [""]
        old_btn = "A"
        for btn in line:
            new_seq = []
            for m in movement(old_btn, btn, keypad):
                for s in seq:
                    s += m
                    s += "A"
                    new_seq.append(s)
            seq = new_seq
            old_btn = btn
        r.extend(seq)

    min_l = min(map(len, r))
    return [s for s in r if len(s) == min_l]


def rev_move(keypad, seq):
    dic = IDX_KEYA if keypad == "A" else IDX_KEYB
    inv = INV_IDX_KEYA if keypad == "A" else INV_IDX_KEYB

    x, y = dic["A"]
    s = ""
    for c in seq:
        if c == "A":
            s += inv[(x, y)]
            continue
        x += mv["^v<>".index(c)][0]
        y += mv["^v<>".index(c)][1]
    return s


def easy():
    s = 0
    for line in t:
        seq = get_seq("A", [line])
        for _ in range(2):
            seq = get_seq("B", seq)
        s += len(seq[0]) * int("".join(line).replace("A", ""))
    print(s)


def hard():
    return


teststr = """379A"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
