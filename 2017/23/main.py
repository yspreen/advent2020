import pathlib
from string import ascii_lowercase
from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def lmap(*a):
    return list(map(*a))


def sint(v):
    try:
        return int(v)
    except:
        return v


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(lambda r: lmap(sint, r.split(" ")), s.splitlines())


class VM:
    def __init__(self, id=0):
        self.R = {k: 0 for k in ascii_lowercase[:16]}
        self.i = 0
        self.mul_count = 0

    def step(self, rcv=None, part_one=False):
        self.locked = False
        r = t[self.i]
        o = 1
        a = r[1]
        if isinstance(a, str) and r[0] == "jnz":
            a = self.R[a]
        b = r[2]
        if isinstance(b, str):
            b = self.R[b]
        if r[0] == "set":
            self.R[a] = b
        if r[0] == "sub":
            self.R[a] -= b
        if r[0] == "mul":
            self.mul_count += 1
            self.R[a] *= b
        if r[0] == "jnz" and a != 0:
            o = b
        self.i += o
        return self.i >= len(t)


def easy():
    v = VM()
    while not v.step():
        continue
    print(v.mul_count)


def hard():
    B = -t[5][2] + t[4][2] * t[0][2]
    C, d = B - t[7][2], -t[-2][2]
    print(len([1 for i in range(B, C + 1)[::d] if not is_prime(i)]))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()