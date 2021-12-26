import enum
import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt, sin, cos, pi
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


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
                        one_i, one_j, one_k = k_a
                        other_i, other_j, other_k = k_b
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


def easy():
    sets = [VectorSet(v, k=i) for (i, v) in enumerate(t)]
    while len(sets) > 1:
        m = other = 0
        for k, s in enumerate(sets[1:]):
            if sets[0].similarity(s) > m:
                m, other = sets[0].similarity(s), k + 1
        assert other > 0
        print("join", other)
        sets[0].join(sets[other])
        del sets[other]
    print(len(sets[0].points))


def hard():
    return


teststr = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
