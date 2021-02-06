import pathlib

input = open(pathlib.Path(__file__).parent / "input.txt").read().splitlines()

state = input[0].split(" ")[-1]
rules = {i.split(" ")[0]: i.split(" ")[-1] for i in input[2:]}
rule_len = len(list(rules.keys())[0])


def easy():
    global rules, state, rule_len
    rule_len_side = rule_len // 2
    prefix = "".join(["." for _ in range(rule_len_side)])
    shift = 0
    iterations = 20

    for i in range(iterations):
        # if i % 10000 == 0:
        #     print(100 * i / iterations)
        new_state = ""

        if state[0] == "#":
            state = prefix + state
            shift += 2
        if state[-1] == "#":
            state = state + prefix
        state = prefix + state + prefix
        while len(state) >= rule_len:
            new_state += rules.get(state[0:rule_len], ".")
            state = state[1:]

        state = new_state

    s = 0
    for i in range(len(state)):
        if state[i] == "#":
            s += i - shift
    print(s)


easy()

state = input[0].split(" ")[-1]


def hard():
    global rules, state, rule_len
    rule_len_side = rule_len // 2
    prefix = "".join(["." for _ in range(rule_len_side)])
    shift = 0
    iterations = 1500
    last_s = 0

    for i in range(iterations):
        new_state = ""

        if state[0] == "#":
            state = prefix + state
            shift += 2
        if state[-1] == "#":
            state = state + prefix
        state = prefix + state + prefix
        while len(state) >= rule_len:
            new_state += rules.get(state[0:rule_len], ".")
            state = state[1:]

        state = new_state
        if i > 1000:
            if i > 1100:
                break
            s = 0
            for j in range(len(state)):
                if state[j] == "#":
                    s += j - shift
            # print(i + 1, s, s - last_s)
            last_s = s
    print((50000000000 - i) * 23 + last_s)


hard()
