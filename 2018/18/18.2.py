import copy
from itertools import product

cycle = """
-2625
-7939
-668
-4008
-1178
-1736
2854
918
2892
78
4764
1779
3253
1898
4950
2688
6184
4465
5988
-1007
2098
352
-512
-1862
-2266
-3115
-7039
-9814
-3800
-6180
-1874
-2246
704
-2124
1159
2451
2140
3335
6375
2132
2992
1800
4942
2626
5818
3625
2357
-920
1048
-1065
85
-3620
192
-8002
-6630
-8712
"""

cycle = cycle.split("\n")
cycle = list(filter(None, cycle))

cycle = [int(i) for i in cycle]

start = 690
last_val = 179568


def print_arr(arr, format=None):
    out = ""
    for y in range(len(arr[0])):
        line = ""
        for x in range(len(arr)):
            line += ("%d" % arr[x][y]) if format is None else format[arr[x][y]]
        out += line + "\n"
    print(out, end="")


class hashable_area:
    def __init__(self, area, clone=False):
        self.area = area if not clone else copy.deepcopy(area)

    def __hash__(self):
        h = 0
        for r in self.area:
            for i in r:
                h *= 4
                h += i
        return h

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.area)


# ha = hashable_area
def ha(arr, *_):
    a = "".join(["".join([str(j) for j in i]) for i in arr])
    return a


areas = {}
for i in product("012", repeat=8):
    i = "".join(i)
    opens = i.count("0")
    trees = i.count("1")
    lumbs = i.count("2")

    i = [int(j) for j in i]
    area = [[0 for _ in range(3)] for _ in range(3)]
    area[0][0] = i[0]
    area[1][0] = i[1]
    area[2][0] = i[2]
    area[0][1] = i[3]
    area[2][1] = i[4]
    area[0][2] = i[5]
    area[1][2] = i[6]
    area[2][2] = i[7]

    for m in [0, 1, 2]:
        area[1][1] = m
        n = m
        if m == 0 and trees >= 3:
            n = 1
        if m == 1 and lumbs >= 3:
            n = 2
        if m == 2 and (lumbs == 0 or trees == 0):
            n = 0
        areas[ha(area)] = n


def unpad_zero(arr):
    del arr[-1]
    del arr[0]
    for i in arr:
        del i[-1]
        del i[0]


def pad_zero(arr):
    for col in arr:
        col.insert(0, 0)
        col.append(0)
    arr.insert(0, [0 for _ in arr[0]])
    arr.append([0 for _ in arr[0]])


def main():
    global input, format, areas, cycle, start, last_val

    minute = start - 1
    val = last_val

    goal = 1000000000

    goal -= minute
    val += sum(cycle) * (goal // len(cycle))
    goal %= len(cycle)
    i = 0
    while i < goal:
        val += cycle[i]
        i += 1
    print(val)


main()
