import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return list(reversed(sorted(map(int, s))))


def easy():
    options = set()
    for num in range(2 ** len(t) - 1):
        b = "".join(reversed(("{:0" + str(len(t)) + "b}").format(num)))
        comb, s, i = [], 0, 0
        for i, e in enumerate(b):
            if e == "0":
                continue
            s += t[i]
            comb.append(t[i])
            if s > 150:
                break
        if s == 150:
            options.add(b)  # (tuple(sorted(comb)))
    print(len(options))
    options = [o.count("1") for o in options]
    print(len([o for o in options if o == min(options)]))


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
