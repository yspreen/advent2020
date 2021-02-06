import pathlib

input = list(
    map(str, open(pathlib.Path(__file__).parent / "input.txt").read().splitlines())
)

arr = [[0 for _ in range(1000)] for _ in range(1000)]


for i in input:
    i = i.split(" ")
    p = i[2].split(",")
    p[1] = p[1][:-1]
    s = i[-1].split("x")
    p = [int(p[0]), int(p[1])]
    s = [int(s[0]), int(s[1])]

    for x in range(p[0], p[0] + s[0]):
        for y in range(p[1], p[1] + s[1]):
            arr[x][y] += 1


count = 0
for a in arr:
    for i in a:
        if i > 1:
            count += 1
print(count)


arr = [[0 for _ in range(1000)] for _ in range(1000)]

claim = {i: True for i in range(len(input))}

for k in range(len(input)):
    i = input[k]
    i = i.split(" ")
    p = i[2].split(",")
    p[1] = p[1][:-1]
    s = i[-1].split("x")
    p = [int(p[0]), int(p[1])]
    s = [int(s[0]), int(s[1])]

    for x in range(p[0], p[0] + s[0]):
        for y in range(p[1], p[1] + s[1]):
            if arr[x][y] != 0:
                claim[k] = False
                claim[arr[x][y] - 1] = False
            arr[x][y] = k + 1

for c in claim:
    if claim[c]:
        print(c + 1)