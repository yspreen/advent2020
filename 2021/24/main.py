import pathlib
from itertools import product
from copy import copy


class ALU:
    def __init__(self, input) -> None:
        self.input = list(reversed(input))
        self.vars = {"w": 0, "x": 0, "y": 0, "z": 0}

    def var(self, s):
        return self.vars[s] if s in self.vars else int(s)

    def step(self, ins):
        if ins[0] == "inp":
            self.vars[ins[1]] = self.input.pop()
        if ins[0] == "add":
            self.vars[ins[1]] += self.var(ins[2])
        if ins[0] == "mul":
            self.vars[ins[1]] *= self.var(ins[2])
        if ins[0] == "div":
            self.vars[ins[1]] //= self.var(ins[2])
        if ins[0] == "mod":
            self.vars[ins[1]] %= self.var(ins[2])
        if ins[0] == "eql":
            self.vars[ins[1]] = 1 if self.vars[ins[1]] == self.var(ins[2]) else 0


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: r.split(" "), s)


def run(pairs, mutation=list):
    final = [0] * 14
    for (i, j) in pairs:
        digits = copy(final)
        M = 9e9
        for n, m in mutation(list(product(range(1, 10), repeat=2))):
            digits[i], digits[j] = n, m
            a = ALU(digits)
            for ins in t:
                a.step(ins)
            if a.vars["z"] <= M:
                M = a.vars["z"]
                final[i], final[j] = n, m
    print("".join(map(str, final)))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    stack, pairs, i = [], [], 0
    for i, ins in enumerate([i for i in t if i[0] == "div"]):
        if ins[2] == "1":
            stack.append(i)
        else:
            pairs.append((stack.pop(), i))
    run(pairs)
    run(pairs, reversed)
