import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


class Element:
    items = {}

    def __init__(self, s):
        s = s.split(" => ")
        s[0] = [i.split(" ") for i in s[0].split(", ")]
        s[1] = s[1].split(" ")
        self.id = s[1][1]
        self.__class__.items[self.id] = self
        self.amount = int(s[1][0])
        self.requirements = []
        for a, e in s[0]:
            a = int(a)
            self.requirements.append([a, e])

    def link(self):
        for row in self.requirements:
            row[1] = self.__class__.items[row[1]]

    def resolve(self, amount=1):
        if amount <= 0:
            return [], -amount
        k = (amount - 1) // self.amount + 1
        r = []
        for a, e in self.requirements:
            r.append([a * k, e])
        return r, self.amount % amount

    @property
    def ore_req(self):
        req = {}
        spares = {}
        for a, e in self.requirements:
            req[e] = req.get(e, 0) + a
        while len(req) > 1:
            for k in list(req.keys()):
                if k == ORE:
                    continue
                new_req, spare = k.resolve(req[k])
                spares[k] = spares.get(k, 0) + spare
                for a, e in new_req:
                    req[e] = req.get(e, 0) + a - spares.get(e, 0)
                    spares[e] = 0
                del req[k]
                break
        return req[ORE]


ORE = Element("1 ORE => 1 ORE")


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().split("\n")
    if t[-1] == "":
        t.pop()
    t = [Element(l) for l in t]
    _ = [e.link() for e in t]


read()


def easy():
    print(Element.items["FUEL"].ore_req)


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
