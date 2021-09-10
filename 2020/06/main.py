import pathlib
from functools import reduce
from string import ascii_lowercase

DIR = pathlib.Path(__file__).parent.absolute()


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").split("\n\n")
    if t[-1] == "":
        t.pop()
    t = [l.split("\n") for l in t]
    if t[-1][-1] == "":
        t[-1].pop()

    return t


def easy():
    t = read()

    t = [len(reduce(lambda a, b: a | set(list(b)), e, set())) for e in t]
    print(sum(t))


def hard():
    t = read()

    t = [
        len(reduce(lambda a, b: a & set(list(b)), e, set(list(ascii_lowercase))))
        for e in t
    ]
    print(sum(t))


if __name__ == "__main__":
    easy()
    hard()
