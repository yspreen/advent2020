import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(list, s)


def numpad(vector, S=None):
    y, x = vector
    if S:
        return S.splitlines()[1:][y][x]
    return y * 3 + x + 1


def easy():
    p, s = (1, 1), ""
    for r in t:
        for m in r:
            m = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}[m]
            p = tuple(map(lambda i: min(2, max(0, i)), (p[0] + m[0], p[1] + m[1])))
        s += str(numpad(p))
    print(s)


def hard():
    p, s = (2, 0), ""
    for r in t:
        for m in r:
            m = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}[m]
            p_ = tuple(map(lambda i: min(4, max(0, i)), (p[0] + m[0], p[1] + m[1])))
            if sum(map(lambda i: abs(i - 2), p_)) <= 2:
                p = p_
        s += str(numpad(p, P))
    print(s)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
P = """
  1  
 234 
56789
 ABC 
  D  
"""
if __name__ == "__main__":
    easy()
    hard()