import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: r.replace("]", "[").split("["), s)


def is_abba(s):
    for i in range(len(s) - 3):
        if s[i] != s[i + 1] and s[i + 1] == s[i + 2] and s[i] == s[i + 3]:
            return True
    return False


def get_aba(s):
    aba = set()
    for i in range(len(s) - 2):
        if s[i] != s[i + 1] and s[i] == s[i + 2]:
            aba.add(s[i + 1] + s[i] + s[i + 1])
    return aba


def easy():
    count = 0
    for row in t:
        flip = False
        has_abba = 0
        for bit in row:
            abba = is_abba(bit)
            if flip and abba:
                has_abba = 0
                break
            if abba and not flip:
                has_abba = 1
            flip = not flip
        count = count + 1 if has_abba else count
    print(count)


def hard():
    count = 0
    for row in t:
        pos = "+".join(row[::2])
        neg = "-".join(row[1::2])
        for bab in get_aba(pos):
            if bab in neg:
                count += 1
                break
    print(count)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()