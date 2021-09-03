import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return {
        k: v
        for k, v in map(
            lambda r: (
                int(r.split(" <-> ")[0]),
                lmap(int, r.split(" <-> ")[1].split(", ")),
            ),
            s.splitlines(),
        )
    }


def visit(from_point):
    next_set = {from_point}
    visited = {from_point}
    while next_set:
        p = list(next_set)[0]
        next_set.discard(p)
        for o in t[p]:
            if o not in visited:
                next_set.add(o)
            visited.add(o)
    return visited


def easy():
    print(len(visit(0)))


def hard():
    pool = set(t.keys())
    c = 0
    while pool:
        c += 1
        p = list(pool)[0]
        pool -= visit(p)
    print(c)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
