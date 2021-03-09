import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").split("\n")
    return t[:-1]


t = read()


class Expression:
    def __init__(self, line, parent=None, parent_index=None):
        self.parent = parent
        self.parent_index = parent_index
        bracket = 0
        sub_indices = []
        for i, c in enumerate(line):
            if c == "(":
                bracket += 1
                if bracket == 1:
                    sub_indices.append([i, 0])
            if c == ")":
                bracket -= 1
                if bracket == 0:
                    sub_indices[-1][1] = i
        self.children = []
        for i, s_e in enumerate(sub_indices):
            sub = line[s_e[0] + 1 : s_e[1]]
            self.children.append(Expression(sub, self, i))
        i = len(sub_indices)
        for s, e in reversed(sub_indices):
            i -= 1
            line = line[:s] + "$%d$" % i + line[e + 1 :]
        self.resolved = False
        self.line = line

    def calc(self):
        line = self.line.split(" ")
        while len(line) > 1:
            has_plus = "+" in line
            for i, op in enumerate(line):
                if op == "+":
                    line[i - 1] = int(line[i - 1]) + int(line[i + 1])
                elif op == "**" or (not has_plus and op == "*"):
                    line[i - 1] = int(line[i - 1]) * int(line[i + 1])
                else:
                    continue
                del line[i : i + 2]
                break
        return int(line[0])

    def resolve(self):
        if self.resolved:
            return self.value
        self.resolved = True
        for c in self.children:
            c.resolve()

        self.value = self.calc()

        if self.parent is not None:
            self.parent.line = self.parent.line.replace(
                "$%d$" % self.parent_index, str(self.value)
            )
        return self.value


def easy():
    print(sum([Expression(i.replace("*", "**")).resolve() for i in t]))


def hard():
    print(sum([Expression(i).resolve() for i in t]))


if __name__ == "__main__":
    easy()
    hard()
