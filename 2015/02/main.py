import pathlib
from math import prod


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    print(sum(map(lambda r: area(*map(int, r.split("x"))), s)))
    print(sum(map(lambda r: bow(*map(int, r.split("x"))), s)))


def area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l + prod(sorted([l, w, h])[:2])


def bow(l, w, h):
    return l * w * h + 2 * sum(sorted([l, w, h])[:2])


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
if __name__ == "__main__":
    read()
