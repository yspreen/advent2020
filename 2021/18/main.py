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


class Pair:
    def __init__(self, stream=None, remove_first=True, parent=None, level=0, pos=0):
        self.parent = parent
        self.level = level
        self.pos = pos
        self.left = 0
        self.right = 0
        if stream is None:
            return
        _ = next(stream) if remove_first else ""
        self.left = self.unwrap_child(stream, 1)
        assert next(stream) == ","
        self.right = self.unwrap_child(stream, 2)
        assert next(stream) == "]"

    def unwrap_child(self, stream, pos):
        i = next(stream)
        if i != "[":
            return int(i)
        else:
            return Pair(stream, False, self, self.level + 1, pos)

    def explode(self):
        return

    def find_explodable(self) -> bool:
        if self.level >= 4:
            self.explode()
            return True
        for p in [self.left, self.right]:
            if p is Pair and p.find_explodable():
                return True
        return False

    def find_split(self) -> bool:
        if self.left is not Pair and self.left >= 10:
            i = self.left
            self.left = Pair(parent=self, level=self.level + 1, pos=1)
            self.left.left = i // 2
            self.left.right = i - i // 2
            return True
        if self.right is not Pair and self.right >= 10:
            i = self.right
            self.right = Pair(parent=self, level=self.level + 1, pos=2)
            self.right.left = i // 2
            self.right.right = i - i // 2
            return True
        if self.left is Pair and self.left.find_split():
            return True
        if self.right is Pair and self.right.find_split():
            return True
        return False


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: Pair(iter(r)), s)


def easy():
    p = Pair(iter("[9,9]"))
    p.left = 11
    print(p.find_split())
    return


def hard():
    return


teststr = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
