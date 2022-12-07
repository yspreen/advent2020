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
    return s[1:]


def parent_dir(path):
    path = "/".join(path.split("/")[:-1])
    if path == "":
        return "/"
    return path


def run():
    path = "/"
    sizes = {}
    for line in t:
        if line.startswith("$ cd"):
            new_dir = line.split(" ")[-1]
            if new_dir == "..":
                path = parent_dir(path)
            else:
                path += ("" if path == "/" else "/") + new_dir
            sizes[path] = sizes.get(path, 0)
        elif line[0] in "0123456789":
            num = int(line.split(" ")[0])
            for dir in tree(path):
                sizes[dir] = sizes.get(dir, 0)
                sizes[dir] += num

    s, size_list = 0, []
    for key, value in sizes.items():
        if value <= 100000:
            s += value
        size_list += [value]
    print(s)

    size_list.sort()
    target = 30000000 - (70000000 - sizes["/"])
    for key in size_list:
        if key >= target:
            return print(key)


def tree(path):
    result = [path]
    while path != "/":
        path = parent_dir(path)
        result += [path]
    return result


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    run()
