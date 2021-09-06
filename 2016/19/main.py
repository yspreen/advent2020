import pathlib
from llist import dllist as llist


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return int(s)


def easy():
    l = llist(range(t))
    i = l.first
    for _ in range(t - 1):
        l.remove(i.next if i.next else l.first)
        i = i.next if i.next else l.first
    print(l[0] + 1)


def hard():
    l = llist(range(t))
    i = l.nodeat(t // 2 - 1)
    odd = t % 2
    for _ in range(t - 1):
        l.remove(i.next if i.next else l.first)
        if odd:
            i = i.next if i.next else l.first
        odd = not odd
    print(l[0] + 1)


teststr = ""  # """5"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
