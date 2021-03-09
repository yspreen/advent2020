import pathlib

serial = open(pathlib.Path(__file__).parent / "input").read().splitlines()[0]
serial = int(serial) % 1000


def main():
    global serial

    arr = [[0 for _ in range(300)] for _ in range(300)]

    rack = 10
    for x in range(300):
        rack += 1
        level = 0
        for y in range(300):
            level += rack
            arr[x][y] = (rack * (level + serial)) // 100 % 10 - 5

    sums = {}
    for size in [3] + list(range(10, 21)):
        for x in range(300 - size + 1):
            for y in range(300 - size + 1):
                s = 0
                for col in arr[x : (x + size)]:
                    for el in col[y : (y + size)]:
                        s += el
                sums["%d,%d,%d" % (x + 1, y + 1, size)] = s
    max3 = max = max_ind = max_ind3 = 0
    for ind in sums:
        if sums[ind] > max:
            max = sums[ind]
            max_ind = ind
        if sums[ind] > max3 and ind[-2:] == ",3":
            max3 = sums[ind]
            max_ind3 = ind
    print(max_ind3[:-2])
    print(max_ind)


main()
