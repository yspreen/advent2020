import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(lambda r: lmap(int, r.split(": ")), s.splitlines())


def easy():
    s = 0
    for a, b in t:
        if a % ((b - 1) * 2) == 0:
            s += a * b
    print(s)


def hard():
    n = 0
    while True:
        n += 1
        for a, b in t:
            if (a + n) % ((b - 1) * 2) == 0:
                break
            if a == t[-1][0]:
                print(n)
                return


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
