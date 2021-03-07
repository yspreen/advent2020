import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool


class Unit:
    last_id = -1
    items = {}
    max_init = 0

    def __init__(self, s, b):
        self.__class__.last_id += 1
        self.id = self.__class__.last_id
        self.items[self.id] = self

        self.units = int(s.split(" ")[0])
        s = s.split(" each with ")[1]
        self.hp = int(s.split(" ")[0])
        s = s.split(" hit points ")[1]

        self.weak = []
        self.immune = []
        if s[0] == "(":
            for bit in s.split(")")[0][1:].split("; "):
                type_ = self.weak if bit[0] == "w" else self.immune
                bit = bit.split(" to ")[1]
                type_.extend(bit.split(", "))
        s = s.split(") ")[-1]

        s = s.split("with an attack that does ")[1]
        self.atk = int(s.split(" ")[0]) + b
        self.atk_type = s.split(" ")[1]
        self.init = int(s.split(" ")[-1])
        self.attacks = None

        self.__class__.max_init = max(self.__class__.max_init, self.init)

    @property
    def effective_power(self):
        return self.atk * self.units

    @property
    def sort_key(self):
        return self.effective_power * (self.max_init + 1) + self.init

    def effective_damage_taken(self, from_unit):
        t = from_unit.atk_type
        if t in self.immune:
            return 0
        a = from_unit.effective_power
        if t in self.weak:
            a *= 2
        return a

    def effective_damage_given(self, to_unit):
        return to_unit.effective_damage_taken(from_unit=self)

    def pick(self, from_units):
        self.attacks = None
        # dmg, unit, sort
        m = (0, 0, 0)
        for u in from_units:
            d = self.effective_damage_given(u)
            if d > m[0] or (d == m[0] and u.sort_key > m[2]):
                m = (d, u, u.sort_key)
        if m[0] == 0:
            return
        self.attacks = m[1]
        from_units.discard(m[1])

    def attack(self):
        if self.units <= 0 or self.attacks is None or self.attacks.units <= 0:
            return 0

        a = self.effective_damage_given(self.attacks)
        a //= self.attacks.hp
        self.attacks.units -= a
        return min(a, 1)


def read(boost):
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    n = 0
    u = [[], []]
    for r in t:
        if r == "":
            n += 1
        if "units" not in r:
            continue
        u[n].append(Unit(r, boost if n == 0 else 0))
    return u


def sim(boost=0):
    IMM, INF = read(boost)

    while True:
        if not IMM or not INF:
            break
        IMM.sort(key=lambda i: -i.sort_key)
        INF.sort(key=lambda i: -i.sort_key)
        other = set(INF)
        for u in IMM:
            u.pick(from_units=other)
        other = set(IMM)
        for u in INF:
            u.pick(from_units=other)
        all = IMM + INF
        all.sort(key=lambda i: -i.init)
        did_attack = 0
        for u in all:
            did_attack |= u.attack()
        if not did_attack:
            return [[], []]
        IMM = list(filter(lambda i: i.units > 0, IMM))
        INF = list(filter(lambda i: i.units > 0, INF))
    return IMM, INF


def check(boost):
    return sum(map(lambda i: i.units, sim(boost)[0]))


def easy():
    IMM, INF = sim()

    print(sum(map(lambda i: i.units, IMM + INF)))


def hard():
    b = 1
    while check(b) == 0:
        b *= 2

    lower = b // 2
    upper = b
    r = 0
    while upper - lower > 1:
        d = (upper - lower) // 2 + lower
        v = check(d)
        if v:
            r = v
            upper = d
        else:
            lower = d
    print(r)


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
if __name__ == "__main__":
    easy()
    hard()