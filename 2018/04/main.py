import pathlib

input = list(
    map(str, open(pathlib.Path(__file__).parent / "input").read().splitlines())
)


def to_time(s):
    s = s.split(" ")[1][:-1].split(":")
    return (60 if s[0] == "00" else 0) + int(s[1])


def easy():
    times = dict()
    guard = None
    start = None
    for i in input:
        if "begins shift" in i:
            guard = int(i.split("#")[1].split(" ")[0])
        else:
            if start is None:
                start = to_time(i)
            else:
                times[guard] = times.get(guard, 0) + to_time(i) - start
                start = None

    max = (-1, -1)

    for i in times:
        if times[i] > max[1]:
            max = (i, times[i])

    max = max[0]

    times = [0 for _ in range(121)]
    for i in input:
        if "begins shift" in i:
            guard = int(i.split("#")[1].split(" ")[0])
        elif guard == max:
            if start is None:
                start = to_time(i)
            else:
                for j in range(start, to_time(i)):
                    times[j] += 1
                start = None

    max_time = (0, 0)
    i = -1
    for j in times:
        i += 1
        if j > max_time[1]:
            max_time = (i - 60, j)

    print(max_time[0] * max)


easy()


def to_time(s):
    s = s.split(" ")[1][:-1].split(":")
    return (60 if s[0] == "00" else 0) + int(s[1])


def hard():
    start = None
    times = dict()
    for i in input:
        if "begins shift" in i:
            guard = int(i.split("#")[1].split(" ")[0])
            if times.get(guard, None) is None:
                times[guard] = dict()
        elif start is None:
            start = to_time(i)
        else:
            for j in range(start, to_time(i)):
                times[guard][j] = times[guard].get(j, 0) + 1
            start = None

    max_time = (0, 0, 0)
    for guard in times:
        for time in times[guard]:
            t = times[guard][time]
            if t > max_time[2]:
                max_time = (guard, time - 60, t)

    print(max_time[0] * max_time[1])


hard()