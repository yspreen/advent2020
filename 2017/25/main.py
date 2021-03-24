import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).split("\n\n")
    S = []
    for state in s[1:]:
        state = lmap(lambda i: i.split(" ")[-1][:-1], state.splitlines())
        S.append(
            [
                (
                    int(state[2 + i]),
                    2 * int(state[3 + i][0] == "r") - 1,
                    ord(state[4 + i]) - 65,
                )
                for i in [0, 4]
            ]
        )
    return S, int(s[0].split(" ")[-2])


def easy():
    s = 0
    i = N
    A = np.zeros(N * 2, np.ubyte)
    for _ in range(N):
        new_val, movement, new_state = t[s][A[i]]
        A[i] = new_val
        i += movement
        s = new_state
    print(A.sum())


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t, N = read()
if __name__ == "__main__":
    easy()
    hard()