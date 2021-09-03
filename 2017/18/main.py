import pathlib
from string import ascii_lowercase


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
        self.sound = self.i = 0
        self.R["p"] = id
        self.buf = []
        self.locked = False

    def step(self, rcv=None, part_one=False):
        self.locked = False
        if rcv is not None:
            self.buf.append(rcv)
        r = t[self.i]
        o = 1
        a = r[1]
        v = None
        if isinstance(a, str) and r[0] == "jgz":
            a = self.R[a]
        if len(r) > 2:
            b = r[2]
            if isinstance(b, str):
                b = self.R[b]
        if r[0] == "snd":
            if part_one:
                self.sound = self.R[a]
            else:
                self.sound += 1
                v = self.R[a]
        if r[0] == "set":
            self.R[a] = b
        if r[0] == "add":
            self.R[a] += b
        if r[0] == "mul":
            self.R[a] *= b
        if r[0] == "mod":
            self.R[a] %= b
        if r[0] == "rcv":
            if part_one and a != 0:
                print(self.sound)
                return 1
            if not part_one:
                if not self.buf:
                    self.locked = True
                    return
                self.R[a] = self.buf.pop(0)
        if r[0] == "jgz" and a > 0:
            o = b
        self.i += o
        return v


def easy():
    v = VM()
    while not v.step(part_one=1):
        continue


def hard():
    a, b, i = VM(0), VM(1), None

    while not a.locked or not b.locked:
        i = a.step(i)
        i = b.step(i)
    print(b.sound)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()