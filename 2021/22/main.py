import numpy as np
import re
import pathlib


def read():
    with open(DIR / "input") as f:
        s = re.sub(
            ".\=",
            "",
            (f.read() if teststr == "" else teststr)
            .replace("on ", "1,")
            .replace("off ", "0,")
            .replace("..", ","),
        ).splitlines()
    return lmap(lambda r: lmap(int, r.split(",")), s)


def step(A, v, x1, x2, y1, y2, z1, z2):
    if x1 > 50 or x2 < -50:
        return
    if y1 > 50 or y2 < -50:
        return
    if z1 > 50 or z2 < -50:
        return
    x1 = max(-50, min(50, x1)) + 50
    x2 = max(-50, min(50, x2)) + 50
    y1 = max(-50, min(50, y1)) + 50
    y2 = max(-50, min(50, y2)) + 50
    z1 = max(-50, min(50, z1)) + 50
    z2 = max(-50, min(50, z2)) + 50
    A[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = v


def easy():
    A = np.zeros((101, 101, 101), dtype=np.int32)
    for r in t:
        step(A, *r)
    print(A.sum())


class Cube:
    def __init__(self, x1, x2, y1, y2, z1, z2, operation=1) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.operation = operation
        self.subtract = []
        self.volume = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * operation

    def intersect(self, other):
        if not self.intersects(other):
            return
        x1 = max(self.x1, other.x1)
        x2 = min(self.x2, other.x2)
        y1 = max(self.y1, other.y1)
        y2 = min(self.y2, other.y2)
        z1 = max(self.z1, other.z1)
        z2 = min(self.z2, other.z2)

        new_sub = Cube(x1, x2, y1, y2, z1, z2, -self.operation)
        for sub in self.subtract:
            sub.intersect(new_sub)
        self.subtract.append(new_sub)

    def total_volume(self):
        return self.volume + sum([s.total_volume() for s in self.subtract])

    def intersects(self, other):
        if self.x1 > other.x2 or other.x1 > self.x2:
            return False
        if self.y1 > other.y2 or other.y1 > self.y2:
            return False
        if self.z1 > other.z2 or other.z1 > self.z2:
            return False
        return True


def hard():
    for cube, on_off in [(Cube(*c[1:]), c[0]) for c in t]:
        for other in cubes:
            other.intersect(cube)
        if on_off:
            cubes.append(cube)
    print(sum([c.total_volume() for c in cubes]))


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t, cubes = read(), []
if __name__ == "__main__":
    easy()
    hard()
