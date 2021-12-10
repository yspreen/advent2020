import pathlib


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()


S = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
B = "([{<)]}>"


def easy():
    E = 0
    for l in t:
        I.append(l)
        s = []
        for c in l:
            i = B.index(c)
            if i < 4:
                s += [i]
            else:
                if s[-1] != i - 4:
                    E += S[c]
                    I.pop()
                    break
                s.pop()
    print(E)


def hard():
    E = []
    for l in I:
        s, S = [], 0
        for c in l:
            i = B.index(c)
            if i < 4:
                s += [i]
            else:
                s.pop()
        for c in reversed(s):
            S *= 5
            S += c + 1
        E.append(S)
    print(sorted(E)[len(E) // 2])


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t, I = read(), []
if __name__ == "__main__":
    easy()
    hard()
