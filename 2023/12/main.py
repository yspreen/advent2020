import numpy as np
import re
import pathlib
import json
from functools import reduce, cache
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: (r.split(" ")[0], lmap(int, r.split(" ")[1].split(","))), s)


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
    (-1, 1),  # UR
    (1, 1),  # DR
    (-1, -1),  # UL
    (1, -1),  # DL
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


def is_possible(line, nums):
    if line.count("#") > sum(nums):
        return False
    if line.count("#") + line.count("?") < sum(nums):
        return False
    is_set = list(filter(None, line.split("?")[0].split(".")))
    if not is_set:
        return True
    if len(is_set) > len(nums):
        return False
    for group, count in list(zip(is_set, nums))[:-1]:
        if len(group) != count:
            return False
    group, count = list(zip(is_set, nums))[-1]
    if len(group) == count:
        return True
    if len(group) > count:
        return False
    if len(group) < count:
        return "?" in line and line.split("?")[0].endswith("#")
    return True


def easy():
    arrange = 0
    for line, nums in t:

        def possibilities(line, idx=0):
            # print(line)
            if idx == len(line):
                return 1 if is_possible(line, nums) else 0
            if line[idx] != "?":
                return possibilities(line, idx + 1)
            if not is_possible(line, nums):
                return 0
            return possibilities(
                line[:idx] + "." + line[idx + 1 :], idx + 1
            ) + possibilities(line[:idx] + "#" + line[idx + 1 :], idx + 1)

        arrange += possibilities(line)
    print(arrange)


class NextState:
    def __init__(self, group_open, group_count, next_counts):
        self.group_open = group_open
        self.group_count = group_count
        self.next_counts = next_counts

    def as_tuple(self):
        return (self.group_open, self.group_count, self.next_counts)

    def next_nums(self, char):
        res = self.next_nums_(char)
        # print(self.as_tuple(), res.as_tuple(), char)
        return res

    def next_nums_(self, char):
        s = NextState(*self.as_tuple())
        if char == ".":
            if s.group_open:
                if s.group_count == 0:
                    s.group_open = False
                    return s
                else:
                    return impossible_state
            return s
        if s.group_open:
            if s.group_count <= 0:
                return impossible_state
            s.group_count -= 1
            return s
        if not s.next_counts:
            return impossible_state
        s.group_open = True
        s.group_count = s.next_counts[0] - 1
        s.next_counts = s.next_counts[1:]
        return s

    def is_possible(self, line):
        if self.group_open and self.group_count > 0:
            return is_possible(line, (self.group_count, *self.next_counts))
        return is_possible(line, self.next_counts)

    def __hash__(self):
        return hash(self.as_tuple())


impossible_state = NextState(False, 0, (-1,))


@cache
def sub_possibilities(line, state):
    if not line:
        return 1 if state.is_possible(line) else 0
    if line[0] != "?":
        return sub_possibilities(line[1:], state.next_nums(line[0]))
    if not state.is_possible(line):
        return 0
    return sub_possibilities(line[1:], state.next_nums(".")) + sub_possibilities(
        line[1:], state.next_nums("#")
    )


def hard():
    arrange = 0
    for line, nums in t:
        line = f"{line}?{line}?{line}?{line}?{line}"
        nums = nums + nums + nums + nums + nums
        arrange += sub_possibilities(line, NextState(0, 0, tuple(nums)))
    print(arrange)


teststr = """?.??.??###??.#.?? 1,1,4,1,1"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
