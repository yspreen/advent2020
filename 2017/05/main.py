import pathlib


def lmap(*a):
    return list(map(*a))


teststr = """"""


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(int, filter(None, s.splitlines()))


def easy():
    n = p = 0
    try:
        while True:
            t[p] += 1
            p += t[p] - 1
            n += 1
    except:
        pass
    print(n)


def hard():
    n = p = 0
    try:
        while True:
            x = -1 if t[p] >= 3 else 1
            t[p] += x
            p += t[p] - x
            n += 1
    except:
        pass
    print(n)


DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    t = read()
    hard()
