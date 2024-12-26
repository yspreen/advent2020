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
        s = (f.read() if teststr == "" else teststr).split("\n\n")
        s1 = s[0].splitlines()
        s2 = s[1].replace(" ->", "").splitlines()
    return lmap(lambda r: lmap(maybeint, r.split(": ")), s1), lmap(
        lambda r: lmap(str, r.split(" ")), s2
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


def easy():
    val = {}
    for k, v in t[0]:
        val[k] = v

    changed = True
    while changed:
        changed = False
        for lhs, op, rhs, out in t[1]:
            if lhs in val and rhs in val and out not in val:
                if op == "AND":
                    val[out] = val[lhs] & val[rhs]
                elif op == "OR":
                    val[out] = val[lhs] | val[rhs]
                elif op == "XOR":
                    val[out] = val[lhs] ^ val[rhs]
                else:
                    val[out] = val[rhs]
                changed = True
    sorted_keys = sorted(val.keys())
    s = ""
    for k in sorted_keys:
        if k.startswith("z"):
            s = f"{val[k]}{s}"
    print(int(s, 2))


def check(wrong):
    for i in range(len(wrong)):
        for j in range(i + 1, len(wrong)):
            for k in range(j + 1, len(wrong)):
                for l in range(k + 1, len(wrong)):
                    t[1][wrong[i]][3], t[1][wrong[j]][3] = (
                        t[1][wrong[j]][3],
                        t[1][wrong[i]][3],
                    )
                    t[1][wrong[k]][3], t[1][wrong[l]][3] = (
                        t[1][wrong[l]][3],
                        t[1][wrong[k]][3],
                    )
                    if count_bit_errors(t) == 0:
                        print(",".join(sorted(wrong)))
                        return 1
                    t[1][wrong[i]][3], t[1][wrong[j]][3] = (
                        t[1][wrong[j]][3],
                        t[1][wrong[i]][3],
                    )
                    t[1][wrong[k]][3], t[1][wrong[l]][3] = (
                        t[1][wrong[l]][3],
                        t[1][wrong[k]][3],
                    )


def hard():
    swap = set()

    for lhs, op, rhs, out in t[1]:
        if out[0] == "z" and op != "XOR":
            swap.add(out)
        if (
            op == "XOR"
            and out[0] not in ["x", "y", "z"]
            and lhs[0] not in ["x", "y", "z"]
            and rhs[0] not in ["x", "y", "z"]
        ):
            swap.add(out)
        if op == "AND" and "x00" not in [lhs, rhs]:
            for lhs, op, rhs, _ in t[1]:
                if (out == lhs or out == rhs) and op != "OR":
                    swap.add(out)
        if op == "XOR":
            for lhs, op, rhs, _ in t[1]:
                if (out == lhs or out == rhs) and op == "OR":
                    swap.add(out)

    print(",".join(sorted(swap)[:-1]))


teststr = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
