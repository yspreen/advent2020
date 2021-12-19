import pathlib
from itertools import permutations


class Pair:
    def __init__(self, stream=None, remove_first=True, parent=None, level=0, pos=0):
        self.parent = parent
        self.level = level
        self.pos = pos
        self.left = 0
        self.right = 0
        if stream is None:
            return
        _ = next(stream) if remove_first else ""
        self.left = self.unwrap_child(stream, L)
        assert next(stream) == ","
        self.right = self.unwrap_child(stream, R)
        assert next(stream) == "]"

    def unwrap_child(self, stream, pos):
        i = next(stream)
        if i != "[":
            return int(i)
        else:
            return Pair(stream, False, self, self.level + 1, pos)

    def explode(self):
        l, r = self.left, self.right

        node, pos = self.parent, self.pos
        while node is not None and pos != R:
            node, pos = node.parent, node.pos
        if node is not None:
            if not isinstance(node.left, Pair):
                node.left += l
            else:
                node.left.add_right(l)

        node, pos = self.parent, self.pos
        while node is not None and pos != L:
            node, pos = node.parent, node.pos
        if node is not None:
            if not isinstance(node.right, Pair):
                node.right += r
            else:
                node.right.add_left(r)

        if self.pos == L:
            self.parent.left = 0
        if self.pos == R:
            self.parent.right = 0

    def add_right(self, num):
        if isinstance(self.right, Pair):
            return self.right.add_right(num)
        self.right += num

    def add_left(self, num):
        if isinstance(self.left, Pair):
            return self.left.add_left(num)
        self.left += num

    def find_explodable(self) -> bool:
        if self.level >= 4:
            self.explode()
            return True
        for p in [self.left, self.right]:
            if isinstance(p, Pair) and p.find_explodable():
                return True
        return False

    def find_split(self) -> bool:
        if not isinstance(self.left, Pair) and self.left >= 10:
            i = self.left
            self.left = Pair(parent=self, level=self.level + 1, pos=L)
            self.left.left = i // 2
            self.left.right = i - i // 2
            return True
        if isinstance(self.left, Pair) and self.left.find_split():
            return True
        if not isinstance(self.right, Pair) and self.right >= 10:
            i = self.right
            self.right = Pair(parent=self, level=self.level + 1, pos=R)
            self.right.left = i // 2
            self.right.right = i - i // 2
            return True
        if isinstance(self.right, Pair) and self.right.find_split():
            return True
        return False

    def __str__(self) -> str:
        return "[" + str(self.left) + "," + str(self.right) + "]"

    def step(self):
        while True:
            if self.find_explodable():
                continue
            if self.find_split():
                continue
            return

    def add(self, other):
        new = Pair()
        new.left, new.right = self, other
        self.pos, other.pos = L, R
        self.parent = other.parent = new
        [i.add_level() for i in [self, other]]
        return new

    def add_level(self):
        self.level += 1
        [(i.add_level() if isinstance(i, Pair) else 0) for i in [self.left, self.right]]

    def magnitude(self):
        l = self.left.magnitude() if isinstance(self.left, Pair) else self.left
        r = self.right.magnitude() if isinstance(self.right, Pair) else self.right
        return 3 * l + 2 * r


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return s


def easy():
    t = lmap(lambda r: Pair(iter(r)), read())
    sum = t[0]
    for other in t[1:]:
        sum = sum.add(other)
        sum.step()
    print(sum.magnitude())


def hard():
    t, m = read(), 0

    for i, j in permutations(range(len(t)), 2):
        if i == j:
            continue
        a, b = iter(t[i]), iter(t[j])
        s = Pair(a).add(Pair(b))
        s.step()
        v = s.magnitude()
        m = max(m, v)
    print(m)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
L, R = 1, 2
if __name__ == "__main__":
    easy()
    hard()
