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
        self.s = len(shorten(s))

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
        return self.s

    @property
    def lengths(self):
        if self.children:
            c = [i.lengths for i in self.children]
            a = c[0]
            for b in c[1:]:
                a = np.outer(a, b)
                for i in range(M + 1):
                    a[i] = np.roll(a[i], i)
                a = np.sum(a, 0)
            return a
        if self.choices:
            return np.sum([s.lengths for s in self.choices], axis=0)
        A = np.zeros(M + 1)
        A[self.s] = 1
        return A


def shorten(s):
    didreplace = 1
    while didreplace:
        didreplace = 0
        for redundant in ["EW", "WE", "NS", "SN"]:
            while redundant in s:
                didreplace = 1
                s = s.replace(redundant, "")
    return s


M = 0


def easy():
    global M
    M = t.max_length
    print(M)


def hard():
    print(t.lengths)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
Segment.resolve()

if __name__ == "__main__":
    easy()
    hard()
