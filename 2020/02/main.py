def easy():
    with open("2020.2/input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    t_ = []
    for l in t:
        l = l.split("-")
        a = int(l[0])
        l = l[1].split(" ")
        b = int(l[0])
        c = l[1][0]
        d = l[-1]

        t_.append((a, b, c, d))
    t = t_

    correct = 0
    for i in t:
        a, b, c, d = i
        n = len(list(filter(lambda i: i == c, d)))
        if a <= n <= b:
            correct += 1

    print(correct)


def hard():
    with open("2020.2/input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    t_ = []
    for l in t:
        l = l.split("-")
        a = int(l[0])
        l = l[1].split(" ")
        b = int(l[0])
        c = l[1][0]
        d = l[-1]

        t_.append((a, b, c, d))
    t = t_

    correct = 0
    for i in t:
        a, b, c, d = i
        if (d[a - 1] == c) != (d[b - 1] == c):
            correct += 1

    print(correct)


if __name__ == "__main__":
    easy()
    hard()