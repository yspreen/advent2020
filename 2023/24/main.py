import pathlib
from os import environ
from sympy import symbols, Eq, solve


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(" @", ",").splitlines()
    return lmap(lambda r: lmap(int, r.split(", ")), s)


def collides(a, b):
    apx, apy, apz, avx, avy, avz = a
    bpx, bpy, bpz, bvx, bvy, bvz = b

    # Define new symbols for t_a and t_b
    t_a, t_b = symbols("t_a t_b")

    # Redefine the equations with t_a and t_b
    equation1_new = Eq(apx + avx * t_a, bpx + bvx * t_b)
    equation2_new = Eq(apy + avy * t_a, bpy + bvy * t_b)

    # Solve the new set of equations
    solution_new = solve((equation1_new, equation2_new), (t_a, t_b))

    # Extract the solutions for t_a and t_b
    if not solution_new:
        return False
    t_a_solution, t_b_solution = solution_new[t_a], solution_new[t_b]
    if t_a_solution < 0 or t_b_solution < 0:
        return False

    # Calculate the intersection point using either line's equation
    # Using line a's equation for demonstration
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


def hard():
    s_px, s_py, s_pz, s_vx, s_vy, s_vz = symbols("s_px s_py s_pz s_vx s_vy s_vz")
    equations = []
    vars = [s_px, s_py, s_pz, s_vx, s_vy, s_vz]
    i = 0
    for apx, apy, apz, avx, avy, avz in t_b:
        t_i = symbols(f"t_{number_to_letters(i)}")
        i += 1
        equations.append(Eq(apx + avx * t_i, s_px + s_vx * t_i))
        equations.append(Eq(apy + avy * t_i, s_py + s_vy * t_i))
        equations.append(Eq(apz + avz * t_i, s_pz + s_vz * t_i))
        vars.append(t_i)

    # Solve the new set of equations
    solution_new = solve(tuple(equations), tuple(vars))

    # Extract the solutions for t_b and t_b
    if not solution_new:
        return

    for s in [s_px, s_py, s_pz, s_vx, s_vy, s_vz]:
        print(solution_new[s])


teststr = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
if environ.get("AOC_SOLVE", "1") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t_b = read()
N = len(t_b)
if __name__ == "__main__":
    # easy()
    hard()
