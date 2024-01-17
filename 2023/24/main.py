import pathlib
from os import environ
from z3 import Solver, Real, And, sat


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(" @", ",").splitlines()
    return lmap(lambda r: lmap(int, r.split(", ")), s)


def vec_to_mc(px, py, vx, vy):
    try:
        m = vy / vx
        c = py - px * m
        return m, c
    except ZeroDivisionError:
        return 0, 0


def collide_xy(am, ac, bm, bc):
    try:
        x = (bc - ac) / (am - bm)
        y = am * x + ac
        return x, y
    except ZeroDivisionError:
        # parallel
        return None, None


def collides(a, b):
    apx, apy, _, avx, avy, _ = a
    bpx, bpy, _, bvx, bvy, _ = b

    # turn into m * x + c
    am, ac = vec_to_mc(apx, apy, avx, avy)
    bm, bc = vec_to_mc(bpx, bpy, bvx, bvy)

    x, y = collide_xy(am, ac, bm, bc)
    if x is None:
        return False

    if (x - apx) / avx < 0:
        return False  # in past (a)
    if (x - bpx) / bvx < 0:
        return False  # in past (b)

    MIN = 2e14
    MAX = 4e14
    return MIN <= x <= MAX and MIN <= y <= MAX


def can_collide(delta_vx, delta_vy):
    apx, apy, _, avx, avy, _ = t[0]
    bpx, bpy, _, bvx, bvy, _ = t[1]
    avx -= delta_vx
    avy -= delta_vy
    bvx -= delta_vx
    bvy -= delta_vy
    am, ac = vec_to_mc(apx, apy, avx, avy)
    bm, bc = vec_to_mc(bpx, bpy, bvx, bvy)
    x, y = collide_xy(am, ac, bm, bc)
    if x is None:
        return False
    for bpx, bpy, _, bvx, bvy, _ in t[2:]:
        bvx -= delta_vx
        bvy -= delta_vy
        bm, bc = vec_to_mc(bpx, bpy, bvx, bvy)
        y_ = bm * x + bc
        if abs(y_ - y) > 1:
            return False
    return True


def easy():
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if collides(t[i], t[j]):
                c += 1
    print(c)


def hard():
    def find_vx_vy():
        MAX_V = 201
        for vx in range(MAX_V * 2):
            vx -= MAX_V
            for vy in range(MAX_V * 2):
                vy -= MAX_V
                if can_collide(vx, vy):
                    return vx, vy

    vx, vy = find_vx_vy()

    apx, apy, apz, avx, avy, avz = t[0]
    bpx, bpy, bpz, bvx, bvy, bvz = t[1]
    avx -= vx
    bvx -= vx
    avy -= vy
    bvy -= vy
    am, ac = vec_to_mc(apx, apy, avx, avy)
    bm, bc = vec_to_mc(bpx, bpy, bvx, bvy)
    x, y = collide_xy(am, ac, bm, bc)
    ta = (x - apx) / avx
    tb = (x - bpx) / bvx

    vz = int(((bpz + tb * bvz) - (apz + ta * avz)) / (tb - ta))
    print(vx, vy, vz)


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
    hard()
