import pathlib
import hashlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()[0]
    return s


def coord(m):
    return (m.count("R") - m.count("L"), m.count("D") - m.count("U"))


def doors_for(h, moves=""):
    h += moves
    opens = ["b", "c", "d", "e", "f"]
    x, y = coord(moves)

    u, d, l, r = str(hashlib.md5((h).encode()).hexdigest())[:4]
    return {
        "U": u in opens and y > 0,
        "D": d in opens and y < 3,
        "L": l in opens and x > 0,
        "R": r in opens and x < 3,
    }


def step(positions, visited, goal_coord):
    new_positions, reached = [], []
    for pos in positions:
        new_moves = [pos + m for (m, open) in doors_for(t, pos).items() if open]
        for m in new_moves:
            if m in visited:
                continue
            visited.add(m)
            if coord(m) == goal_coord:
                reached.append(m)
                continue
            new_positions.append(m)
    return new_positions, reached


def easy():
    goal, visited, positions = (3, 3), {""}, [""]
    while True:
        positions, found = step(positions, visited, goal)
        if found:
            return print(found[0])


def hard():
    goal, visited, positions, allfound = (3, 3), {""}, [""], []
    while positions:
        positions, found = step(positions, visited, goal)
        allfound.extend(found)
    allfound.sort(key=lambda i: len(i))
    print(len(allfound[-1]))


teststr = ""  # "ihgpwlah"
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
