import pathlib

DIR = pathlib.Path(__file__).parent.absolute()


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").replace("+", "")
    t = [tuple(l.split(" ")) for l in t.split("\n")]
    if t[-1] == "":
        t.pop()
    if t[-1][-1] == "":
        t.pop()

    return t


glob = 0


def run(input, i):
    global glob

    ins, par = input[i]

    if ins == "acc":
        glob += int(par)
    if ins == "jmp":
        return int(par)

    return 1


def easy():
    t = read()
    i = 0
    i_s = set()
    while True:
        if i in i_s:
            print(glob)
            return
        i_s.add(i)
        i += run(t, i)


def mutate(input, i):
    if input[i][0] == "acc":
        raise Exception()

    t = [l for l in input]
    line = t[i]
    line = ({"jmp": "nop", "nop": "jmp"}[line[0]], line[1])
    t[i] = line

    return t


def hard():
    global glob

    t_orig = read()
    N = len(t_orig)
    for n in range(N):
        try:
            t = mutate(t_orig, n)
        except:
            continue
        glob = 0
        i = 0
        i_s = set()
        while True:
            if i in i_s:
                break
            if i == N:
                print(glob)
                return
            i_s.add(i)
            i += run(t, i)


if __name__ == "__main__":
    easy()
    hard()