import numpy as np
import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).split("\n\n")
    return lmap(
        lambda i: np.array(lmap(lambda j: lmap(int, j.split(",")), i.splitlines()[1:])),
        s,
    )


class VectorSet:
    def __init__(self, vectors, k=0) -> None:
        self.diffs = all_diffs(vectors, k)
        self.diff_tuples = set(map(diff_to_tuple, self.diffs.values()))
        self.vectors = {k: vectors}
        self.points = set(tuple(vector) for vector in vectors)
        self.scanners = [np.array((0, 0, 0))]

    def similarity(self, other: "VectorSet") -> int:
        return len(self.diff_tuples & other.diff_tuples)

    def join(self, other: "VectorSet") -> None:
        possible_offs = {}
        for target_tuple in self.diff_tuples & other.diff_tuples:
            for k_a, v_a in self.diffs.items():
                if diff_to_tuple(v_a) != target_tuple:
                    continue
                for k_b, v_b in other.diffs.items():
                    if diff_to_tuple(v_b) != target_tuple:
                        continue
                    for rot in vector_matches(v_a, v_b):
                        one_i, _, one_k = k_a
                        other_i, _, other_k = k_b
                        d = tuple(
                            self.vectors[one_k][one_i]
                            - rotations(other.vectors[other_k][other_i])[rot]
                        )
                        possible_offs[(d, rot)] = possible_offs.get((d, rot), 0) + 1
        move, rotate = [
            k for (k, v) in possible_offs.items() if v == max(possible_offs.values())
        ][0]
        move = np.array(move)
        new_vectors = [rotations(v)[rotate] + move for v in other.vectors[other_k]]
        self.vectors[other_k] = new_vectors
        self.points |= set(tuple(vector) for vector in new_vectors)
        self.diff_tuples |= other.diff_tuples
        self.diffs.update({k: rotations(v)[rotate] for (k, v) in other.diffs.items()})
        self.scanners += [move]


def vector_matches(one, other):
    matches = []
    for rotation, rotated in enumerate(rotations(other)):
        if tuple(one) == tuple(rotated):
            matches.append(rotation)
    return matches


def rotate_vector(v, axis, rotations=1):
    ax, ay, az = axis
    vx, vy, vz = v

    if rotations == 0:
        return np.array(v)

    if ax:
        v = [vx, -vz, vy]
    if ay:
        v = [vz, vy, -vx]
    if az:
        v = [-vy, vx, vz]

    return rotate_vector(v, axis, rotations - 1)


def rotations(v):
    res = []
    v = np.array(v)

    x = [1, 0, 0]
    y = [0, 1, 0]
    z = [0, 0, 1]

    for _ in range(4):
        for _ in range(4):
            res.append(v)
            v = rotate_vector(v, x)
        v = rotate_vector(v, z)
    for i in range(2):
        v = rotate_vector(v, y, i + 1)
        for _ in range(4):
            v = rotate_vector(v, x)
            res.append(v)

    return res


def diff_to_tuple(diff):
    return tuple(sorted([abs(n) for n in diff]))


def all_diffs(vectors, k=0):
    diffs = {}
    for i, vi in enumerate(vectors):
        for (j, vj) in [(j, vj) for (j, vj) in enumerate(vectors) if i != j]:
            diffs[(i, j, k)] = vi - vj
    return diffs


def run():
    sets = [VectorSet(v, k=i) for (i, v) in enumerate(t)]
    while len(sets) > 1:
        m = other = 0
        for k, s in enumerate(sets[1:]):
            if sets[0].similarity(s) > m:
                m, other = sets[0].similarity(s), k + 1
        sets[0].join(sets[other])
        del sets[other]
    print(len(sets[0].points))

    points = list(sets[0].scanners)
    points.sort(key=lambda p: sum(map(abs, p)))
    last = points.pop()
    print(max([sum(abs(np.array(p) - np.array(last))) for p in points]))


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    run()
