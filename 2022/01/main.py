f = open("input")
elves = f.read().split("\n\n")
elves = list(map(lambda e: list(map(int, e.splitlines())), elves))
elves = list(map(sum, elves))
print(max(elves))
print(sum(sorted(elves)[-3:]))
