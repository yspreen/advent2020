import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


class Moon:
    items = []

    states = set()
    stepcount = 0

    def __init__(self, x, y, z):
        self.pos = np.array([x, y, z], np.int32)
        self.vel = np.zeros_like(self.pos, np.int32)
        Moon.items.append(self)

    def update_vel(self):
        for moon in Moon.items:
            if moon == self:
                continue
            for dim in range(3):
                if moon.pos[dim] < self.pos[dim]:
                    self.vel[dim] -= 1
                if moon.pos[dim] > self.pos[dim]:
                    self.vel[dim] += 1

    def update_pos(self):
        self.pos += self.vel

    @property
    def potential(self):
        return abs(self.pos).sum()

    @property
    def kinetic(self):
        return abs(self.vel).sum()

    @property
    def energy(self):
        return self.potential * self.kinetic

    @classmethod
    def get_energy(cls):
        return sum([i.energy for i in cls.items])

    @classmethod
    def hash(cls, dim=-1):
        a = [(i.pos if dim < 0 else [i.pos[dim]]) for i in cls.items]
        a += [(i.vel if dim < 0 else [i.vel[dim]]) for i in cls.items]
        a = np.concatenate(a)
        return a.data.tobytes()


def read():
    Moon.items = []
    Moon.states = set()
    Moon.stepcount = 0
    with open(DIR / "input.txt") as f:
        t = (
            f.read()
            .replace("<", "")
            .replace(">", "")
            .replace("x", "")
            .replace("y", "")
            .replace("z", "")
            .replace(" ", "")
            .replace("=", "")
            .split("\n")
        )
    if t[-1] == "":
        t.pop()
    t = [Moon(*[int(i) for i in l.split(",")]) for l in t]


def step(dim=-1):
    Moon.stepcount += 1
    for m in Moon.items:
        m.update_vel()
    for m in Moon.items:
        m.update_pos()
    h = Moon.hash(dim=dim)
    if h in Moon.states:
        return True
    Moon.states.add(h)


def easy():
    read()
    for _ in range(1000):
        step()
    print(Moon.get_energy())


def lcm(a):
    l = a[0]
    for i in a[1:]:
        l = l * i // gcd(l, i)
    return l


def hard():
    constraints = []
    for dim in range(3):
        read()
        Moon.states.add(Moon.hash(dim=dim))
        while True:
            if step(dim=dim):
                constraints.append(Moon.stepcount)
                break
    print(lcm(constraints))


if __name__ == "__main__":
    easy()
    hard()
