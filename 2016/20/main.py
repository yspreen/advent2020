import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(int, r.split("-")), s)


def easy():
    t.sort(key=lambda i: i[0])
    i = min_allowed = 0
    while True:
        if t[i][0] > min_allowed:
            return print(min_allowed)
        min_allowed = max(min_allowed, t[i][1] + 1)
        i += 1


def hard():
    for i in range(len(t)):
        for j in range(i):
            if t[j][1] >= t[i][0]:
                if t[i][1] > t[j][1]:
                    t[j][1] = t[i][1]
                t[i] = [-1, -1]
                break
    N = 4294967296
    for start, end in t:
        if start < 0:
            continue
        N -= end - start + 1
    print(N)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
