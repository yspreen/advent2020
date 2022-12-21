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
from sympy import symbols, solve


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: r.replace(": ", " = "), s)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]


def subs(vars, s, var_a, var_b):
    s = s.replace(var_a, str(vars[var_a]))
    s = s.replace(var_b, str(vars[var_b]))
    return s


def easy():
    solved = set([])
    root = None
    vars = {}
    while "root" not in solved:
        for row in t:
            start = row.split(" = ")[0]
            end = row.split(" = ")[1]
            if start in solved:
                continue
            if re.sub(r"[0-9\s]+", "", end) == "":
                vars[start] = eval(end)
                solved.add(start)
                continue
            parts = end.split(" ")
            var_a = parts[0]
            var_b = parts[-1]
            if var_a not in solved or var_b not in solved:
                continue
            vars[start] = eval(subs(vars, end, var_a, var_b))
            solved.add(start)

    print(int(vars["root"]))


def hard():
    from sympy.core.sympify import sympify
    from sympy.parsing.sympy_parser import parse_expr
    from sympy import simplify

    statements = {}
    for row in t:
        start = row.split(" = ")[0]
        end = f"({row.split(' = ')[1]})"
        statements[start] = end
    statements["humn"] = " x "

    lhs, rhs = statements["root"].replace("(", "").replace(")", "").split("+")

    didrepl = True
    while didrepl:
        didrepl = False
        for key, value in statements.items():
            if key in lhs:
                didrepl = True
                lhs = lhs.replace(key, value)
    didrepl = True
    while didrepl:
        didrepl = False
        for key, value in statements.items():
            if key in rhs:
                didrepl = True
                rhs = rhs.replace(key, value)

    lhs = simplify(sympify(lhs))
    rhs = simplify(sympify(rhs))

    sol = solve(lhs - rhs)

    print(str(sol)[1:-1])


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
