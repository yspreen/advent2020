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


def flipside(side):
    return int("".join(reversed("{0:010b}".format(side))), 2)


class Tile:
    items = {}
    sides = {}
    topleft = None

    def __init__(self, id, a, flipped=False):
        self.id = int(id)
        if flipped:
            a = np.flip(a, 0)
        else:
            Tile(self.id + 10000, a.copy(), True)
        self.a = a
        Tile.items[self.id] = self
        self.sides = list()
        self.neighbors = [None] * 4
        self.did_set = False
        for l in [
            a[0],  # u 0
            a.T[-1],  # r 1
            reversed(a[-1]),  # d 2
            reversed(a.T[0]),  # l 3
        ]:
            s = int("".join([str(i) for i in l]), 2)
            self.sides.append(s)
            Tile.sides[s] = Tile.sides.get(s, set())
            Tile.sides[s].add(self.id)

    def set(self):
        if self.did_set:
            return
        self.did_set = True
        if self.id > 10000:
            other = self.id - 10000
        else:
            other = self.id + 10000
        Tile.remove(other)
        topleft = True
        for d, side in enumerate(self.sides):
            flip = flipside(side)
            other = list(Tile.sides[flip] - set([self.id]))
            if len(other) != 1:
                continue
            self.place(d, flip, other[0])
            if d in [0, 3]:
                topleft = False
        if topleft:
            Tile.topleft = self

    def place(self, dir, side, id):
        tile = Tile.items[id]
        self.neighbors[dir] = tile
        mirror = (2 + 2 * (dir % 2)) - dir
        tile.rotate_until(side, mirror)
        tile.set()

    def rotate_until(self, side, dir):
        while self.sides[dir] != side:
            self.rotate()

    def rotate(self, k=1):
        for _ in range(k % 4):
            self.a = np.rot90(self.a)
            self.sides = self.sides[1:] + self.sides[:1]

    @classmethod
    def get_matrix(cls):
        tiles = [[None for _ in range(12)] for _ in range(12)]
        d = i = j = 0
        tile = cls.topleft
        while tile is not None:
            tiles[i][j] = tile.a[1:-1, 1:-1]
            tile_ = tile.neighbors[1 + 2 * d]
            if tile_ != None:
                j += 1 - 2 * d
                tile = tile_
                continue
            tile = tile.neighbors[2]
            d = 1 - d
            i += 1
        tiles = [np.hstack(tuple(t)) for t in tiles]
        return np.vstack(tuple(tiles))

    @classmethod
    def remove(cls, id):
        tile = cls.items.get(id, None)
        if tile is None:
            return
        del cls.items[id]
        for s in tile.sides:
            cls.sides[s].discard(id)


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").split("\n\n")
    if t[-1] == "":
        t.pop()
    for i, e in enumerate(t):
        a = e.split("\n")[1:]
        if a[-1] == "":
            a.pop()
        a = [[0 if j == "." else 1 for j in l] for l in a]
        t[i] = Tile(e.split("\n")[0][5:-1], np.array(a, dtype=np.int32))


t = read()
monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split(
    "\n"
)
monster = [[1 if j == "#" else 0 for j in l] for l in monster]
monster = np.array(monster, dtype=np.int32)


def easy():
    edges = list()
    for s in Tile.sides.values():
        if len(s) == 1:
            edges.extend([i % 10000 for i in s])
    counts = {e: edges.count(e) for e in set(edges)}
    print(prod([k for k, v in counts.items() if v == 4]))


def find_match(A, B):
    matches = []
    n = A.shape[0] - B.shape[0]
    m = A.shape[1] - B.shape[1]
    for i, j in product(range(n + 1), range(m + 1)):
        B_ = np.pad(B, ((i, n - i), (j, m - j)))
        if (A - B_).min() == 0:
            matches.append(B_)
    if matches:
        return matches


def orientations(A):
    o = []
    for _ in range(2):
        A = np.flip(A, 0)
        for _ in range(4):
            A = np.rot90(A)
            o.append(A.copy())
    return o


def hard():
    list(Tile.items.values())[0].set()
    a = Tile.get_matrix()
    for A in orientations(a):
        matches = find_match(A, monster)
        if matches is not None:
            break
    for match in matches:
        A -= match
    print(A.sum())


if __name__ == "__main__":
    easy()
    hard()
