import numpy as np


def get(x, y):
    return A[y, x % A.shape[1]]


A = None


def check(x, y):
    global A
    with open("2020.3/input") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    t = [[1 if e == "#" else 0 for e in l] for l in t]
    A = np.matrix(t, dtype=np.uint32)

    pos = np.array([0, 0])
    mov = np.array([x, y])

    n = 0
    while True:
        pos += mov
        if pos[1] >= A.shape[0]:
            break
        n += get(*pos)
    return n


def easy():
    print(check(3, 1))


def hard():
    a = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    a = [check(*t) for t in a]
    print(np.prod(a))


if __name__ == "__main__":
    easy()
    hard()