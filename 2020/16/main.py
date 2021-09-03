import pathlib
from math import prod

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").split("\n\n")
    if t[-1] == "":
        t.pop()
    t = [l.split("\n") for l in t]
    if t[-1][-1] == "":
        t[-1].pop()

    rules = []
    for l in t[0]:
        rules.append(tuple(map(int, l.split(" ")[-3].split("-"))))
        rules.append(tuple(map(int, l.split(" ")[-1].split("-"))))
    t[0] = [l.split(":")[0] for l in t[0]]
    t[1] = list(map(int, t[1][1].split(",")))
    t[2] = [list(map(int, l.split(","))) for l in t[2][1:]]
    return t + [rules]


t = read()


def easy():
    invalids = 0
    for i, row in enumerate(t[2]):
        for num in row:
            valid = False
            for rule in t[3]:
                if rule[0] <= num <= rule[1]:
                    valid = True
                    break
            if not valid:
                invalids += num
                t[2][i] = None
                break
    t[2] = list(filter(None, t[2]))
    print(invalids)


def hard():
    possible = {name: set([i for i in range(len(t[1]))]) for name in t[0]}
    for row in t[2]:
        for i, num in enumerate(row):
            last = False
            for j, rule in enumerate(t[3]):
                curr = rule[0] <= num <= rule[1]
                if j % 2 == 1 and not (curr or last):
                    possible[t[0][j // 2]].discard(i)
                last = curr
    final = {}
    for _ in range(20):
        for k, v in possible.items():
            if len(v) == 1:
                final[k] = list(v)[0]
                for other in possible.values():
                    other.discard(final[k])
    print(prod([t[1][v] for k, v in final.items() if "departure " in k]))


if __name__ == "__main__":
    easy()
    hard()
