import re
import pathlib


def read():
    with open(DIR / "input") as f:
        s = re.sub(r"[,\.]", "", f.read() if teststr == "" else teststr).splitlines()[0]
    return int(s.split(" ")[-3]), int(s.split(" ")[-1])


def diag(x, y):
    return x + y - 2


def sum_to(diag):
    return diag * (diag + 1) // 2


def pos(x, y):
    return sum_to(diag(x, y)) + (diag(x, y) + 1 - y - 1 + 1)


def next(n):
    return (n * 252533) % 33554393


def easy():
    n = 20151125
    for _ in range(pos(X, Y)):
        n = next(n)
    print(n)


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
Y, X = read()
if __name__ == "__main__":
    easy()
    hard()
