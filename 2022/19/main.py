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
        s = (f.read() if teststr == "" else teststr).replace(":", "").splitlines()
    return lmap(lambda r: list(filter(None, lmap(maybeint, r.split(" "))))[1:], s)


def maybeint(line):
    try:
        return int(line)
    except Exception:
        return None


class Blueprint:
    def __init__(
        self,
        ore_cost_ore,
        clay_cost_ore,
        silver_cost_ore,
        silver_cost_clay,
        geo_cost_ore,
        geo_cost_silver,
    ):
        self.ore_cost_ore = ore_cost_ore
        self.clay_cost_ore = clay_cost_ore
        self.silver_cost_ore = silver_cost_ore
        self.silver_cost_clay = silver_cost_clay
        self.geo_cost_ore = geo_cost_ore
        self.geo_cost_silver = geo_cost_silver

    def can_build(self, resources, robot):
        if robot == "O":
            return resources.ore >= self.ore_cost_ore
        if robot == "C":
            return resources.ore >= self.clay_cost_ore
        if robot == "S":
            return (
                resources.ore >= self.silver_cost_ore
                and resources.clay >= self.silver_cost_clay
            )
        if robot == "G":
            return (
                resources.ore >= self.geo_cost_ore
                and resources.silver >= self.geo_cost_silver
            )
        assert False, f"unreachable {robot}"


class Resources:
    def __init__(self, ore=0, clay=0, silver=0, geo=0):
        self.ore = ore
        self.clay = clay
        self.silver = silver
        self.geo = geo

    def add(self, robots):
        return Resources(
            self.ore + robots.ore,
            self.clay + robots.clay,
            self.silver + robots.silver,
            self.geo + robots.geo,
        )

    def remove(self, robot, blueprint):
        ore = self.ore
        clay = self.clay
        silver = self.silver
        geo = self.geo
        if robot == "O":
            ore -= blueprint.ore_cost_ore
        if robot == "C":
            ore -= blueprint.clay_cost_ore
        if robot == "S":
            ore -= blueprint.silver_cost_ore
            clay -= blueprint.silver_cost_clay
        if robot == "G":
            ore -= blueprint.geo_cost_ore
            silver -= blueprint.geo_cost_silver
        return Resources(ore, clay, silver, geo)

    def to_tuple(self):
        return (self.ore, self.clay, self.silver, self.geo)


class Robots:
    def __init__(self, ore=0, clay=0, silver=0, geo=0):
        self.ore = ore
        self.clay = clay
        self.silver = silver
        self.geo = geo

    def add(self, robot):
        if robot == "O":
            return Robots(self.ore + 1, self.clay, self.silver, self.geo)
        if robot == "C":
            return Robots(self.ore, self.clay + 1, self.silver, self.geo)
        if robot == "S":
            return Robots(self.ore, self.clay, self.silver + 1, self.geo)
        if robot == "G":
            return Robots(self.ore, self.clay, self.silver, self.geo + 1)

    def to_tuple(self):
        return (self.ore, self.clay, self.silver, self.geo)


class Timeline:
    def __init__(self, blueprint, resources, robots):
        self.blueprint = blueprint
        self.resources = resources
        self.robots = robots

    def futures(self):
        next_possible = []
        added_G = False
        if self.blueprint.can_build(self.resources, "G"):
            next_possible = ["G"]
            added_G = True
        else:
            for next_robot in ["O", "C", "S"]:
                if self.blueprint.can_build(self.resources, next_robot):
                    next_possible.append(next_robot)
        self.resources = self.resources.add(self.robots)
        futures = [self]
        for next_robot in next_possible:
            futures.append(self.build(next_robot))
        return futures, added_G

    def build(self, robot):
        return Timeline(
            self.blueprint,
            self.resources.remove(robot, self.blueprint),
            self.robots.add(robot),
        )

    def to_tuple(self):
        return (self.resources.to_tuple(), self.robots.to_tuple())


def run_blueprint(blueprint):
    m = 0
    timelines = [Timeline(blueprint, Resources(), Robots(ore=1))]
    for j in range(24):
        # print(j)
        new_timelines = set()
        m_ = m
        for timeline in timelines:
            if timeline.robots.geo < m:
                continue
            futures, added_G = timeline.futures()
            if m_ != m and not added_G:
                continue
            tuples = {t.to_tuple() for t in futures}
            new_timelines |= tuples
            if added_G:
                m_ = m + 1
        m = m_
        timelines = [
            Timeline(blueprint, Resources(*res), Robots(*rob))
            for res, rob in new_timelines
        ]
    return max([t.resources.geo for t in timelines])


def easy():
    blueprints = [Blueprint(*r) for r in t]
    # print(blueprints[0])

    from multiprocessing import Pool

    with Pool(16) as p:
        results = p.map(run_blueprint, blueprints)

    s = 0
    for i, m in enumerate(results):
        s += m * (i + 1)
    print(s)


def hard():
    return


teststr = """    Blueprint 1:       Each ore robot costs 4 ore.       Each clay robot costs 2 ore.       Each obsidian robot costs 3 ore and 14 clay.       Each geode robot costs 2 ore and 7 obsidian.
    Blueprint 2:       Each ore robot costs 2 ore.       Each clay robot costs 3 ore.       Each obsidian robot costs 3 ore and 8 clay.       Each geode robot costs 3 ore and 12 obsidian."""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
