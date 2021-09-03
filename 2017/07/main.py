import pathlib


class Program:
    items = {}
    root = set()
    leafs = set()

    def __init__(self, s):
        self.name = s.split(" ")[0]
        self.items[self.name] = self
        self.weight = int(s.split("(")[1].split(")")[0])
        if "->" in s:
            self.children = s.split(" -> ")[1].split(", ")
        else:
            self.children = []
            self.leafs.add(self)
        self.child_weight = 0
        self.parent = None
        self.root.add(self)

    @classmethod
    def resolve_all(cls):
        for v in cls.items.values():
            v.resolve()
        cls.root = list(cls.root)[0]

    def resolve(self):
        for i, v in enumerate(self.children):
            v = self.items[v]
            self.children[i] = v
            v.parent = self
            self.root.discard(v)

    def calc_weights(self):
        for c in self.children:
            c.calc_weights()
            self.child_weight += c.total_weight

    @property
    def bal(self):
        return len(set([c.total_weight for c in self.children])) < 2

    @property
    def total_weight(self):
        return self.child_weight + self.weight


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    lmap(Program, s.splitlines())
    Program.resolve_all()


def easy():
    print(Program.root.name)


def hard():
    Program.root.calc_weights()
    n = filter(lambda i: not i.bal, Program.items.values())
    n = list(filter(lambda i: all([j.bal for j in i.children]), n))[0]
    others = sorted([i.total_weight for i in n.children])[1]
    c = list(filter(lambda i: i.total_weight != others, n.children))[0]
    print(others - c.child_weight)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
read()
if __name__ == "__main__":
    easy()
    hard()
