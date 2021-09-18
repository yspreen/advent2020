import numpy as np
import pathlib
from python_tsp.exact import solve_tsp_dynamic_programming


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    ns, costs = {}, {}
    for i in s:
        p1 = ns.get(i.split(" ")[0], len(ns))
        ns[i.split(" ")[0]] = p1
        p2 = ns.get(i.split(" ")[2], len(ns))
        ns[i.split(" ")[2]] = p2
        c = int(i.split(" ")[-1])
        costs[(p1, p2)] = c
    A = np.zeros((len(ns) + 1, len(ns) + 1))  # + float("inf")
    for tup, c in costs.items():
        A[tup[0] + 1, tup[1] + 1] = A[tup[1] + 1, tup[0] + 1] = c
    return A


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
A = read()
if __name__ == "__main__":
    print(int(solve_tsp_dynamic_programming(A)[1]))
    print(-int(solve_tsp_dynamic_programming(-A)[1]))
