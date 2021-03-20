import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product


class CircularNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = self if next is None else next

    def insert(self, value):
        self.next = self.__class__(value, self.next)
        return self.next


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return int(s.splitlines()[0])


def easy():
    n = CircularNode(0)
    for i in range(2017):
        for _ in range(t):
            n = n.next
        n = n.insert(i + 1)
    print(n.next.value)


def hard():
    zero = n = CircularNode(0)
    for i in range(50000000):
        for _ in range(t):
            n = n.next
        n = n.insert(i + 1)
    print(zero.next.value)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()