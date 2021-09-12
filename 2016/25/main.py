import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda i: i.split(" "), s)


def reg(letter):
    return ord(letter) - 97


def try_multiply(ptr, ins, mem):
    instr = ins[ptr]
    if instr[2] == "-2":
        inc = ins[ptr - 2] if ins[ptr - 2][0] == "inc" else ins[ptr - 1]
        dec = ins[ptr - 2] if ins[ptr - 2][0] == "dec" else ins[ptr - 1]
        if inc[0] != "inc" or dec[0] != "dec" or dec[1] != instr[1]:
            return
        mem[reg(inc[1])] += mem[reg(dec[1])]
        mem[reg(dec[1])] = 0
    elif instr[2] == "-5" and ins[ptr - 5][0] == "cpy":
        inc = ins[ptr - 4] if ins[ptr - 4][0] == "inc" else ins[ptr - 3]
        dec = ins[ptr - 4] if ins[ptr - 4][0] == "dec" else ins[ptr - 3]
        cpy = ins[ptr - 5]
        if inc[0] != "inc" or dec[0] != "dec" or cpy[2] != dec[1]:
            return
        try:
            val = int(cpy[1])
        except:
            val = mem[reg(cpy[1])]
        mem[reg(inc[1])] += val * mem[reg(instr[1])]
        mem[reg(instr[1])] = 0


def step(ptr, ins, mem):
    instr, delta, output = ins[ptr], 1, None
    if instr[0] == "cpy":
        try:
            val = int(instr[1])
        except:
            val = mem[reg(instr[1])]
        mem[reg(instr[2])] = val
    if instr[0] == "jnz":
        try_multiply(ptr, ins, mem)
        try:
            val = int(instr[1])
        except:
            val = mem[reg(instr[1])]
        if val != 0:
            try:
                delta = int(instr[2])
            except:
                delta = mem[reg(instr[2])]
    if instr[0] == "inc":
        mem[reg(instr[1])] += 1
    if instr[0] == "dec":
        mem[reg(instr[1])] -= 1
    if instr[0] == "out":
        try:
            output = int(instr[1])
        except:
            output = mem[reg(instr[1])]
    return delta, output


def run(init=0):
    i, m, x, o = 0, [init, 0, 0, 0], 0, -1
    while i < N:
        x += 1
        delta, out = step(i, t, m)
        i += delta
        if out is not None:
            if out not in [0, 1] or (o == 0) == (out == 0):
                return False
            o = out
        if x == 100000:
            return o > -1


def easy():
    x = 1
    while not run(x):
        x += 1
    print(x)


def hard():
    return


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
N = len(t)
if __name__ == "__main__":
    easy()
    hard()
