import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return lmap(int, s.split(","))


def run(mod):
    m = (inf, inf)
    for i in range(mi, ma):
        cost = 0
        for num in t:
            cost += mod(abs(num - i))
        if cost < m[0]:
            m = (cost, i)
    print(m[0])


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
mi, ma = min(t), max(t)
if __name__ == "__main__":
    run(int)
    run(lambda i: (i * (i + 1)) // 2)
