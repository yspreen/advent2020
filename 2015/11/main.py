import pathlib

z = ord("z")
a = ord("a")


def count_up(pw, digit=0):
    c = ord(pw[-1 - digit]) + (2 if pw[-1 - digit] in "hnk" else 1)
    if c > z:
        c = a
    pw[-1 - digit] = chr(c)
    if c == a:
        count_up(pw, digit + 1)
    return pw


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def meets(pw):
    if "i" in pw or "o" in pw or "l" in pw:
        return False
    last = count_abc = aa = abc = skip_last = 0
    for c in pw:
        c, skip_last = ord(c), skip_last - 1
        if last == c and skip_last != 0:
            aa, skip_last = aa + 1, 1
        if c == last + 1:
            count_abc += 1
            if count_abc == 2:
                abc = 1
        else:
            count_abc = 0
        last = c
    return aa >= 2 and abc


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    pw = list(t)
    while not meets(pw):
        count_up(pw)
    print("".join(pw))
    count_up(pw)
    while not meets(pw):
        count_up(pw)
    print("".join(pw))
