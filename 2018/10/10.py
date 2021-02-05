import pathlib

input = open(pathlib.Path(__file__).parent / "input.txt").read().splitlines()


def parse_input(i):
    i1 = i.split("<")[1].split(",")[0]
    i3 = i.split("<")[2].split(",")[0]
    i2 = i.split(">")[0].split(",")[-1]
    i4 = i.split(">")[1].split(",")[-1]
    return [int(i1), int(i2), int(i3), int(i4)]


input = [parse_input(i) for i in input]


def velo_step(ins):
    for i in ins:
        i[0] += i[2]
        i[1] += i[3]


def get_order(ins):
    order = 0
    for i in ins[::2]:
        for j in ins[::2]:
            order += min([abs(i[0] - j[0]), abs(i[1] - j[1])])
    return order


def main():
    global input
    from copy import deepcopy

    orig = deepcopy(input)

    orders = []
    do_step = 6
    while do_step > 0:
        do_step -= 1
        order = get_order(input)
        if do_step < 5 and order < orders[-1]:
            do_step = 5
        orders.append(order)
        velo_step(input)

    second = orders.index(min(orders))
    input = orig

    for _ in range(second):
        velo_step(input)

    min_x = min([i[0] for i in input])
    min_y = min([i[1] for i in input])

    for i in input:
        i[0] -= min_x
        i[1] -= min_y

    max_x = max([i[0] for i in input])
    max_y = max([i[1] for i in input])

    arr = [["." for _ in range(max_y + 1)] for _ in range(max_x + 1)]

    for i in input:
        arr[i[0]][i[1]] = "#"

    out = ""
    for y in range(len(arr[0])):
        for x in range(len(arr)):
            out += arr[x][y]
        out += "\n"
    print(out)
    print(second)


main()
