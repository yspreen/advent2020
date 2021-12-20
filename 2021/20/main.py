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
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(".#".index, s[0]), np.array(lmap(lambda r: lmap(".#".index, r), s[2:]))


def step(array):
    array = np.pad(array, ((3, 3), (3, 3)), "edge")
    new = np.zeros_like(array)
    for i in range(array.shape[0] - 2):
        for j in range(array.shape[1] - 2):
            n = int("".join(lmap(str, array[i : i + 3, j : j + 3].flatten())), 2)
            new[i + 1, j + 1] = band[n]
    return new[1:-1, 1:-1]


def easy():
    # aprint(np.pad(t, ((1, 1), (1, 1))))
    # aprint(step(np.pad(t, ((1, 1), (1, 1)))))
    print(step(step(np.pad(t, ((1, 1), (1, 1))))).sum())


def aprint(arr):
    for row in arr:
        for e in row:
            print(".#"[e], end="")
        print()


def hard():
    return


teststr = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
band, t = read()
if __name__ == "__main__":
    easy()
    hard()
