import pathlib
from hashlib import md5


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def hash(num):
    return str(md5((t + str(num)).encode()).hexdigest())


def easy():
    i = 1
    while True:
        if hash(i).startswith("00000"):
            return print(i)
        i += 1


def hard():
    i = 1
    while True:
        if hash(i).startswith("000000"):
            return print(i)
        i += 1


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
