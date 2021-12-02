import pathlib


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()


def easy():
    n, b = 0, 9999
    for a in t:
        if int(a) > b:
            n += 1
        b = int(a)
    print(n)


def hard():
    n = 0
    b = 9999
    for i in range(len(t) - 2):
        a = int(t[i]) + int(t[i + 1]) + int(t[i + 2])
        if a > b:
            n += 1
        b = a
    print(n)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
