import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    list(map(lambda r: Wire(r.split(" -> ")[0].split(" "), r.split(" -> ")[1]), s))


class Wire:
    items = {}

    def __init__(self, inp, out):
        self.output = out
        self.inp = inp + ["", ""]
        self.__class__.items[out] = self
        self.val = None

    def calc(self):
        if self.val is not None:
            return self.val
        elif self.inp[1] == "AND":
            self.val = v(self.inp[0]) & v(self.inp[2])
        elif self.inp[1] == "OR":
            self.val = v(self.inp[0]) | v(self.inp[2])
        elif self.inp[1] == "LSHIFT":
            self.val = v(self.inp[0]) << v(self.inp[2])
        elif self.inp[1] == "RSHIFT":
            self.val = v(self.inp[0]) >> v(self.inp[2])
        elif self.inp[0] == "NOT":
            self.val = ~v(self.inp[1])
        else:
            self.val = v(self.inp[0])
        return self.val


def v(key):
    try:
        return int(key)
    except:
        return Wire.items[key].calc()


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
if __name__ == "__main__":
    read()
    x = v("a")
    for wire in Wire.items.values():
        wire.val = x if wire.output == "b" else None
    print(x, v("a"), sep="\n")
