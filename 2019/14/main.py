import pathlib

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


class Element:
    items = {}

    def __init__(self, s):
        s = s.split(" => ")
        s[0] = [i.split(" ") for i in s[0].split(", ")]
        s[1] = s[1].split(" ")
        self.id = s[1][1]
        self.__class__.items[self.id] = self
        self.amount = int(s[1][0])
        self.requirements = []
        for a, e in s[0]:
            a = int(a)
            self.requirements.append([a, e])

    def link(self):
        for row in self.requirements:
            row[1] = self.__class__.items[row[1]]

    def resolve(self, amount=1, decimal=False):
        k = (amount - 1) // self.amount + 1
        if decimal:
            k = amount / self.amount
        r = []
        for a, e in self.requirements:
            r.append([a * k, e])
        return r, (0 if decimal else k * self.amount - amount)

    def ore_req(self, num=1, decimal=False):
        need = {e: a * num for a, e in self.requirements}
        have = {}
        while len(need) > 1:
            for element, needed in need.items():
                if element == ORE:
                    continue
                needed -= have.get(element, 0)
                if needed <= 0:
                    have[element] = -needed
                    del need[element]
                    break
                have[element] = 0
                added_needs, spare = element.resolve(needed, decimal=decimal)
                have[element] = have.get(element, 0) + spare
                for a, e in added_needs:
                    need[e] = need.get(e, 0) + a
                del need[element]
                break
        return need.get(ORE, 0)


ORE = Element("1 ORE => 1 ORE")


def read():
    with open(DIR / "input") as f:
        t = f.read().split("\n")
    if t[-1] == "":
        t.pop()
    t = [Element(l) for l in t]
    _ = [e.link() for e in t]


read()


def easy():
    print(Element.items["FUEL"].ore_req())


def hard():
    N = int(1e12)

    i = int(Element.items["FUEL"].ore_req(1, True)) + 1
    i = N // i
    while Element.items["FUEL"].ore_req(i + 1) < N:
        i += 1
    print(i)


if __name__ == "__main__":
    easy()
    hard()
