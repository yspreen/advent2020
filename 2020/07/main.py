import numpy as np
import re
import pathlib
from functools import reduce
from string import ascii_lowercase

DIR = pathlib.Path(__file__).parent.absolute()


class BagDef:
    defs = {}

    def __init__(self, arr):
        self.name = arr[0]
        self.specs = []
        self.parents = []
        del arr[0]
        for spec in arr:
            spec = spec.split(" ")
            if spec[0] == "no":
                continue
            num = int(spec[0])
            del spec[0]
            spec = " ".join(spec)
            self.specs.append((num, spec))
        BagDef.defs[self.name] = self

    def backstep(self):
        _specs = []
        for num, spec in self.specs:
            _specs.append((num, BagDef.defs[spec]))
        self.specs = _specs

        for num, spec in self.specs:
            spec.parents.append((num, self))

    @property
    def parent_combos(self):
        c = set([self.name])
        for num, parent in self.parents:
            c |= parent.parent_combos
        return c

    @property
    def child_combos(self):
        c = 1
        for num, child in self.specs:
            c += num * child.child_combos
        return c


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "")
    t = t.replace(" bags", "")
    t = t.replace(" bag", "")
    t = t.replace(".", "")
    t = t.replace(" contain", ",")
    t = t.split("\n")
    if t[-1] == "":
        t.pop()
    t = [l.split(", ") for l in t]
    if t[-1] == "":
        t.pop()
    if t[-1][-1] == "":
        t[-1].pop()

    t = [BagDef(l) for l in t]
    for b in t:
        b.backstep()

    return t


def easy():
    print(len(BagDef.defs["shiny gold"].parent_combos) - 1)


def hard():
    print(BagDef.defs["shiny gold"].child_combos - 1)


if __name__ == "__main__":
    read()
    easy()
    hard()