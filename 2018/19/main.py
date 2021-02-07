import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd
from itertools import permutations, product
from multiprocessing import Pool
from sympy import simplify, symbols, solve


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().splitlines()
    return t[0], [[i[:4], *map(int, i[5:].split(" "))] for i in t[1:]]


def op():
    try:
        o = t[reg[ip]]
    except:
        return True
    code, A, B, C = o

    if code == "addr":
        reg[C] = reg[A] + reg[B]
    if code == "addi":
        reg[C] = reg[A] + B
    if code == "mulr":
        reg[C] = reg[A] * reg[B]
    if code == "muli":
        reg[C] = reg[A] * B
    if code == "banr":
        reg[C] = reg[A] & reg[B]
    if code == "bani":
        reg[C] = reg[A] & B
    if code == "borr":
        reg[C] = reg[A] | reg[B]
    if code == "bori":
        reg[C] = reg[A] | B
    if code == "setr":
        reg[C] = reg[A]
    if code == "seti":
        reg[C] = A
    if code == "gtir":
        reg[C] = 1 if A > reg[B] else 0
    if code == "gtri":
        reg[C] = 1 if reg[A] > B else 0
    if code == "gtrr":
        reg[C] = 1 if reg[A] > reg[B] else 0
    if code == "eqir":
        reg[C] = 1 if A == reg[B] else 0
    if code == "eqri":
        reg[C] = 1 if reg[A] == B else 0
    if code == "eqrr":
        reg[C] = 1 if reg[A] == reg[B] else 0
    reg[ip] += 1


def easy():
    while not op():
        continue
    print(reg[0])


def hard():
    global reg

    reg = [0] * 6
    reg[0] = 1
    easy()


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
ip, t = read()
ip = int(ip[4])
reg = [0] * 6


if __name__ == "__main__":
    easy()
    hard()