import pathlib
from itertools import product


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[2:]

    t = {}
    size = None
    for name, size, use, avail, _ in map(lambda r: list(filter(None, r.split(" "))), s):
        x, y = map(lambda i: int(i[1:]), name.split("-")[1:])
        size, use, avail = map(lambda i: int(i[:-1]), [size, use, avail])
        t[(x, y)] = (size, use, avail)
        size = (x + 1, y + 1)
    return size, t


def easy():
    valid = 0
    for x1, y1, x2, y2 in product(*map(lambda i: range(size[i]), [0, 1, 0, 1])):
        if x1 == x2 and y1 == y2:
            continue
        _, use1, _ = t[(x1, y1)]
        if use1 == 0:
            continue
        _, _, avail2 = t[(x2, y2)]
        if use1 <= avail2:
            empty[0], empty[1] = (x2, y2)
            valid += 1
        if use1 > 200:
            empty[2] = min(empty[2], x1)
    print(valid)


def hard():
    steps = empty[1] + abs(empty[0] - (size[0] - 2)) + 1
    steps += 5 * (size[0] - 2)
    steps += 2 * (empty[0] - (empty[2] - 1))
    print(steps)

    if not print_map:
        return
    for y, x in product(*map(lambda i: range(size[i]), [1, 0])):
        if x == 0:
            print()
        if x == 0 and y == 0:
            print("S", end="")
        elif x == size[0] - 1 and y == 0:
            print("G", end="")
        elif t[(x, y)][1] > 100:
            print("#", end="")
        elif t[(x, y)][1] == 0:
            print("-", end="")
        else:
            print(".", end="")
    print()


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
size, t = read()
empty = [0, 0, float("inf")]
print_map = 0
if __name__ == "__main__":
    easy()
    hard()
