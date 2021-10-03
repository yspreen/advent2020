import pathlib
from math import sqrt


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def presents(x, limit=9e9, mult=10):
    sq = int(sqrt(x)) + 1
    values = {1, x}
    for num in range(2, sq):
        if x % num == 0:
            s = x // num
            if s <= limit:
                values.add(num)
            if num <= limit:
                values.add(s)
    return sum(values) * mult


def easy():
    for i in range(int(8e5), t)[::8]:
        if presents(i) >= t:
            return print(i)


def hard():
    for i in range(int(8e5), t)[::8]:
        if presents(i, 50, 11) >= t:
            return print(i)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = int(read())
if __name__ == "__main__":
    easy()
    hard()
