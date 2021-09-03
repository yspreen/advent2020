import pathlib


def lmap(*a):
    return list(map(*a))


class Group:
    items = []
    garbage = [0]

    def __init__(self, s, start=0, score=1):
        self.items.append(self)
        i = start + 1
        self.children = []
        self.score = score
        garbage = False
        while i < len(s):
            if s[i] == "!" and garbage:
                i += 1
            elif s[i] == ">" and garbage:
                garbage = False
            elif s[i] == "<" and not garbage:
                garbage = True
            elif s[i] == "{" and not garbage:
                child = Group(s, i, score + 1)
                i = child.end
                self.children.append(child)
            elif s[i] == "}" and not garbage:
                break
            elif garbage:
                self.garbage[0] += 1

            i += 1
        self.end = i


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return Group(s.splitlines()[0])


def easy():
    print(sum([i.score for i in Group.items]))


def hard():
    print(Group.garbage[0])


teststr = ""  #'{<{o"i!a,<{i<a>}'  # """{{{},{},{{}}}}"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()