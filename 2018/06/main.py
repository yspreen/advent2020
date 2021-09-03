import pathlib

input = open(pathlib.Path(__file__).parent / "input").read().splitlines()
input = [[int(i.split(", ")[0]), int(i.split(", ")[1])] for i in input]


def easy():
    global input
    from contextlib import suppress

    enclosed = []
    for i in range(len(input)):
        t_r_b_l = [False, False, False, False]

        for j in range(len(input)):
            t = input[i][1] - input[j][1]
            l = input[i][0] - input[j][0]
            if t > 0:  # top
                if l > 0:  # left
                    if l >= t:
                        t_r_b_l[3] = True
                    if l <= t:
                        t_r_b_l[0] = True
                else:  # right
                    l = -l
                    if l >= t:
                        t_r_b_l[1] = True
                    if l <= t:
                        t_r_b_l[0] = True
            else:  # bottom
                t = -t
                if l > 0:  # left
                    if l >= t:
                        t_r_b_l[3] = True
                    if l <= t:
                        t_r_b_l[2] = True
                else:  # right
                    l = -l
                    if l >= t:
                        t_r_b_l[1] = True
                    if l <= t:
                        t_r_b_l[2] = True
        if t_r_b_l[0] and t_r_b_l[1] and t_r_b_l[2] and t_r_b_l[3]:
            # print(i)
            enclosed.append(i)

    min_x = min([i[0] for i in input])
    min_y = min([i[1] for i in input])

    for i in input:
        i[0] -= min_x
        i[1] -= min_y

    max_x = max([i[0] for i in input]) + 1
    max_y = max([i[1] for i in input]) + 1

    arr = [
        ([[-1, max_x + max_y] for _ in range(max_y)] + [0]) for _ in range(max_x)
    ] + [([0 for _ in range(max_y)] + [0])]

    queue = input
    while len(queue):
        i = queue[0]
        queue = queue[1:]
        if i in input:
            n = input.index(i) + 1
            arr[i[0]][i[1]] = [n, 0]
        else:
            m = [-1, max_x + max_y]
            with suppress(Exception):
                j = arr[i[0] + 1][i[1]]
                if j[1] + 1 < m[1]:
                    m = [j[0], j[1] + 1]
                elif j[1] + 1 == m[1] and m[0] != j[0]:
                    m = [0, m[1]]
            with suppress(Exception):
                j = arr[i[0] - 1][i[1]]
                if j[1] + 1 < m[1]:
                    m = [j[0], j[1] + 1]
                elif j[1] + 1 == m[1] and m[0] != j[0]:
                    m = [0, m[1]]
            with suppress(Exception):
                j = arr[i[0]][i[1] + 1]
                if j[1] + 1 < m[1]:
                    m = [j[0], j[1] + 1]
                elif j[1] + 1 == m[1] and m[0] != j[0]:
                    m = [0, m[1]]
            with suppress(Exception):
                j = arr[i[0]][i[1] - 1]
                if j[1] + 1 < m[1]:
                    m = [j[0], j[1] + 1]
                elif j[1] + 1 == m[1] and m[0] != j[0]:
                    m = [0, m[1]]
            arr[i[0]][i[1]] = m
        with suppress(Exception):
            p = [i[0] + 1, i[1]]
            if arr[p[0]][p[1]][0] == -1 and p not in queue:
                queue.append(p)
        with suppress(Exception):
            p = [i[0] - 1, i[1]]
            if arr[p[0]][p[1]][0] == -1 and p not in queue:
                queue.append(p)
        with suppress(Exception):
            p = [i[0], i[1] + 1]
            if arr[p[0]][p[1]][0] == -1 and p not in queue:
                queue.append(p)
        with suppress(Exception):
            p = [i[0], i[1] - 1]
            if arr[p[0]][p[1]][0] == -1 and p not in queue:
                queue.append(p)

    import string

    chars = "." + string.ascii_lowercase + string.ascii_uppercase

    out = ""
    for y in range(max_y):
        for x in range(max_x):
            out += chars[arr[x][y][0]]
        out += "\n"

    m = [0]

    for i in enclosed:
        n = i + 1
        c = out.count(chars[n])
        if c > m[0]:
            m = [c, n, chars[n]]

    print(m[0])


easy()


maxd = 10000

min_x = min([i[0] for i in input])
min_y = min([i[1] for i in input])

for i in input:
    i[0] -= min_x
    i[1] -= min_y

max_x = max([i[0] for i in input]) + 1
max_y = max([i[1] for i in input]) + 1


def hard():
    global input

    arr = [
        ([[-1, max_x + max_y] for _ in range(max_y)] + [0]) for _ in range(max_x)
    ] + [([0 for _ in range(max_y)] + [0])]

    c = 0
    for x in range(max_x):
        for y in range(max_y):
            d = 0
            for i in input:
                d += abs(i[0] - x)
                d += abs(i[1] - y)
                if d > maxd:
                    break
            if d < maxd:
                c += 1
    print(c)


hard()
