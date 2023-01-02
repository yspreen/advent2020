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
    except Exception:
        return line


paths = {}
flows = {}
idx = {}
valves = []
G = np.array([[0]])


def make_G():
    global G
    for pos, flow, dest in t:
        paths[pos] = dest
        flows[pos] = flow
        idx[pos] = len(valves)
        valves.append(pos)
    G = np.zeros((len(paths), len(paths)), dtype=int) + inf

    for start in valves:
        G[idx[start], idx[start]] = 0
        visited = {start}
        next_valves = {start}
        while next_valves:
            next_valves_ = set()
            for valve in next_valves:
                for path in paths[valve]:
                    if path in visited:
                        continue
                    visited |= {path}
                    next_valves_ |= {path}
                    G[idx[start], idx[path]] = min(
                        G[idx[start], idx[path]], G[idx[start], idx[valve]] + 1
                    )
                    G[idx[path], idx[start]] = min(
                        G[idx[path], idx[start]], G[idx[start], idx[valve]] + 1
                    )
            next_valves = next_valves_

    for i in reversed(range(len(valves))[1:]):
        if flows[valves[i]] == 0:
            del flows[valves[i]]
            del paths[valves[i]]
            del idx[valves[i]]
            del valves[i]
            G = np.delete(G, i, 0)
            G = np.delete(G, i, 1)
    for i, valve in enumerate(valves):
        idx[valve] = i


# Finds the minimum TSP tour cost.
# m - 2D adjacency matrix representing graph
# S - The start node (0 ≤ S < N)
def tsp(m, S):
    N = G.shape[0]
    print(N)
    # Initialize memo table.
    # Fill table with null values or +0
    memo = np.zeros((N, 2 ** N), dtype=int) + inf
    setup(m, memo, S, N)
    solve(m, memo, S, N)
    min_cost = find_min_cost(m, memo, S, N)
    tour = find_optimal_tour(m, memo, S, N)
    return (min_cost, tour)


# Initializes the memo table by caching
# the optimal solution from the start
# node to every other node.
def setup(m, memo, S, N):
    for i in range(N):
        if i == S:
            continue
        # Store the optimal value from node S
        # to each node i (this is given as input
        # in the adjacency matrix m).
        memo[i, 1 << S | 1 << i] = m[S, i]


def solve(m, memo, S, N):
    for r in range(3, N + 1):
        for subset in bit_combinations(r, N):
            if not_in(S, subset):
                continue
            for step in range(N):
                if step == S or not_in(step, subset):
                    continue
                # The subset state without the step node
                state = subset ^ (1 << step)
                min_dist = inf
                for end in range(N):
                    if end == S or end == step or not_in(end, subset):
                        continue
                    new_distance = memo[end, state] + m[end, step]
                    if new_distance < min_dist:
                        min_dist = new_distance
                memo[step, subset] = min_dist


# Returns true if the ith bit in 'subset' is not set
def not_in(i, subset):
    return ((1 << i) & subset) == 0


def bit_tuple_num(bits):
    n = 0
    for bit in bits:
        n *= 2
        n += bit
    return n


bit_combinations_cache = {}


def bit_combinations(r, n):
    if (r, n) in bit_combinations_cache:
        return bit_combinations_cache[(r, n)]
    bit_combinations_cache[(r, n)] = subsets = []
    r_combinations(0, 0, r, n, subsets)
    return subsets


# Recursive method to generate bit sets.
def r_combinations(s, at, r, n, subsets):
    if r == 0:
        subsets.append(s)
    else:
        for i in range(at, n):
            # Flip on ith bit
            s |= 1 << i
            r_combinations(s, i + 1, r - 1, n, subsets)
            # Backtrack and flip off ith bit
            s &= ~(1 << i)


def find_min_cost(m, memo, S, N):
    # The end state is the bit mask with
    # N bits set to 1 (equivalently 2**N - 1)
    end_state = (1 << N) - 1
    min_tour_cost = inf
    for e in range(N):
        if e == S:
            continue
        tour_cost = memo[e, end_state] + m[e, S]
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
    return min_tour_cost


def easy():
    make_G()
    print(bit_combinations(3, 4))
    print(tsp(G, 0))


def find_optimal_tour(m, memo, S, N):
    lastIndex = S
    state = (1 << N) - 1
    # End state
    tour = [0 for _ in range(N + 1)]
    for i in reversed(range(1, N)):
        index = -1
        for j in range(N):
            if j == S or not_in(j, state):
                continue
            if index == -1:
                index = j
            prev_dist = memo[index, state] + m[index, lastIndex]
            new_dist = memo[i, state] + m[i, lastIndex]
            if new_dist < prev_dist:
                index = j
        tour[i] = index
        state = state ^ (1 << index)
        lastIndex = index
    tour[0] = tour[N] = S
    return tour


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
inf = 9999999
t = read()
if __name__ == "__main__":
    easy()
    hard()
