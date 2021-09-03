import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(int, s.splitlines()[0].split("\t"))


def step():
    m = (0, 0)
    for i, v in enumerate(t):
        if v > m[0]:
            m = (v, i)
    c = m[0]
    i = m[1]
    t[i] = 0
    while c > 0:
        c -= 1
        i += 1
        i %= N
        t[i] += 1


def easy():
    seen = set()

    k = 0
    while tuple(t) not in seen:
        k += 1
        seen.add(tuple(t))
        step()
    print(k)


def hard():
    easy()


teststr = ""  # """0	2	7	0"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
N = len(t)
if __name__ == "__main__":
    easy()
    hard()