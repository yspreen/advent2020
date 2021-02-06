import pathlib

input = list(
    map(int, open(pathlib.Path(__file__).parent / "input.txt").read().splitlines())
)

currents = dict()
current = 0
runs = 0
done = False
print(sum(input))
while not done:
    for i in input:
        runs += 1
        current += i
        if currents.get(current, False):
            print(current)
            done = True
            break
        currents[current] = True
