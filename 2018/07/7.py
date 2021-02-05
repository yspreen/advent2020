import pathlib

input = list(
    map(
        lambda l: l.split(", "),
        open(pathlib.Path(__file__).parent / "input.txt").read().splitlines(),
    )
)

requirements = dict()

for i in input:
    requirements[i[1]] = requirements.get(i[1], []) + [i[0]]
    requirements[i[0]] = requirements.get(i[0], [])


def easy():
    global input
    import string
    from contextlib import suppress

    total = len(requirements)
    output = ""
    while len(output) < total:
        for l in string.ascii_uppercase:
            i = requirements.get(l, None)
            if isinstance(i, list) and len(i) == 0:
                output += l
                for r in requirements.keys():
                    with suppress(Exception):
                        requirements[r].remove(l)
                requirements[l] = None
                break

    print(output)


easy()

requirements = dict()

for i in input:
    requirements[i[1]] = requirements.get(i[1], []) + [i[0]]
    requirements[i[0]] = requirements.get(i[0], [])


def hard():
    global input
    import string
    from contextlib import suppress

    letters = "." + string.ascii_uppercase  # align letter with time needed
    total = len(requirements)
    output = ""
    second = -1
    workers = [[0, 0] for _ in range(5)]
    while len(output) < total:
        second += 1
        for w in workers:
            if w[0] != 0:
                w[1] -= 1
                if w[1] == 0:
                    l = w[0]
                    output += l
                    for r in requirements.keys():
                        with suppress(Exception):
                            requirements[r].remove(l)
                    w[0] = 0
        for w in workers:
            if w[0] == 0:
                for l in letters:
                    i = requirements.get(l, None)
                    if isinstance(i, list) and len(i) == 0:
                        requirements[l] = None
                        w[0] = l
                        w[1] = 60 + letters.index(l)
                        break

    print(second)


hard()
