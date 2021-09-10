import numpy as np
import pathlib

DIR = pathlib.Path(__file__).parent.absolute()

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


class VM:
    def read(self):
        with open(DIR / "input") as f:
            t = f.read().replace("\n", "").split(",")
        if t[-1] == "":
            t.pop()
        t = [int(i) for i in t]
        self.t = {i: v for i, v in enumerate(t)}

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
            # if not self.inputs:
            #     return
            self.t[a] = self.A[self.pos]  # self.inputs.pop(0)
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

    def draw(self):
        if len(self.outputs) != 2:
            return
        color, angle = self.outputs
        self.outputs = []
        self.A[self.pos] = color
        self.touched[self.pos] = 1
        self.h += angle * 2 - 1
        self.h %= 4
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
        if not (
            0 <= self.pos[0] < self.A.shape[0] and 0 <= self.pos[1] < self.A.shape[1]
        ):
            self.pad()

    def calc(self):
        if self.done:
            return []
        self.d = 0
        self.outputs = []
        while self.d is not None:
            self.i += self.d
            self.d = self.op(self.i)
            self.draw()
        return self.outputs

    def pad(self):
        n = self.A.shape[0] // 2
        self.A = np.pad(self.A, ((n, n), (n, n)))
        self.touched = np.pad(self.touched, ((n, n), (n, n)))
        self.pos = (self.pos[0] + n, self.pos[1] + n)

    @property
    def direction(self):
        return directions[self.h]

    def __init__(self, starting=0):
        self.read()
        self.outputs = []
        # self.inputs = list(inp)

        self.h = self.i = self.d = self.r = 0
        self.pos = (0, 0)
        self.A = np.zeros((2, 2), np.int32)
        self.A[self.pos] = starting
        self.touched = np.zeros((2, 2), np.int32)
        self.done = False


def prettyprint(t):
    while t.sum(1)[0] == 0:
        t = t[1:, :]
    while t.sum(0)[0] == 0:
        t = t[:, 1:]
    while t.sum(1)[-1] == 0:
        t = t[:-1, :]
    while t.sum(0)[-1] == 0:
        t = t[:, :-1]
    if t.shape[1] % 5:
        t = np.pad(t, ((0, 0), (0, 1)))
    print(ocr(t))


OCR = {
    422148690: "A",
    959335004: "B",
    422068812: "C",
    1024344606: "E",
    1024344592: "F",
    422074958: "G",
    623856210: "H",
    203491916: "J",
    625758866: "K",
    554189342: "L",
    959017488: "P",
    959017618: "R",
    623462988: "U",
    588583044: "Y",
    1008869918: "Z",
}


def ocr(t):
    c = OCR[int("".join([str(i) for i in t[:, :5].reshape(-1)]), 2)]
    if t.shape[1] > 5:
        c += ocr(t[:, 5:])
    return c


def easy():
    v = VM()
    v.calc()
    print(v.touched.sum())


def hard():
    v = VM(1)
    v.calc()
    prettyprint(v.A)


if __name__ == "__main__":
    easy()
    hard()
