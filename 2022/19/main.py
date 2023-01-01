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

    def __str__(self):
        return f"O:{self.ore} C:{self.clay} S:{self.silver} G:{self.geo}"

    def better_than(self, other):
        return (
            self.ore > other.ore
            or self.clay > other.clay
            or self.silver > other.silver
            or self.geo > other.geo
        )


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

    def better_than(self, other):
        return (
            self.ore > other.ore
            or self.clay > other.clay
            or self.silver > other.silver
            or self.geo > other.geo
        )


class Timeline:
    max_resource_ore = None
    max_resource_clay = None
    max_resource_silver = None
    max_resource_geo = None
    max_robot_ore = None
    max_robot_clay = None
    max_robot_silver = None
    max_robot_geo = None

    def __init__(self, blueprint, resources, robots):
        self.blueprint = blueprint
        self.resources = resources
        self.robots = robots

    def copy_with_robot(self, r):
        return Timeline(self.blueprint, self.resources, self.robots, r)

    def futures(self):
        next_possible = []
        for next_robot in ["O", "C", "S", "G"]:
            if self.blueprint.can_build(self.resources, next_robot):
                next_possible.append(next_robot)
        self.resources = self.resources.add(self.robots)
        futures = [self]
        for next_robot in next_possible:
            futures.append(self.build(next_robot))
        return futures

    def build(self, robot):
        return Timeline(
            self.blueprint,
            self.resources.remove(robot, self.blueprint),
            self.robots.add(robot),
        )

    def inferior_to(self, other):
        better = self.resources.better_than(other.resources) or self.robots.better_than(
            other.robots
        )
        return not better


N = 24


def best_timelines():
    return [
        Timeline.max_resource_ore,
        Timeline.max_resource_clay,
        Timeline.max_resource_silver,
        Timeline.max_resource_geo,
        Timeline.max_robot_ore,
        Timeline.max_robot_clay,
        Timeline.max_robot_silver,
        Timeline.max_robot_geo,
    ]


def easy():
    blueprints = [Blueprint(*r) for r in t]
    # print(blueprints[0])
    s = 0

    for i, blueprint in enumerate(blueprints):
        # print(i)
        timelines = [Timeline(blueprint, Resources(), Robots(ore=1))]
        Timeline.max_resource_ore = timelines[0]
        Timeline.max_resource_clay = timelines[0]
        Timeline.max_resource_silver = timelines[0]
        Timeline.max_resource_geo = timelines[0]
        Timeline.max_robot_ore = timelines[0]
        Timeline.max_robot_clay = timelines[0]
        Timeline.max_robot_silver = timelines[0]
        Timeline.max_robot_geo = timelines[0]
        for j in range(24):
            print(j)
            new_timelines = []
            for timeline in timelines:
                new_timelines += timeline.futures()
            timelines = []
            for timeline in new_timelines:
                if timeline.resources.ore > Timeline.max_resource_ore.resources.ore:
                    Timeline.max_resource_ore = timeline
                if timeline.resources.clay > Timeline.max_resource_clay.resources.clay:
                    Timeline.max_resource_clay = timeline
                if (
                    timeline.resources.silver
                    > Timeline.max_resource_silver.resources.silver
                ):
                    Timeline.max_resource_silver = timeline
                if timeline.resources.geo > Timeline.max_resource_geo.resources.geo:
                    Timeline.max_resource_geo = timeline
                if timeline.robots.ore > Timeline.max_robot_ore.robots.ore:
                    Timeline.max_robot_ore = timeline
                if timeline.robots.clay > Timeline.max_robot_clay.robots.clay:
                    Timeline.max_robot_clay = timeline
                if timeline.robots.silver > Timeline.max_robot_silver.robots.silver:
                    Timeline.max_robot_silver = timeline
                if timeline.robots.geo > Timeline.max_robot_geo.robots.geo:
                    Timeline.max_robot_geo = timeline
            for timeline in new_timelines:
                inferior = False
                for other in best_timelines():
                    if other == timeline:
                        continue
                    if timeline.inferior_to(other):
                        inferior = True
                        break
                if not inferior:
                    timelines.append(timeline)
        m = max([timeline.resources.geo for timeline in timelines])
        print(m)
        # print(timelines[0].resources)
        s += m * (i + 1)
    # print(s)


def hard():
    return


teststr = """    Blueprint 1:       Each ore robot costs 4 ore.       Each clay robot costs 2 ore.       Each obsidian robot costs 3 ore and 14 clay.       Each geode robot costs 2 ore and 7 obsidian.
    Blueprint 2:       Each ore robot costs 2 ore.       Each clay robot costs 3 ore.       Each obsidian robot costs 3 ore and 8 clay.       Each geode robot costs 3 ore and 12 obsidian."""
# teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
