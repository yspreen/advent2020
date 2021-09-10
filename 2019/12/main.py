import numpy as np
import pathlib
from math import gcd
from multiprocessing import Pool

DIR = pathlib.Path(__file__).parent.absolute()


class Moon:
    def __init__(self, x, y, z):
        self.pos = np.array([x, y, z], np.int32)
        self.vel = np.zeros_like(self.pos, np.int32)

    def update_vel(self, items):
        for moon in items:
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


def get_energy(items):
    return sum([i.energy for i in items])


def hash(items, dim=-1):
    a = [(i.pos if dim < 0 else [i.pos[dim]]) for i in items]
    a += [(i.vel if dim < 0 else [i.vel[dim]]) for i in items]
    a = np.concatenate(a)
    return a.data.tobytes()


def read():
    with open(DIR / "input") as f:
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
    return [Moon(*[int(i) for i in l.split(",")]) for l in t]


def step(items, states=set(), dim=-1):
    for m in items:
        m.update_vel(items)
    for m in items:
        m.update_pos()
    h = hash(items, dim=dim)
    if h in states:
        return True
    states.add(h)


def easy():
    items = read()
    for _ in range(1000):
        step(items)
    print(get_energy(items))


def lcm(a):
    l = a[0]
    for i in a[1:]:
        l = l * i // gcd(l, i)
    return l


def find_constraint(dim):
    items = read()
    states = set([hash(items, dim=dim)])
    i = 0
    while True:
        i += 1
        if step(items, states, dim=dim):
            return i


def hard():
    with Pool(3) as p:
        constraints = p.map(find_constraint, [0, 1, 2])
    print(lcm(constraints))


if __name__ == "__main__":
    easy()
    hard()
