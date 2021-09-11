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


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda i: i.split(" "), s)


def register_for(letter):
    return ord(letter) - 97


def step(ptr, ins, mem):
    try:
        return unsafe_step(ptr, ins, mem)
    except:
        return 1


def toggle(t, i):
    repl = {
        "inc": "dec",
        "dec": "inc",
        "jnz": "cpy",
        "cpy": "jnz",
        "tgl": "inc",
    }
    t[i][0] = repl[t[i][0]]


def unsafe_step(ptr, ins, mem):
    instr = ins[ptr]
    delta = 1
    if instr[0] == "cpy":
        try:
            val = int(instr[1])
        except:
            val = mem[register_for(instr[1])]
        mem[register_for(instr[2])] = val
    if instr[0] == "jnz":
        try:
            val = int(instr[1])
        except:
            val = mem[register_for(instr[1])]
        if val != 0:
            try:
                delta = int(instr[2])
            except:
                delta = mem[register_for(instr[2])]
    if instr[0] == "inc":
        mem[register_for(instr[1])] += 1
    if instr[0] == "dec":
        mem[register_for(instr[1])] -= 1
    if instr[0] == "tgl":
        try:
            val = int(instr[1])
        except:
            val = mem[register_for(instr[1])]
        ptr += val
        if ptr < N:
            toggle(ins, ptr)
    return delta


def run(init=0):
    i = 0
    m = [0] * 4
    m[0] = init
    t_ = deepcopy(t)
    x = 0
    while i < N:
        x += 1
        i += step(i, t_, m)
        if x == 1000000:
            print(i, t_, m)
            return
    print(m[0])


def easy():
    run(7)


def hard():
    run(12)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
N = len(t)
if __name__ == "__main__":
    easy()
    hard()
