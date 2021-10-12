import pathlib


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def presents(max_fact=9e9, mult=10, limit=1e6):
    max_fact, limit, houses = int(max_fact), int(limit), [0] * int(limit)
    for i in range(limit):
        for k, j in enumerate(range(limit)[:: (i + 1)][1:]):
            if k == max_fact or j >= limit:
                break
            houses[j] += i * mult
            if houses[j] >= t:
                return print(j)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = int(read())
if __name__ == "__main__":
    presents()
    presents(50, 11)
