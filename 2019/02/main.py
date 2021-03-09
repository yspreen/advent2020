def calc(a, b):
    with open("2019.2/input") as f:
        t = f.read().replace('\r', '').split(',')
    if t[-1] == '':
        t.pop()

    t = [int(i) for i in t]
    t[1] = a
    t[2] = b

    i = 0
    while t[i] != 99:
        if t[i] == 1:
            t[t[i+3]] = t[t[i+1]] + t[t[i+2]]
        else:
            t[t[i+3]] = t[t[i+1]] * t[t[i+2]]

        i += 4

    return t[0]


def easy():
    print(calc(12, 2))

def hard():
    for i in range(100):
        for j in range(100):
            if calc(i, j) == 19690720:
                print(100 * i + j)
                return

if __name__ == "__main__":
    easy()
    hard()