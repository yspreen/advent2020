import numpy as np
import re
import pathlib
import json
import random
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product
from time import sleep

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


def readkey():
    import sys
    import tty
    import termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def getkey():
    k = ""
    while k == "":
        k = readkey()
    if k == "\x1b[C":
        return 4
    elif k == "\x1b[D":
        return 3
    elif k == "\x1b[A":
        return 1
    elif k == "\x1b[B":
        return 2


directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
heading_to_direction = {1: 0, 2: 2, 3: 3, 4: 1}
direction_to_heading = {v: k for k, v in heading_to_direction.items()}


class VM:
    def read(self):
        with open(DIR / "input.txt") as f:
            t = f.read().replace("\n", "").split(",")
        if t[-1] == "":
            t.pop()
        t = [int(i) for i in t]
        self.t = {i: v for i, v in enumerate(t)}

    def op(self, i):
        code = self.t[i]
        ins = code % 100
        mode_a = digit(code, 2)
        mode_b = digit(code, 3)
        mode_c = digit(code, 4)

        a = self.t.get(i + 1, 0)
        if mode_a == 2:
            a += self.r
            mode_a = 0
        if mode_a == 0 and ins != 3:
            a = self.t.get(a, 0)
        b = self.t.get(i + 2, 0)
        if mode_b == 0:
            b = self.t.get(b, 0)
        if mode_b == 2:
            b = self.t.get(self.r + b, 0)
        c = self.t.get(i + 3, 0)
        if mode_c == 2:
            c += self.r

        if ins == 99:
            self.done = True
            return
        if ins == 1:
            self.t[c] = a + b
            return 4
        if ins == 2:
            self.t[c] = a * b
            return 4
        if ins == 3:
            if not len(self.inputs):
                return
            self.t[a] = self.inputs.pop(0)
            return 2
        if ins == 4:
            self.outputs.append(a)
            return 2
        if ins == 5:
            if a != 0:
                return b - i
            return 3
        if ins == 6:
            if a == 0:
                return b - i
            return 3
        if ins == 7:
            self.t[c] = 1 if a < b else 0
            return 4
        if ins == 8:
            self.t[c] = 1 if a == b else 0
            return 4
        if ins == 9:
            self.r += a
            return 2

    def add_goals(self):
        for i, d in enumerate(directions):
            newpos = tuple([p + d[j] for j, p in enumerate(self.pos)])
            if newpos not in self.visited:
                self.goals.append(newpos)
                self.visited.append(newpos)
            if self.origins.get(newpos, None) is None:
                self.origins[newpos] = (i, tuple(self.pos))

    def draw(self):
        if len(self.outputs) != 1:
            return
        status = self.outputs.pop()
        newpos = [p + self.direction[i] for i, p in enumerate(self.pos)]
        if status > 0:
            self.pos = newpos
            self.add_goals()
        else:
            self.setA(newpos, 1)
        if not (
            0 < (self.pos[0] + self.o) < self.A.shape[0] - 1
            and 0 < (self.pos[1] + self.o) < self.A.shape[1] - 1
        ):
            self.pad()
        if status == 2:
            self.done = True

    def move(self, heading):
        self.h = heading_to_direction[heading]
        self.calc(heading)

    def getA(self, pos):
        return self.A[pos[0] + self.o, pos[1] + self.o]

    def setA(self, pos, v):
        self.A[pos[0] + self.o, pos[1] + self.o] = v

    def calc(self, *inp):
        if self.done:
            return
        self.inputs.extend(inp)
        self.d = 0
        self.outputs = []
        while self.d is not None:
            self.i += self.d
            self.d = self.op(self.i)
            self.draw()

    def pad(self):
        n = self.A.shape[0] // 2
        self.A = np.pad(self.A, ((n, n), (n, n)))
        self.o += n

    def __init__(self):
        self.read()
        self.outputs = []
        self.inputs = []

        self.h = self.o = self.i = self.d = self.r = 0
        self.A = np.zeros((4, 4), np.int32)
        self.pos = [1, 1]
        self.done = False
        self.goals = []
        self.visited = []
        self.origins = {}
        self.add_goals()

    @property
    def direction(self):
        return directions[self.h % 4]

    def print(self):
        import os

        for i, r in enumerate(self.A):
            for j, e in enumerate(r):
                if (i, j) == (self.pos[0] + self.o, self.pos[1] + self.o):
                    print("o", end="")
                    continue
                print("#" if e == 1 else " ", end="")
            print()


v = VM()


def flip(heading):
    return heading + (heading % 2) - (1 - heading % 2)


def to(pos):
    direction = (pos[0] - v.pos[0], pos[1] - v.pos[1])
    direction = directions.index(direction)
    return direction_to_heading[direction]


def easy():
    current_goal = None
    while not v.done:
        # v.print()

        if current_goal is None:
            current_goal = v.goals.pop()
            # print("new goal: ", current_goal)
        if v.origins[current_goal][1] != tuple(v.pos):
            # print("too far:  ", v.origins[current_goal][1], "!=", tuple(v.pos))
            v.move(flip(direction_to_heading[v.origins[tuple(v.pos)][0]]))
        else:
            # print("neighbor: ", v.pos)
            v.move(to(current_goal))
            current_goal = None

        # sleep(0.01)
    pointer = tuple(v.pos)
    steps = 0
    while pointer != (1, 1):
        steps += 1
        pointer = v.origins[pointer][1]
    print(steps)


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
