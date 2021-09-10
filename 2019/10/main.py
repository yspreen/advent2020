import numpy as np
import pathlib
from math import atan2, gcd, pi as π

DIR = pathlib.Path(__file__).parent.absolute()


def read():
    with open(DIR / "input") as f:
        t = f.read()
    n = len(t.split("\n")[0])
    t = t.replace("\n", "").replace("#", "1").replace(".", "0")
    return np.array([int(i) for i in t], dtype=np.int32).reshape(-1, n)


t = read()
coord = list(zip(*np.where(t == 1)))


def get_vector(a, b):
    v = (b[0] - a[0], b[1] - a[1])
    return (v[0] / gcd(*v), v[1] / gcd(*v))


def easy():
    vectors = {}
    for i, asteroid in enumerate(coord):
        vectors[i] = set()
        for other in coord:
            if other == asteroid:
                continue
            vector = get_vector(asteroid, other)
            vectors[i].add(vector)
    i, m = sorted(list(vectors.items()), key=lambda i: -len(i[1]))[0]
    print(len(m))
    coord.append(coord.pop(i))


def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def angle(b):
    return (atan2(b[1], -b[0]) * (180 / π)) % 360


def hard():
    home = coord.pop()
    vectors = {}
    for asteroid in coord:
        vector = get_vector(home, asteroid)
        vectors[vector] = vectors.get(vector, [])
        vectors[vector].append(asteroid)
    for v in vectors.keys():
        vectors[v].sort(key=lambda i: distance(home, i))
    order = sorted(list(vectors.keys()), key=lambda i: angle(i))
    destroyed = 0
    while True:
        for vector in order:
            if not vectors[vector]:
                continue
            removed = vectors[vector].pop(0)
            destroyed += 1
            if destroyed == 200:
                print(removed[1] * 100 + removed[0])
                return


if __name__ == "__main__":
    easy()
    hard()
