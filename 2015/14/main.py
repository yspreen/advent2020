import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: lmap(lambda i: int(r.split(" ")[i]), [3, 6, -2]), s)


def easy():
    N, m = 2503, 0
    for spd, dur, rst in t:
        dist = spd * dur * (N // (dur + rst))
        left = N % (dur + rst)
        dist += spd * dur if left > dur else spd * left
        m = max(m, dist)
    print(m)


def hard():
    r = [[0, 0, 0, dur + 1, [spd, 0], [dur, rst]] for (spd, dur, rst) in t]
    for _ in range(2503):
        m = [0, []]
        for j in range(len(r)):
            r[j][3] -= 1
            if r[j][3] == 0:
                r[j][1] = 1 - r[j][1]
                r[j][3] = r[j][5][r[j][1]]
            r[j][2] += r[j][4][r[j][1]]
            if m[0] == r[j][2]:
                m[1] += [j]
            if m[0] < r[j][2]:
                m = [r[j][2], [j]]
        for x in m[1]:
            r[x][0] += 1
    print(max([i[0] for i in r]))


teststr = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
    hard()
