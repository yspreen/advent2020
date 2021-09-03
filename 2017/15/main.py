import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(lambda r: int(r.split(" ")[-1]), s.splitlines())


def easy():
    c = 0
    a, b = t
    for _ in range(40000000):
        a *= A
        b *= B
        a %= M
        b %= M
        if a & N == b & N:
            c += 1
    print(c)


def hard():
    c = 0
    a, b = t
    for _ in range(5000000):
        while True:
            a *= A
            a %= M
            if not a & 3:
                break
        while True:
            b *= B
            b %= M
            if not b & 7:
                break
        if a & N == b & N:
            c += 1
    print(c)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
A, B, M, N = 16807, 48271, 2147483647, 2 ** 16 - 1
if __name__ == "__main__":
    easy()
    hard()
