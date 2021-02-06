import re
import pathlib

input = open(pathlib.Path(__file__).parent / "input.txt").read().splitlines()
input = [
    [i[0]] + re.sub(r"[^0-9,]", "", i.replace("..", ",")).split(",") for i in input
]

min_x = min_y = -1
for i in input:
    i[1] = int(i[1])
    i[2] = int(i[2])
    i[3] = int(i[3])
    if i[0] == "x":
        if min_x == -1 or min_x > i[1]:
            min_x = i[1]
        if min_y == -1 or min_y > i[2]:
            min_y = i[2]
        if min_y == -1 or min_y > i[3]:
            min_y = i[3]
    else:
        if min_x == -1 or min_x > i[2]:
            min_x = i[2]
        if min_x == -1 or min_x > i[3]:
            min_x = i[3]
        if min_y == -1 or min_y > i[1]:
            min_y = i[1]
for i in input:
    if i[0] == "x":
        i[1] -= min_x - 1  # -1 because overflow to the left
        i[2] -= min_y
        i[3] -= min_y
    else:
        i[2] -= min_x - 1
        i[3] -= min_x - 1
        i[1] -= min_y

source = 500 - min_x + 1

arr = [[0]]
size_x = size_y = 1


def set_arr(x_f, x_t, y_f, y_t):
    global arr, size_x, size_y

    while x_t + 2 > size_x:  # +1 for overflow to the right
        arr.append([0 for _ in arr[0]])
        size_x += 1
    while y_t + 1 > size_y:
        for i in arr:
            i.append(0)
        size_y += 1

    for i in range(x_f, x_t + 1):
        for j in range(y_f, y_t + 1):
            arr[i][j] = 1


for i in input:
    if i[0] == "x":
        set_arr(i[1], i[1], i[2], i[3])
    else:
        set_arr(i[2], i[3], i[1], i[1])


def look(x, y, v=None):
    global arr, size_x, size_y

    if x < 0 or y < 0 or x >= size_x or y >= size_y:
        return -1
    if v is None:
        return arr[x][y]
    arr[x][y] = v


def main():
    global arr, size_x, size_y

    cursors = [(source, 0)]
    closed_check = []

    while len(cursors):
        new_cc = []
        for cc in closed_check:
            cc[4] += 1
            if cc[4] < 100:
                if arr[cc[2]][cc[3]] == 3:
                    cursors.append((cc[0], cc[1]))
                else:
                    new_cc.append(cc)
        closed_check = new_cc

        new_cursors = []
        for (x, y) in cursors:
            look(x, y, 2)
            if look(x, y + 1) == 0:
                new_cursors.append((x, y + 1))
            if look(x, y + 1) in [1, 3]:
                wall_l = wall_r = True
                if look(x - 1, y) == 2:
                    wall_l = False
                if look(x - 1, y) == 0:
                    wall_l = False
                    new_cursors.append((x - 1, y))
                if look(x + 1, y) == 2:
                    wall_r = False
                if look(x + 1, y) == 0:
                    wall_r = False
                    new_cursors.append((x + 1, y))
                if wall_l or wall_r:
                    if wall_l:
                        direction = +1
                    else:
                        direction = -1

                    pos = [x + direction, y]
                    is_closed = True
                    if look(x - 1, y) != 3 and look(x + 1, y) != 3:
                        while look(pos[0], pos[1]) != 1:
                            if look(pos[0], pos[1] + 1) not in [1, 3]:
                                is_closed = False
                                closed_check.append([x, y, pos[0], pos[1] + 1, 0])
                                break
                            pos[0] += direction

                    if is_closed:
                        look(x, y, 3)
                        if look(x - 1, y) == 2 and (x - 1, y) not in new_cursors:
                            new_cursors.append((x - 1, y))
                        if look(x + 1, y) == 2 and (x + 1, y) not in new_cursors:
                            new_cursors.append((x + 1, y))
                        if look(x, y - 1) == 2 and (x, y - 1) not in new_cursors:
                            new_cursors.append((x, y - 1))
        cursors = new_cursors
    water = 0
    for r in arr:
        for i in r:
            if i > 1:
                water += 1

    print(water)
    water = 0
    for r in arr:
        for i in r:
            if i > 2:
                water += 1
    print(water)


main()