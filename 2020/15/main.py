import pathlib

DIR = pathlib.Path(__file__).parent.absolute()


def read():
    with open(DIR / "input") as f:
        t = f.read().split(",")
    return [int(i) for i in t]


t = read()
tick = mem = last_num = None


def add_num(n):
    global last_num, tick
    tick += 1
    mem[last_num] = tick
    last_num = n


def get_new_num():
    return tick - mem.get(last_num, tick + 1) + 1


def solve(N):
    global mem, last_num, tick
    mem = {}
    tick = last_num = -1
    for n in t:
        add_num(n)
    for _ in range(N - len(t)):
        add_num(get_new_num())
    print(last_num)


def easy():
    solve(2020)


def hard():
    solve(30000000)


if __name__ == "__main__":
    easy()
    hard()
