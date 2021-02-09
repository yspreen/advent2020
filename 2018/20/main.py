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


class Segment:
    unresolved = []

    @classmethod
    def resolve(cls):
        while len(cls.unresolved):
            e = cls.unresolved.pop()
            for i in range(len(e)):
                e[i] = Segment(e[i])

    def __init__(self, s):
        self.choices = []
        self.children = []
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
        self.s = shorten(s)

    def print(self, prefix=[]):
        print(*prefix, self.s)
        for i in self.children:
            i.print(prefix + [">"])
        for i in self.choices:
            i.print(prefix + ["|"])

    @property
    def max_length(self):
        if self.children:
            return "".join([i.max_length for i in self.children])
        if self.choices:
            s = [i.max_length for i in self.choices]
            s = [(i, len(i)) for i in s]
            s.sort(key=lambda i: i[1])
            return s[-1][0]
        return self.s

    @property
    def lengths(self):
        if self.children:
            c = [i.lengths for i in self.children]
            return [sum(t) for t in product(*c)]
        if self.choices:
            return [i for s in self.choices for i in s.lengths]
        return [len(self.s)]


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
    print(len(t.max_length))


def hard():
    print(len([i for i in t.lengths if i >= 1000]))


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
Segment.resolve()

if __name__ == "__main__":
    easy()
    hard()
