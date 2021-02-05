import re

input = """
#ip 4
addi 4 16 4
seti 1 7 1
seti 1 8 2
mulr 1 2 3
eqrr 3 5 3
addr 3 4 4
addi 4 1 4
addr 1 0 0
addi 2 1 2
gtrr 2 5 3
addr 4 3 4
seti 2 1 4
addi 1 1 1
gtrr 1 5 3
addr 3 4 4
seti 1 8 4
mulr 4 4 4
addi 5 2 5
mulr 5 5 5
mulr 4 5 5
muli 5 11 5
addi 3 4 3
mulr 3 4 3
addi 3 21 3
addr 5 3 5
addr 4 0 4
seti 0 5 4
setr 4 1 3
mulr 3 4 3
addr 4 3 3
mulr 4 3 3
muli 3 14 3
mulr 3 4 3
addr 5 3 5
seti 0 2 0
seti 0 0 4
"""

input = input.split("\n")
input = list(filter(None, input))

ip = int(input[0].split(" ")[-1])
input = input[1:]


def do_operation(reg, op):
    out = [j for j in reg]
    if op[0] == 'addr':
        out[op[3]] = reg[op[1]] + reg[op[2]]
    elif op[0] == 'addi':
        out[op[3]] = reg[op[1]] + op[2]
    elif op[0] == 'mulr':
        out[op[3]] = reg[op[1]] * reg[op[2]]
    elif op[0] == 'muli':
        out[op[3]] = reg[op[1]] * op[2]
    elif op[0] == 'banr':
        out[op[3]] = reg[op[1]] & reg[op[2]]
    elif op[0] == 'bani':
        out[op[3]] = reg[op[1]] & op[2]
    elif op[0] == 'borr':
        out[op[3]] = reg[op[1]] | reg[op[2]]
    elif op[0] == 'bori':
        out[op[3]] = reg[op[1]] | op[2]
    elif op[0] == 'setr':
        out[op[3]] = reg[op[1]]
    elif op[0] == 'seti':
        out[op[3]] = op[1]
    elif op[0] == 'gtir':
        out[op[3]] = 1 if op[1] > reg[op[2]] else 0
    elif op[0] == 'gtri':
        out[op[3]] = 1 if reg[op[1]] > op[2] else 0
    elif op[0] == 'gtrr':
        out[op[3]] = 1 if reg[op[1]] > reg[op[2]] else 0
    elif op[0] == 'eqir':
        out[op[3]] = 1 if op[1] == reg[op[2]] else 0
    elif op[0] == 'eqri':
        out[op[3]] = 1 if reg[op[1]] == op[2] else 0
    elif op[0] == 'eqrr':
        out[op[3]] = 1 if reg[op[1]] == reg[op[2]] else 0
    else:
        return None

    return out


def change_opcode(reg, op, code):
    op[0] = code
    return do_operation(reg, op)


input_ = []
for i in input:
    i1 = [i.split(" ")[0]] + [int(j) for j in i.split(" ")[1:]]
    input_.append(i1)
input = input_


def main():
    global input, ip

    reg = [0 for _ in range(6)]
    reg[ip] = 0
    while reg[ip] < len(input):
        op = input[reg[ip]]
        reg = do_operation(reg, op)
        # print(reg)
        reg[ip] += 1
    print(reg)


main()
