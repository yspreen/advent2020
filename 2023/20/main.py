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


class Node:
    def __init__(self, s, idx):
        left, right = s.split(" -> ")
        self.idx = idx
        self.name = left.replace("&", "").replace("%", "")
        self.kind = left[0]
        self.out = right.split(", ")
        self.inputs = []

    def __repr__(self):
        return f"{self.name}, {self.kind}, {self.out}"

    def run_flip(self, pulse, _, state):
        if pulse == "h":
            return []
        state[self.idx] = 1 - state[self.idx]
        return [(o, "lh"[state[self.idx]], self.name) for o in self.out]

    def run_conj(self, pulse, orig, state):
        inputs = state[self.idx]
        orig_idx = self.inputs.index(orig)
        mask = 1 << orig_idx
        if pulse == "h":
            inputs |= mask
        if pulse == "l" and inputs & mask:
            inputs -= mask
        state[self.idx] = inputs
        val = "l" if inputs == 2 ** (len(self.inputs)) - 1 else "h"
        return [(o, val, self.name) for o in self.out]

    def run(self, pulse, orig, state):
        if self.kind == "%":
            return self.run_flip(pulse, orig, state)
        if self.kind == "&":
            return self.run_conj(pulse, orig, state)
        if self.kind == "b":
            return [(o, "l", self.name) for o in self.out]


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    s = [Node(j, i) for i, j in enumerate(s)]
    s = {node.name: node for node in s}
    for _, node in s.items():
        for name in node.out:
            if name not in s:
                continue
            s[name].inputs.append(node.name)
    return s


def run(state):
    pulses = [("broadcaster", "l", "")]
    counts = [0, 0]
    rx = False
    while pulses:
        pulses_ = []
        for name, pulse, orig in pulses:
            counts[0 if pulse == "l" else 1] += 1
            if name not in t:
                rx = rx or pulse == "l"
                continue
            pulses_.extend(t[name].run(pulse, orig, state))
        pulses = pulses_
    return tuple(counts), rx


def easy():
    state = [0 for _ in t]
    counts = (0, 0)
    for _ in range(1000):
        count, _ = run(state)
        counts = (counts[0] + count[0], counts[1] + count[1])
    print(prod(counts))


def hard():
    state = [0 for _ in t]
    for i in range(1, 99999999999):
        _, rx = run(state)
        if rx:
            return print(i)


teststr = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
