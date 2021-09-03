import pathlib


class CircularNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = self if next is None else next

    def insert(self, value):
        self.next = self.__class__(value, self.next)
        return self.next


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return int(s.splitlines()[0])


def easy():
    n = CircularNode(0)
    for i in range(2017):
        for _ in range(t):
            n = n.next
        n = n.insert(i + 1)
    print(n.next.value)


def hard():  # 1, 7, 27
    n = l = 0
    for i in range(50000000):
        n += t + 1
        n %= i + 1
        if n == 0:
            l = i + 1
    print(l)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()