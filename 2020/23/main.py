import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product
import llist

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read(add=0):
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").replace("\n", "")
    t = llist.dllist([int(i) for i in t])

    for i in range(10, add + 1):
        t.append(i)
    i = t.first
    while i is not None:
        lookup[i.value] = i
        i = i.next

    return len(t), t


lookup = {}
N, t = read()
curr = t.first
pick = [0, 0, 0]
picknode = [0, 0, 0]


def move():
    global curr, pick, picknode

    i: llist.dllistnode = curr.next
    for k in range(3):
        i = t.first if i is None else i
        j = i.next
        picknode[k] = i
        pick[k] = t.remove(i)
        i = j
    i = curr.value - 1
    while i in pick or i < 1:
        i = (i - 1) if i > 1 else N
    j = lookup[i]
    for k in range(3):
        newnode = picknode[k]
        t.insertnode(newnode, j.next)
        lookup[newnode.value] = newnode
        j = newnode
    curr = curr.next
    curr = t.first if curr is None else curr


def easy():
    for _ in range(100):
        move()
    while t.last.value != 1:
        t.rotate(1)
    print("".join(map(str, t))[:-1])


def hard():
    global t, N, curr
    N, t = read(1000000)
    curr = t.first
    for _ in range(10000000):
        move()
    while t.last.value != 1:
        t.rotate(1)

    while True:
        try:
            print(lookup[1].next.value * lookup[1].next.next.value)
            return
        except:
            t.rotate(1)


if __name__ == "__main__":
    easy()
    hard()
