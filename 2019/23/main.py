import pathlib


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


class VM:
    items = {}
    idle = set([])

    def read(self):
        with open(DIR / "input") as f:
            t = f.read().replace("\n", "").split(",")
        if t[-1] == "":
            t.pop()
        t = [int(i) for i in t]
        self.t = {i: v for i, v in enumerate(t)}
        self.t_ = dict(self.t)

    def op(self, i):
        code = self.t[i]
        ins = code % 100
        mode_a = digit(code, 2)
        mode_b = digit(code, 3)
        mode_c = digit(code, 4)

        a = self.t.get(i + 1, 0)
        if mode_a == 2:
            a += self.r
            mode_a = 0
        if mode_a == 0 and ins != 3:
            a = self.t.get(a, 0)
        b = self.t.get(i + 2, 0)
        if mode_b == 0:
            b = self.t.get(b, 0)
        if mode_b == 2:
            b = self.t.get(self.r + b, 0)
        c = self.t.get(i + 3, 0)
        if mode_c == 2:
            c += self.r

        if ins == 99:
            self.done = True
            return
        if ins == 1:
            self.t[c] = a + b
            return 4
        if ins == 2:
            self.t[c] = a * b
            return 4
        if ins == 3:
            self.idle.discard(self.addr)
            if not len(self.inputs):
                self.idle_i += 1
                if self.idle_i > 5:
                    self.idle.add(self.addr)
                self.inputs = [-1]
            self.t[a] = self.inputs.pop(0)
            return 2
        if ins == 4:
            self.outputs.append(a)
            return 2
        if ins == 5:
            if a != 0:
                return b - i
            return 3
        if ins == 6:
            if a == 0:
                return b - i
            return 3
        if ins == 7:
            self.t[c] = 1 if a < b else 0
            return 4
        if ins == 8:
            self.t[c] = 1 if a == b else 0
            return 4
        if ins == 9:
            self.r += a
            return 2

    def draw(self, use_nat):
        if len(self.outputs) != 3:
            return
        a, x, y = self.outputs
        self.outputs = []
        self.items[a].inputs.extend([x, y])
        if a == 255 and not use_nat:
            return y

    def step(self, use_nat=False):
        if self.done:
            return
        if self.addr == 255:
            return self.nat()
        self.d = self.op(self.i)
        self.i += 0 if self.d is None else self.d
        return self.draw(use_nat)

    def nat(self):
        self.inputs = self.inputs[-2:]
        if len(self.idle) < 50:
            return
        self.items[0].inputs.extend(self.inputs)
        if self.i == self.inputs[1]:
            return self.i
        self.i = self.inputs[1]
        self.idle.discard(0)

    def __init__(self, addr=0):
        self.read()
        self.outputs = []
        self.inputs = [addr]

        self.addr = addr
        self.items[addr] = self
        self.idle_i = self.i = self.d = self.r = 0
        self.done = False


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
vs = [VM(i) for i in range(50)] + [VM(255)]


def run(nat=False):
    while True:
        for v in vs:
            i = v.step(use_nat=nat)
            if i is not None:
                return print(i)


def easy():
    run()


def hard():
    run(True)


if __name__ == "__main__":
    easy()
    hard()
