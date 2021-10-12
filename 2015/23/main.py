import re
import pathlib


def may_int(s):
    if s in "ab":
        return "ab".index(s)
    try:
        return int(s)
    except:
        return s


def read():
    with open(DIR / "input") as f:
        s = re.sub(r"[\+,]", "", f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(may_int, r.split(" ")), s)


def do(i):
    ins = t[i]
    if ins[0] == "hlf":
        r[ins[1]] //= 2
    if ins[0] == "tpl":
        r[ins[1]] *= 3
    if ins[0] == "inc":
        r[ins[1]] += 1
    if ins[0] == "jmp":
        return ins[1]
    if ins[0] == "jie" and not (r[ins[1]] % 2):
        return ins[2]
    if ins[0] == "jio" and r[ins[1]] == 1:
        return ins[2]
    return 1


def run(a):
    i, N, r[0], r[1] = 0, len(t), a, 0
    while i < N:
        i += do(i)
    print(r[1])


def easy():
    run(0)


def hard():
    run(1)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t, r = read(), [0, 0]
if __name__ == "__main__":
    easy()
    hard()
