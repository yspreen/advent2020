import pathlib


class Cluster:
    def __init__(self, p):
        self.points = set([p])


class Pos:
    items = []

    def dist(self, other):
        return sum(map(lambda i: abs(other.p[i] - self.p[i]), range(4)))

    def __init__(self, s):
        self.p = list(map(int, s.split(",")))
        self.cluster = Cluster(self)
        merge = []
        for i in self.items:
            if i.dist(self) <= 3:
                merge.append(i)
        self.items.append(self)
        for i in merge:
            self.cluster.points |= i.cluster.points
            for p in i.cluster.points:
                p.cluster = self.cluster


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()
    for r in t:
        Pos(r)


def easy():
    s = set()
    for i in Pos.items:
        s |= {i.cluster}
    print(len(s))


def hard():
    return


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
read()
if __name__ == "__main__":
    easy()
    hard()