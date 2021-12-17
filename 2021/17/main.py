import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return lmap(int, s.split("x=")[1].replace(", y=", "..").split(".."))


def step(x, y, vx, vy):
    x += vx
    y += vy
    vx -= 1 if vx > 0 else 0
    vy -= 1
    return x, y, vx, vy


def run(vx, vy):
    x = y = 0
    while x <= xmax and y >= ymin and (x < xmin or y > ymax):
        x, y, vx, vy = step(x, y, vx, vy)
    return x <= xmax and y >= ymin


def easy():
    for i in range(-ymin):
        startval = i = -ymin - i
        y = 0
        while y > ymax:
            y -= i
            i += 1
        if y < ymin:
            continue
        return print(sumto(startval - 1))


def hard():
    pairs = []
    for vx in range(xmax + 1):
        for vy in range(ymin, -ymin):
            if run(vx, vy):
                pairs.append((vx, vy))
    print(len(pairs))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
sumto = lambda x: (x + 1) * x // 2
xmin, xmax, ymin, ymax = read()
if __name__ == "__main__":
    easy()
    hard()
