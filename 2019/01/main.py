def easy():
    import pathlib

    with open(pathlib.Path(__file__).parent.absolute() / "input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    t = [int(i) for i in t]
    t = [i // 3 for i in t]
    t = [i - 2 for i in t]

    print(sum(t))


def hard():
    import pathlib

    with open(pathlib.Path(__file__).parent.absolute() / "input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    t = [int(i) for i in t]
    t = [i // 3 for i in t]
    t = [i - 2 for i in t]

    s = sum(t)
    while sum(t) > 0:
        t = [int(i) for i in t]
        t = [i // 3 for i in t]
        t = [i - 2 for i in t]
        t = [(i if i > 0 else 0) for i in t]
        s += sum(t)

    print(s)


if __name__ == "__main__":
    easy()
    hard()