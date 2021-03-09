import re
import pathlib

input1, input2 = [
    list(
        filter(
            None,
            open(pathlib.Path(__file__).parent / "input")
            .read()
            .split("\n" * 4)[i]
            .splitlines(),
        )
    )
    for i in range(2)
]
units = []


def do_operation(reg, op, hard_table=False):
    t = list(range(16))
    if hard_table:
        t = [14, 0, 15, 8, 10, 1, 3, 5, 7, 9, 2, 11, 6, 12, 13, 4]
    out = [j for j in reg]
    if op[0] == t[0]:
        out[op[3]] = reg[op[1]] + reg[op[2]]
    elif op[0] == t[1]:
        out[op[3]] = reg[op[1]] + op[2]
    elif op[0] == t[2]:
        out[op[3]] = reg[op[1]] * reg[op[2]]
    elif op[0] == t[3]:
        out[op[3]] = reg[op[1]] * op[2]
    elif op[0] == t[4]:
        out[op[3]] = reg[op[1]] & reg[op[2]]
    elif op[0] == t[5]:
        out[op[3]] = reg[op[1]] & op[2]
    elif op[0] == t[6]:
        out[op[3]] = reg[op[1]] | reg[op[2]]
    elif op[0] == t[7]:
        out[op[3]] = reg[op[1]] | op[2]
    elif op[0] == t[8]:
        out[op[3]] = reg[op[1]]
    elif op[0] == t[9]:
        out[op[3]] = op[1]
    elif op[0] == t[10]:
        out[op[3]] = 1 if op[1] > reg[op[2]] else 0
    elif op[0] == t[11]:
        out[op[3]] = 1 if reg[op[1]] > op[2] else 0
    elif op[0] == t[12]:
        out[op[3]] = 1 if reg[op[1]] > reg[op[2]] else 0
    elif op[0] == t[13]:
        out[op[3]] = 1 if op[1] == reg[op[2]] else 0
    elif op[0] == t[14]:
        out[op[3]] = 1 if reg[op[1]] == op[2] else 0
    elif op[0] == t[15]:
        out[op[3]] = 1 if reg[op[1]] == reg[op[2]] else 0
    else:
        return None
    return out


def change_opcode(reg, op, code):
    op[0] = code
    return do_operation(reg, op)


input_ = []
for i in range(len(input1))[::3]:
    i1 = [int(j) for j in re.sub(r"[^0-9,]", "", input1[i]).split(",")]
    i2 = [int(j) for j in re.sub(r"[^0-9 ]", "", input1[i + 1]).split(" ")]
    i3 = [int(j) for j in re.sub(r"[^0-9,]", "", input1[i + 2]).split(",")]
    input_.append([i1, i2, i3])
input1 = input_


def easy():
    global input1
    three = 0
    for i in input1:
        correct = 0
        for j in range(16):
            if change_opcode(i[0], i[1], j) == i[2]:
                correct += 1
        if correct >= 3:
            three += 1
    print(three)


easy()
units = []


def change_opcode(reg, op, code):
    op[0] = code
    return do_operation(reg, op)


input_ = []
for i in range(len(input2))[::1]:
    i1 = [int(j) for j in re.sub(r"[^0-9 ]", "", input2[i]).split(" ")]
    input_.append(i1)
input2 = input_


def hard():
    global input2
    reg = [0] * 4
    for i in input2:
        reg = do_operation(reg, i, 1)
    print(reg[0])


hard()