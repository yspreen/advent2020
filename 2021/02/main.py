import pathlib


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()


def easy():
    b = a = 0

    for line in t:
        verb = line.split(" ")[0]
        num = int(line.split(" ")[-1])
        if verb == "forward":
            a += num
        if verb == "up":
            b -= num
        if verb == "down":
            b += num
    print(a * b)


def hard():
    d = h = a = 0

    for line in t:
        verb = line.split(" ")[0]
        num = int(line.split(" ")[-1])
        if verb == "forward":
            h += num
            d += num * a
        if verb == "up":
            a -= num
        if verb == "down":
            a += num
    print(h * d)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
