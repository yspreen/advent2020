import re
import pathlib


def read():
    with open(DIR / "input") as f:
        s = re.sub(
            r"Sue \d+: ", "", (f.read() if teststr == "" else teststr)
        ).splitlines()
    return lmap(lambda r: lmap(str, r.split(", ")), s)


def easy():
    print([i + 1 for i, s in enumerate(t) if len(set(s) & set(card)) == 3][0])


def hard():
    c = {l.split(": ")[0]: int(l.split(": ")[1]) for l in card}
    for i, a in enumerate(t):
        s = 0
        for l in a:
            name, val = l.split(": ")[0], int(l.split(": ")[1])
            if name in ["cats", "trees"]:
                s += 1 if val > c[name] else 0
            elif name in ["pomeranians", "goldfish"]:
                s += 1 if val < c[name] else 0
            else:
                s += 1 if val == c[name] else 0
        print(i + 1 if s == 3 else "", end="\n" if s == 3 else "")


card = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".splitlines()
teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
    hard()
