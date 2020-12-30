import numpy as np
import re
import pathlib

DIR = pathlib.Path(__file__).parent.absolute()


def seat_id(s):
    return int(s, 2)


def read():
    with open(DIR / "input.txt") as f:
        t = (
            f.read()
            .replace("\r", "")
            .replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1")
            .split("\n")
        )
    if t[-1] == "":
        t.pop()

    t.sort()
    return t


def easy():
    t = read()
    print(seat_id(t[-1]))


def hard():
    t = [seat_id(s) for s in read()]

    last = -1
    for seat in t:
        if last == seat - 2:
            print(seat - 1)
            return
        last = seat


if __name__ == "__main__":
    easy()
    hard()