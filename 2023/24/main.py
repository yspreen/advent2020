import pathlib
from os import environ
from z3 import Solver, Real, And, sat


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(" @", ",").splitlines()
    return lmap(lambda r: lmap(int, r.split(", ")), s)


def collides(a, b):
    apx, apy, _, avx, avy, _ = a
    bpx, bpy, _, bvx, bvy, _ = b

    # turn into m * x + c
    am = avy / avx
    ac = apy - apx * am
    bm = bvy / bvx
    bc = bpy - bpx * bm

    if am == bm:
        return False  # parallel
    x = (bc - ac) / (am - bm)
    y = am * x + ac

    if (x - apx) / avx < 0:
        return False  # in past (a)
    if (x - bpx) / bvx < 0:
        return False  # in past (b)

    MIN = 2e14
    MAX = 4e14
    return MIN <= x <= MAX and MIN <= y <= MAX


def easy():
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if collides(t[i], t[j]):
                c += 1
    print(c)


teststr = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
N = len(t)
if __name__ == "__main__":
    easy()
