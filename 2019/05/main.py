def digit(num, dig):
    dig = 10 ** dig
    return (num // dig) % 10


memory = []
inputs = []


def op(i):
    global memory, inputs

    code = memory[i]
    ins = code % 100
    mode_a = digit(code, 2)
    mode_b = digit(code, 3)
    mode_c = digit(code, 4)

    try:
        a = memory[i + 1]
        b = memory[i + 2]
        c = memory[i + 3]
        if mode_a == 0 and ins != 3:
            a = memory[a]
        if mode_b == 0:
            b = memory[b]
    except:
        # end of memory.
        pass

    if ins == 99:
        return 0
    if ins == 1:
        memory[c] = a + b
        return 4
    if ins == 2:
        memory[c] = a * b
        return 4
    if ins == 3:
        memory[a] = inputs.pop()
        return 2
    if ins == 4:
        print(a)
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
        memory[c] = 1 if a < b else 0
        return 4
    if ins == 8:
        memory[c] = 1 if a == b else 0
        return 4
    return


def calc(*inp):
    global memory, inputs
    with open("2019.5/input") as f:
        t = f.read().replace("\n", "").split(",")
    if t[-1] == "":
        t.pop()
    t = [int(i) for i in t]

    inp = list(inp)
    inp.reverse()
    inputs = inp
    memory = t

    i = -1
    d = 1
    while d != 0:
        i += d
        d = op(i)


def easy():
    calc(1)


def hard():
    calc(5)


if __name__ == "__main__":
    easy()
    hard()