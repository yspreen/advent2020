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
        s = f.read() if teststr == "" else teststr
    s = s.replace("Valve ", "")
    s = re.sub(r"[a-z\=\;\,]", "", s)
    s = re.sub(r" +", " ", s)
    s = s.splitlines()
    return lmap(
        lambda line: [line[0], line[1], line[2:]],
        lmap(lambda r: lmap(maybeint, r.split(" ")), s),
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
]


def to_tuple(closed):
    l = []
    for k in closed_valves:
        if k in closed:
            l.append(k)

    return tuple(l)


def BFS(start):
    global M
    options = [(start, 29, to_tuple(closed_valves), 0, 0)]
    history = {options[0]: [start]}

    while options:
        new_o = []
        for params in options:
            pos, time, closed, flow, released = params
            M = max(M, released)
            if released == 1659:
                print("optimal")
                print(history[params])
            if time == 0:
                continue
            if pos in closed and flows[pos] > 0:
                closed_ = to_tuple(set(closed) - set([pos]))
                flow_ = flow + flows[pos]
                new_state = (pos, time - 1, closed_, flow_, released + flow_)
                new_o.append(new_state)
                history[new_state] = history.get(params, []) + [new_state[0]]
            for new_p, cost in paths_d[pos]:
                if time > cost and len(closed) > 0:
                    new_state = (
                        new_p,
                        time - cost,
                        closed,
                        flow,
                        released + flow * cost,
                    )
                    new_o.append(new_state)
                    history[new_state] = history.get(params, []) + [new_state[0]]
                else:
                    new_state = (new_p, 0, closed, flow, released + flow * time)
                    new_o.append(new_state)
                    history[new_state] = history.get(params, []) + [new_state[0]]
        options = list(set(new_o))


def elephant(start):
    global M
    options = [(start, start, 25, to_tuple(closed_valves), 0, 0)]

    while options:
        new_o = []
        for posA, posB, time, closed, flow, released in options:
            M = max(M, released)
            if time == 0:
                continue
            if pos in closed and flows[pos] > 0:
                closed_ = to_tuple(set(closed) - set([pos]))
                flow_ = flow + flows[pos]
                new_o.append((pos, time - 1, closed_, flow_, released + flow_))
            for new_p, cost in paths_d[pos]:
                if time > cost and len(closed) > 0:
                    new_o.append(
                        (new_p, time - cost, closed, flow, released + flow * cost)
                    )
                else:
                    new_o.append((new_p, 0, closed, flow, released + flow * time))
        options = list(set(new_o))


paths = {}
paths_d = {}
flows = {}
closed_valves = []
M = 0


def calc_paths(start):
    pos = [(start, 0)]
    paths_d[start] = []
    v = set([start])

    while pos:
        new_p = []
        for p, c in pos:
            c += 1
            for dest in paths[p]:
                if dest in v:
                    continue
                v |= set([dest])
                if flows[dest] > 0:
                    paths_d[start].append((dest, c))
                else:
                    new_p.append((dest, c))
        pos = new_p


def easy():
    for start, c, dest in t:
        paths[start] = dest
        flows[start] = c

    calc_paths("AA")

    for pos in paths.keys():
        if flows[pos] == 0:
            continue
        closed_valves.append(pos)
        calc_paths(pos)

    BFS("AA")
    print(M)


def hard():
    return


teststr = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
