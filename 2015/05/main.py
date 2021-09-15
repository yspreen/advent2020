import re
import pathlib


def nice(s):
    return (
        re.search(r"[aeiou].*[aeiou].*[aeiou]", s)
        and re.search(r"(.)\1", s)
        and not re.search(r"(ab|cd|pq|xy)", s)
    )


def nice2(s):
    return re.search(r"(..).*\1", s) and re.search(r"(.).\1", s)


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()


def easy():
    print(sum([1 if nice(s) else 0 for s in t]))


def hard():
    print(sum([1 if nice2(s) else 0 for s in t]))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
