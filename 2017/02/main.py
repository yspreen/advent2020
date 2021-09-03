import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        t = lmap(lambda r: lmap(int, r.split("\t")), f.read().splitlines())
    return t


def easy():
    print(sum(map(lambda r: max(r) - min(r), t)))


def hard():
    s = 0
    for r in t:
        try:
            for i, a in enumerate(r):
                for b in r[i + 1 :]:
                    a_, b_ = (a, b) if a > b else (b, a)
                    if a_ % b_ == 0:
                        s += a_ // b_
                        raise Exception()
        except:
            pass
    print(s)


DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
