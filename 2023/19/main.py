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
from os import environ


class Rule:
    def __init__(self, s):
        self.condition = None
        self.go_to = s.split(":")[-1]
        if ":" not in s:
            return
        self.condition = ("xmas".find(s[0]), s[1], int(s.split(":")[0][2:]))

    def __repr__(self):
        return f"{self.go_to}: {self.condition}"

    def matches(self, part):
        if not self.condition:
            return True
        if self.condition[1] == "<":
            return part[self.condition[0]] < self.condition[2]
        if self.condition[1] == ">":
            return part[self.condition[0]] > self.condition[2]


def read():
    with open(DIR / "input") as f:
        rules, parts = (f.read() if teststr == "" else teststr).split("\n\n")
    rules = map(
        lambda i: (i.split("{")[0], i.split("{")[1][:-1].split(",")), rules.splitlines()
    )
    rules = {r[0]: lmap(Rule, r[1]) for r in rules}
    parts = lmap(
        lambda part: lmap(int, re.sub(r"[^0-9\,]+", "", part).split(",")),
        parts.splitlines(),
    )
    return rules, parts


def easy():
    s = 0
    for part in parts:
        flow = "in"
        while flow not in ["R", "A"]:
            for rule in rules[flow]:
                if rule.matches(part):
                    flow = rule.go_to
                    break
        if flow == "A":
            s += sum(part)
    print(s)


def hard():
    return


teststr = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
rules, parts = read()
if __name__ == "__main__":
    easy()
    hard()
