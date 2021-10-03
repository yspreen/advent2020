import pathlib
from math import sqrt


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def presents(x):
    sq = int(sqrt(x)) + 1
    values = {1, x}
    for num in range(2, sq):
        if x % num == 0:
            values.add(num)
            values.add(x // num)
    return sum(values) * 10


def presents2(x):
    sq = int(sqrt(x)) + 1
    values = {1, x}
    for num in range(2, sq):
        if x % num == 0:
            s = x // num
            if s <= 50:
                values.add(num)
            if num <= 50:
                values.add(s)
    return sum(values) * 11


def easy():
    for i in range(int(8e5), t)[::8]:
        if presents(i) >= t:
            return print(i)


def hard():
    for i in range(int(8e5), t)[::8]:
        if presents2(i) >= t:
            return print(i)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = int(read())
if __name__ == "__main__":
    easy()
    hard()
