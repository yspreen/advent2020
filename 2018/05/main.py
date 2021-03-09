import pathlib

input = open(pathlib.Path(__file__).parent / "input").read().replace("\n", "")


from string import ascii_lowercase as letters


def easy():
    global input

    i = 0
    while i < len(input) - 1:
        c1 = input[i]
        c2 = input[i + 1]

        if c1.lower() == c2.lower() and c1 != c2:
            input = input[:i] + input[i + 2 :]
            if i > 0:
                i -= 1
        else:
            i += 1

    print(len(input))


easy()


def hard():
    global input

    lengths = []
    for letter in letters:
        new_input = input.replace(letter, "").replace(letter.upper(), "")
        i = 0
        while i < len(new_input) - 1:
            c1 = new_input[i]
            c2 = new_input[i + 1]

            if c1.lower() == c2.lower() and c1 != c2:
                new_input = new_input[:i] + new_input[i + 2 :]
                if i > 0:
                    i -= 1
            else:
                i += 1

        lengths.append(len(new_input))

    print(min(lengths))


hard()
