import numpy as np
import re
import pathlib
import json
from functools import reduce, cache
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256
from os import environ
from sortedcontainers import SortedSet
from collections import defaultdict


def consolidate_graph(graph):
    """
    Consolidates an undirected graph by collapsing linear paths between intersections into single edges
    with associated distances.

    :param graph: A dictionary representing the graph, where keys are nodes and values are lists of neighbors.
    :return: A new graph with consolidated paths and intersections only.
    """

    def is_intersection(node):
        """
        Determines if a node is an intersection (more than two neighbors or a dead end).

        :param node: The node to check.
        :return: True if the node is an intersection, False otherwise.
        """
        return len(graph[node]) != 2

    def find_next_intersection(start, prev_node):
        """
        Recursive function to find the next intersection starting from a given node.

        :param start: The starting node of the path.
        :param prev_node: The previous node in the path to avoid backtracking.
        :return: A tuple of the next intersection node and the total distance.
        """
        for neighbor in graph[start]:
            if neighbor != prev_node:
                if is_intersection(neighbor):
                    return neighbor, 1
                else:
                    next_intersection, distance = find_next_intersection(
                        neighbor, start
                    )
                    return next_intersection, distance + 1
        return start, 0  # Dead end

    consolidated_graph = {}

    for node in graph:
        if is_intersection(node):
            consolidated_graph[node] = []
            for neighbor in graph[node]:
                if neighbor != node:  # Avoid looping back to the same node
                    end_node, distance = find_next_intersection(neighbor, node)
                    if end_node != node:  # Avoid adding the same node
                        consolidated_graph[node].append((end_node, distance + 1))

    return consolidated_graph


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(str, r), s)


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


@cache
def neighbors(x, y, step):
    if step == 1:
        if t[x][y] == "v":
            return {(x + 1, y)}
        if t[x][y] == "^":
            return {(x - 1, y)}
        if t[x][y] == ">":
            return {(x, y + 1)}
        if t[x][y] == "<":
            return {(x, y - 1)}
    n = set()
    for d_x, d_y in mv:
        x_ = x + d_x
        y_ = y + d_y
        if x_ < 0 or y_ < 0:
            continue
        if x_ >= N or y_ >= M:
            continue
        if t[x_][y_] == "#":
            continue
        n.add((x_, y_))
    return n


def DFS(start, goal, graph):
    longest = 0
    stack = llist([(start, 0)])
    visited = set()

    while stack:
        current, path_len = stack.last.value

        if current not in visited:
            visited.add(current)

            if current == goal and path_len > longest:
                longest = path_len

            for neighbor, cost in graph[current]:
                if neighbor in visited:
                    continue
                stack.append((neighbor, path_len + cost))
        else:
            stack.pop()
            visited.remove(current)

    return longest


def run(step):
    graph = {}
    ps = [(0, 1)]
    visited = set(ps)
    for p in ps:
        for n in neighbors(*p, step):
            graph[p] = graph.get(p, []) + [n]
            if n not in visited:
                ps.append(n)
                visited.add(n)
    graph = consolidate_graph(graph)
    print(DFS((0, 1), (N - 1, M - 2), graph))


def main():
    run(1)
    run(2)


teststr = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
N = len(t)
M = len(t[0])
if __name__ == "__main__":
    main()
