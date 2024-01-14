import pathlib
from os import environ
import math


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(" @", ",").splitlines()
    return lmap(lambda r: lmap(int, r.split(", ")), s)


def collides(a, b):
    apx, apy, apz, avx, avy, avz = a
    bpx, bpy, bpz, bvx, bvy, bvz = b

    # Define new symbols for t_a and t_b
    var("t_a t_b")

    # Redefine the equations with t_a and t_b
    equation1_new = Eq(apx + avx * t_a == bpx + bvx * t_b)
    equation2_new = Eq(apy + avy * t_a == bpy + bvy * t_b)

    # Solve the new set of equations
    solution_new = solve([equation1_new, equation2_new], t_a, t_b)

    # Extract the solutions for t_a and t_b
    if not solution_new:
        return False
    t_a_solution, t_b_solution = [sol.rhs() for sol in solution_new[0]]
    if t_a_solution < 0 or t_b_solution < 0:
        return False

    # Calculate the intersection point using either line's equation
    x = apx + avx * t_a_solution
    y = apy + avy * t_a_solution

    MIN = 2e14
    MAX = 4e14
    return MIN <= x <= MAX and MIN <= y <= MAX


def number_to_letters(n):
    """
    Convert a number to a string representing its unique combination of lowercase letters.
    0 -> a, 1 -> b, ..., 25 -> z, 26 -> aa, 27 -> ab, etc.
    """
    result = ""

    while n >= 0:
        # Calculate the letter and prepend it to the result
        result = chr((n % 26) + 97) + result
        n = n // 26 - 1

        if n < 0:
            break

    return result


def easy():
    c = 0
    for i in range(N):
        print(i)
        for j in range(i + 1, N):
            if collides(t_b[i], t_b[j]):
                c += 1
    print(c)


def distance_pair(t, i, j, x):
    i_px, i_py, i_pz, i_vx, i_vy, i_vz = t[i]
    j_px, j_py, j_pz, j_vx, j_vy, j_vz = t[j]
    return (
        abs((i_px + x * i_vx) - (j_px + x * j_vx))
        + abs((i_py + x * i_vy) - (j_py + x * j_vy))
        + abs((i_pz + x * i_vz) - (j_pz + x * j_vz))
    )


def calc_distance(t, time):
    d = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            d += distance_pair(t, i, j, time)
    return d


def hard():
    digits = len(str(t[0][0]))
    best = 0
    for d in range(digits)[::-1]:
        min = (0, 99e99)
        for i in range(20):
            i -= 10
            i *= d
            new_d = calc_distance(t, time=i + best)
            if new_d < min[1]:
                min = (i, new_d)
        print(min)
        best += min[0]

    print(best)


teststr = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
N = len(t)
if __name__ == "__main__":
    # easy()
    hard()
