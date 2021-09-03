import pathlib


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    return t[0], [[i[:4], *map(int, i[5:].split(" "))] for i in t[1:]]


def fact(N):
    n = 0
    for a in range(N):
        if N % (a + 1) == 0:
            n += a + 1
    print(n)


def easy():
    fact(945)


def hard():
    fact(10551345)


DIR = pathlib.Path(__file__).parent.absolute()
ip, t = read()
ip = int(ip[4])


if __name__ == "__main__":
    easy()
    hard()
