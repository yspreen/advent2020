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


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]
mv_3d = [
    (-1, 0, 0),  # U
    (1, 0, 0),  # D
    (0, -1, 0),  # L
    (0, 1, 0),  # R
    (0, 0, -1),  # B
    (0, 0, 1),  # F
]


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

    def __str__(self):
        s = "ore_cost_ore: " + str(self.ore_cost_ore)
        s += "; clay_cost_ore: " + str(self.clay_cost_ore)
        s += "; silver_cost_ore: " + str(self.silver_cost_ore)
        s += "; silver_cost_clay: " + str(self.silver_cost_clay)
        s += "; geo_cost_ore: " + str(self.geo_cost_ore)
        s += "; geo_cost_silver: " + str(self.geo_cost_silver)
        return s

    def potential_builds(self, resources, timeline):
        pot = []
        if resources.ore >= self.ore_cost_ore and "O" not in timeline.ignore_robots:
            pot += ["O"]
        if resources.ore >= self.clay_cost_ore and "C" not in timeline.ignore_robots:
            pot += ["C"]
        if (
            resources.ore >= self.silver_cost_ore
            and resources.clay >= self.silver_cost_clay
            and "S" not in timeline.ignore_robots
        ):
            pot += ["S"]
        if (
            resources.ore >= self.geo_cost_ore
            and resources.ore >= self.geo_cost_ore
            and "G" not in timeline.ignore_robots
        ):
            pot += ["G"]
        return pot


class Resources:
    def __init__(self, ore=0, clay=0, obs=0, geo=0):
        self.ore = ore
        self.clay = clay
        self.obs = obs
        self.geo = geo

    def add(self, robots):
        self.ore += robots.ore
        self.clay += robots.clay
        self.obs += robots.obs
        self.geo += robots.geo

    def remove(self, robot, blueprint):
        ore = self.ore
        clay = self.clay
        obs = self.obs
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
            obs -= blueprint.geo_cost_silver
        return Resources(ore, clay, obs, geo)


class Robots:
    def __init__(self, ore=0, clay=0, obs=0, geo=0):
        self.ore = ore
        self.clay = clay
        self.obs = obs
        self.geo = geo

    def add(self, robot):
        if robot == "O":
            return Robots(self.ore + 1, self.clay, self.obs, self.geo)
        if robot == "C":
            return Robots(self.ore, self.clay + 1, self.obs, self.geo)
        if robot == "S":
            return Robots(self.ore, self.clay, self.obs + 1, self.geo)
        if robot == "G":
            return Robots(self.ore, self.clay, self.obs, self.geo + 1)


class Timeline:
    def __init__(self, blueprint, resources, robots):
        self.blueprint = blueprint
        self.resources = resources
        self.robots = robots
        self.ignore_robots = set([])

    def futures(self):
        pot_robots = self.blueprint.potential_builds(self.resources, self)
        self.resources.add(self.robots)
        futures = [self]
        for robot in pot_robots:
            futures.append(self.build(robot))
            self.ignore_robots.add(robot)
        return futures

    def build(self, robot):
        return Timeline(
            self.blueprint,
            self.resources.remove(robot, self.blueprint),
            self.robots.add(robot),
        )


def easy():
    blueprints = [Blueprint(*r) for r in t]
    print(blueprints[0])

    for blueprint in blueprints:
        timelines = [Timeline(blueprint, Resources(), Robots(ore=1))]
        for i in range(24):
            print(i)
            new_timelines = []
            for timeline in timelines:
                new_timelines += timeline.futures()
            timelines = new_timelines


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
