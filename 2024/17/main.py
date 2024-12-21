import numpy as np
import re
import pathlib
import json
from functools import reduce, cmp_to_key
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
from os import environ


def read():
    with open(DIR / "input") as f:
        s = (
            (f.read() if teststr == "" else teststr)
            .replace("Program: ", "")
            .split("\n\n")
        )
    return lmap(lambda r: lmap(int, r.split(",")), s[1].splitlines())[0], lmap(
        lambda r: int(r.split(": ")[1]), s[0].splitlines()
    )


def maybeint(line):
    try:
        return int(line)
    except:
        return line


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
    (-1, 1),  # UR
    (1, 1),  # DR
    (-1, -1),  # UL
    (1, -1),  # DL
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
]


def BFS(start, can_walk, goal, cost_fn=None):
    cost_fn = (lambda _, __: 1) if cost_fn is None else cost_fn

    options = [(start, 0)]
    visited = set([start])

    while options:
        new_o = []
        for pos, cost in options:
            for d in mv:
                new_p = (pos[0] + d[0], pos[1] + d[1])
                if new_p[0] < 0:  # lower bound check
                    continue
                if new_p[1] < 0:  # lower bound check
                    continue
                try:
                    assert can_walk(pos, new_p)
                except:
                    continue  # upper bound check
                if new_p in visited:
                    continue
                visited.add(new_p)
                cost_ = cost + cost_fn(pos, new_p)
                new_o.append((new_p, cost_))
                if goal(new_p):
                    return cost_
        options = new_o
    return None


def combo(A, B, C, opcode):
    if opcode < 4 or opcode > 6:
        return opcode
    return [A, B, C][opcode - 4]


def print_combo(A, B, C, opcode):
    if opcode < 4 or opcode > 6:
        return str(opcode)
    return ["A", "B", "C"][opcode - 4]


def run(program, A, B, C, I):
    o = []
    ret_pointer = I + 2
    if not (0 <= I < len(program)):
        return None
    get_combo = lambda: combo(A, B, C, program[I + 1])
    opcode = program[I]
    if opcode == 0:  # adv
        if I + 1 == len(program):
            return None
        A = A // (2 ** get_combo())
    if opcode == 1:  # bxl
        if I + 1 == len(program):
            return None
        B = B ^ program[I + 1]
    if opcode == 2:  # bst
        if I + 1 == len(program):
            return None
        B = get_combo() % 8
    if opcode == 3:  # jnz
        if I + 1 == len(program):
            return None
        if A != 0:
            ret_pointer = program[I + 1]
    if opcode == 4:  # bxc
        if I + 1 == len(program):
            return None
        B = B ^ C
    if opcode == 5:  # out
        if I + 1 == len(program):
            return None
        o += [str(get_combo() % 8)]
    if opcode == 6:  # bdv
        if I + 1 == len(program):
            return None
        B = A // (2 ** get_combo())
    if opcode == 7:  # cdv
        if I + 1 == len(program):
            return None
        C = A // (2 ** get_combo())
    return ret_pointer, A, B, C, o


def pad(i):
    if i < 10:
        return f" {i}"
    return str(i)


def print_run(program, A, B, C, I):
    o = []
    ret_pointer = I + 2
    if not (0 <= I < len(program)):
        print(f"{pad(I)}: break")
        return None
    get_combo = lambda: combo(A, B, C, program[I + 1])
    get_print_combo = lambda: print_combo(A, B, C, program[I + 1])
    opcode = program[I]
    if opcode == 0:  # adv
        if I + 1 == len(program):
            return None
        A = A // (2 ** get_combo())
        print(f"{pad(I)}: A = floor(A / 2 ** {get_print_combo()})")
    if opcode == 1:  # bxl
        if I + 1 == len(program):
            return None
        B = B ^ program[I + 1]
        print(f"{pad(I)}: B = B ^ {program[I + 1]}")
    if opcode == 2:  # bst
        if I + 1 == len(program):
            return None
        B = get_combo() % 8
        print(f"{pad(I)}: B = {get_print_combo()} % 8")
    if opcode == 3:  # jnz
        if I + 1 == len(program):
            return None
        print(f"{pad(I)}: if A != 0:")
        print(f"{pad(I)}:   jump to {program[I + 1]}")
        if A != 0:
            ret_pointer = program[I + 1]
    if opcode == 4:  # bxc
        if I + 1 == len(program):
            return None
        B = B ^ C
        print(f"{pad(I)}: B = B ^ C")
    if opcode == 5:  # out
        if I + 1 == len(program):
            return None
        o += [str(get_combo() % 8)]
        print(f"{pad(I)}: print({get_print_combo()} % 8)")
    if opcode == 6:  # bdv
        if I + 1 == len(program):
            return None
        B = A // (2 ** get_combo())
        print(f"{pad(I)}: B = floor(A / 2 ** {get_print_combo()})")
    if opcode == 7:  # cdv
        if I + 1 == len(program):
            return None
        C = A // (2 ** get_combo())
        print(f"{pad(I)}: C = floor(A / 2 ** {get_print_combo()})")
    return ret_pointer, A, B, C, o


def test_reg_A(A):
    _, B, C = t[1]
    program = list(t[0])
    I = 0
    o = []

    while True:
        result = run(program, A, B, C, I)
        if result is None:
            break
        I, A, B, C, o_ = result
        o += o_
    return ",".join(o) == ",".join([str(i) for i in program])


def print_reg_A(A):
    _, B, C = t[1]
    program = list(t[0])
    I = 0
    o = []

    while True:
        result = run(program, A, B, C, I)
        if result is None:
            break
        I, A, B, C, o_ = result
        o += o_
    print(",".join(o))


def easy():
    A, B, C = t[1]
    # A = 108299861817585
    program = list(t[0])
    I = 0
    o = []

    while True:
        result = run(program, A, B, C, I)
        if result is None:
            break
        I, A, B, C, o_ = result
        o += o_
    print(",".join(o))


def calc(A, nums):
    try:
        return (((A % 8) ^ nums[3]) ^ nums[7]) ^ (A // 2 ** ((A % 8) ^ nums[3])) % 8
    except Exception:
        return


def find_number(nums, i=0, prev=0):
    if i == len(nums):
        return prev // 8
    for A in range(prev, prev + 8):
        if calc(A, nums) != nums[-i - 1]:
            continue
        future = find_number(nums, i + 1, prev=A * 8)
        if future is not None:
            return future

    return None


def hard():
    program = list(t[0])
    print(find_number(program))
    return

    A, B, C = t[1]
    # A = 0b10101001010100010000100001001010100000000000000
    A = find_number(program)
    I = 0
    o = []

    # print("A =", A)
    # print("B =", B)
    # print("C =", C)
    # print()

    while True:
        result = run(program, A, B, C, I)
        if result is None:
            break
        I, A, B, C, o_ = result
        o += o_
    print(",".join(o))
    # print(",".join([str(p) for p in program]))


teststr = """"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
