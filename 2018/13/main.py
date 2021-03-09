import pathlib


carts_char = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3,
    "/|": 4,
    "\|": 5,
    "|/": 6,
    "|\\": 7,
}
tracks_char = {
    " ": 0,
    "|": 1,
    "-": 2,
    "\\": 3,
    "/": 4,
    "+": 5,
}
cart_track_char = {
    "^": "|",
    ">": "-",
    "v": "|",
    "<": "-",
}


input = open(pathlib.Path(__file__).parent / "input").read().splitlines()
carts = []
tracks = [[0 for _ in range(len(input))] for _ in range(len(input[0]))]

y = -1
for l in input:
    y += 1
    x = -1
    for i in l:
        x += 1
        c = carts_char.get(i, None)
        if c is not None:
            carts.append([x, y, c, 0, 0, 0, 0, 0])
            i = cart_track_char[i]
        tracks[x][y] = tracks_char[i]


printed = crash = False
crashed = []


def step_carts(revert_order=False):
    global tracks, crash, carts, crashed, printed

    cart_pos = {}
    i = 0
    for c in carts:
        if revert_order:
            for rev_i in range(4):
                c[rev_i] = c[rev_i + 4]
        else:
            for rev_i in range(4):
                c[rev_i + 4] = c[rev_i]
            d = c[2]
            t = tracks[c[0]][c[1]]
            if cart_pos.get("%d,%d" % (c[0], c[1]), None) is not None:
                if not printed:
                    print("%d,%d" % (c[0], c[1]))
                    printed = True
                crash = True
                crashed = [i, cart_pos["%d,%d" % (c[0], c[1])]]

            if d == 0:  # up
                if t == 1:
                    c[1] -= 1
                elif t == 3:
                    c[0] -= 1
                    c[2] = 3
                elif t == 4:
                    c[0] += 1
                    c[2] = 1
                elif t == 5:  # intersection
                    intersect = c[3]
                    c[3] = (c[3] + 1) % 3
                    if intersect == 0:  # l
                        c[0] -= 1
                        c[2] = 3
                    elif intersect == 1:  # s
                        c[1] -= 1
                    else:  # r
                        c[0] += 1
                        c[2] = 1
            elif d == 1:  # right
                if t == 2:
                    c[0] += 1
                elif t == 3:
                    c[1] += 1
                    c[2] = 2
                elif t == 4:
                    c[1] -= 1
                    c[2] = 0
                elif t == 5:  # intersection
                    intersect = c[3]
                    c[3] = (c[3] + 1) % 3
                    if intersect == 0:  # l
                        c[1] -= 1
                        c[2] = 0
                    elif intersect == 1:  # s
                        c[0] += 1
                    else:  # r
                        c[1] += 1
                        c[2] = 2
            elif d == 2:  # down
                if t == 1:
                    c[1] += 1
                elif t == 3:
                    c[0] += 1
                    c[2] = 1
                elif t == 4:
                    c[0] -= 1
                    c[2] = 3
                elif t == 5:  # intersection
                    intersect = c[3]
                    c[3] = (c[3] + 1) % 3
                    if intersect == 0:  # l
                        c[0] += 1
                        c[2] = 1
                    elif intersect == 1:  # s
                        c[1] += 1
                    else:  # r
                        c[0] -= 1
                        c[2] = 3
            else:  # left
                if t == 2:
                    c[0] -= 1
                elif t == 3:
                    c[1] -= 1
                    c[2] = 0
                elif t == 4:
                    c[1] += 1
                    c[2] = 2
                elif t == 5:  # intersection
                    intersect = c[3]
                    c[3] = (c[3] + 1) % 3
                    if intersect == 0:  # l
                        c[1] += 1
                        c[2] = 2
                    elif intersect == 1:  # s
                        c[0] -= 1
                    else:  # r
                        c[1] -= 1
                        c[2] = 0
            if cart_pos.get("%d,%d" % (c[0], c[1]), None) is not None:
                crash = True
                crashed = [i, cart_pos["%d,%d" % (c[0], c[1])]]

            cart_pos["%d,%d" % (c[0], c[1])] = i
        i += 1


def main():
    global tracks, crash, carts, crashed

    num_carts = len(carts)

    while num_carts > 1:
        while not crash:
            while not crash:
                step_carts()

            step_carts(True)

            max_x = max([i[0] for i in carts])
            carts = sorted(carts, key=lambda k: k[1] * (max_x + 1) + k[0])
            crash = False
            step_carts(False)

        crash = False
        del carts[max(crashed)]
        del carts[min(crashed)]
        num_carts -= 2
    print("%d,%d" % (carts[0][0], carts[0][1]))


main()
