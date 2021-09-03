import pathlib


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    return [[i[:4], *map(int, i[5:].split(" "))] for i in t[1:]]


def test():
    s = set()
    b = c = d = z = i = 0
    while True:
        b = c | A
        c = C
        while True:
            c += b & 255
            c &= D
            c *= B
            c &= D
            if b < 256:
                if i == 0:
                    print(c)
                if c in s:
                    print(d)
                    return
                d = c
                i = 1
                s.add(c)
                break
            else:
                b //= 256


def easy():
    return


def hard():
    test()


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
A, B, C, D = t[6][2], t[11][2], t[7][1], t[10][2]


if __name__ == "__main__":
    easy()
    hard()
