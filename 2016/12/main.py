import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda i: i.split(" "), s)


def register_for(letter):
    return ord(letter) - 97


def step(pointer, instr, mem):
    delta = 1
    if instr[0] == "cpy":
        try:
            val = int(instr[1])
        except:
            val = mem[register_for(instr[1])]
        mem[register_for(instr[2])] = val
    if instr[0] == "jnz":
        try:
            val = int(instr[1])
        except:
            val = mem[register_for(instr[1])]
        if val != 0:
            delta = int(instr[2])
    if instr[0] == "inc":
        mem[register_for(instr[1])] += 1
    if instr[0] == "dec":
        mem[register_for(instr[1])] -= 1
    return delta


def run(init=0):
    i = 0
    N = len(t)
    m = [0] * 4
    m[2] = init
    while i < N:
        i += step(i, t[i], m)
    print(m[0])


def easy():
    run()


def hard():
    run(1)


teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
t = read()
if __name__ == "__main__":
    easy()
    hard()
