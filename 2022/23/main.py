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


def read():
    with open(DIR / "input") as f:
        s = (
            (f.read() if teststr == "" else teststr)
            .replace(".", "0")
            .replace("#", "1")
            .splitlines()
        )
    return np.array(lmap(lambda r: lmap(int, r), s), dtype=int)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]


class Elf:
    all_positions = {}
    all_elves = []
    proposal = {}
    someone_moved = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.proposed_pos = (0, 0)
        self.last_stored_position = (x, y)
        Elf.all_positions[(x, y)] = self
        self.order = deepcopy(default_order)
        Elf.all_elves.append(self)

    def change_order(self):
        self.order = self.order[1:] + [self.order[0]]

    def after_move(self):
        x, y = self.last_stored_position
        assert Elf.all_positions[(x, y)] == self
        del Elf.all_positions[(x, y)]
        x, y = self.x, self.y
        assert Elf.all_positions.get((x, y), None) is None
        Elf.all_positions[(x, y)] = self
        self.last_stored_position = (x, y)

    def get_proposal(self):
        """-   If there is no Elf in the N, NE, or NW adjacent positions, the Elf
            proposes moving *north* one step.
        -   If there is no Elf in the S, SE, or SW adjacent positions, the Elf
            proposes moving *south* one step.
        -   If there is no Elf in the W, NW, or SW adjacent positions, the Elf
            proposes moving *west* one step.
        -   If there is no Elf in the E, NE, or SE adjacent positions, the Elf
            proposes moving *east* one step."""
        x, y = self.x, self.y
        if (
            Elf.all_positions.get((x, y - 1), None) is None
            and Elf.all_positions.get((x - 1, y - 1), None) is None
            and Elf.all_positions.get((x + 1, y - 1), None) is None
            and Elf.all_positions.get((x, y + 1), None) is None
            and Elf.all_positions.get((x - 1, y + 1), None) is None
            and Elf.all_positions.get((x + 1, y + 1), None) is None
            and Elf.all_positions.get((x - 1, y), None) is None
            and Elf.all_positions.get((x + 1, y), None) is None
        ):
            return
        for dir in self.order:
            if dir == "W":
                if (
                    Elf.all_positions.get((x, y - 1), None) is None
                    and Elf.all_positions.get((x - 1, y - 1), None) is None
                    and Elf.all_positions.get((x + 1, y - 1), None) is None
                ):
                    return x, y - 1
            if dir == "E":
                if (
                    Elf.all_positions.get((x, y + 1), None) is None
                    and Elf.all_positions.get((x - 1, y + 1), None) is None
                    and Elf.all_positions.get((x + 1, y + 1), None) is None
                ):
                    return x, y + 1
            if dir == "S":
                if (
                    Elf.all_positions.get((x + 1, y), None) is None
                    and Elf.all_positions.get((x + 1, y - 1), None) is None
                    and Elf.all_positions.get((x + 1, y + 1), None) is None
                ):
                    return x + 1, y
            if dir == "N":
                if (
                    Elf.all_positions.get((x - 1, y), None) is None
                    and Elf.all_positions.get((x - 1, y - 1), None) is None
                    and Elf.all_positions.get((x - 1, y + 1), None) is None
                ):
                    return x - 1, y

    def propose(self):
        self.proposed_pos = None
        pos = self.get_proposal()
        self.change_order()
        if pos is None:
            return
        if Elf.proposal.get(pos, None) is None:
            Elf.proposal[pos] = self
            self.proposed_pos = pos
            return
        other_elf = Elf.proposal[pos]
        other_elf.proposed_pos = None

    def move(self):
        pos = self.proposed_pos
        if pos is None:
            return
        Elf.someone_moved = True
        self.x, self.y = pos
        self.after_move()


default_order = ["N", "S", "W", "E"]


def easy():
    for x, y in zip(*np.where(t == 1)):
        Elf(x, y)

    for _ in range(10):
        for e in Elf.all_elves:
            e.propose()
        for e in Elf.all_elves:
            e.move()
        Elf.proposal = {}
        Elf.someone_moved = False

    min_x = inf
    min_y = inf
    max_x = -inf
    max_y = -inf
    for x, y in Elf.all_positions:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    print(((max_x - min_x) + 1) * ((max_y - min_y) + 1) - len(Elf.all_elves))


def hard():
    N = 10
    while True:
        N += 1
        for e in Elf.all_elves:
            e.propose()
        for e in Elf.all_elves:
            e.move()
        if not Elf.someone_moved:
            return print(N)
        Elf.proposal = {}
        Elf.someone_moved = False


teststr = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
.............."""
teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
