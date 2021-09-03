import pathlib
from sympy import solve


def read():
    with open(DIR / "input") as f:
        t = f.read().splitlines()[0]
    return Segment(t[1:-1])


def solve(before, segment):
    after = set()
    if segment.children:
        state = before
        for c in segment.children:
            state = solve(state, c)
        after = state
    elif segment.choices:
        for c in segment.choices:
            after |= solve(before, c)
    else:
        for p in before:
            direction = dirs[p]
            for c in segment.s:
                direction += c
                p = (p[0] + y_dist[c], p[1] + x_dist[c])
                dirs[p] = dirs.get(p, direction)
            after.add(p)
    return after


x_dist = {
    "N": 0,
    "E": 1,
    "S": 0,
    "W": -1,
}
y_dist = {
    "N": -1,
    "E": 0,
    "S": 1,
    "W": 0,
}


class Segment:
    unresolved = []
    items = []

    @classmethod
    def resolve(cls):
        while len(cls.unresolved):
            e = cls.unresolved.pop()
            for i in range(len(e)):
                e[i] = Segment(e[i])

    def __init__(self, s):
        self.choices = []
        self.children = []
        self.items.append(self)
        self.s = s
        segments = [-1]
        splits = [-1]
        brace_num = 0
        for i, e in enumerate(s):
            if e == "(":
                brace_num += 1
                if brace_num == 1:
                    segments.append(i)
            if e == ")":
                brace_num -= 1
                if brace_num == 0:
                    segments.append(i)
            if e == "|" and brace_num == 0:
                splits.append(i)
        segments.append(len(s))
        splits.append(len(s))

        if len(splits) > 2:
            for i in range(1, len(splits)):
                a, b = splits[i - 1], splits[i]
                self.choices.append(s[a + 1 : b])
        elif len(segments) > 2:
            for i in range(1, len(segments)):
                a, b = segments[i - 1], segments[i]
                if b - a < 2:
                    continue
                self.children.append(s[a + 1 : b])
        self.unresolved.append(self.children)
        self.unresolved.append(self.choices)


def easy():
    dirs[(0, 0)] = ""
    solve(set([(0, 0)]), t)
    print(max([len(v) for v in dirs.values()]))


def hard():
    print(len([len(v) for v in dirs.values() if len(v) >= 1000]))


DIR = pathlib.Path(__file__).parent.absolute()
t = read()
Segment.resolve()
dirs = {}

if __name__ == "__main__":
    easy()
    hard()
