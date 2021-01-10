with open("2019.4/input.txt") as f:
    t = f.read().replace("\n", "").split("-")
if t[-1] == "":
    t.pop()

lower = [int(i) for i in t[0]]
upper = [int(i) for i in t[1]]
lowerint = int(t[0])
upperint = int(t[1])


## Slower but less code:
# def iter(check):
#     n = 0
#     for number in range(1000000):
#         if not (lowerint <= number <= upperint):
#             continue
#         number = [int(i) for i in str(number + 1000000)[1:]]
#         last_i = -1
#         broken = False
#         for i in number:
#             if last_i > i:
#                 broken = True
#                 break
#             last_i = i
#         if not broken and check(number):
#             n += 1
#     print(n)


def iter(check):
    n = 0
    for a in range(lower[0], upper[0] + 1):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            if check([a, b, c, d, e, f]):
                                x = 0
                                for elem in [a, b, c, d, e, f]:
                                    x *= 10
                                    x += elem
                                if lowerint <= x <= upperint:
                                    n += 1
    print(n)


def easycheck(number):
    x = -1
    precheck = False
    for elem in number:
        if elem == x:
            precheck = True
            break
        x = elem
    if precheck:
        return True


def hardcheck(number):
    last_elem = -1
    counter = 0
    for elem in number:
        if elem == last_elem:
            counter += 1
        else:
            if counter == 1:
                return True
            counter = 0
        last_elem = elem
    if counter == 1:
        return True


if __name__ == "__main__":
    iter(easycheck)
    iter(hardcheck)