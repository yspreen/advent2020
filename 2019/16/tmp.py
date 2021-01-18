import numpy as np

N = 10


def pprint(l):
    for i in l:
        print(("    " + str(i))[-3:], end="")
    print()


# last = [0 for _ in range(N)]
# for j in range(N):
#     curr = [[0, 1, 0, -1][(i // (j + 1)) % 4] for i in range(N)]
#     # pprint([a - b for a, b in zip(curr, last)])
#     last = curr


def ppprint(A):
    for r in A:
        pprint(r)


A = np.zeros((N, N), np.int32)


for i in range(N):
    x = [-1, 1, 1, -1][i % 4]
    for j in range(1, N + 1):
        y = j // (i + 1)
        if y >= N:
            continue
        A[y, j - 1] += x
ppprint(A)