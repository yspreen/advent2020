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
from typing import Optional


class DLList:
    def __init__(self, elem, prev=None, aftr=None):
        self.elem = elem  # type: int
        self.mod = mod(elem)  # type: int
        self.prev = prev  # type: Optional[DLList]
        self.aftr = aftr  # type: Optional[DLList]

    def __str__(self):
        return f"[{str(self.elem)}]"

    def remove(self):
        prev, after = self.prev, self.aftr
        self.prev = None
        self.aftr = None
        prev.aftr = after
        after.prev = prev
        return prev, after

    def insert_after(self, new_elem):
        old_after = self.aftr

        self.aftr = new_elem
        new_elem.prev = self
        new_elem.aftr = old_after
        old_after.prev = new_elem

    def insert_prev(self, new_elem):
        old_prev = self.prev

        self.prev = new_elem
        new_elem.aftr = self
        new_elem.prev = old_prev
        old_prev.aftr = new_elem

    def find(self, value):
        curr = self
        while curr.elem != value:
            curr = curr.aftr
        return curr

    def plus(self, offset):
        curr = self
        while offset > 0:
            curr = curr.aftr
            offset -= 1
        while offset < 0:
            curr = curr.prev
            offset += 1
        return curr.elem

    def print_all(self):
        curr = self.aftr
        s = str(self)
        while curr != self:
            s += str(curr)
            curr = curr.aftr
        print(s)

    def elem_list(self):
        l = [self]
        c = self.aftr
        while c is not self:
            l.append(c)
            c = c.aftr
        return l


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(int, s)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]


def easy():
    prev = None
    start = None
    for elem in t:
        curr = DLList(elem, prev)
        start = curr if start is None else start
        if prev is not None:
            prev.aftr = curr
        prev = curr
    start.prev = prev
    prev.aftr = start

    curr = start

    all_nodes = curr.elem_list()
    # curr.print_all()
    for node in all_nodes:
        curr = node
        value = curr.elem

        if value != 0:
            prev, after = curr.remove()
            if value > 0:
                for _ in range(value - 1):
                    after = after.aftr
                after.insert_after(curr)
            else:
                for _ in range(-value - 1):
                    prev = prev.prev
                prev.insert_prev(curr)

        # curr.print_all()

    zero = curr.find(0)
    print(zero.plus(1000) + zero.plus(2000) + zero.plus(3000))


def mod(x):
    if x == 0:
        return 0
    N = len(t) - 1
    if x < 0:
        return (x % N) - N
    return ((x - 1) % N) + 1


def hard():
    prev = None
    start = None
    for elem in t:
        curr = DLList((elem * 811589153), prev)
        start = curr if start is None else start
        if prev is not None:
            prev.aftr = curr
        prev = curr
    start.prev = prev
    prev.aftr = start

    curr = start

    all_nodes = curr.elem_list()
    # curr.print_all()
    for node in all_nodes * 10:
        # print(node.mod)
        curr = node
        value = curr.mod

        if value != 0:
            prev, after = curr.remove()
            if value > 0:
                for _ in range(value - 1):
                    after = after.aftr
                after.insert_after(curr)
            else:
                for _ in range(-value - 1):
                    prev = prev.prev
                prev.insert_prev(curr)

        # curr.print_all()

    zero = curr.find(0)
    print(zero.plus(1000) + zero.plus(2000) + zero.plus(3000))


teststr = """1
2
-3
3
-2
0
4"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
