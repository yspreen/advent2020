import pathlib

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").replace("+", "")
    t = t.split("\n")
    if t[-1] == "":
        t.pop()
    t = [int(i) for i in t]

    return t


def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False

    return True


def add_remove(A, new, old):
    i = 0
    N = len(A)
    while old != inf or new != inf:
        if i == N - 1 and old == inf:
            A.append(new)
            return
        if A[i] == old:
            del A[i]
            old = inf
            continue
        if A[i] >= new:
            A.insert(i, new)
            new = inf
        i += 1


def check_validity(A, k):
    i = 0

    while A[i] < k and i < 24:
        j = 24
        while A[i] + A[j] > k and j > i + 1:
            j -= 1
        if A[i] + A[j] == k:
            return True
        i += 1


found = 0


def easy():
    global found
    t = read()

    k = 25
    A = t[:k]
    A.sort()

    i = k
    while i < len(t):
        if not check_validity(A, t[i]):
            found = t[i]
            print(t[i])
            return
        add_remove(A, t[i], t[i - k])
        i += 1


def hard():
    t = read()

    i = 0
    j = 1

    while True:
        S = sum(t[i : j + 1])
        if S == found:
            print(min(t[i : j + 1]) + max(t[i : j + 1]))
            return
        if S > found:
            i += 1
            if i > j:
                j += 1
        else:
            j += 1


if __name__ == "__main__":
    easy()
    hard()
