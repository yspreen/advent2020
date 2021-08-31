import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from copy import deepcopy, copy


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    s = lmap(
        lambda i: i.replace("a ", "")
        .replace(",", "")
        .replace("and ", "")
        .replace(" generator", "+")
        .replace("-compatible microchip", "-")[:-1]
        .split(" ")[4:],
        s[:3],
    )
    return lmap(set, s) + [set()]


def flipped(element):
    return element[:-1] + {"-": "+", "+": "-"}[element[-1]]


def is_valid(arrangement):
    for row in arrangement:
        has_gen = has_unmatched = False
        for e in row:
            if e[-1] == "+":
                has_gen = True
                if has_unmatched:
                    return False
            elif flipped(e) not in row:
                has_unmatched = True
                if has_gen:
                    return False
    return True


def make_hash(arrangement, elev=-1):
    return tuple(map(lambda i: tuple(sorted(i)), arrangement + [[elev]]))


def moves(cost, elev, arrangement):
    cost += 1
    output = []
    delta = []
    if elev > 0:
        delta += [elev - 1]
    if elev < 3:
        delta += [elev + 1]
    for new_elev in delta:
        for e_one in arrangement[elev]:
            arrangement[elev] -= {e_one}
            arrangement[new_elev] |= {e_one}
            if is_valid(arrangement):
                output.append((cost, new_elev, deepcopy(arrangement)))
            for e_two in arrangement[elev]:
                arrangement[elev] -= {e_two}
                arrangement[new_elev] |= {e_two}
                if is_valid(arrangement):
                    output.append((cost, new_elev, deepcopy(arrangement)))
                arrangement[elev] |= {e_two}
                arrangement[new_elev] -= {e_two}
            arrangement[elev] |= {e_one}
            arrangement[new_elev] -= {e_one}

    return output


def easy():
    global goal, reached

    goal = [set(), set(), set(), t[0] | t[1] | t[2]]
    goal_h = make_hash(goal, 3)

    positions = [(0, 0, deepcopy(t))]
    reached = set()

    while True:
        new_p = []
        for p in positions:
            new_moves = moves(*p)
            for m in new_moves:
                h = make_hash(m[2], m[1])
                if h == goal_h:
                    print(m[0])
                    return
                if h in reached:
                    continue
                reached.add(h)
                new_p.append(m)
        positions = new_p


def hard():
    return


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
reached = goal = t = read()
if __name__ == "__main__":
    easy()
    hard()
