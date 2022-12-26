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

    def __str__(self):
        s = "ore_cost_ore: " + str(self.ore_cost_ore)
        s += "; clay_cost_ore: " + str(self.clay_cost_ore)
        s += "; silver_cost_ore: " + str(self.silver_cost_ore)
        s += "; silver_cost_clay: " + str(self.silver_cost_clay)
        s += "; geo_cost_ore: " + str(self.geo_cost_ore)
        s += "; geo_cost_silver: " + str(self.geo_cost_silver)
        return s

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
        if robot == "O":
            self.ore -= blueprint.ore_cost_ore
        if robot == "C":
            self.ore -= blueprint.clay_cost_ore
        if robot == "S":
            self.ore -= blueprint.silver_cost_ore
            self.clay -= blueprint.silver_cost_clay
        if robot == "G":
            self.ore -= blueprint.geo_cost_ore
            self.silver -= blueprint.geo_cost_silver

    def __str__(self):
        return f"O:{self.ore} C:{self.clay} S:{self.silver} G:{self.geo}"


class Robots:
    def __init__(self, ore=0, clay=0, silver=0, geo=0):
        self.ore = ore
        self.clay = clay
        self.silver = silver
        self.geo = geo

    def add(self, robot):
        if robot == "O":
            self.ore += 1
        if robot == "C":
            self.clay += 1
        if robot == "S":
            self.silver += 1
        if robot == "G":
            self.geo += 1


class Timeline:
    def __init__(self, blueprint, resources, robots, lookahead=1):
        self.blueprint = blueprint
        self.resources = resources
        self.robots = robots
        self.lookahead = lookahead
        self.lookahead2 = lookahead + 1

    def next_robot(self):
        future = self.resources
        for _ in range(self.lookahead):
            future = future.add(self.robots)
        future2 = self.resources
        for _ in range(self.lookahead2):
            future2 = future2.add(self.robots)
        if self.blueprint.can_build(future2, "G"):
            return "G"
        if self.blueprint.can_build(future, "S"):
            return "S"
        desired_ratio = self.blueprint.silver_cost_clay / (
            self.blueprint.silver_cost_ore
        )
        if (
            self.robots.clay < self.robots.ore * desired_ratio
            and self.blueprint.can_build(future, "C")
        ):
            return "C"
        return "O"

    def step(self):
        next_robot = self.next_robot()
        can_build = next_robot and self.blueprint.can_build(self.resources, next_robot)
        self.resources = self.resources.add(self.robots)
        print(self.resources)

        if not can_build:
            return
        self.build(next_robot)
        print("build " + next_robot)

    def build(self, robot):
        self.resources.remove(robot, self.blueprint)
        self.robots.add(robot)


def easy():
    N = 24
    blueprints = [Blueprint(*r) for r in t]

    max_g = 0

    for blueprint in [blueprints[1]]:
        for lookahead in [0, 1, 2, 3, 4, 5]:
            timeline = Timeline(blueprint, Resources(), Robots(1), lookahead)
            for _ in range(N):
                timeline.step()
            if timeline.resources.geo > max_g:
                print("lookahead", lookahead)
                max_g = timeline.resources.geo
            print()
    print(max_g)


def hard():
    return


teststr = """    Blueprint 1:       Each ore robot costs 4 ore.       Each clay robot costs 2 ore.       Each obsidian robot costs 3 ore and 14 clay.       Each geode robot costs 2 ore and 7 obsidian.
    Blueprint 2:       Each ore robot costs 2 ore.       Each clay robot costs 3 ore.       Each obsidian robot costs 3 ore and 8 clay.       Each geode robot costs 3 ore and 12 obsidian."""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
