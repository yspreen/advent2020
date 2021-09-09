import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(make_func, s)


def make_func(s):
    t = s.split(" ")
    if s.startswith("swap position"):
        return Swap(t[2], t[5])
    if s.startswith("swap letter"):
        return SwapLetter(t[2], t[5])
    if s.startswith("rotate right"):
        return Rotate(t[2])
    if s.startswith("rotate left"):
        return Rotate("-" + t[2])
    if s.startswith("rotate based"):
        return RotateLetter(t[6])
    if s.startswith("reverse"):
        return Reverse(t[2], t[4])
    if s.startswith("move"):
        return Move(t[2], t[5])


class Swap:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __call__(self, w):
        w[((self.a, self.b,),)] = w[
            (
                (
                    self.b,
                    self.a,
                ),
            )
        ]
        return w


class SwapLetter:
    def __init__(self, a, b):
        self.a = ord(a)
        self.b = ord(b)

    def __call__(self, w):
        try:
            x = np.where(w == self.a)[0][0]
            y = np.where(w == self.b)[0][0]
            return Swap(x, y)(w)
        except:
            return w


class Rotate:
    def __init__(self, n):
        self.n = int(n)

    def __call__(self, w):
        return np.roll(w, self.n)


class RotateLetter:
    def __init__(self, l):
        self.l = ord(l)

    def __call__(self, w):
        try:
            idx = np.where(w == self.l)[0][0]
            idx += 2 if idx >= 4 else 1
            return Rotate(idx)(w)
        except:
            return w


class Reverse:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __call__(self, w):
        w[self.a : self.b + 1] = np.flip(w[self.a : self.b + 1])
        return w


class Move:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __call__(self, w):
        v = w[self.a]
        w = np.delete(w, self.a)
        w = np.insert(w, self.b, v)
        return w


# def test(before, after, modifier):
#     word = np.array(lmap(ord, before))
#     result = make_func(modifier)(word)
#     result = "".join(map(chr, result))
#     assert result == after


# def tests():
#     test("abcde", "ebcda", "swap position 4 with position 0")
#     test("ebcda", "edcba", "swap letter d with letter b")
#     test("edcba", "abcde", "reverse positions 0 through 4")
#     test("abcde", "bcdea", "rotate left 1 step")
#     test("bcdea", "bdeac", "move position 1 to position 4")
#     test("bdeac", "abdec", "move position 3 to position 0")
#     test("abdec", "ecabd", "rotate based on position of letter b")
#     test("ecabd", "decab", "rotate based on position of letter d")


def easy():
    # tests()
    a = np.array(lmap(ord, "abcdefgh"))
    for func in t:
        a = func(a)
    print("".join(map(chr, a)))


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
