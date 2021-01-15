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
        k = (amount - 1) // self.amount + 1
        r = []
        for a, e in self.requirements:
            r.append([a * k, e])
        print(
            "producing %d x %d %s, leaving %d spare (for %d needed)"
            % (k, self.amount, self.id, k * self.amount - amount, amount)
        )
        return r, k * self.amount - amount

    @property
    def ore_req(self):
        need = {e: a for a, e in self.requirements}
        have = {}
        while len(need) > 1:
            for element, needed in need.items():
                if element == ORE:
                    continue
                needed -= have.get(element, 0)
                if needed <= 0:
                    have[element] = -needed
                    del need[element]
                    break
                have[element] = 0
                added_needs, spare = element.resolve(needed)
                have[element] = have.get(element, 0) + spare
                for a, e in added_needs:
                    need[e] = need.get(e, 0) + a
                del need[element]
                break
        return need[ORE]


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
