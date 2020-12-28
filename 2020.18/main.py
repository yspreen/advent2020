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
    with open(DIR / "input.txt") as f:
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
                elif not has_plus and op == "*":
                    line[i - 1] = int(line[i - 1]) * int(line[i + 1])
                else:
                    continue
                del line[i]
                del line[i]
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


def calc(line):
    sign = "+"
    result = 0
    while line:
        op = line[0]
        if op.startswith("("):
            line[0] = line[0][1:]
            op = str(calc(line))
        else:
            line.pop(0)
        if op in ["*", "+"]:
            sign = op
        else:
            num = op.replace(")", "")
            num = int(num)
            if sign == "+":
                result += num
            else:
                result *= num
        if op.endswith(")"):
            line.insert(0, "0" + ")" * (op.count(")") - 1))
            line.insert(0, "+")
            return result
    return result


def easy():
    print(sum([calc(i.split(" ")) for i in t]))


def hard():
    print(sum([Expression(i).resolve() for i in t]))


if __name__ == "__main__":
    easy()
    hard()
