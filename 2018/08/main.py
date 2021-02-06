import pathlib

input = list(
    map(int, open(pathlib.Path(__file__).parent / "input.txt").read().splitlines())
)
total = 0


def child_len(i):
    global input, total

    childs = input[i]
    nums = input[i + 1]
    length = nums + 2
    i += 2
    for _ in range(childs):
        c = child_len(i)
        length += c
        i += c
    total += sum(input[i : i + nums])

    return length


def easy():
    global input, total

    child_len(0)
    print(total)


easy()
total = 0


def hard_child_len(i):
    global input, total

    childs = input[i]
    nums = input[i + 1]
    length = nums + 2
    value = 0
    i += 2
    values = []
    for _ in range(childs):
        c = hard_child_len(i)
        length += c[0]
        i += c[0]
        values.append(c[1])
    if childs == 0:
        value = sum(input[i : i + nums])
    else:
        for meta in input[i : i + nums]:
            if meta >= 1 and meta <= childs:
                value += values[meta - 1]

    return (length, value)


def hard():
    global input, total

    hard_child_len(0)
    print(hard_child_len(0)[1])


hard()
