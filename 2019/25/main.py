import pathlib
from string import ascii_lowercase


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
            if not len(self.inputs):
                return
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

    def draw(self):
        if len(self.outputs) != 1:
            return
        c = self.outputs.pop()
        self.A += chr(c)

    def calc(self, *inp):
        if self.done:
            return
        self.inputs.extend(inp)
        self.d = 0
        self.outputs = []
        k = 0
        while not self.done and self.d is not None and k < 100000:
            k += 1
            self.i += self.d
            self.d = self.op(self.i)
            self.draw()
        return self.outputs

    def execute(self, cmd=""):
        if not cmd:
            return self.calc()
        if cmd[-1] != "\n":
            cmd += "\n"
        for i in range(10):
            cmd = cmd.replace(str(i + 1), ascii_lowercase[i])
        return self.calc(*[ord(i) for i in cmd])

    def __init__(self):
        self.read()
        self.outputs = []
        self.inputs = []

        self.i = self.d = self.r = 0
        self.A = ""
        self.done = False


class Game:
    def __init__(self):
        self.v = VM()
        self.pos = ""
        self.location_pos = {}
        self.dirs = {}
        self.neighbors = {}
        self.back = {}
        self.items = {}
        self.location = None
        self.seen = set([""])

    def reset_vm(self):
        self.v = VM()

    def parse(self):
        t = "\n" + self.v.A
        self.v.A = ""

        for entry in t.split("\n==")[1:]:
            location = entry.split("\n")[0].replace("==", "").strip()
            pos = self.location_pos.get(location, self.pos)
            rev = ""
            if pos:
                rev = back_dir[{v: k for k, v in directions.items()}[pos[-1]]][0]
            self.location_pos[location] = pos
            blocks = entry.split("\n\n")
            for b in blocks:
                if b.startswith("Doors here lead:"):
                    dirs = list(map(lambda i: i[2:], b.split("\n")[1:]))
                    dirs = [i for i in dirs if i[0] != rev]
                    self.dirs[location] = dirs
                    self.neighbors[location] = [pos + d[0] for d in dirs]
                if b.startswith("Items here:"):
                    items = list(map(lambda i: i[2:], b.split("\n")[1:]))
                    for i in items:
                        self.items[i] = pos
        self.location = location
        self.pos = pos

    def route(self, goal):
        r = []

        while goal != "":
            d = self.back[goal]
            goal = goal[:-1]
            r.append(back_dir[d])

        r.reverse()
        return r

    def take_route(self, goal):
        for r in self.route(goal):
            self.v.execute(r)

    def go_home(self, p):
        rs = self.route(p)
        rs.reverse()
        for r in rs:
            self.v.execute(back_dir[r])

    def next(self):
        nexts = list(zip(self.dirs[self.location], self.neighbors[self.location]))
        nexts = [i for i in nexts if i[1] not in self.seen]

        if not nexts:
            n = self.back.get(self.pos, None)
            if n is None:
                return True
        else:
            n = nexts[0]
            self.back[n[1]] = self.back.get(n[1], back_dir[n[0]])
            n = n[0]

        self.pos = (
            (self.pos + directions[n])
            .replace("ns", "")
            .replace("sn", "")
            .replace("ew", "")
            .replace("we", "")
        )
        self.seen.add(self.pos)
        self.v.execute(n)
        self.parse()


DIR = pathlib.Path(__file__).parent.absolute()
directions = [
    "north",
    "east",
    "south",
    "west",
]
directions = {d: d[0] for d in directions}
back_dir = {
    "north": "south",
    "east": "west",
    "south": "north",
    "west": "east",
}
SCALE = "Pressure-Sensitive Floor"


def easy():
    g = Game()
    g.v.execute()
    g.parse()
    while not g.next():
        continue
    for i, p in list(g.items.items()):
        g.reset_vm()
        g.take_route(p)
        g.v.execute("take " + i)
        g.v.A = ""
        if not g.v.done:
            g.v.execute(g.back[p])
        if not g.v.done and g.v.A.strip()[:2] == "==":
            continue
        else:
            del g.items[i]
    light_items = []
    for i, p in g.items.items():
        g.reset_vm()
        g.take_route(p)
        g.v.execute("take " + i)
        g.go_home(p)
        g.take_route(g.location_pos[SCALE])
        if "heavier" in g.v.A:
            light_items.append(i)
    g.reset_vm()
    for n in range(1, 2 ** len(light_items)):
        g.reset_vm()
        for i, item in enumerate(light_items):
            if "{0:09b}".format(n)[-i - 1] == "1":
                p = g.items[item]
                g.take_route(p)
                g.v.execute("take " + item)
                g.go_home(p)
        g.v.A = ""
        g.take_route(g.location_pos[SCALE])
        if "Alert!" not in g.v.A:
            print(g.v.A.split("typing ")[1].split(" ")[0])
            return


def hard():
    return


if __name__ == "__main__":
    easy()
    hard()
