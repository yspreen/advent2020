import pathlib
from functools import reduce


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return lmap(str, s.splitlines()[0].split(","))


def reduce():
    global t
    replaced = True
    while replaced:
        replaced = False
        for k, v in {"ne": "sw", "nw": "se"}.items():
            try:
                a = t.index(k)
                b = t.index(v)
                del t[max(a, b)]
                del t[min(a, b)]
                replaced = 1
            except:
                pass
    replaced = True
    while replaced:
        replaced = False
        for k, v in {"ne": "s", "nw": "s", "se": "n", "sw": "n"}.items():
            try:
                a = t.index(k)
                b = t.index(v)
                t[a] = v + k[1]
                del t[b]
                replaced = 1
            except:
                pass
    replaced = True
    while replaced:
        replaced = False
        for k, v in {"nw": "ne", "sw": "se"}.items():
            try:
                a = t.index(k)
                b = t.index(v)
                t[a] = k[0]
                del t[b]
                replaced = 1
            except:
                pass
    replaced = True
    while replaced:
        replaced = False
        for k, v in {"n": "s"}.items():
            try:
                a = t.index(k)
                b = t.index(v)
                del t[max(a, b)]
                del t[min(a, b)]
                replaced = 1
            except:
                pass


def easy():
    reduce()
    print(len(t))


def hard():
    global t
    t_ = read()
    t = []
    m = 0
    for w in t_:
        t += [w]
        reduce()
        m = max(m, len(t))
    print(m)


teststr = ""  # """ne,ne,sw,sw"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
