import pathlib


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def next(seq):
    r, prev, count = "", "", 0
    for e in seq:
        if e != prev and prev != "":
            r += str(count) + prev
            count = 0
        count += 1
        prev = e
    return r + str(count) + prev


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    for _ in range(40):
        t = next(t)
    print(len(t))
    for _ in range(10):
        t = next(t)
    print(len(t))
