import pathlib
from math import prod

DIR = pathlib.Path(__file__).parent.absolute()


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "")
    t = t.split("\n")
    if t[-1] == "":
        t.pop()
    t = [int(i) for i in t]
    t.sort()

    return t


def valids(list, startjolt=0, ones=0, threes=0):
    if len(list) == 0:
        return ones, threes
    for i, e in enumerate(list):
        if e > startjolt + 3:
            break
        excluded = list[i + 1 :]
        oneadd = 1 if e - startjolt == 1 else 0
        threeadd = 1 if e - startjolt == 3 else 0

        result = valids(excluded, e, ones + oneadd, threes + threeadd)
        if result is not None:
            return result


target = 0
valid_counts = {}


def count_valids(list, startjolt=0):
    global target

    counter = 0
    if startjolt == target:
        return 1
    for i, e in enumerate(list):
        if e > startjolt + 3:
            break
        excluded = list[i + 1 :]

        r = valid_counts.get(e, -1)
        r = r if r >= 0 else count_valids(excluded, e)
        counter += r
    valid_counts[startjolt] = counter
    return counter


def easy():
    t = read()
    t += [t[-1] + 3]

    print(prod(list(valids(t))))


def hard():
    global target
    t = read()
    t += [t[-1] + 3]
    target = t[-1]

    count_valids(t)
    print(valid_counts[0])


if __name__ == "__main__":
    easy()
    hard()
