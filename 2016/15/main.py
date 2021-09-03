import pathlib
from copy import deepcopy


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(".", "").splitlines()
    return lmap(lambda r: lmap(int, map(lambda i: r.split(" ")[i], [3, 11])), s)


def run(t):
    for i in range(len(t)):
        t[i][1] += i + 1
        t[i][1] %= t[i][0]

    N = 0
    for i in range(len(t)):
        m = (t[i][0] - t[i][1]) % t[i][0]
        X = 1
        for j in range(i):
            X *= t[j][0]
        while N % t[i][0] != m:
            N += X
    print(N)


def easy():
    run(deepcopy(t))


def hard():
    run(t + [[11, 0]])


teststr = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
