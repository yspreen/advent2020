class Orbital:
    objects = {}

    def __init__(self, name, root_name):
        self.name = name
        self.root_name = root_name
        Orbital.objects[name] = self
        self.chain_length = 0
        self.children = []

    def link_root(self):
        root = Orbital.objects.get(self.root_name, None)
        self.root = root
        if root is not None:
            root.children.append(self)

    def calc_chain_len(self):
        if self.root is not None:
            self.chain_length = self.root.chain_length + 1
        for c in self.children:
            c.calc_chain_len()

    @property
    def root_chain_str(self):
        if self.root is None:
            return ""
        return self.root.root_chain_str + self.root.name + "."


def remove_shared_prefix(a, b):
    if len(a) == 0 or len(b) == 0 or a[0] != b[0]:
        return (a, b)
    return remove_shared_prefix(a[1:], b[1:])


def easy():
    with open("2019.6/input.txt") as f:
        t = f.read().replace("\r", "").split("\n")
    if t[-1] == "":
        t.pop()

    Orbital("COM", "")
    for l in t:
        Orbital(l.split(")")[1], l.split(")")[0])

    for o in Orbital.objects.values():
        o.link_root()
    Orbital.objects["COM"].calc_chain_len()

    print(sum([o.chain_length for o in Orbital.objects.values()]))


def hard():
    san = Orbital.objects["SAN"]
    you = Orbital.objects["YOU"]
    san_str = san.root_chain_str
    you_str = you.root_chain_str

    san_str, you_str = remove_shared_prefix(san_str, you_str)
    san_str = list(filter(lambda s: s == ".", san_str))
    you_str = list(filter(lambda s: s == ".", you_str))
    print(len(san_str) + len(you_str))


if __name__ == "__main__":
    easy()
    hard()