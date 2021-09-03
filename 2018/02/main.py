import pathlib

input = list(
    map(str, open(pathlib.Path(__file__).parent / "input").read().splitlines())
)


def main():
    twos = 0
    threes = 0

    for i in input:
        d = dict()
        for letter in i:
            d[letter] = d.get(letter, 0) + 1
        was_two = False
        was_three = False
        for v in d.values():
            if not was_two and v == 2:
                twos += 1
                was_two = True
            elif not was_three and v == 3:
                threes += 1
                was_three = True

    print(twos * threes)


    n = len(input[0])
    for i in range(len(input)):
        for j_ in range(len(input) - i - 1):
            j = j_ + i + 1
            wrong = 0
            for k in range(n):
                if input[i][k] != input[j][k]:
                    wrong += 1
                    if wrong > 1:
                        break
            if wrong == 1:
                for a, b in zip(input[i], input[j]):
                    if a == b:
                        print(a, end="")
                print()
                return


main()
