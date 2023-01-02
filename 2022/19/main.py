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
from multiprocessing import Pool


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
        N,
        ore_cost_ore,
        clay_cost_ore,
        silver_cost_ore,
        silver_cost_clay,
        geo_cost_ore,
        geo_cost_silver,
    ):
        self.N = N
        self.ore_cost_ore = ore_cost_ore
        self.clay_cost_ore = clay_cost_ore
        self.silver_cost_ore = silver_cost_ore
        self.silver_cost_clay = silver_cost_clay
        self.geo_cost_ore = geo_cost_ore
        self.geo_cost_silver = geo_cost_silver

        self.max_silver = geo_cost_silver * N
        self.max_ore = geo_cost_ore * N // 2 + self.max_silver * silver_cost_ore // 2
        self.max_clay = self.max_silver * silver_cost_ore // 2

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


class Timeline:
    def __init__(self, blueprint, resources, robots):
        self.blueprint = blueprint
        self.resources = resources
        self.robots = robots
        self.dont_build_next = set()

    def futures(self, max_geodes, time_left, time_left_with_new_builds, max_ore):
        if (
            time_left * self.robots.geo + time_left_with_new_builds + self.resources.geo
            < max_geodes
        ):
            return []
        next_possible = set()
        for next_robot in {"O", "C", "S", "G"} - self.dont_build_next:
            if self.blueprint.can_build(self.resources, next_robot):
                next_possible.add(next_robot)
        self.resources = self.resources.add(self.robots)
        self.dont_build_next |= next_possible
        futures = [self]
        for next_robot in next_possible:
            if next_robot == "O" and (
                self.resources.ore >= self.blueprint.max_ore
                or self.robots.ore == max_ore
            ):
                continue
            if next_robot == "C" and self.resources.clay >= self.blueprint.max_clay:
                continue
            if next_robot == "S" and self.resources.silver >= self.blueprint.max_silver:
                continue
            futures.append(self.build(next_robot))
        return futures

    def build(self, robot):
        return Timeline(
            self.blueprint,
            self.resources.remove(robot, self.blueprint),
            self.robots.add(robot),
        )


def run_blueprint(blueprint):
    N = blueprint.N
    current_best = max_geodes = 0
    for max_ore in range(1, N):
        timelines = [Timeline(blueprint, Resources(), Robots(ore=1))]
        time_left = N
        for j in range(N):
            time_left -= 1
            time_left_with_new_builds = (time_left * (time_left + 1)) // 2
            new_timelines = []
            for timeline in timelines:
                max_for_timeline = (
                    timeline.resources.geo + time_left * timeline.robots.geo
                )
                if max_for_timeline > max_geodes:
                    max_geodes = max_for_timeline
                new_timelines += timeline.futures(
                    max_geodes, time_left, time_left_with_new_builds, max_ore
                )
            timelines = new_timelines
        new_best = max([t.resources.geo for t in timelines] + [0])
        if new_best == current_best:
            return new_best
        current_best = new_best
    return current_best


def easy():
    blueprints = [Blueprint(24, *r) for r in t]

    with Pool(16) as p:
        results = p.map(run_blueprint, blueprints)

    s = 0
    for i, m in enumerate(results):
        s += m * (i + 1)
    print(s)


def hard():
    blueprints = [Blueprint(32, *r) for r in t]

    with Pool(16) as p:
        results = p.map(run_blueprint, blueprints[:3])

    print(prod(results))


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
