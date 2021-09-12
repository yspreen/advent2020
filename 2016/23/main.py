import re
import pathlib
from copy import deepcopy


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda i: i.split(" "), s)


def reg(letter):
    return ord(letter) - 97


def step(ptr, ins, mem):
    try:
        return unsafe_step(ptr, ins, mem)
    except:
        return 1


def toggle(t, i):
    repl = {
        "inc": "dec",
        "dec": "inc",
        "jnz": "cpy",
        "cpy": "jnz",
        "tgl": "inc",
    }
    t[i][0] = repl[t[i][0]]


def no_num(s):
    return not re.match(r".*[0-9].*", s)


def try_multiply(ptr, ins, mem):
    instr = ins[ptr]
    if instr[2] == "-2":
        inc = ins[ptr - 2] if ins[ptr - 2][0] == "inc" else ins[ptr - 1]
        dec = ins[ptr - 2] if ins[ptr - 2][0] == "dec" else ins[ptr - 1]
        if inc[0] != "inc" or dec[0] != "dec" or dec[1] != instr[1]:
            return
        mem[reg(inc[1])] += mem[reg(dec[1])]
        mem[reg(dec[1])] = 0
    elif instr[2] == "-5" and no_num(ins[ptr - 5][1] + ins[ptr - 5][2]):
        inc = ins[ptr - 4] if ins[ptr - 4][0] == "inc" else ins[ptr - 3]
        dec = ins[ptr - 4] if ins[ptr - 4][0] == "dec" else ins[ptr - 3]
        cpy = ins[ptr - 5]
        if inc[0] != "inc" or dec[0] != "dec":
            return
        mem[reg(inc[1])] += mem[reg(cpy[1])] * mem[reg(instr[1])]
        mem[reg(instr[1])] = 0


def unsafe_step(ptr, ins, mem):
    instr = ins[ptr]
    delta = 1
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
    if instr[0] == "tgl":
        try:
            val = int(instr[1])
        except:
            val = mem[reg(instr[1])]
        ptr += val
        if ptr < N:
            toggle(ins, ptr)
    return delta


def run(init=0):
    i = 0
    m = [0] * 4
    m[0] = init
    t_ = deepcopy(t)
    x = 0
    while i < N:
        x += 1
        i += step(i, t_, m)
        if x == 1000000:
            print(i, t_, m)
            return
    print(m[0])


def easy():
    run(7)


def hard():
    run(12)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
N = len(t)
if __name__ == "__main__":
    easy()
    hard()
