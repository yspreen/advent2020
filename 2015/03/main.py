import pathlib


move = {"v": (0, 1), "^": (0, -1), "<": (-1, 0), ">": (1, 0)}


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return lmap(lambda r: move[r], s)


def easy():
    p, visited = (0, 0), {(0, 0)}
    for m in t:
        p = (p[0] + m[0], p[1] + m[1])
        visited.add(p)
    print(len(visited))


def hard():
    p, visited, i = [(0, 0), (0, 0)], [{(0, 0)}, {(0, 0)}], 0
    for m in t:
        p[i] = (p[i][0] + m[0], p[i][1] + m[1])
        visited[i].add(p[i])
        i = 1 - i
    print(len(visited[0] | visited[1]))


teststr = """"""
lmap = lambda *a: list(map(*a))
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
