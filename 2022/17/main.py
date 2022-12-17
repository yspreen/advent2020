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
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return lmap(str, s)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
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


def easy():
    A = np.zeros((8, 7), dtype=int)
    A[7, :] = 1
    t_ = t + t  # prop wrong
    t_.reverse()

    W = H = stopped = i = 0
    while True:
        if not t_:
            t_ += reversed(t)

        pos = 2
        A = pad_top(A)
        new_piece = move(shapes[i], 2, 0)
        W = new_piece.shape[1] - 2
        i += 1
        i %= len(shapes)
        if A.shape[0] > 200:
            H += A.shape[0] - 200
            A = A[:200, :]
        while True:
            if not t_:
                t_ += reversed(t)
            m_v = t_.pop()
            if m_v == "<" and pos > 0:
                new_move = move(new_piece, -1, 0)
                if not collision(A, new_move):
                    pos -= 1
                    new_piece = new_move
            if m_v == ">" and pos + W < 7:
                new_move = move(new_piece, 1, 0)
                if not collision(A, new_move):
                    pos += 1
                    new_piece = new_move
            new_move = move(new_piece, 0, 1)
            if collision(A, new_move):
                A = set_piece(A, new_piece)
                stopped += 1
                if stopped == 2022:
                    height = A.shape[0] - 1
                    i = 0
                    while A[i, :].sum() == 0:
                        height -= 1
                        i += 1
                    return print(height + H)
                break
            else:
                new_piece = new_move
    # print(A)


def set_piece(A, p):
    while p.shape[0] < A.shape[0]:
        p = np.pad(p, ((0, 1), (0, 0)))
    while p.shape[1] < A.shape[1]:
        p = np.pad(p, ((0, 0), (0, 1)))
    return A + p


def pad_top(A):
    while A[0:7, :].max() > 0:
        A = move(A, 0, 1)
    return A


def hard():
    return


shapes = """....
....
....
####

...
.#.
###
.#.

...
..#
..#
###

#
#
#
#

..
..
##
##""".split(
    "\n\n"
)

teststr = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")


def collision(x, y):
    xmin = x.shape[0]
    if x.shape[0] > y.shape[0]:
        xmin = y.shape[0]
    ymin = x.shape[1]
    if x.shape[1] > y.shape[1]:
        ymin = y.shape[1]
    if (x[:xmin, :ymin] + y[:xmin, :ymin]).max() > 1:
        return True
    return False


def move(np_array, x, y):
    if x >= 0:
        return np.pad(np_array, ((y, 0), (x, 0)))
    return np.pad(np_array, ((y, 0), (0, 0)))[:, -x:]


shapes = lmap(
    lambda block: np.array(
        lmap(
            lambda line: lmap(int, line),
            block.replace(".", "0").replace("#", "1").splitlines(),
        ),
        dtype=int,
    ),
    shapes,
)

t = read()
if __name__ == "__main__":
    easy()
    hard()
