import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols, solve


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().splitlines()[0]
    return Segment(t[1:-1])


class SegmentState:
    directions = {}

    def __init__(self, before, segment):
        self.before = before
        self.after = set()
        self.segment = segment

    def solve(self):
        if self.segment.children:
            state = self.before
            for c in self.segment.children:
                n = SegmentState(state, c)
                n.solve()
                state = n.after
            self.after = state
        else:
            for p in self.before:
                if self.segment.choices:
                    for c in self.segment.choices:
                        n = SegmentState(set([p]), c)
                        n.solve()
                        self.after |= n.after
                else:
                    direction = self.directions[p]
                    for c in self.segment.s:
                        direction += c
                        p = (p[0] + y_dist[c], p[1] + x_dist[c])
                        self.directions[p] = self.directions.get(p, direction)
                    self.after.add(p)


x_dist = {
    "N": 0,
    "E": 1,
    "S": 0,
    "W": -1,
}
y_dist = {
    "N": -1,
    "E": 0,
    "S": 1,
    "W": 0,
}


class Segment:
    unresolved = []
    items = []

    @classmethod
    def resolve(cls):
        while len(cls.unresolved):
            e = cls.unresolved.pop()
            for i in range(len(e)):
                e[i] = Segment(e[i])

    def __init__(self, s):
        self.choices = []
        self.children = []
        self.items.append(self)
        self.id = len(self.items)
        self.s = s
        segments = [-1]
        splits = [-1]
        brace_num = 0
        for i, e in enumerate(s):
            if e == "(":
                brace_num += 1
                if brace_num == 1:
                    segments.append(i)
            if e == ")":
                brace_num -= 1
                if brace_num == 0:
                    segments.append(i)
            if e == "|" and brace_num == 0:
                splits.append(i)
        segments.append(len(s))
        splits.append(len(s))

        if len(splits) > 2:
            for i in range(1, len(splits)):
                a, b = splits[i - 1], splits[i]
                self.choices.append(s[a + 1 : b])
        elif len(segments) > 2:
            for i in range(1, len(segments)):
                a, b = segments[i - 1], segments[i]
                if b - a < 2:
                    continue
                self.children.append(s[a + 1 : b])
        self.unresolved.append(self.children)
        self.unresolved.append(self.choices)
        self.l = len(shorten(s))

    def print(self, prefix=[]):
        print(*prefix, self.s)
        for i in self.children:
            i.print(prefix + [">"])
        for i in self.choices:
            i.print(prefix + ["|"])

    @property
    def max_length(self):
        if self.children:
            return sum([i.max_length for i in self.children])
        if self.choices:
            s = [i.max_length for i in self.choices]
            s.sort(key=lambda i: -i)
            return s[0]
        return self.l


def shorten(s):
    didreplace = 1
    while didreplace:
        didreplace = 0
        for redundant in ["EW", "WE", "NS", "SN"]:
            while redundant in s:
                didreplace = 1
                s = s.replace(redundant, "")
    return s


def easy():
    print(t.max_length)


def hard():
    SegmentState.directions[(0, 0)] = ""
    SegmentState(set([(0, 0)]), t).solve()
    lens = [len(v) for v in SegmentState.directions.values()]
    lens = [i for i in lens if i >= 1000]
    print(len(lens))


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
Segment.resolve()

if __name__ == "__main__":
    easy()
    hard()